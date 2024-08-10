import pandas as pd
import streamlit as st
import ast

df=pd.read_csv("movies.csv")

st.header("Know Your Movie")
st.write("***")

# DATA CLEANING

df=df.dropna()
df = df.drop(index=3209)
df = df.drop(index=4064)
df = df.drop(index=4971)

# REMOVING ALL THE NON-ENGLISH TITLE

df=df[df.original_title.apply(lambda y : y.isascii())]
df['original_title']=df['original_title'].str.lower()

# FILTER YOUR MOVIE BY RATING

df.rename(columns={"vote_average":"rating"},inplace=True)

st.subheader("FILTER YOUR MOVIE BY RATING")

min=st.selectbox("Min Rating",(1,2,3,4,5,6,7,8,9,10))
max=st.selectbox("Max Rating",(1,2,3,4,5,6,7,8,9,10))

filter_data=df[df.rating.apply(lambda y: min<=y<=max)]

st.write(filter_data)

st.write("***")

# FILTER YOUR MOVIE BY GENRE

st.subheader("FILTER YOUR MOVIE BY GENRE")

df['genre_names'] = df['genre_names'].apply(ast.literal_eval)

genre = ['Drama','Crime','History','Comedy','Romance','Animation','Family','Fantasy','Thriller','Adventure','Western','Action','War','Science Fiction','Music','Mystery','History','TV Movie']

select_genre=st.multiselect("Genre",genre,genre)

filter_by_genre=df[df.genre_names.apply(lambda y: all(i in select_genre for i in y))]

st.write(filter_by_genre)

st.write("***")

# ABOUT YOUR MOVIE

st.subheader("ABOUT YOUR MOVIE")

movie_name=st.text_area("Enter the movie name:",placeholder="Movie Name").lower()

movie_desc=df[df.original_title==movie_name]["overview"]
movie_rating=df[df.original_title==movie_name]["rating"]
movie_release_date=df[df.original_title==movie_name]["release_date"]
if not movie_desc.empty:
   st.write("Release Date: ",movie_release_date.iloc[0])
   st.write("Description: ",movie_desc.iloc[0])
   st.write("Rating: ",round(movie_rating.iloc[0],1),"/10")
