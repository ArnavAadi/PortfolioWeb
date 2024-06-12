import streamlit as st

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

    st.write(content)