# 📊 AI-Powered Sales Data Analyzer with Groq & AutoViz

This is a Python-based web application built with **Streamlit**, **Groq**, and **AutoViz** for analyzing and visualizing sales data. The app provides automatic analysis of sales data, including descriptive, predictive, and prescriptive analysis, and also generates visualizations using the AutoViz library.

## Features

- **Upload CSV/Excel**: Users can upload CSV or Excel files containing sales data for analysis.
- **AI-Generated Analysis Plan**: The app uses **Groq LLM** to generate insights and suggestions for descriptive, predictive, and prescriptive analysis.
- **Dimensions & Measures Identification**: Automatically identifies categorical variables (Dimensions) and numerical variables (Measures) from the dataset.
- **Automated EDA**: Utilizes **AutoViz** for generating visualizations based on the uploaded data.
- **Custom AI Queries**: Users can ask custom questions related to the dataset, and Groq LLM will generate responses based on the data.

## Video Demo

To get a quick overview of how this app works, check out the following video:

[Watch the Demo](https://drive.google.com/file/d/1foBIQrQnvD803oiiUUeVYTr4qILDGu1L/view?usp=sharing)

## Requirements

- **Python 3.x**
- **Streamlit**: For building the web app.
- **pandas**: For data manipulation and analysis.
- **matplotlib**: For generating plots.
- **langchain_groq**: For interacting with the Groq LLM.
- **AutoViz**: For automated visualizations.

### Install Required Libraries

To run this app locally, first install the required dependencies:

```bash
pip install -r requirements.txt
