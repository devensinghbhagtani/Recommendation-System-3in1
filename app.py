import streamlit as st
import pickle
import pandas as pd
import requests
import numpy as np
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title=None, options=["", " ", "  "],
    icons=['film', 'music-note-beamed', 'book'], menu_icon="cast", default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important"},
        "icon": {"color": "white", "font-size": "16px"},
        "nav-link": {"padding": "10px", "font-weight": "normal", "font-size": "15px", "text-align": "center", "margin": "0px", "--hover-color": "#7d4848"},
        "nav-link-selected": {"text-align": "center", "font-weight": "normal", "font-size": "15px"},
    }

)

if selected == "":
    def fetch_poster(movie_title, year, movie_id):
        response = requests.get('https://www.omdbapi.com/?i={}&apikey=3ac1a5bd'.format(movie_id))
        data = response.json()
        if 'Error' in data:
            response = requests.get('https://www.omdbapi.com/?t={}&y={}&apikey=3ac1a5bd'.format(movie_title, year))
            data = response.json()
        return data['Poster']

    def recommend(movie):

        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]
        recommended_movies = []
        recommended_movies_posters = []
        print(selected_movie_name)
        for i in movies_list:
            movie_id = movies.iloc[i[0]].title
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id, movies.iloc[i[0]].year, movies.iloc[i[0]].movie_id ))
        return recommended_movies, recommended_movies_posters


    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    similarity = pickle.load(open('similarity.pkl', 'rb'))
    st.title('Movie Recommender')
    selected_movie_name = st.selectbox(
        'Select a Movie for Recommendations:',
        movies['title'].values)

    if st.button('Recommend'):
        names, posters = recommend(selected_movie_name)
        num_recommendations = len(names)

        num_columns = 4
        num_rows = 2
        image_width = 150
        image_height = 225

        cols = st.columns(num_columns)

        for i in range(num_recommendations):
            with cols[i % num_columns]:
                st.write(names[i])
                st.markdown(
                    f'<div style="width:{image_width}px; height:{image_height}px; overflow:hidden; position:relative; margin-bottom:30px;">'
                    f'<img src="{posters[i]}" style="width:{image_width}px; height:{image_height}px; object-fit:cover; position:absolute; top:0; left:0;">'
                    f'</div>',
                    unsafe_allow_html=True)

if selected == " ":
    def recommendmusic(music):
        music_index = songs[songs['music_name'] == music].index[0]
        distances = similaritymusic[music_index]
        music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
        recommended_music = []
        recommended_music_posters = []
        print(selected_music_name)
        for i in music_list:
            recommended_music.append(songs.iloc[i[0]].music_name)
            recommended_music_posters.append(songs.iloc[i[0]].thumbnail)
        return(recommended_music, recommended_music_posters)

    music_dict = pickle.load(open('music_dict.pkl', 'rb'))
    songs = pd.DataFrame(music_dict)
    similaritymusic = pickle.load(open('similarmusic.pkl', 'rb'))

    st.title('Music Recommender')
    selected_music_name = st.selectbox(
        'Select a Song for Recommendations:',
        songs['music_name'].values)

    if st.button('Recommend'):
        names, posters = recommendmusic(selected_music_name)
        num_recommendations = len(names)

        num_columns = 3
        num_rows = (num_recommendations + num_columns - 1) // num_columns
        image_width = 225
        image_height = 150
        cols = st.columns(num_columns)

        for i in range(num_recommendations):
            with cols[i % num_columns]:
                st.write(names[i])
                st.markdown(
                    f'<div style="width:{image_width}px; height:{image_height}px; overflow:hidden; position:relative; margin-bottom:30px;">'
                    f'<img src="{posters[i]}" style="width:{image_width}px; height:{image_height}px; object-fit:cover; position:absolute; top:0; left:0;">'
                    f'</div>',
                    unsafe_allow_html=True)

if selected == "  ":
    def recommend_book(book_name):
        index = np.where(pt.index == book_name)[0][0]
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:9]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)
        return data, data

    pt_df = pickle.load(open('pt.pkl', 'rb'))
    pt = pd.DataFrame(pt_df)
    similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
    books_df = pickle.load(open('books.pkl', 'rb'))
    books = pd.DataFrame(books_df)

    st.title('Book Recommender')
    selected_book_name = st.selectbox(
        'Select a Book for Recommendations:',
        pt.index)

    if st.button('Recommend'):
        names, posters = recommend_book(selected_book_name)
        num_recommendations = len(names)

        num_columns = 4
        num_rows = (num_recommendations + num_columns - 1) // num_columns
        image_width = 125
        image_height = 225
        cols = st.columns(num_columns)

        for i in range(num_recommendations):
            with cols[i % num_columns]:
                st.write(names[i][0])
                st.markdown(
                    f'<div style="width:{image_width}px; height:{image_height}px; overflow:hidden; position:relative; margin-bottom:30px;">'
                    f'<img src="{posters[i][2]}" style="width:{image_width}px; height:{image_height}px; object-fit:cover; position:absolute; top:0; left:0;">'
                    f'</div>',
                    unsafe_allow_html=True)