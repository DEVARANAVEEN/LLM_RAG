from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load a pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def build_faiss_index(documents):
    """Convert text into embeddings and build a FAISS index."""
    document_sentences = documents.split('. ')
    document_sentences = [sentence.strip() for sentence in document_sentences if sentence]
    
    document_vectors = model.encode(document_sentences).astype('float32')
    index = faiss.IndexFlatL2(document_vectors.shape[1])
    index.add(document_vectors)
    
    return index, document_sentences

def search_faiss(index, document_sentences, query, top_k=2):
    """Search FAISS for the most relevant text snippets."""
    query_vector = model.encode([query]).astype('float32')
    _, indices = index.search(query_vector, top_k)
    
    return [document_sentences[i] for i in indices[0]]
