from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

import os
os.environ['HF_HOME'] = 'D:/huggingface_cache'

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
docs=[
    'Uttar Pradesh: It is the state with the largest population in India, and it is also known for its rich cultural heritage and historical sites.',
    'Sikkim: This is the least populated state in India, famous for its scenic beauty and the Kanchenjunga mountain range.',
    'Maharashtra: The state is home to the bustling city of Mumbai, financial capital of India, and it is also known for its vibrant culture and historical sites.',
    'Karnataka: Known for its technological advancements and the IT hub of Bengaluru, Karnataka also boasts of beautiful coastal regions and ancient temples.',
    'Tamil Nadu: Famous for its rich history, cultural diversity, and the iconic Marina Beach in Chennai, Tamil Nadu is also known for its traditional dance forms like Bharatanatyam',
]
query="tell me about maharashtra"

doc_embed=embedding.embed_documents(docs)
query_embed=embedding.embed_query(query)

query_similarity=np.array(cosine_similarity([query_embed],doc_embed)[0]) # cosine_similarity take 2D vectors
best_match_index = np.argmax(query_similarity)
best_score = query_similarity[best_match_index]

print(f"Most similar vector is at index {best_match_index} with similarity {best_score}")
print(docs[best_match_index])