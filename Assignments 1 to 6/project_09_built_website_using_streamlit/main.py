import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple data Dashboard")


uploaded_files = st.file_uploader("Choose a CSV file",type="csv")


if uploaded_files is not None:
    st.write("File uploaded!...")
    df = pd.read_csv(uploaded_files)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader('Filter data')
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select columns to filter by",columns)

    unique_values = df[selected_columns].unique()
    selected_values = st.selectbox("Select values",unique_values)
    

    filtered_df = df[df[selected_columns] == selected_values]
    st.write(filtered_df)

    st.subheader("PLot data")

    x_column = st.selectbox("select x-axis column",columns)
    y_column = st.selectbox("select y-axis column",columns)
     

    if st.button("Generate PLot"):
        st.line_chart(filtered_df[[x_column, y_column]].set_index(x_column))
    else:
         st.write("No file uploaded yet.")