import streamlit as st
import pandas as pd

st.title("My Recipe Decider App")

# Google Sheet Link
sheet_id = "1Ff6SAEXw6-uRlukpFfglmhBKs2Mi3SbES2TqZr0E1Lw"
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

# Read spreadsheet
try:
    df = pd.read_csv(csv_url)
    
    # Clean up the data (by removing accidental spaces)
    df.columns = df.columns.str.strip()
    df['Name'] = df['Name'].fillna('').astype(str).str.strip()
    df['Category'] = df['Category'].fillna('').astype(str).str.strip()
    df['Ingredients'] = df['Ingredients'].fillna('').astype(str).str.strip()


    meal_choice = st.radio("What meal are you eating?", ["Breakfast", "Lunch", "Dinner", "Snack"])

    st.write("You seleted", {meal_choice})

except Exception as e:
    st.error("Could not connect right now.")

