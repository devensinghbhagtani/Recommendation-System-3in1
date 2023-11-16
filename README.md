# Movie-Recommendation-System-3in1 Project
This project consists of three recommendation systems for movies, music, and books. Each module is developed in separate Python notebooks and includes data scraping, data preprocessing, and recommendation functionalities.

Interactive Streamlit application providing a user-friendly interface to interact with each recommendation system.
Allows users to select a module (Movies, Music, or Books) and receive recommendations based on their choices.

## Modules
- ###  Movie Module
    File: Movie Module.pynb
    - Data preprocessing on a movie dataset obtained by web scraping IMDb.
    - Utilizes the OMDB API to fetch movie posters for recommendations
    - Utilizes cosine similarity to recommend movies based on input.

![image](https://user-images.githubusercontent.com/67409912/283428999-f9960ffe-6c1c-4112-8c5f-e4e89f19570a.png)
- ### Music Module
    File: Music Module.pynb
    - Scrapes music-related data from a source and preprocesses it.
    - Uses cosine similarity to recommend music based on user input.

![image](https://user-images.githubusercontent.com/67409912/283429025-5ae98dd2-68db-4ada-b466-e213d2b55345.png)
- ### Book Module
    File: Book Module.pynb
    - Implements a popularity-based recommendation system and collaborative filtering to suggest books.

![image](https://user-images.githubusercontent.com/67409912/283429035-edd962d5-2748-4ad8-b510-6eb1a9249cbc.png)
## About the Dataset
- Movie Dataset: Web-scraped movie dataset from IMDb containing movie details such as title, year, genre, overview, director, and cast.
- Music Dataset: Music dataset obtained through web scraping, including details like music name, singer, album, release, and lyrics.
- Book Dataset: A dataset sourced from Kaggle containing information about books, users, and ratings.
