# News Article Summarizer (TextRank) 
## Overview

This project implements an extractive text summarization tool using the TextRank algorithm, inspired by Google’s PageRank. The app allows users to upload or paste a news article and automatically generates a concise summary highlighting the most important sentences.

The system is built with Streamlit for interactivity and uses Natural Language Processing (NLP) techniques such as TF-IDF vectorization, cosine similarity, and graph-based ranking to determine sentence importance.

## Key Features
- Interactive Streamlit App: Upload or paste a text article directly into the web interface.
- Automatic Summarization: Generates a summary with a user-selected number of sentences.
- TextRank Algorithm: Identifies key sentences based on their similarity and contextual importance.
- TF-IDF + Cosine Similarity: Measures semantic similarity between sentences.
- Graph-Based Ranking: Applies PageRank on a sentence similarity graph to find the most central sentences.

## Methodology
### Text Preprocessing
- Input text is split into individual sentences using nltk.sent_tokenize.
- Each sentence is cleaned by:
    - Removing special characters and numbers.
    - Converting to lowercase for uniformity.

### Sentence Vectorization
- Uses TF-IDF (Term Frequency–Inverse Document Frequency) to convert sentences into numerical feature vectors.
- TF-IDF ensures that common words (like “the”, “and”) have less influence compared to informative words.

### Similarity Matrix Construction
- The cosine similarity between every pair of sentence vectors is calculated.
- This creates a similarity matrix, where each entry indicates how semantically close two sentences are.

### Graph Construction
- Sentences are represented as nodes in a graph.
- Edges connect sentences with their similarity scores as weights.

### Ranking (TextRank Algorithm)
- The PageRank algorithm is applied on this sentence similarity graph using networkx.pagerank().
- Sentences that are central and connected to other highly similar sentences receive higher scores.

### Summary Generation
- Sentences are ranked by their PageRank scores.
- The top N (user-selected) sentences are extracted and ordered in their original sequence to maintain coherence.

## Tech Stack
| Component              | Library/Tool                     |
| ---------------------- | -------------------------------- |
| Web Interface          | Streamlit                        |
| NLP Processing         | NLTK                             |
| Vectorization          | Scikit-learn (TF-IDF)            |
| Graph Operations       | NetworkX                         |
| Similarity Computation | Scikit-learn (Cosine Similarity) |
| Language               | Python 3.10+                     |

## Quickstart
### Clone the Repository
```
git clone https://github.com/yourusername/TextRank-News-Summarizer.git
cd TextRank-News-Summarizer
```

### Create a Virtual Environment
```
python -m venv venv
venv\Scripts\activate  # For Windows
source venv/bin/activate  # For macOS/Linux
```

### Install Dependencies
```
pip install -r requirements.txt
```
(Typical dependencies include: streamlit, nltk, scikit-learn, networkx)

### Download NLTK Data
- Run this once to download the tokenizer model:

```
import nltk
nltk.download('punkt')
```

### Launch the App
```
streamlit run app.py
```
Then open the provided URL (usually http://localhost:8501
) in your browser.

## Example Usage
- Choose Paste Text or Upload .txt File.
- Set the number of sentences for the summary using the slider.
- Click Summarize.
- The summarized text appears instantly below.

## Acknowledgments
- NLTK for text preprocessing and sentence tokenization.
- NetworkX for graph construction and PageRank computation.
- Streamlit for providing a clean, interactive UI for rapid deployment.

This project demonstrates the power of graph-based NLP algorithms in identifying the most relevant sentences for concise and meaningful text summarization. It provides a simple yet effective foundation for building automated summarization tools that can be expanded with deep learning models like BERT in the future.
