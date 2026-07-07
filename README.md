# 🎬 Movie Recommendation System

An interactive **Content-Based Movie Recommendation System** built using **Machine Learning, Python, Scikit-learn, and Streamlit**. The application recommends movies similar to a user's selected movie by analyzing movie metadata such as genres, cast, crew, keywords, and overview using **CountVectorizer** and **Cosine Similarity**.

## 🌐 Live Demo

🚀 **Streamlit App:**  
https://movie-recommendation-system-6jwfxbvkappk3wfqj27z3v.streamlit.app/

---

## 📌 Project Overview

This project implements a **Content-Based Recommendation Engine** that suggests movies with similar characteristics based on their metadata. Movie features such as genres, keywords, cast, crew, and overview are combined into a single feature vector using **CountVectorizer**, and movie similarity is calculated using **Cosine Similarity**.

The application is built with **Streamlit** and integrates the **TMDB API** to display movie posters, ratings, release year, runtime, and genres for each recommendation.

---

## ✨ Features

- 🎥 Recommend top 5 similar movies instantly
- 🖼️ Display movie posters using the TMDB API
- ⭐ Show movie ratings
- 📅 Show release year
- ⏱️ Display runtime
- 🎭 Display genres
- ⚡ Fast recommendation engine using a precomputed similarity matrix
- 🎨 Modern and responsive Streamlit UI
- ☁️ Deployed on Streamlit Cloud

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests
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
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
├── runtime.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

1. Load the TMDB Movies and Credits datasets.
2. Merge both datasets.
3. Perform data cleaning and feature engineering.
4. Combine genres, keywords, cast, crew, and overview into a single feature.
5. Convert text into numerical vectors using **CountVectorizer**.
6. Compute **Cosine Similarity** between movies.
7. Recommend the top 5 most similar movies.
8. Fetch movie posters and metadata using the **TMDB API**.

---

## 📊 Dataset

This project uses the **TMDB 5000 Movies Dataset**, containing metadata for approximately **5,000 movies**, including movie titles, genres, keywords, cast, crew, overview, ratings, release dates, and runtime.

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/DevendraKumar577/movie-recommendation-system.git
```

Move to the project directory

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

## 💻 Usage

1. Select your favourite movie.
2. Click **Recommend Movies**.
3. Instantly receive five similar movie recommendations with posters and movie details.

---

## 🚀 Project Highlights

- Developed a Content-Based Movie Recommendation System using Machine Learning.
- Built a recommendation engine using **CountVectorizer** and **Cosine Similarity**.
- Integrated the **TMDB API** to fetch real-time movie posters and metadata.
- Designed a modern, responsive Streamlit interface.
- Successfully deployed the application on **Streamlit Cloud**.

---

## 📈 Future Improvements

- Hybrid Recommendation System
- Collaborative Filtering
- Personalized User Recommendations
- Genre-based Filtering
- Movie Search Autocomplete
- User Authentication
- Watchlist Feature

---

## 👨‍💻 Author

**Devendra Kumar**

- GitHub: https://github.com/DevendraKumar577

---

## ⭐ Support

If you found this project useful, please consider giving this repository a **⭐ Star** on GitHub.
