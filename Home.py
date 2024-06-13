import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.JPG",)

with col2:
    st.title("Arnav Aggarwal")
    content = """"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ultrices lectus libero, at pellentesque ex laoreet ac. Sed pellentesque diam nec ipsum volutpat cursus. Suspendisse quis lectus mauris. Phasellus nibh elit, imperdiet ut orci sit amet, laoreet consectetur nibh. Integer sit amet ante at orci posuere fringilla. In ex erat, dignissim molestie aliquet eu, lobortis consequat odio. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum efficitur dignissim bibendum. 
    Praesent feugiat turpis et eleifend venenatis. 
    """

    st.info(content)

st.write("<h4>Below you can find some apps made by me. Feel free to contact me</h4>", unsafe_allow_html=True)


col3, empty_col, col4= st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:

    for index, row in df.iterrows():
        if index<10:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{row['image']}")
            st.write(f"[Source Code]({row['url']})")

with col4:

    for index, row in df.iterrows():
        if index>9:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{row['image']}")
            st.write(f"[Source Code]({row['url']})")