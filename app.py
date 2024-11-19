import streamlit as st
import pickle
import pandas as pd
import requests

def fecth_poster(movie_id): 
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c34aaf89e7ee8e6b7c9d57d7cb82d1dc&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similar_movies[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_posters.append(fecth_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies, recommended_movies_posters


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similar_movies = pickle.load(open('similarity.pkl', 'rb'))

movies = pd.DataFrame(movie_dict)
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',
     movies['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    
    