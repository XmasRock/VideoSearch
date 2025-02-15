from langchain.chains import ConversationalRetrievalChain
from langchain.llms import Ollama
from langchain.vectorstores import Qdrant
from langchain_core.messages import HumanMessage

# Créer un chatbot avec contexte
def create_chatbot():
    ollama = Ollama()
    client = QdrantClient(host="localhost", port=6333)
    retriever = client.as_retriever()
    
    # Créer une chaîne de récupération conversationnelle
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=ollama,
        retriever=retriever,
        return_source_documents=True
    )
    
    # Fonction pour répondre à une question
    def answer_question(query, chat_history=None):
        if chat_history is None:
            chat_history = []
        response = qa_chain({"question": query, "chat_history": chat_history})
        return response
    
    return answer_question

# Exemple d'utilisation
chatbot = create_chatbot()
query = "Quelle est la meilleure vidéo sur le sujet X ?"
response = chatbot(query)
print(response["answer"])

# Pour remettre à zéro le contexte, passez un historique de chat vide
response = chatbot(query, chat_history=[])
