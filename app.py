import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv  # Import dotenv
import getpass
import matplotlib.pyplot as plt
from langchain_groq import ChatGroq
from autoviz.AutoViz_Class import AutoViz_Class

# Load environment variables from .env file
load_dotenv()

# Set up API key from the environment
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.warning("⚠️ GROQ_API_KEY not set in the environment. Please set it in the .env file.")

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=1024,
    timeout=30,
    max_retries=2,
)

def analyze_with_groq(prompt):
    """Send a prompt to Groq LLM and return the response."""
    messages = [("human", prompt)]
    response = llm.invoke(messages)
    return response.content  # Extract text from response

def identify_dimensions_measures(df):
    """Identify dimensions (categorical) and measures (numerical) from the dataset."""
    dimensions = [col for col in df.columns if df[col].dtype == 'object']
    measures = [col for col in df.columns if df[col].dtype in ['int64', 'float64']]
    return dimensions, measures

# Streamlit UI
st.title("📊 AI-Powered Sales Data Analyzer with Groq & AutoViz")

# File Upload
uploaded_file = st.file_uploader("📂 Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Check file type and read accordingly
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    
    st.success("✅ File uploaded successfully!")

    # Identify Dimensions & Measures
    dimensions, measures = identify_dimensions_measures(df)

    # Display Identified Columns
    st.subheader("📌 Identified Columns")
    st.write(f"**Dimensions (Categorical Variables):** {', '.join(dimensions)}")
    st.write(f"**Measures (Numerical Variables):** {', '.join(measures)}")

    # AI-Generated Analysis Plan
    analysis_prompt = f"""
    Given the dataset below, determine:
    1. What **descriptive analysis** can be done? (e.g., summary statistics, trends, distributions)
    2. What **predictive analysis** can be done? (e.g., forecasting, regression)
    3. What **prescriptive analysis** can be done? (e.g., recommendations, optimizations)
    
    Dimensions: {', '.join(dimensions)}
    Measures: {', '.join(measures)}
    
    Dataset Overview:
    {df.head(5).to_string()}
    """
    analysis = analyze_with_groq(analysis_prompt)
    st.subheader("📊 AI-Generated Analysis Plan")
    st.write(analysis)

    # Dataset Overview
    dataset_prompt = f"Explain the dataset below, describing each column and its possible meaning:\n\n{df.head(5).to_string()}"
    overview = analyze_with_groq(dataset_prompt)
    st.subheader("📌 AI-Generated Dataset Overview")
    st.write(overview)

    # Statistical Summary
    stats_prompt = f"Analyze and explain the statistical summary of the dataset:\n\n{df.describe().to_string()}"
    summary = analyze_with_groq(stats_prompt)
    st.subheader("📊 AI-Generated Statistical Summary")
    st.write(summary)

    # Display Dataset Preview
    st.subheader("📌 Preview of the Dataset")
    st.dataframe(df.head())

    # Automated Visual EDA using AutoViz
    st.subheader("📊 Automated EDA with AutoViz")

    AV = AutoViz_Class()
    dft = AV.AutoViz(
        "",
        dfte=df,
        chart_format="svg",
        verbose=0
    )

    # Display all AutoViz generated plots
    figs = [plt.figure(num) for num in plt.get_fignums()]
    for fig in figs:
        st.pyplot(fig)

    # User Queries
    st.subheader("💡 Ask the AI About Your Dataset")
    user_query = st.text_area("Enter your question about the dataset:")

    if st.button("Ask AI"):
        if user_query:
            query_prompt = f"Answer this question based on the dataset:\n\n{user_query}\n\nDataset:\n{df.head(5).to_string()}"
            answer = analyze_with_groq(query_prompt)
            st.write("🧠 AI Response:")
            st.write(answer)
        else:
            st.warning("⚠️ Please enter a question!")

else:
    st.info("📂 Please upload a CSV or Excel file to proceed.")
