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

    st.header("Our Live Recipe Box")

    # Display each recipe on screen
    for index, row in df.iterrows():
        # Skip empty rows if there are any
        if not row['Name']:
            continue
            
        st.subheader(f"{row['Name']}")
        
        # Display Categories beautifully
        st.caption(f"Categories: {row['Category']}")
        
        # Display Ingredients
        st.write("**Ingredients needed:**")
        # Split ingredients by comma so we can bullet point them
        ingredient_list = [ing.strip() for ing in row['Ingredients'].split(',')]
        for ing in ingredient_list:
            # Highlight substitutions if they use a slash '/'
            if '/' in ing:
                st.write(f"- 🔀 {ing} *(You can use either!)*")
            else:
                st.write(f"- {ing}")
                
        st.write("---") # Visual divider line

except Exception as e:
    st.error("Uh oh! Could not connect to the spreadsheet. Make sure your Google Sheet is set to 'Anyone with the link can view'.")
