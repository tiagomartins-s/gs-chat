"""
Gerenciador de chat e embeddings
"""
import json
import os
from typing import List, Dict, Any
from datetime import datetime
import numpy as np
import faiss
from openai import OpenAI

class ChatManager:
    def __init__(self, api_key: str, storage_file: str = "chat_history.json"):
        self.client = OpenAI(api_key=api_key)
        self.storage_file = storage_file
        self.messages: List[Dict[str, Any]] = []
        self.embeddings: List[np.ndarray] = []
        self.embedding_to_message_idx: List[int] = []  # Mapeia índice de embedding para índice de mensagem
        self.index = None
        self.embedding_dim = 1536  # Dimensão dos embeddings do OpenAI text-embedding-ada-002
        
        # Carregar histórico se existir
        self.load_history()
        
    def add_message(self, role: str, content: str, context: List[Dict] = None):
        """Adiciona uma mensagem ao chat e cria seu embedding"""
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "context": context if context else None
        }
        self.messages.append(message)
        
        # Criar embedding da mensagem
        if role == "user":
            embedding = self._create_embedding(content)
            self.embeddings.append(embedding)
            self.embedding_to_message_idx.append(len(self.messages) - 1)
            self._update_index()
        
        # Salvar histórico após adicionar mensagem
        self.save_history()
    
    def _create_embedding(self, text: str) -> np.ndarray:
        """Cria embedding para um texto"""
        response = self.client.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        return np.array(response.data[0].embedding, dtype=np.float32)
    
    def _update_index(self):
        """Atualiza o índice FAISS com os embeddings"""
        if not self.embeddings:
            return
        
        embeddings_array = np.array(self.embeddings).astype('float32')
        
        if self.index is None:
            self.index = faiss.IndexFlatL2(self.embedding_dim)
        
        # Reconstruir índice com todos os embeddings
        self.index = faiss.IndexFlatL2(self.embedding_dim)
        self.index.add(embeddings_array)
    
    def search_relevant_messages(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Busca mensagens relevantes usando busca semântica"""
        if not self.embeddings or self.index is None:
            return []
        
        # Criar embedding da query
        query_embedding = self._create_embedding(query)
        query_embedding = query_embedding.reshape(1, -1).astype('float32')
        
        # Buscar mensagens mais relevantes
        distances, indices = self.index.search(query_embedding, min(top_k, len(self.messages)))
        
        relevant_messages = []
        for embedding_idx in indices[0]:
            if embedding_idx < len(self.embedding_to_message_idx):
                message_idx = self.embedding_to_message_idx[embedding_idx]
                if message_idx < len(self.messages):
                    msg = self.messages[message_idx]
                    relevant_messages.append(msg)
        
        return relevant_messages
    
    def get_all_messages(self) -> List[Dict[str, Any]]:
        """Retorna todas as mensagens do chat"""
        return self.messages
    
    def get_chat_context_for_ai(self, query: str, top_k: int = 10) -> List[Dict[str, str]]:
        """Retorna contexto formatado para a API do ChatGPT"""
        # Buscar mensagens relevantes
        relevant_messages = self.search_relevant_messages(query, top_k=top_k)
        
        # Se não houver mensagens relevantes, usar todas as mensagens do usuário
        if not relevant_messages:
            relevant_messages = [msg for msg in self.messages if msg["role"] == "user"]
        
        # Formatar como mensagens para a API
        context = []
        for msg in relevant_messages:
            context.append({
                "role": "user",
                "content": msg["content"]
            })
        
        return context
    
    def save_history(self):
        """Salva o histórico de mensagens em arquivo JSON"""
        try:
            # Criar diretório se não existir
            storage_dir = os.path.dirname(self.storage_file)
            if storage_dir and not os.path.exists(storage_dir):
                os.makedirs(storage_dir, exist_ok=True)
            
            # Preparar dados para salvar (embeddings não podem ser serializados em JSON)
            save_data = {
                "messages": self.messages,
                "embedding_to_message_idx": self.embedding_to_message_idx
            }
            
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Erro ao salvar histórico: {e}")
    
    def load_history(self):
        """Carrega o histórico de mensagens do arquivo JSON"""
        if not os.path.exists(self.storage_file):
            return
        
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.messages = data.get("messages", [])
            self.embedding_to_message_idx = data.get("embedding_to_message_idx", [])
            
            # Reconstruir embeddings e índice
            if self.messages:
                self._rebuild_embeddings()
        except Exception as e:
            print(f"Erro ao carregar histórico: {e}")
            # Se houver erro, começar do zero
            self.messages = []
            self.embeddings = []
            self.embedding_to_message_idx = []
    
    def _rebuild_embeddings(self):
        """Reconstrói embeddings a partir das mensagens carregadas"""
        self.embeddings = []
        self.embedding_to_message_idx = []
        
        for idx, msg in enumerate(self.messages):
            if msg["role"] == "user":
                try:
                    embedding = self._create_embedding(msg["content"])
                    self.embeddings.append(embedding)
                    self.embedding_to_message_idx.append(idx)
                except Exception as e:
                    print(f"Erro ao recriar embedding para mensagem {idx}: {e}")
        
        if self.embeddings:
            self._update_index()
    
    def clear_history(self):
        """Limpa todo o histórico e remove o arquivo de persistência"""
        self.messages = []
        self.embeddings = []
        self.embedding_to_message_idx = []
        self.index = None
        
        # Remover arquivo de persistência
        if os.path.exists(self.storage_file):
            try:
                os.remove(self.storage_file)
            except Exception as e:
                print(f"Erro ao remover arquivo de histórico: {e}")

