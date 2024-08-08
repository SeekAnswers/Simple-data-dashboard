#1)Importing needed libraries - Streamlit, Pandas and Matplotlib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#2) Creating title for application
st.title("Seek Answers Simple Data dashboard")
#3) Creating a file upload button or window
uploaded_file = st.file_uploader('Choose a CSV file', type = 'csv')

#Let's explore how this works in the backend
if uploaded_file is not None:
    #st.write('File uploaded...') #Anytime user uploads a file, entire script would be rerun
    df = pd.read_csv(uploaded_file) #If we want to read this in as a Pandas dataframe and write the Pandas dataframe
    
#4)Display a subtitle
    st.subheader('Data Preview')
#5)Writing the dataframe
    st.write(df.head())
#6)Writing the data summary(basically a statistical summary)
    st.subheader('Data Summary')
    st.write(df.describe())
#7)Filtering the data
    st.subheader('Filter Data')
    #Here, let's pass in some widgets the user could interact with
    #So, one can gather the unique columns available
    columns = df.columns.tolist()
    selected_column = st.selectbox('select column to filter by', columns) #st.selectbox gives us a dropdown list of all the values we pass to
    #The unique values from the selected column can be grabbed
    unique_values = df[selected_column].unique() #with this we can select a value within a column and grab all of the different rows that match the value
    selected_value = st.selectbox('Select value', unique_values)
#8)Next, we can display the filtered data and plot it on screen
    #filtered_df = df[selected_value].plot.line  #I wonder what this does
    filtered_df = df[df[selected_column] == selected_value] #This is grabbing all of the rows where the dataframe at the selected column is equal to the selected value
    st.write(filtered_df) #write   can as well do the displaying on streamlit
#9)Now to drawing up a plot
    st.subheader('Plot Data')
    #We would then select the x and y column we want to plot
    x_column = st.selectbox('Select x-axis column', columns)
    y_column = st.selectbox('Select y-axis column', columns)

    #So a button can be generated for selection of what parameter(s)/variable(s) that would occupy the x and y-axis
    if st.button('Generate Plot'):
        st.line_chart(filtered_df.set_index(x_column) [y_column])

else:
    st.write('Waiting on file upload...')
