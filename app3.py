import streamlit as st
import pickle

# LOADING FILES.........
movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = movies['title'].values

# Load theatre background image
theatre_image = '//Users/sanjayyadav/Downloads/photo.webp'

# Setting background image
st.image(theatre_image, use_column_width=True)

# MAKING TITLE AND BUTTON......
st.title("Movie Recommendation System")
selectvalue = st.selectbox("Select Movie: ", movies_list)

# USED FUNCTION TO RECOMMEND MOVIES WHICH ARE SIMILAR...........
def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie = []

    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

# MADE BUTTON TO WORK AND RECOMMEND MOVIE.......
if st.button("Recommend movie"):
    movie_names = recommend(selectvalue)

    st.write("Recommended Movies:")
    for movie_name in movie_names:
        st.write(movie_name)
