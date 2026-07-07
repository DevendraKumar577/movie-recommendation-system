# 🎬 Movie Recommendation System

An interactive **Content-Based Movie Recommendation System** built using **Machine Learning, Python, Scikit-learn, and Streamlit**. The application recommends movies similar to a user's selected movie by analyzing movie metadata such as genres, cast, crew, keywords, and overview using **CountVectorizer** and **Cosine Similarity**.

## 🌐 Live Demo

🚀 **Try the App:**  
https://movie-recommendation-system-6jwfxbvkappk3wfqj27z3v.streamlit.app/

## 📌 Project Overview

This project implements a **Content-Based Recommendation Engine** that suggests movies with similar characteristics based on their metadata. Movie features such as genres, keywords, cast, crew, and overview are combined into a single feature vector using **CountVectorizer**, and movie similarity is calculated using **Cosine Similarity**.

The application is built with **Streamlit** and integrates the **TMDB API** to display movie posters, ratings, release year, runtime, and genres for each recommendation.

---

## ✨ Features

- 🎥 Recommend top 5 similar movies instantly
- 🖼️ Fetch and display movie posters using the TMDB API
- ⭐ Display movie ratings
- 📅 Show release year
- ⏱️ Display movie runtime
- 🎭 Show movie genres
- ⚡ Fast recommendation generation using a precomputed similarity matrix
- 🎨 Modern and responsive Streamlit interface
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
5. Convert the combined text into numerical vectors using **CountVectorizer**.
6. Compute **Cosine Similarity** between all movies.
7. Recommend the top 5 most similar movies.
8. Fetch movie posters and metadata dynamically using the **TMDB API**.

---

## 📊 Dataset

This project uses the **TMDB 5000 Movies Dataset**, which contains metadata for approximately **5,000 movies**, including:

- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Overview
- Release Date
- Ratings
- Runtime

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/DevendraKumar577/movie-recommendation-system.git
```

### Navigate to the project directory

```bash
cd movie-recommendation-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 💻 Usage

1. Open the web application.
2. Select your favourite movie.
3. Click **Recommend Movies**.
4. Instantly receive five similar movie recommendations with posters and additional movie information.

---

## 🚀 Project Highlights

- Developed a Content-Based Movie Recommendation System using Machine Learning.
- Implemented a recommendation engine using **CountVectorizer** and **Cosine Similarity**.
- Integrated the **TMDB API** to fetch movie posters and metadata.
- Designed a modern, interactive, and responsive Streamlit interface.
- Successfully deployed the application on **Streamlit Cloud**.

---

## 📈 Future Improvements

- Hybrid Recommendation System
- Collaborative Filtering
- Personalized User Recommendations
- Movie Search Autocomplete
- Genre-based Filtering
- User Authentication
- Watchlist Feature
- Recently Viewed Movies

---

## 👨‍💻 Author

**Devendra Kumar**

- GitHub: https://github.com/DevendraKumar577

---

## 🌐 Live Application

https://movie-recommendation-system-6jwfxbvkappk3wfqj27z3v.streamlit.app/

---

## ⭐ Support

If you found this project useful, please consider giving this repository a **⭐ Star** on GitHub.
