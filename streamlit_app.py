import streamlit

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.title('🥣 Omega 3 and blueberry oatmeal')
streamlit.title('🥗 Kale, Spinach and Rocket smoothie ')
streamlit.title('🐔 Hard-Boiled Free-Range Eggs')
streamlit.title('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
