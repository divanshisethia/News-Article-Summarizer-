import streamlit as st
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

# Download tokenizer (only once)
nltk.download('punkt')

# App title
st.title("News Article Summarizer (TextRank)")

st.write("Upload or paste a news article and get a short summary using TextRank.")

# Input options
option = st.radio("Choose input method:", ["Paste text", "Upload .txt file"])

if option == "Paste text":
    text = st.text_area("Paste your news article here:", height=250)
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type="txt")
    text = uploaded_file.read().decode("utf-8") if uploaded_file else ""

# Number of summary sentences
num_sentences = st.slider("Select number of sentences for summary:", 2, 10, 5)

# Process button
if st.button("Summarize"):
    if not text.strip():
        st.warning("Please enter or upload some text.")
    else:
        # Step 1: Split into sentences
        sentences = nltk.sent_tokenize(text)

        # Step 2: Clean sentences
        clean_sentences = [re.sub(r'[^a-zA-Z]', ' ', s) for s in sentences]
        clean_sentences = [s.lower() for s in clean_sentences]

        # Step 3: TF-IDF Vectorization
        vectorizer = TfidfVectorizer()
        sentence_vectors = vectorizer.fit_transform(clean_sentences)

        # Step 4: Build Similarity Graph
        sim_matrix = cosine_similarity(sentence_vectors)
        graph = nx.from_numpy_array(sim_matrix)

        # Step 5: Apply PageRank
        scores = nx.pagerank(graph)

        # Step 6: Rank and summarize
        ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
        selected_sentences = sorted(ranked_sentences[:num_sentences], key=lambda x: sentences.index(x[1]))
        summary = ' '.join([s for _, s in selected_sentences])

        # Display results
        st.subheader("Summary:")
        st.write(summary)
