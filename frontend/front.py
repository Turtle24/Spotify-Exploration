import streamlit as st
import time

st.title('Title of Project')
img = st.file_uploader('File uploader')
st.image('images/banner.png')

count = 100
st.progress(count)
st.spinner()
with st.spinner(text='In progress'):

    st.success('Done')
st.balloons()
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
try:
    print('Huh')
except Exception as e:
    st.exception(e)