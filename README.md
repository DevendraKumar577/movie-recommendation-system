# 🎬 Movie Recommendation System

An interactive **Content-Based Movie Recommendation System** built using **Python, Scikit-learn, NLP, Streamlit, and the TMDB 5000 Movies Dataset**. The application recommends similar movies based on their metadata, including genres, cast, crew, keywords, and movie overview.

## 🌐 Live Demo

🚀 **Try the App:**  
https://movie-recommendation-system-6jwfxbvkappk3wfqj27z3v.streamlit.app/

---

## 📌 Features

- 🎥 Recommend top 5 similar movies instantly
- 🖼️ Fetch movie posters dynamically using the TMDB API
- ⭐ Display IMDb-style ratings
- 📅 Show release year
- ⏱️ Display movie runtime
- 🎭 Show genres for every recommendation
- 🎨 Modern and responsive Streamlit UI
- 🧠 Content-Based Recommendation using Cosine Similarity
- ⚡ Fast recommendation generation using precomputed similarity matrix

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **NLTK (NLP preprocessing)**
- **TMDB API**
- **Pickle**
- **Git & GitHub**

---

## 📂 Dataset

This project uses the **TMDB 5000 Movies Dataset**, containing movie metadata such as:

- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Overview

The recommendation engine combines these features into a single text representation and computes similarity between movies using **Cosine Similarity**. Content-based recommender systems compare movie attributes rather than relying on user ratings, making them suitable for recommending similar items based on metadata. :contentReference[oaicite:0]{index=0}

---

## ⚙️ How It Works

1. Load the TMDB dataset.
2. Clean and preprocess movie metadata.
3. Merge important features:
   - Genres
   - Keywords
   - Cast
   - Crew
   - Overview
4. Apply NLP preprocessing.
5. Convert text into numerical vectors.
6. Compute the Cosine Similarity matrix.
7. Recommend the five most similar movies.
8. Fetch posters and movie information using the TMDB API.

---

## 📁 Project Structure

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

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/DevendraKumar577/movie-recommendation-system.git
```

### Move to project directory

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

## 📸 Application Preview

### 🏠 Home Page

> Add screenshot here

```
images/home.png
```

### 🎬 Recommendations

> Add screenshot here

```
images/recommendation.png
```

---

## 💡 Future Improvements

- User login system
- Collaborative Filtering
- Hybrid Recommendation System
- Personalized recommendations
- Search autocomplete
- Movie trailers integration
- Watchlist feature
- Recommendation explanation using AI

---

## 📈 Project Highlights

- Built a Content-Based Recommendation Engine
- Implemented NLP-based feature engineering
- Used Cosine Similarity for movie matching
- Integrated TMDB API for real-time movie information
- Developed an interactive Streamlit web application
- Deployed on Streamlit Cloud

---

## 👨‍💻 Author

**Devendra Kumar**

- GitHub: https://github.com/DevendraKumar577
- LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ If you found this project useful

Please consider giving this repository a **Star ⭐**.
