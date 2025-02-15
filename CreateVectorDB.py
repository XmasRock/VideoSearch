import pytube
from langchain.llms import Ollama
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient

# Fonction pour télécharger et transcrire une vidéo
def download_and_transcribe_video(video_url):
    yt = pytube.YouTube(video_url)
    title = yt.title
    # Transcrire la vidéo (simplifié ici)
    transcript = "Transcript de la vidéo"
    return title, transcript

# Fonction pour résumer le texte avec Ollama
def summarize_text(text):
    ollama = Ollama()
    prompt = f"Résumer le texte suivant : {text}"
    summary = ollama(prompt)
    return summary

# Créer une base vectorisée avec Qdrant
def create_vector_db(video_urls):
    client = QdrantClient(host="localhost", port=6333)
    embeddings = HuggingFaceEmbeddings()
    
    for url in video_urls:
        title, transcript = download_and_transcribe_video(url)
        summary = summarize_text(transcript)
        vector = embeddings.compute_embedding(summary)
        
        # Enregistrer les métadonnées
        metadata = {
            "url": url,
            "title": title
        }
        
        # Insérer le vecteur dans Qdrant avec les métadonnées
        client.upsert(
            collection_name="videos",
            vectors=[{"id": 0, "vector": vector, "payload": metadata}],
            wait=True
        )

# Exemple d'utilisation
video_urls = ["https://example.com/video1", "https://example.com/video2"]
create_vector_db(video_urls)
