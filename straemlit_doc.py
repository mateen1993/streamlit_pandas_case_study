import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
col1, col2 = st.columns(2)
with col1:
    st.header('Learning Streamlit')
    st.subheader('Sub header')
    st.write('Normal text')
    st.markdown("""
    ### Fav Movies
    - race 3
    - housful
    """)
with col2:
    st.code("""
    def foo (input):
        return foo ** 2
    x = foo (2)
        """)
    st.latex('x^2 + y^2 + 2 = 0')

    df = pd.DataFrame({
    'name':['sam', 'rat', 'oyo'],
    'marks': [50,60,70],
    'package':[10,12,14]
    })
    st.dataframe(df)

    st.metric('Revenue', 'Rs 3L', '3%')

    st.json({
    'name':['sam', 'rat', 'oyo'],
    'marks': [50,60,70],
    'package':[10,12,14]
    })

#st.image('image.jpg') st.vedio('video.mp4')

st.sidebar.title('Sidebar')

#col1, col2 = st.columns(2)
st.error('login failed')
st.success('success')
st.info('info')
st.warning('warning')

bar = st.progress(0)
for i in range(1,101):
    time.sleep(0.1)
    #bar.progress(i)

email = st.text_input('Enter email')
age = st.number_input('Enter age')
date = st.date_input('Enter registration date') 

# user input , button
email = st.text_input('Enter email')
password = st.text_input('Enter Password')
gender = st.selectbox('Select Gender', ['male', 'female', 'others'])

btn = st.button('Submit')
#if button is clicked
if btn:
    if email == 'abc@gmail.com' and password == '1234':
        st.success('login successful')
        #st.balloons()
        st.write(gender)
    else:
        st.error('login failed')

   # file upload  
file =  st.file_uploader('upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())