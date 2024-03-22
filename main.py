import pandas as pd
import streamlit as st

df = pd.read_csv('data.csv')

def get_similar_or_higher_quality_items(df, item_number):
    # Define the order of quality from lowest to highest
    quality_order = ['BTI', 'Low', 'Medium', 'High']
    
    # Find the quality of the selected item
    selected_quality = df.loc[df['Item Number'] == item_number, 'Quality'].values[0]
    
    # Check for an invalid selected item or quality
    if selected_quality not in quality_order:
        return 'Invalid item number or quality.'
    
    # Get all items with the selected or next higher quality
    if selected_quality == 'High':
        # For 'High' quality, return all items with 'High' quality
        similar_quality_items = df[df['Quality'] == 'High']['Item Number'].tolist()
    else:
        # Find the index of the selected quality and get the next higher quality
        next_quality_index = quality_order.index(selected_quality) + 1
        if next_quality_index < len(quality_order):
            next_quality = quality_order[next_quality_index]
            similar_quality_items = df[df['Quality'] == next_quality]['Item Number'].tolist()
        else:
            return 'No recommendations'  # This case should not happen given the quality order

    # If there are no items of the required quality, return 'No recommendations'
    if not similar_quality_items:
        return 'No recommendations'

st.set_page_config(page_title="Product Recommendation", page_icon=":robot:", layout="centered")
st.header("Product Recommendation")

st.image(image='recommendation.jpeg', width=500)

st.markdown("## Please enter your Item Number")


def get_text():
    input_text = st.text_area(label="Question", label_visibility='collapsed', placeholder="Please enter the product description...", key="text_input")
    return input_text

item_number = int(get_text())

st.write("Product Recommendations: ")

if item_number:
    response = get_similar_or_higher_quality_items(df, item_number)

    st.write(response)