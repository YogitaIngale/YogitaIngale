import pandas as pd
df = pd.read_csv('city_data.csv')

# Display the first few rows
print(df.head())

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Combine all text fields into a single text field
df['combined'] = df['name'] + ' ' + df['description'] + ' ' + df['location']

# Vectorize the combined text field
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])

def get_response(query):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    best_match_idx = np.argmax(similarities)
    return df.iloc[best_match_idx]

# Example query
query = "Tell me about the best restaurant"
response = get_response(query)
print(response)

def chat():
    print("Welcome to the City Chat-Bot! Ask me anything about the city.")
    while True:
        query = input("You: ")
        if query.lower() in ['exit', 'quit', 'bye']:
            print("Chat-Bot: Goodbye!")
            break
        response = get_response(query)
        print(f"Chat-Bot: {response['description']} at {response['location']}")

# Start the chat
chat()

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the dataset
df = pd.read_csv('city_data.csv')

# Combine all text fields into a single text field
df['combined'] = df['name'] + ' ' + df['description'] + ' ' + df['location']

# Vectorize the combined text field
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])

def get_response(query):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    best_match_idx = np.argmax(similarities)
    return df.iloc[best_match_idx]

def chat():
    print("Welcome to the City Chat-Bot! Ask me anything about the city.")
    while True:
        query = input("You: ")
        if query.lower() in ['exit', 'quit', 'bye']:
            print("Chat-Bot: Goodbye!")
            break
        response = get_response(query)
        print(f"Chat-Bot: {response['description']} at {response['location']}")

# Start the chat
chat()
