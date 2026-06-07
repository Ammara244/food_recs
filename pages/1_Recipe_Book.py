import streamlit as st
import pandas as pd

st.title("Recipes")
st.write("Browse through all the recipes available")

sheet_id = "1Ff6SAEXw6-uRlukpFfglmhBKs2Mi3SbES2TqZr0E1Lw"
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

try:
    df = pd.read_csv(csv_url)
    df.columns = df.columns.str.strip()
    df['Name'] = df['Name'].fillna('').astype(str).str.strip()
    df['Category'] = df['Category'].fillna('').astype(str).str.strip()
    df['Ingredients'] = df['Ingredients'].fillna('').astype(str).str.strip()

    for index, row in df.iterrows():
        if not row['Name']:
            continue
            
        st.subheader(f"{row['Name']} ")
        st.caption(f"Categories: {row['Category']}")
        st.write("**Ingredients needed:**")
        
        ingredient_list = [ing.strip() for ing in row['Ingredients'].split(',')]
        for ing in ingredient_list:
            if '/' in ing:
                st.write(f"- either {ing}")
            else:
                st.write(f"- {ing}")
        st.write("---")

except Exception as e:
    st.error("Could not connect to the spreadsheet.")
