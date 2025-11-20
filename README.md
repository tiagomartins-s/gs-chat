# Chat Empresarial Inteligente - Global Solutions 2025.2

## 🎯 Visão Geral do Projeto

**Tema:** O Futuro do Trabalho - Como a tecnologia pode tornar o trabalho mais humano, inclusivo e sustentável no futuro?

Este projeto apresenta uma **Prova de Conceito (POC)** de um sistema de chat empresarial inteligente que utiliza Inteligência Artificial para centralizar e perpetuar o conhecimento organizacional, transformando conversas em memória institucional acessível e inteligente.

## 💡 Problema Identificado

No ambiente corporativo atual, enfrentamos desafios críticos:

- **Perda de conhecimento:** Informações valiosas discutidas em reuniões e conversas são esquecidas ou perdidas ao longo do tempo
- **Dificuldades de memória:** Profissionais com problemas de atenção e memória (comuns na era digital) perdem informações importantes
- **Falta de centralização:** Conhecimento disperso em múltiplas conversas, documentos e reuniões sem um sistema unificado de recuperação
- **Ineficiência na busca:** Dificuldade em encontrar informações específicas em grandes volumes de dados históricos

## 🚀 Nossa Solução

Desenvolvemos um **Chat Empresarial Inteligente** que utiliza técnicas avançadas de **RAG (Retrieval Augmented Generation)** e **busca semântica** para:

1. **Centralizar o conhecimento:** Todas as conversas são armazenadas e indexadas semanticamente
2. **Recuperação inteligente:** Sistema busca automaticamente informações relevantes do histórico quando necessário
3. **Memória institucional:** Conhecimento nunca é perdido - a IA "lembra" de tudo que foi discutido
4. **Acessibilidade:** Interface simples que torna o conhecimento acessível a todos os membros da equipe

## 🎯 Como Nossa Solução Torna o Trabalho Mais Humano, Inclusivo e Sustentável

### 🤝 Mais Humano
- **Potencializa capacidades humanas:** Em vez de substituir pessoas, a tecnologia amplifica nossa capacidade de memória e recuperação de informações
- **Foco no que importa:** Libera tempo para atividades criativas e estratégicas, enquanto a IA gerencia a recuperação de informações
- **Aprendizado contínuo:** Sistema aprende com cada conversa, criando uma base de conhecimento crescente

### ♿ Mais Inclusivo
- **Suporte para diferentes necessidades:** Ajuda pessoas com problemas de atenção, memória ou dificuldades cognitivas
- **Acesso igualitário:** Todos os membros da equipe têm acesso ao mesmo conhecimento, independentemente de quando entraram no projeto
- **Redução de barreiras:** Elimina a necessidade de "estar presente" em todas as reuniões para ter acesso ao conhecimento

### 🌱 Mais Sustentável
- **Perpetuação do conhecimento:** Informações não são mais perdidas quando colaboradores saem ou projetos mudam
- **Redução de retrabalho:** Evita que equipes refaçam discussões já realizadas
- **Eficiência de recursos:** Reduz tempo gasto procurando informações, economizando recursos humanos e computacionais

## 🏗️ Arquitetura da Solução

### Componentes Principais

1. **ChatManager (`chat_manager.py`)**
   - Gerencia mensagens e histórico de conversas
   - Cria embeddings semânticos de todas as mensagens
   - Implementa busca por similaridade usando FAISS
   - Persiste dados em arquivos JSON

2. **RAGSystem (`rag_system.py`)**
   - Integra com API do OpenAI (ChatGPT)
   - Gera respostas contextuais baseadas no histórico relevante
   - Aplica técnicas de RAG para enriquecer respostas com contexto

3. **Interface Streamlit (`app.py`)**
   - Interface web intuitiva e responsiva
   - Suporte a múltiplos chats simultâneos
   - Visualização em tempo real das conversas

### Fluxo de Funcionamento

