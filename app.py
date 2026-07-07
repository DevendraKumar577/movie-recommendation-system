import streamlit as st
import pandas as pd
import pickle
import requests
from datetime import datetime

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:1rem;
padding-bottom:2rem;
padding-left:3rem;
padding-right:3rem;
}

.hero{

padding:38px;

border-radius:22px;

background:linear-gradient(135deg,#1E3A8A,#2563EB);

color:white;

margin-bottom:25px;

box-shadow:0 16px 40px rgba(37,99,235,.28);

text-align:center;

}

.hero h1{

font-size:48px;

font-weight:800;

margin-bottom:8px;

text-align:center;

}

.hero p{

font-size:18px;

opacity:0.92;

text-align:center;

max-width:900px;

margin:auto;

}

.metric{

background:#111827;

padding:18px;

border-radius:15px;

text-align:center;

border:1px solid #30363d;

transition:0.3s;

min-height:140px;
display:flex;
flex-direction:column;
justify-content:center;

}

.metric:hover{

border:1px solid #3B82F6;

transform:translateY(-6px);

box-shadow:0 12px 28px rgba(37,99,235,0.25);

transition:all .3s ease;

}

.metric h2{

color:#60A5FA;

margin:0;

font-size:34px;

}

.metric h4{

margin-top:10px;

color:white;

}

.section-title{

font-size:30px;

font-weight:700;

margin-top:30px;

margin-bottom:15px;

}

.movie-card{

background:#111827;

padding:16px;

border-radius:18px;

border:1px solid #2E3440;

overflow:hidden;

transition:.3s;

box-shadow:0 8px 18px rgba(0,0,0,.18);

margin-bottom:18px;

}

.movie-card:hover{

transform:translateY(-8px);

box-shadow:0 16px 30px rgba(37,99,235,.25);

border:1px solid #3B82F6;

}

.movie-card:hover{

transform:translateY(-8px);

box-shadow:0 18px 35px rgba(37,99,235,.25);

border:1px solid #3B82F6;

}

.movie-title{

font-size:20px;

font-weight:700;

color:white;

text-align:center;

margin-top:14px;

margin-bottom:10px;

}

.small-text{

color:#E5E7EB;

font-size:14px;

text-align:left;

padding-left:14px;

margin-bottom:6px;

}
            
.movie-info{

padding:12px;

}            

.footer{

text-align:center;

margin-top:50px;

color:gray;

}
            
.stButton > button{

width:100%;
height:52px;

background:linear-gradient(90deg,#2563EB,#1D4ED8);

color:white;

border:none;

border-radius:12px;

font-size:18px;

font-weight:600;

transition:all .3s ease;

}

.stButton > button:hover{

transform:translateY(-2px);

box-shadow:0 8px 20px rgba(37,99,235,.35);

}           

</style>
""",unsafe_allow_html=True)

# --------------------------------------------------
# LOAD FILES
# --------------------------------------------------

movies = pickle.load(open("movie_list.pkl","rb"))

similarity = pickle.load(open("similarity.pkl","rb"))

movie_list = movies["title"].values

# --------------------------------------------------
# API
# --------------------------------------------------

API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

# --------------------------------------------------
# FUNCTIONS
# --------------------------------------------------

def get_movie_details(movie_id):

    url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    try:

        data=requests.get(url).json()

        poster=None

        if data.get("poster_path"):

            poster="https://image.tmdb.org/t/p/w500"+data["poster_path"]

        return{

            "poster":poster,

            "overview":data.get("overview","Not Available"),

            "rating":data.get("vote_average","N/A"),

            "runtime":data.get("runtime","N/A"),

            "release":data.get("release_date","N/A"),

            "language":data.get("original_language","N/A"),

            "genres":", ".join([g["name"] for g in data.get("genres",[])])

        }

    except:

        return None
    
def recommend(movie):

    index = movies[movies["title"] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    for i in distances[1:6]:

        movie_id = movies.iloc[i[0]].movie_id

        details = get_movie_details(movie_id)

        recommended_movies.append({

            "title": movies.iloc[i[0]].title,

            "movie_id": movie_id,

            "details": details

        })

    return recommended_movies


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🎬 Movie AI")

    st.markdown("---")

    st.subheader("📌 About Project")

    st.write("""
This project recommends movies using a
**Content-Based Recommendation System**
built with Machine Learning.

The similarity between movies is calculated
using cosine similarity on movie tags.
""")

    st.markdown("---")

    st.subheader("🛠 Tech Stack")

    st.markdown("""
- Python
- Pandas
- Scikit-Learn
- Streamlit
- TMDB API
""")

    st.markdown("---")

    st.subheader("📊 Dataset")

    st.write("TMDB 5000 Movies Dataset")

    st.markdown("---")

    st.caption("Developed by Devendra Kumar")


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""

<div class="hero">

<div style="
font-size:48px;
font-weight:800;
text-align:center;
margin-bottom:10px;
">
🎬 Movie Recommendation System
</div>

<p>

Discover similar movies instantly using a
Machine Learning powered Content-Based Recommendation Engine.

</p>

</div>

""", unsafe_allow_html=True)


# --------------------------------------------------
# METRIC CARDS
# --------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.markdown("""

<div class="metric">

<h2>5000+</h2>

<h4>Movies</h4>

</div>

""", unsafe_allow_html=True)

with c2:

    st.markdown("""

<div class="metric">

<h2>ML</h2>

<h4>Recommendation</h4>

</div>

""", unsafe_allow_html=True)

with c3:

    st.markdown("""

<div class="metric">

<h2>TMDB</h2>

<h4>API</h4>

</div>

""", unsafe_allow_html=True)

with c4:

    st.markdown("""

<div class="metric">

<h2>Python</h2>

<h4>Scikit-Learn</h4>

</div>

""", unsafe_allow_html=True)


st.markdown("<div class='section-title'>🎥 Select Your Favourite Movie</div>", unsafe_allow_html=True)

selected_movie = st.selectbox(
    "Select Movie",
    movie_list,
    label_visibility="collapsed"
)

recommend_button = st.button(

    "🚀 Recommend Movies",

    width="stretch"

)

# --------------------------------------------------
# SELECTED MOVIE DETAILS
# --------------------------------------------------

if selected_movie:

    selected_index = movies[movies["title"] == selected_movie].index[0]

    selected_movie_id = movies.iloc[selected_index].movie_id

    selected_details = get_movie_details(selected_movie_id)

    if selected_details:

        st.markdown("<div class='section-title'>🎥 Selected Movie</div>", unsafe_allow_html=True)

        left, right = st.columns([1, 2])

        with left:

            if selected_details["poster"]:

                st.image(selected_details["poster"], width="stretch")

        with right:

            st.subheader(selected_movie)

            st.write(selected_details["overview"])

            m1, m2 = st.columns(2)

            with m1:
                st.metric("⭐ Rating", selected_details["rating"])

                st.metric("🌍 Language", str(selected_details["language"]).upper())

            with m2:
                st.metric("⏱ Runtime", f"{selected_details['runtime']} min")

                release = selected_details["release"]

                if release != "N/A" and release:
                    year = release[:4]
                else:
                    year = "N/A"

                st.metric("📅 Release", year)

            st.markdown("### 🎭 Genres")

            st.write(selected_details["genres"])

            # --------------------------------------------------
# RECOMMENDATIONS
# --------------------------------------------------

if recommend_button:

    with st.spinner("🎬 Finding similar movies..."):

        recommendations = recommend(selected_movie)

    st.markdown(
        f"""
        <div class='section-title'>
            🎬 Top 5 Recommendations for
            <span style="color:#2563EB;">{selected_movie}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(5)

    for col, movie in zip(cols, recommendations):

        details = movie["details"]

        with col:

            if details and details["poster"]:
                st.image(details["poster"], use_container_width=True)

            st.markdown(
                f"""
                <h4 style="
                    text-align:center;
                    margin-top:12px;
                    margin-bottom:10px;
                    min-height:55px;
                    font-weight:700;
                ">
                    {movie['title']}
                </h4>
                """,
                unsafe_allow_html=True
            )

            if details:

                rating = details.get("rating", "N/A")

                release = details.get("release", "N/A")
                year = release[:4] if release and release != "N/A" else "N/A"

                runtime = details.get("runtime", "N/A")
                genres = details.get("genres", "N/A")

                st.markdown(
                    f"""
                    <div style="
                        background:#111827;
                        color:white;
                        padding:14px;
                        border-radius:12px;
                        margin-top:8px;
                        border:1px solid #2E3440;
                        min-height:155px;
                    ">

                    <p style="margin:6px 0;">⭐ <b>Rating:</b> {rating}</p>

                    <p style="margin:6px 0;">📅 <b>Year:</b> {year}</p>

                    <p style="margin:6px 0;">⏱ <b>Runtime:</b> {runtime} min</p>

                    <p style="margin:6px 0;">🎭 <b>Genres:</b> {genres}</p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

# --------------------------------------------------
# RECOMMENDATION SUMMARY
# --------------------------------------------------

# --------------------------------------------------
# RECOMMENDATION SUMMARY
# --------------------------------------------------

if recommend_button:

    st.markdown("---")

    # Create 3 columns (left, center, right)
    left, center, right = st.columns([1, 4, 1])

    with center:

        st.markdown(
            """
            <h2 style="text-align:center; margin-bottom:18px;">
            🧠 Why These Movies?
            </h2>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="
                background:#EAF3FF;
                padding:22px;
                border-radius:12px;
                text-align:center;
                font-size:18px;
                line-height:1.45;
                color:#1F2937;
            ">

            These recommendations are generated using a
            <b>Content-Based Recommendation System</b>.<br>

            The model compares movies based on their metadata (tags) and calculates their similarity using
            <b>Cosine Similarity</b>.<br>

            Movies with similar genres, keywords, cast, crew and storyline are ranked and the top similar movies are displayed.

            </div>
            """,
            unsafe_allow_html=True
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
    """
<div class="footer">

<h3>🎬 Movie Recommendation System</h3>

<p>
Built using <b>Python</b>, <b>Streamlit</b>,
<b>Scikit-Learn</b> and <b>TMDB API</b>.
</p>

<p>
Developed by <b>Devendra Kumar</b>
</p>

</div>
""",
    unsafe_allow_html=True
)