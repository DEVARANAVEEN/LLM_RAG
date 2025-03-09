from wikipedia_scraper import fetch_wikipedia_summary
from faiss_indexer import build_faiss_index, search_faiss
from llm_responder import generate_answer

# Step 1: Fetch Wikipedia Data
query_topic = "US aircraft near-miss incidents"
documents = fetch_wikipedia_summary(query_topic)

if documents:
    # Step 2: Build FAISS Index
    index, document_sentences = build_faiss_index(documents)

    # Step 3: Perform Search
    query = "What are the recent near-miss incidents?"
    retrieved_docs = search_faiss(index, document_sentences, query)

    # Step 4: Generate AI Response
    answer = generate_answer(query, retrieved_docs)

    print("\nAI Generated Answer:\n", answer)
else:
    print("No Wikipedia data found.")
