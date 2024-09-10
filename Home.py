import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlalchemy

# Function to load data
@st.cache_data
def load_data():
    try:
        conn = sqlalchemy.create_engine("postgresql://postgres:.@localhost:5432/telecom")
        return pd.read_sql("SELECT * FROM xdr_data", conn)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Load data
df = load_data()

# Set page title
st.title("Telecom Data - Exploratory Data Analysis")

# Sidebar for navigation
st.sidebar.title("Dashboard Navigation")
page = st.sidebar.radio("Select a page:", 
                         ["User Overview Analysis", 
                          "User Engagement Analysis", 
                          "Experience Analysis", 
                          "Satisfaction Analysis"])

# ---- User Overview Analysis ----
if page == "User Overview Analysis":
    st.subheader("User Overview Analysis")
    st.write("Initial Data")
    st.write(df.head())

    # Handle Missing Values
    st.subheader("Handle Missing Values")
    missing_columns = df.columns[df.isnull().any()].tolist()
    if missing_columns:
        missing_column = st.selectbox("Choose a column to fill missing values", missing_columns)
        fill_method = st.radio("Fill method", ["Fill with Mean", "Fill with Median", "Drop Rows"])

        if st.button("Apply Fill"):
            if fill_method == "Fill with Mean":
                df[missing_column] = df[missing_column].fillna(df[missing_column].mean())
            elif fill_method == "Fill with Median":
                df[missing_column] = df[missing_column].fillna(df[missing_column].median())
            else:
                df = df.dropna(subset=[missing_column])
            st.success(f"{missing_column} cleaned successfully")
    else:
        st.info("No missing values in the dataset.")

    # Descriptive Statistics
    st.subheader("Descriptive Statistics")
    st.write(df.describe())

    # Plotting
    st.subheader("Distribution of a Selected Numeric Feature")
    numeric_column = st.selectbox("Choose a numeric column to visualize", df.select_dtypes(include=['float64', 'int']).columns)
    plt.figure(figsize=(10, 4))
    sns.histplot(df[numeric_column], bins=20, kde=True)
    plt.title(f"Distribution of {numeric_column}")
    st.pyplot(plt)

# ---- User Engagement Analysis ----
elif page == "User Engagement Analysis":
    st.subheader("User Engagement Analysis")
    st.write("Handset Type Distribution")

    if 'Handset Type' in df.columns:
        handset_counts = df['Handset Type'].value_counts()
        st.bar_chart(handset_counts)

        # Plotting
        plt.figure(figsize=(10, 4))
        sns.countplot(x='Handset Type', data=df)
        plt.title("Count of Users by Handset Type")
        plt.xticks(rotation=45)
        st.pyplot(plt)
    else:
        st.warning("Handset Type column not found in the dataset.")

# ---- Experience Analysis ----
elif page == "Experience Analysis":
    st.subheader("Experience Analysis")
    st.write("Comparison: Handset Type vs. Total DL (Bytes)")
    df_clean = df.dropna(subset=["Handset Type", "Total DL (Bytes)"])  # Clean data

    if not df_clean.empty:
        fig, ax = plt.subplots()
        sns.boxplot(x="Handset Type", y="Total DL (Bytes)", data=df_clean, ax=ax)
        plt.title("Total Download (Bytes) by Handset Type")
        plt.xticks(rotation=90)
        st.pyplot(fig)
    else:
        st.warning("No data available for the selected analysis.")

# ---- Satisfaction Analysis ----
elif page == "Satisfaction Analysis":
    st.subheader("Satisfaction Analysis")
    st.write("Distribution of Satisfaction Scores")

    if 'Satisfaction Score' in df.columns:
        plt.figure(figsize=(10, 4))
        sns.histplot(df['Satisfaction Score'], bins=20, kde=True)
        plt.title("Distribution of Satisfaction Scores")
        st.pyplot(plt)
    else:
        st.warning("Satisfaction Score column not found in the dataset.")