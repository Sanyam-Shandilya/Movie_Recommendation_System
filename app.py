import streamlit as st
import pickle as pkl
import pandas as pd
import requests


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMGZkZTZlNTc5YThiMTljMjU0ZjYyZWVkNDQ1NDIyYyIsInN1YiI6IjY0Njc5ZWJiYzM1MTRjMDExZGNhNTQyNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3RwDN8IJcLsfum-ipSv5HfKGUAnGQ8FParIFk4VriH0"
}


movies_li = pkl.load(open("movies.pkl","rb"))
movies_names = movies_li["title"].values

def recommend(movie):
    simi = pkl.load(open("similarity.pkl","rb"))
    movie_ind = movies_li[movies_li["title"]==movie].index[0]
    dist = simi[movie_ind]
    li = sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:11]
    name=[]
    img=[]
    for i in li:
        ind=movies_li.iloc[i[0]].id
        url = "https://api.themoviedb.org/3/movie/"+str(ind)+"?language=en-US"
        response = requests.get(url, headers=headers)
        data = response.json()
        img.append("http://image.tmdb.org/t/p/w500/"+data["poster_path"])
        name.append(movies_li.iloc[i[0]].title)
    return name,img


st.title("Movie recommendation System")

selected_name =st.selectbox("Choose a movie for recomendation:",movies_names)
if st.button("Recommend"):
    name,img =recommend(selected_name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.image(img[0])
        st.text(name[0])
    with col2:
        st.image(img[1])
        st.text(name[1])
    with col3:
        st.image(img[2])
        st.text(name[2])
    with col4:
        st.image(img[3])
        st.text(name[3])
    with col5:
        st.image(img[4])
        st.text(name[4])
    
    col6,col7,col8,col9,col10 = st.columns(5)
    with col6:
        st.image(img[5])
        st.text(name[5])
    with col7:
        st.image(img[6])
        st.text(name[6])
    with col8:
        st.image(img[7])
        st.text(name[7])
    with col9:
        st.image(img[8])
        st.text(name[8])
    with col10:
        st.image(img[9])
        st.text(name[9])
    