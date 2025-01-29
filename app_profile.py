import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Mr. Nemadzhilili Rudzani"
field = "Computational Chemistry"
institution = "University of Venda"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# background
st.header("Master of Science (MSc) in Computational Chemistry")
st.write("University of Venda | 2025 – Present")

st.header("Bachelor of Science Honours in Computational Chemistry")
st.write("University of Venda | 2024")

st.header("Bachelor of Science (BSc) in Chemistry")
st.write("University of Venda | 2021 – 2023")

st.header("Skills")
st.write("Computational Chemistry: Molecular modeling, molecular dynamics simulations, docking studies, quantum chemistry calculations Software Proficiency: BIOVIA Discovery Studio, Gaussian, AutoDock, Chimera, VMD Programming & Data Analysis: Python (learning), scripting for computational chemistry applications Teaching & Demonstration: Assisting undergraduate students with practical and theoretical chemistry concepts Research & Analysis: Literature review, data interpretation, computational methodology development ")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

# Add a contact section
st.header("Contact Information")
email = "nemadzhililirudzani@gmail.com"
st.write(f"You can reach {name} at {email}.")