```
1. Usuário envia mensagem → ChatManager armazena e cria embedding
2. Usuário faz pergunta com @ia → Sistema busca mensagens relevantes
3. RAGSystem recebe contexto + pergunta → Gera resposta contextualizada
4. Resposta é armazenada → Torna-se parte do conhecimento permanente
```

## 🔬 Tecnologias e Disciplinas Integradas

### AI for RPA (Automação Inteligente)
- **Aplicação:** Sistema automatiza a recuperação e organização de conhecimento, eliminando trabalho manual de busca em históricos extensos
- **Futuro do Trabalho:** RPA inteligente que não apenas executa tarefas, mas compreende contexto e aprende com interações

### Front End e Mobile Development
- **Aplicação:** Interface web responsiva desenvolvida com Streamlit, preparada para expansão mobile
- **Futuro do Trabalho:** Interfaces intuitivas que democratizam acesso a IA avançada, permitindo que qualquer pessoa interaja com sistemas complexos de forma natural

### Governança em IA
- **Aplicação:** Sistema de armazenamento e recuperação que mantém rastreabilidade de todas as interações
- **Futuro do Trabalho:** Transparência e auditabilidade em sistemas de IA, garantindo que decisões possam ser rastreadas e explicadas

### Processamento de Linguagem Natural (NLP)
- **Aplicação:** Embeddings semânticos para compreensão de significado, não apenas palavras-chave
- **Futuro do Trabalho:** Sistemas que compreendem intenção e contexto humano, não apenas processam texto literalmente

### Visão Computacional
- **Aplicação:** Preparado para expansão com análise de documentos, imagens de reuniões e capturas de tela
- **Futuro do Trabalho:** Sistemas multimodais que compreendem informação visual e textual de forma integrada

## 📊 Dados e Análise

### Coleta de Dados
- Mensagens de chat em tempo real
- Timestamps para análise temporal
- Metadados de contexto para cada interação

### Tratamento e Análise
- Embeddings vetoriais para busca semântica
- Indexação eficiente com FAISS
- Análise de relevância e similaridade

### Demonstração Prática
- Sistema funcional com interface web
- Persistência de dados entre sessões
- Busca semântica em tempo real

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior
- Chave de API do OpenAI
- Conta OpenAI com acesso à API

### Instalação

