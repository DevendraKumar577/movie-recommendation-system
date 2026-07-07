# 🎬 Movie Recommendation System

An interactive **Content-Based Movie Recommendation System** built using **Machine Learning, Python, Scikit-Learn, and Streamlit**. The application recommends movies similar to a user's selected movie by analyzing movie metadata such as genres, cast, crew, keywords, and overview using Natural Language Processing (NLP) techniques.

## 🌐 Live Demo

**🔗 Streamlit App:** https://movie-recommendation-system-6jwfxbvkappk3wfqj27z3v.streamlit.app/

---

## 📌 Project Overview

This project uses a **Content-Based Recommendation Engine** to suggest movies with similar characteristics. It processes movie metadata, converts textual features into numerical vectors using **CountVectorizer**, and computes similarity scores using **Cosine Similarity**.

The web application is developed using **Streamlit**, allowing users to select any movie and instantly receive five similar movie recommendations along with their posters fetched from the TMDB API.

---

## ✨ Features

- 🎥 Recommend 5 similar movies instantly
- 🖼️ Display movie posters using TMDB API
- ⚡ Fast recommendation engine using Cosine Similarity
- 🎨 Interactive Streamlit UI
- 📱 Responsive design
- 🤖 Machine Learning powered recommendation engine
- ☁️ Deployed on Streamlit Cloud

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Pickle
- TMDB API
- CountVectorizer
- Cosine Similarity

---

## 📂 Project Structure

```text
movie-recommendation-system/
│
├── app.py
├── Movie_Recommendation.ipynb
├── movie_list.pkl
├── similarity.pkl
├── requirements.txt
├── runtime.txt
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
└── README.md
```

---

## ⚙️ How It Works

1. Load the TMDB movie dataset.
2. Merge movie and credits datasets.
3. Perform feature engineering.
4. Combine genres, keywords, cast, crew, and overview into a single text feature.
5. Convert text into vectors using CountVectorizer.
6. Compute Cosine Similarity between movies.
7. Recommend the top 5 most similar movies.
8. Fetch movie posters using the TMDB API.

---

## 📊 Dataset

The project is built using the **TMDB 5000 Movie Dataset**, containing metadata for approximately **5,000 movies**, including genres, cast, crew, keywords, overviews, budgets, revenues, and ratings. :contentReference[oaicite:0]{index=0}

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/DevendraKumar577/movie-recommendation-system.git
```

Move into the project directory

```bash
cd movie-recommendation-system
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 💻 Demo

1. Select your favourite movie.
2. Click **Recommend Movies**.
3. Get five similar movie recommendations with posters instantly.

---

## 📈 Future Improvements

- Hybrid Recommendation System
- Collaborative Filtering
- Personalized User Recommendations
- Movie Search Autocomplete
- Genre-wise Filtering
- Movie Ratings Integration
- User Authentication
- Watchlist Feature

---

## 👨‍💻 Author

**Devendra Kumar**

- GitHub: https://github.com/DevendraKumar577

---

## ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.
