import streamlit as st
import pickle
import pandas as pd

# Recommendation function
def recommend(movie):
    # Find the index of the selected movie
    movie_index = movies[movies['title'] == movie].index[0]
    # Get similarity scores for the selected movie
    distances = similarity[movie_index]
    # Sort movies based on similarity scores
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Get recommended movie titles
    recommended_movies = []
    for i in movies_list:
        movie_id =[0]

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load movie data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))  # Use correct file name for similarity matrix

# Streamlit app title
st.title('Movie Recommender System')

# Dropdown menu to select a movie
selected_movie_name = st.selectbox(
    "Select a movie:",
    movies['title'].values
)

# Button to show recommendations
if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)


