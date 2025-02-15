import streamlit as st

# Créer une interface utilisateur
def create_ui(chatbot):
    st.title("Chatbot Vidéos")
    query = st.text_input("Posez votre question")
    if st.button("Réinitialiser le contexte"):
        chat_history = []
    else:
        chat_history = st.session_state.get("chat_history", [])
    
    if query:
        response = chatbot(query, chat_history)
        st.write(response["answer"])
        chat_history.append((query, response["answer"]))
        st.session_state["chat_history"] = chat_history

# Exemple d'utilisation
chatbot = create_chatbot()
create_ui(chatbot)

# Exécuter avec Streamlit
#streamlit run main.py
