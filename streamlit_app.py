import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.title('🥣 Omega 3 and blueberry oatmeal')
streamlit.title('🥗 Kale, Spinach and Rocket smoothie ')
streamlit.title('🐔 Hard-Boiled Free-Range Eggs')
streamlit.title('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display the table on the page.
streamlit.dataframe(fruits_to_show)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  frustyvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return frustyvice_normalized
  
#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you Like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.") 
  else:
  back_from_function = get_fruityvice_data(fruit_choice)
  streanlit.dataframe(back_from_function)
  
# try:
#   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#     streamlit.error("Please select a fruit to get information")
#   else:
#     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#     streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()
#streamlit.text(fruityvice_response.json())
#line31:streamlit.write('The user entered ', fruit_choice)
# altering data into normalized format 
# getting the normalized data into dataframe
streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
add_my_fruit = streamlit.text_input('What fruit would you like to add')
my_cur.execute("insert into fruit_load_list values ('" + add_my_fruit + "')")
my_data_row = my_cur.fetchone()
streamlit.write('thanks for adding ' + add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
