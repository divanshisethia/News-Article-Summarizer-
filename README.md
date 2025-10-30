News Article Summarizer
This project is a Streamlit web app that summarizes long news articles using the TextRank algorithm.
It extracts the most important sentences from an article to give a short and meaningful summary.

Features
Upload or paste any news article
Automatically generates a summary (top sentences)
Adjustable summary length
Simple and user-friendly interface

How It Works
The article is split into sentences.
Each sentence is converted into vectors using TF-IDF.
Cosine similarity is calculated between sentences.
A graph is created with sentences as nodes and similarities as edges.
PageRank algorithm is applied to find the most important sentences.
Top sentences are selected as the final summary.

Technologies Used
Python
Streamlit
NLTK
Scikit-learn
NetworkX

Installation
# Clone the repository
git clone https://github.com/yourusername/news-summarizer.git
cd news-summarizer

# Install dependencies
pip install -r requirements.txt

Run the App
streamlit run app.py
Then open your browser and go to:
http://localhost:8501

Example
Input:
Ever noticed how plane seats appear to be getting smaller? Experts question if packed-out planes are putting passenger comfort at risk…
Output Summary:
Experts question if packed-out planes are putting passenger comfort at risk. Airlines have been shrinking seat sizes over the past decade.

Project Structure
news-summarizer/
│
├── app.py                # Streamlit app
├── test.csv              # Dataset (optional)
├── requirements.txt      # Dependencies
└── README.md             # Documentation

Author
Divanshi Sethia
