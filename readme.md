# Smart Course Search Tool with Gradio and Sentence Transformers [Smart Search Tool](https://huggingface.co/spaces/Zedoman/SearchTool)

## Overview
This project implements a smart search tool for Analytics Vidhya's free courses using Gradio, Sentence Transformers, and Cosine Similarity. The tool allows users to input a query, and the most relevant courses from a dataset of free courses are suggested based on the similarity of the query to the course descriptions. <br>

The project uses the `sentence-transformers` library to generate embeddings of both the query and course descriptions. It then computes cosine similarity to rank the courses and present the most relevant results to the user.

## Features
- **Semantic Search:** Uses pre-trained models from `sentence-transformers` to generate embeddings for both the query and course descriptions. <br>
- **Cosine Similarity:** Calculates the similarity between the query and course descriptions to rank them. <br>
- **Gradio Interface:** A simple web-based user interface for querying courses and displaying results. <br>

## Technology Stack
- **Gradio:** A Python library for creating user-friendly interfaces to machine learning models. <br>
- **Sentence-Transformers:** A library for working with transformer models designed for tasks like semantic textual similarity. <br>
- **Scikit-learn:** Used for calculating cosine similarity between text embeddings. <br>
- **Pandas:** For handling and manipulating course data. <br>
- **JSON:** For storing and reading the course data. <br>

## Installation

1. **Clone the repository:** <br>
   ```bash
   git clone https://github.com/Zedoman/Smart_Search_Tool
   cd Smart_Search_Tool

2. **Set up the environment: Make sure you have Python 3.x installed, and create a virtual environment:** <br>
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install the dependencies: Install the required libraries using pip:** <br>
    ```bash
    pip install -r requirements.txt

4. **Create the requirements.txt file as follows:** <br>
    ```bash
    gradio
    sentence-transformers
    scikit-learn
    pandas
    numpy


## Setup and Configuration
1. **Data Configuration: The course data is stored in a JSON file named courses.json. The file should be structured like this:** <br>
   {
  "free_courses": [
    {
      "title": "Course Title",
      "description": "Course Description",
      "curriculum": [
          "Introduction to Generative AI",
          "Text Generation Using Generative AI",
          "Image Generation Using Generative AI"
        ]
    },
    {
      "title": "Another Course Title",
      "description": "Another Course Description",
      "curriculum": [
          "Introduction to Generative AI",
          "Text Generation Using Generative AI",
          "Image Generation Using Generative AI"
        ]
    },
    ...
  ]
  }

  The JSON file should be located in the data/ directory. <br>

2. **Model Configuration:** The project uses the sentence-transformers/all-MiniLM-L6-v2 model to generate embeddings for both the query and the course descriptions. This model is pre-trained and should be downloaded automatically by the SentenceTransformer class when running the application.   <br>


## Running the Application
1. **Start the Gradio Interface:** After installing the dependencies and setting up the project, you can start the Gradio interface by running the following command: <br>
   ```bash
    python app.py

2. **Using the Interface:** The Gradio interface will launch a local web server and open a browser window with the search interface. You can enter any keyword or query, and the tool will return the top 3 most relevant courses based on the descriptions. <br>

The results will display the course title and description. <br>


## How It Works

1. **Loading Data:** The course data is loaded from a JSON file located in the data/ folder. This data is then converted into a Pandas DataFrame for easier manipulation. <br>

2. **Generating Embeddings:** Both the user query and course descriptions are passed through a pre-trained model (sentence-transformers/all-MiniLM-L6-v2) to generate embeddings. <br>

3. **Computing Similarity:** The cosine similarity is calculated between the query embedding and each course description embedding. The courses are ranked based on the similarity score, and the top 3 results are returned. <br>

4. **Displaying Results:** The results are displayed in a Gradio interface with course titles and descriptions. <br>


## Example Usage
1. **Query:** "Deep learning basics" <br>

The system will return courses that are most relevant to deep learning topics. <br>
 
2. **Query:** "Python for beginners" <br>

It will suggest courses that are suitable for beginners learning Python. <br>


## Future Improvements
1. Additional Features: Integrate more filtering options (e.g., course difficulty level, duration). <br>
2. Advanced Ranking: Use other ranking algorithms like BM25 or fine-tune the model on course-specific data. <br>
3. Deploying the App: Deploy the Gradio app on cloud platforms like Heroku or Hugging Face Spaces for wider access. <br>


## File Structure
   ```bash
   ├── app.py                  # Main Python script to run the Gradio app
   ├── data/                   # Folder containing the courses data (courses.json)
   │   └── courses.json        # JSON file with course data
   ├── requirements.txt        # Python dependencies
   ├── README.md               # Project documentation
   └── venv/                   # Virtual environment (if created)




