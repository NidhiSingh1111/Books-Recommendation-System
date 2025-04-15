# BOOKS RECOMMENDATION SYSTEM 



# 📚 Books Recommendation System

A book recommendation system is an intelligent application that suggests books to users based on their interests or preferences. It plays a vital role in platforms like Amazon, Goodreads, or Kindle, where personalized recommendations can enhance user experience and increase engagement.

There are several types of recommendation systems:
- **Collaborative Filtering**: Based on user behavior and preferences.
- **Content-Based Filtering**: Based on book metadata (title, author, genre, etc.)
- **Hybrid Systems**: Combine both techniques.

### 🧬 Our Approach: Collaborative-Based Filtering

In this project, we’ve used **Collaborative-Based Filtering**, which works by:
- Extracting features (like title, author, tags, and description) from the book dataset.
- Using **TF-IDF Vectorization** to convert text into numerical format.
- Computing **cosine similarity** between books to find the most similar titles.
- Recommending top N books that are closest in similarity to the selected book.

This approach is fast and doesn’t require user interaction history, making it ideal for new users or small-scale systems.


## 🚀 Features

- Recommend books based on a selected title
- User-friendly web interface
- Trained model using content-based filtering
- Fast and responsive UI with dropdown search
- Deployed using Render

## 🛠️ Tech Stack

- Python
- Flask
- Pandas / NumPy
- Scikit-learn
- Pickle (for model serialization)
- HTML / CSS (frontend)
- Render (for deployment)
