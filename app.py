import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5bbfad7ce0f4ad426285c3f16fed7149'.format(movie_id))
     data=response.json()
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_movies=[]
     recommended_movies_posters=[]
     for i in movies_list:
          movie_id=movies.iloc[i[0]].movie_id

          recommended_movies.append(movies.iloc[i[0]].title)
          # fetch poster from api
          recommended_movies_posters.append(fetch_poster(movie_id))
     return recommended_movies,recommended_movies_posters

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('MOVIE NAME RECOMMENDER SYSTEM')

selected_movie_name = st.selectbox('Enter Movie Name',movies['title'].values)

if st.button('Recommend'):
     names, posters = recommend(selected_movie_name)

     col1, col2, col3, col4, col5 = st.columns(5)
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



import bz2file as bz2
import pickle

#def compressed_pickle(title, data):

 #with bz2.BZ2File('title' + '.pbz2', 'w') as f:
    #pickle.dump( data, f)

#compressed_pickle('similarity.pkl', similarity)

def compressed_pickle(sim, data):

 with bz2.BZ2File('sim' + '.pbz2', 'w') as f:
    pickle.dump(data, f)

compressed_pickle('title.pbz2', st.title)