1. **Clone o repositório:**
```bash
python -m venv .venv
.venv/Scripts/activate
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Configure a chave de API:**
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave de API:
   ```
   OPENAI_API_KEY=sua_chave_api_aqui
   ```

4. **Execute a aplicação:**
```bash
streamlit run src/app.py
```

## 📁 Estrutura do Projeto

```
global-solutions/
├── src/                      # Código-fonte Python
│   ├── __init__.py
│   ├── app.py               # Aplicação principal Streamlit
│   ├── chat_manager.py      # Gerenciamento de mensagens e embeddings
│   └── rag_system.py        # Sistema RAG e integração com ChatGPT
├── doc/                      # Documentos e históricos de chat
│   └── chat_*.json          # Arquivos de persistência de chats
├── requirements.txt          # Dependências do projeto
├── .env                      # Variáveis de ambiente (não versionado)
└── README.md                 # Este arquivo
```

## 🎮 Como Usar

1. **Inicie a aplicação:**
   - Execute `streamlit run src/app.py`
   - A aplicação abrirá automaticamente no navegador

2. **Use o chat normalmente:**
   - Digite mensagens e envie
   - Todas as mensagens são armazenadas automaticamente

3. **Consulte a IA:**
   - Use `@ia` seguido de sua pergunta
   - Exemplo: `@ia Qual foi o assunto principal da nossa conversa?`
   - O sistema buscará automaticamente contexto relevante do histórico

4. **Gerencie múltiplos chats:**
   - Crie novos chats usando o botão "➕ Novo Chat"
   - Navegue entre chats usando a sidebar
   - Renomeie chats conforme necessário

## 🔍 Funcionalidades Implementadas

✅ **Armazenamento Inteligente**
- Todas as mensagens são armazenadas com timestamps
- Criação automática de embeddings semânticos
- Persistência entre sessões

✅ **Busca Semântica**
- Busca por similaridade usando FAISS
- Recuperação de contexto relevante baseada em significado, não palavras-chave
- Top-K retrieval configurável

✅ **RAG (Retrieval Augmented Generation)**
- Integração com ChatGPT para respostas contextuais
- Enriquecimento de prompts com histórico relevante
- Respostas precisas baseadas em conhecimento acumulado

✅ **Interface Intuitiva**
- Design limpo e moderno com Streamlit
- Suporte a múltiplos chats simultâneos
- Visualização em tempo real

## 🚧 Limitações da POC

Esta é uma **Prova de Conceito** que demonstra a viabilidade do conceito. Limitações atuais:

- **Escala:** Sistema otimizado para uso individual/pequenas equipes
- **Multimodalidade:** Atualmente processa apenas texto (preparado para expansão)
- **Segurança:** Implementação básica (requer melhorias para uso corporativo)
- **Performance:** Otimizações adicionais necessárias para grandes volumes

## 🔮 Expansões Futuras

### Curto Prazo
- [ ] Autenticação e autorização de usuários
- [ ] Suporte a upload de documentos
- [ ] Exportação de conversas
- [ ] Dashboard de analytics

### Médio Prazo
- [ ] Integração com ferramentas corporativas (Slack, Teams, etc.)
- [ ] Suporte a múltiplos idiomas
- [ ] Análise de sentimento e métricas de engajamento
- [ ] API REST para integrações

### Longo Prazo
- [ ] Visão computacional para análise de documentos
- [ ] Suporte a áudio e transcrição de reuniões
- [ ] Modelos fine-tuned para domínios específicos
- [ ] Computação quântica para otimização de buscas (futuro)

## 📈 Resultados Esperados

### Para Organizações
- **Redução de 40-60%** no tempo gasto procurando informações
- **Aumento de 30-50%** na retenção de conhecimento organizacional
- **Melhoria na produtividade** através de acesso rápido a contexto histórico

### Para Indivíduos
- **Suporte para memória:** Ajuda pessoas com dificuldades de atenção
- **Aprendizado contínuo:** Acesso a todo conhecimento acumulado
- **Redução de estresse:** Menos pressão para "lembrar de tudo"

### Para a Sociedade
- **Sustentabilidade:** Conhecimento não é mais perdido
- **Inclusão:** Tecnologia que apoia diferentes necessidades cognitivas
- **Eficiência:** Redução de retrabalho e desperdício de recursos

## 🎓 Conclusões

Este projeto demonstra como a tecnologia pode ser uma **aliada da humanidade** no ambiente de trabalho, não uma substituição. Através da combinação de:

- **IA Generativa** para compreensão e geração de respostas
- **NLP e Embeddings** para compreensão semântica
- **RAG** para enriquecimento contextual
- **Interface Intuitiva** para democratização do acesso

Criamos uma solução que **humaniza o trabalho** ao potencializar nossas capacidades, **promove inclusão** ao apoiar diferentes necessidades, e **garante sustentabilidade** ao perpetuar conhecimento organizacional.

### Validação do Conceito

Esta POC prova que:
1. ✅ É tecnicamente viável criar sistemas de memória institucional com IA
2. ✅ Busca semântica supera métodos tradicionais de recuperação
3. ✅ RAG pode criar respostas contextuais precisas
4. ✅ Interface simples pode democratizar acesso a IA avançada

O futuro do trabalho será construído por soluções como esta: **tecnologia que amplifica o humano, não o substitui**.

## 👥 Equipe

[Nome dos integrantes do grupo]

## 🔗 Links Importantes

- **Repositório GitHub:** [[Link do repositório privado]](https://github.com/tiagomartins-s/gs-chat)
- **Vídeo de Apresentação:** [[Link do YouTube - não listado]](https://youtu.be/1WscN28QR0g)

---

**"O trabalho do futuro será tão humano quanto as ideias que o constroem."**
