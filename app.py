# from typing import List, Any
# import movies as movies
import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
            movie_id))
    data = response.json()
    #print(data)

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


movies_dicts = pickle.load(open('movie_dicts.pkl', 'rb'))
movies = pd.DataFrame(movies_dicts)
movie_list = pickle.load(open('movie_list.pkl', 'rb'))
movie_list = movie_list['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))
#...........st.image('C:\Users\Tejitha nakka\PycharmProjects\clone-movie\images\BGOO.png')
st.title('Movie Recommendation System')
assert isinstance(movie_list, object)
selected_movie_name = st.selectbox(
    "You would like to check for:",
    movie_list)
st.write(selected_movie_name)
#..............t.header('The related items to your search are... ')
if st.button('Search for Recommendations'):
    with st.sidebar:
        import time
        with st.empty():
            for seconds in range(6):
                st.write(f"⏳ {seconds} seconds have passed")
                time.sleep(1)
            st.header("✔️ Wait over!")
        st.subheader("We will introduce the player soon...")
    st.header('The related items to your search are... ')
    #print the recomendations
    names, posters = recommend(selected_movie_name)
    coll0, col2, col3, col4, col5 = st.columns(5)
    with coll0:
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
if st.button('Load More Recommendations'):
    with st.sidebar:
        import time

        with st.empty():
            for seconds in range(6):
                st.write(f"⏳ {seconds} seconds have passed")
                time.sleep(1)
            st.header("✔️ Wait over!")
        st.subheader("We will introduce the player soon...")
    st.header('The related items to your search are... ')
    #st.write(selected_movie_name)
    #st.image(fetch_poster(selected_movie_name))
    names, posters = recommend(selected_movie_name)
    coll0, col2, col3, col4, col5 = st.columns(5)
    with coll0:
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
    names, posters = recommend(selected_movie_name)
    coll6, col7, col8, col9, col10 = st.columns(5)
    with coll6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])
else:
    print(".")