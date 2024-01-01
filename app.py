import os
import streamlit as st
import pickle
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def fetch_poster(movie_id):  # gets posters from the api
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']  # full path of image


def recommend(movie):  # returns recommended movies with their posters
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    similar_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # taking top 5 movies

    movie_names = []  # for movies
    movie_posters = []  # for posters

    for i in similar_movies:
        movie_names.append(movies.iloc[i[0]].title)  # adding names of the recommended movies
        # fetch poster from api
        movie_id = movies.iloc[i[0]].movie_id
        movie_posters.append(fetch_poster(movie_id))

    return movie_names, movie_posters


similarity = pickle.load(open('similarity.pkl', 'rb'))  # gives all similarities from jupyter
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))  # gives movie names in form of a dictionary from jupyter
movies = pd.DataFrame(movies_dict)
st.title('Movie Recommendation System')  # title of our page
selected_movie_name = st.selectbox('Select Movie of your choice ',
                                   movies['title'].values)  # making a drop-down menu containing titles of movies

if st.button('Recommend Similar Movies'):
    names, posters = recommend(selected_movie_name)
    movie1, movie2, movie3, movie4, movie5 = st.columns(5)  # making 5 columns with names and poster of the movies
    with movie1:
        st.text(names[0])
        st.image(posters[0])
    with movie2:
        st.text(names[1])
        st.image(posters[1])
    with movie3:
        st.text(names[2])
        st.image(posters[2])
    with movie4:
        st.text(names[3])
        st.image(posters[3])
    with movie5:
        st.text(names[4])
        st.image(posters[4])
