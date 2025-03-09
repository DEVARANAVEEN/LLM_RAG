import openai

client = openai.OpenAI(api_key="YOUR_OPENAI_API_KEY")

def generate_answer(query, retrieved_docs):
    """Generate an AI-based response using retrieved Wikipedia content."""
    context = "\n".join(retrieved_docs)
    
    prompt = f"You are an expert on the retrieved documents, answer based on them:\n\n{context}\n\nQuestion: {query}\nAnswer:"
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert assistant using Wikipedia as a knowledge base."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content
