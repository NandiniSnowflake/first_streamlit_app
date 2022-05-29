
import streamlit
import pandas
import requests

fruityvise_response = requests.get("https://www.fruityvice.com//api/fruit/watermelon")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.title("My Mom's New Healthy Dinner")
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected = streamlit.multiselect("pick some Fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)

streamlit.header('Fruityvise Fruit Advice!')
streamlit.text(fruityvise_response.json())
fruityvise.normalized = pandas.json_normalize(fruityvise_response.json())
streamlit.dataframe(fruityvise.normalized)
