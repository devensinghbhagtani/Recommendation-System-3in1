# Recommendation-System (3in1)
This project consists of three recommendation systems for movies, music, and books. Each module is developed in separate Python notebooks and includes data scraping, data preprocessing, and recommendation functionalities.

Interactive Streamlit application providing a user-friendly interface to interact with each recommendation system.
Allows users to select a module (Movies, Music, or Books) and receive recommendations based on their choices.

## Modules
- ###  Movie Module
    File: Movie-Recommender.pynb
    - Data preprocessing on a movie dataset obtained by web scraping IMDb.
    - Utilizes the OMDB API to fetch movie posters for recommendations
    - Utilizes cosine similarity to recommend movies based on input.

<img src="https://user-images.githubusercontent.com/67409912/283428999-f9960ffe-6c1c-4112-8c5f-e4e89f19570a.png" alt="Movie-Module" width="600"/>

- ### Music Module
    File: Music-Recommender.pynb
    - Scrapes music-related data from a source and preprocesses it.
    - Uses cosine similarity to recommend music based on user input.

<img src="https://user-images.githubusercontent.com/67409912/283429025-5ae98dd2-68db-4ada-b466-e213d2b55345.png" alt="Movie-Module" width="600"/>

- ### Book Module
    File: Book-Recommender.pynb
    - Implements a popularity-based recommendation system and collaborative filtering to suggest books.

<img src="https://user-images.githubusercontent.com/67409912/283429035-edd962d5-2748-4ad8-b510-6eb1a9249cbc.png" alt="Movie-Module" width="600"/>

## About the Dataset
### Dataset Collection
The datasets utilized in this project were meticulously scraped and curated to focus specifically on the latest Bollywood movies and songs, aiming to provide comprehensive details including crew information, directors, actors, and song lyrics.

 - #### Movie Dataset:
    The movie dataset comprises the latest Bollywood movies, primarily targeting recent releases. Most available datasets on the internet often featured Hollywood movies or older Indian films lacking detailed crew information necessary for generating similarity matrices. To enhance the recommendation system's accuracy, a dedicated effort was made to gather information on plots, genres, directors, and casts of these contemporary Bollywood movies.
 - #### Music Dataset:
   The music dataset is centered around the latest Bollywood music, a niche area that lacked readily available comprehensive datasets on the internet. The dataset includes song details such as artist names, release dates, and importantly, song lyrics. This detailed information was sourced from the azmusic website after considerable effort using various tools and significant time investment.
 - #### Book Dataset:
   A dataset sourced from Kaggle containing information about books, users, and ratings.
