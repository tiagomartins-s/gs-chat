"""
Aplicação Streamlit - GS Chat AI
"""
import streamlit as st
import os
import uuid
from dotenv import load_dotenv
from chat_manager import ChatManager
from rag_system import RAGSystem

# Carregar variáveis de ambiente
load_dotenv()

# Configuração da página
st.set_page_config(
    page_title="GS Chat AI",
    page_icon="💬",
    layout="wide"
)

# Inicializar sessão
if "api_key" not in st.session_state:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("⚠️ Por favor, configure a variável OPENAI_API_KEY no arquivo .env")
        st.stop()
    st.session_state.api_key = api_key
    st.session_state.rag_system = RAGSystem(api_key)

# Inicializar estrutura de chats
if "chats" not in st.session_state:
    st.session_state.chats = {}  # {chat_id: {"name": str, "chat_manager": ChatManager}}
    st.session_state.current_chat_id = None

# Inicializar chat atual se não houver nenhum
if st.session_state.current_chat_id is None or st.session_state.current_chat_id not in st.session_state.chats:
    if not st.session_state.chats:
        # Criar primeiro chat
        chat_id = str(uuid.uuid4())
        chat_manager = ChatManager(st.session_state.api_key, storage_file=f"doc/chat_{chat_id}.json")
        st.session_state.chats[chat_id] = {
            "name": "Novo Chat",
            "chat_manager": chat_manager
        }
        st.session_state.current_chat_id = chat_id
    else:
        # Usar o primeiro chat disponível
        st.session_state.current_chat_id = list(st.session_state.chats.keys())[0]

def main():
    st.title("💬 GS Chat AI")
    st.markdown("---")
    
    # Obter chat atual
    current_chat = st.session_state.chats[st.session_state.current_chat_id]
    chat_manager = current_chat["chat_manager"]
    
    # Sidebar para lista de chats
    with st.sidebar:
        st.header("💬 Chats")
        
        # Botão para criar novo chat
        if st.button("➕ Novo Chat", use_container_width=True):
            chat_id = str(uuid.uuid4())
            new_chat_manager = ChatManager(st.session_state.api_key, storage_file=f"doc/chat_{chat_id}.json")
            st.session_state.chats[chat_id] = {
                "name": "Novo Chat",
                "chat_manager": new_chat_manager
            }
            st.session_state.current_chat_id = chat_id
            st.rerun()
        
        st.markdown("---")
        
        # Lista de chats
        if st.session_state.chats:
            for chat_id, chat_data in st.session_state.chats.items():
                is_current = chat_id == st.session_state.current_chat_id
                button_label = f"💬 {chat_data['name']}"
                
                if is_current:
                    st.markdown(f"**{button_label}**")
                else:
                    if st.button(button_label, key=f"chat_{chat_id}", use_container_width=True):
                        st.session_state.current_chat_id = chat_id
                        st.rerun()
    
    # Campo para editar nome do chat no topo
    col1, col2 = st.columns([3, 1])
    with col1:
        new_name = st.text_input(
            "Nome do Chat:",
            value=current_chat["name"],
            key=f"chat_name_{st.session_state.current_chat_id}",
            label_visibility="collapsed"
        )
        if new_name != current_chat["name"]:
            current_chat["name"] = new_name
            st.rerun()
    
    st.markdown("---")
    
    # Container principal do chat
    chat_container = st.container()
    
    with chat_container:
        messages = chat_manager.get_all_messages()
        
        if not messages:
            st.info("👋 Comece a conversar! Digite uma mensagem e envie. Use @ia para chamar a inteligência artificial.")
        else:
            # Exibir todas as mensagens
            for idx, msg in enumerate(messages):
                if msg["role"] == "user":
                    # Mensagem do usuário
                    with st.chat_message("user"):
                        st.write(msg["content"])
                else:
                    # Mensagem da IA
                    with st.chat_message("assistant"):
                        st.write(msg["content"])
    
    # Input de mensagem
    user_input = st.chat_input("Digite sua mensagem...")
    
    if user_input:
        # Verificar se é chamada para a IA
        if user_input.strip().lower() == "@ia":
            st.warning("⚠️ Por favor, faça uma pergunta após @ia. Exemplo: '@ia Qual foi o assunto principal da conversa?'")
        elif user_input.strip().lower().startswith("@ia"):
            # Extrair a pergunta (remover @ia)
            query = user_input[3:].strip()
            
            if not query:
                st.warning("⚠️ Por favor, faça uma pergunta após @ia.")
            else:
                # Adicionar mensagem do usuário
                chat_manager.add_message("user", user_input)
                
                # Buscar contexto relevante
                with st.spinner("🤔 Buscando contexto e gerando resposta..."):
                    context = chat_manager.get_chat_context_for_ai(query)
                    
                    # Gerar resposta da IA
                    response, full_context = st.session_state.rag_system.generate_response(query, context)
                    
                    # Adicionar resposta da IA com contexto
                    chat_manager.add_message("assistant", response, context=full_context)
                
                st.rerun()
        else:
            # Mensagem normal do usuário
            chat_manager.add_message("user", user_input)
            st.rerun()

if __name__ == "__main__":
    main()

