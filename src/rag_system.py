"""
Sistema RAG para integração com ChatGPT
"""
from typing import List, Dict
from openai import OpenAI

class RAGSystem:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
    
    def generate_response(self, query: str, context: List[Dict[str, str]]) -> tuple[str, List[Dict[str, str]]]:
        """
        Gera resposta usando ChatGPT com contexto RAG
        
        Returns:
            tuple: (resposta, contexto_completo_enviado)
        """
        # Preparar mensagens para a API
        messages = []
        
        # Adicionar contexto do RAG
        if context:
            messages.append({
                "role": "system",
                "content": "Você é um assistente útil. Use o contexto fornecido das conversas anteriores para responder à pergunta do usuário de forma precisa e relevante."
            })
            
            # Adicionar contexto das mensagens relevantes
            for ctx_msg in context:
                messages.append(ctx_msg)
        
        # Adicionar a pergunta atual
        messages.append({
            "role": "user",
            "content": query
        })
        
        # Chamar API do ChatGPT
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7
        )
        
        answer = response.choices[0].message.content
        
        return answer, messages

