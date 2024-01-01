# Movie Recommendation System
## Overview
This project implements a content-based movie recommendation system that suggests similar movies based on various criteria such as plot/summary, actors, and directors. Cosine similarity metric is used to calculate similarities among the movies in the database. I have used Streamlit to create an interactive webpage where the user enters the title of the movie they like and the system displays the top 5 recommendations based on the calculated cosine similarities. 

[Click here](https://movie-recommendation-system-tqjyipepfpzyjtbrlcyevp.streamlit.app/) to check out the website!

## Screenshot
![image](https://github.com/hansika-sachdeva/Movie-Recommendation-System/assets/91721473/3b55b5f0-6010-41e9-89d4-669a5364ba45)

## Technologies Used
- Programming language - Python
- Machine learning libraries - Numpy, Pandas, Scikit-learn, nltk
- Requests - python library to get data from TMDB API
- Streamlit - python framework for creating the webpage

## Dataset
TMDB 5000 Movie Dataset (https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## How to use
### Installation
1. Clone the repository to your local machine.
2. Install the required dependencies by running the following code in the terminal:
   
   ```
   pip install -r requirements.txt
   ```
### Running the system
1. Replace API_KEY in the ```app.py``` with your own TMDB API key.
2. Open the terminal from your project directory and run the Streamlit app by executing the following command:
   
   ```
   streamlit run app.py
   ```
4. The webpage will automatically open in your default browser or type ```http://localhost:8501``` in the address bar of your browser.
5. Input the title of a movie to receive recommendations.

### How to get the API key?
Create an account on [https://www.themoviedb.org/](https://www.themoviedb.org/) .Click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. You will see the API key in your API sidebar once your request is approved.

