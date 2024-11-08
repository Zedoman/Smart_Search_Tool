import gradio as gr
from sentence_transformers import SentenceTransformer
import pandas as pd
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Function to load courses data from the JSON file
def load_courses():
    with open('data/courses.json', 'r') as file:
        data = json.load(file)
    return data['free_courses']

# Load course data
courses_data = load_courses()

# Convert the course data to a pandas DataFrame for easier manipulation
df_courses = pd.DataFrame(courses_data)

# Initialize SentenceTransformer model for semantic search
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Function to process the query and find the most relevant course
def smart_search(query):
    # Encode the query
    query_embedding = model.encode([query])[0]  # Get the embedding for the query

    # Compute similarity between the query and course descriptions
    similarities = []
    for _, row in df_courses.iterrows():
        course_description = row['description']
        course_embedding = model.encode([course_description])[0]  # Get embedding for course description
        
        # Compute cosine similarity
        similarity = cosine_similarity([query_embedding], [course_embedding])[0][0]
        similarities.append(similarity)

    # Sort courses by similarity score and return top 3 results
    df_courses['similarity'] = similarities
    df_courses_sorted = df_courses.sort_values(by='similarity', ascending=False)
    top_courses = df_courses_sorted.head(3)

    return top_courses[['title', 'description']].to_dict(orient='records')

# Build the Gradio interface
interface = gr.Interface(fn=smart_search,
                         inputs="text",
                         outputs="json",
                         title="Smart Course Search",
                         description="Enter a keyword or query, and find the most relevant courses on Analytics Vidhya.")

# Launch the interface
interface.launch()
