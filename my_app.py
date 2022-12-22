
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("This is a title")

st.text("This is a text")

# markdown

st.markdown("#### This is markdown")

# Header/Subheader

st.header("This is a header")

st.subheader("This is a subheader")

# success/info/error/warning/exception

st.success("This is a success message")

st.info("This is a info message")

st.error("This is a error message")

st.warning("This is a warning message")

st.exception("NameError('name three not defined')")

# help

st.help(range)

# write

st.write("Hello")

st.write(range(10))

# image

img = Image.open("images.jpeg")
st.image(img, caption="Cat")

# video

st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")

# checkbox

st.checkbox("Up and Down")

cbox = st.checkbox("Hide and Seek")

if cbox:
    st.write("Hide")
else:
    st.write("Seek")

# radio button

color = st.radio("Select a color", ("red", "purple", "green"))
st.write("Your color is", color)

# button

st.button("Button")

if st.button("Click me"):
    st.success("Prediction is ...")

# select box

st.selectbox("Your color", ["Blue", "Red", "Green"])

occupation =  st.selectbox("Your occupation is", ["Programmer", "Data Scientist", "Data Analyst"])
st.write("You selected", occupation)

# multiselect

# st.multiselect("Select multiple numbers", [1,2,3,4,5])

selection = st.multiselect("Select multiple numbers", [1,2,3,4,5])
st.write("You selected", selection)

# slider

option1 = st.slider("Select a number", min_value=5, max_value=70, value=20, step=5)
option2 = st.slider("Select a number", min_value=5, max_value=70, value=20)
st.slider("Select a number", min_value=5, max_value=70)
st.slider("Select a number", min_value=5)
st.slider("Select a number", )

result = option1 * option2
st.write("Result is", result)

# text input

name = st.text_input("Enter your name", placeholder="Your name here")
if st.button("Submit"):
    st.write("Hello", name.title())

# code

st.code("import pandas as pd")
st.code("import pandas as pd\nimport numpy as np")

# echo

with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df

 # date input

import datetime
today = st.date_input("Today is", datetime.datetime.now())

st.write("Today is", today)

# time input

st.time_input(str(pd.Timestamp.now()))

# sidebar

st.sidebar.title("Sidebar title")

st.sidebar.header("Sidebar header")
a=st.sidebar.slider("input",0,5,2,1)
x=st.sidebar.slider("input2")

st.write("# sidebar input result")
st.success(a*x)

import pickle

filename = 'my_model'
model = pickle.load(open(filename, 'rb'))

# st.write(df.describe())

TV = st.sidebar.number_input("TV:",min_value=5, max_value=300)
radio = st.sidebar.number_input("radio:",min_value=1, max_value=50)
newspaper = st.sidebar.number_input("newspaper:",min_value=0, max_value=120)

my_dict = {
           "TV": TV,
           "radio": radio,
           "newspaper": newspaper
          }

df=pd.DataFrame.from_dict([my_dict])

st.table(df)

if st.button("Predict"):
    pred = model.predict(df)
    st.write(pred[0])

