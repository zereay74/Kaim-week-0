import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title = 'Simple Dashboard', layout = 'wide')

with st.sidebar:
    selected_option = st.radio ('Select and option', [1,2])

st.title('Simple Streamlit Dashbored')

if selected_option == 1:
    st.header('Option 1: Upload csv data')

    uploaded_file = st.file_uploader('Choose CSV file to upload', type = 'csv')

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.subheader('Uploaded Data Review')

        data['Timestamp'] = pd.to_datetime(data['Timestamp'])  # Ensure the 'timestamp' column is in datetime format

        st.dataframe(data.head())

        st.subheader('Graph of the uploadded data')

        if st.checkbox('Show Plot'):
            if data.shape[1] >= 2:
                x_col = st.selectbox("Select X-axis column", data.columns)
                y_col = st.selectbox('Select Y-axis column', data.columns)

                fig, ax = plt.subplots(figsize = (8,4))
                ax.plot(data[x_col], data[y_col], marker = 'o', color = 'b' )
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                ax.set_title(f'{y_col} vs {x_col}')
                st.pyplot(fig)
                
            else:
                st.warning("Data must have at least two columns to plot")
    else:
        st.warning("Please Upload CSV file to diplay and plot the data")
elif selected_option == 2:
    st.warning('Display simple data and plot')

    st.subheader('Sample data preview')

    sample_data ={
        'Month': ['January', 'Feberuary', 'March', 'April', 'May', 'June'],
        'Sales': [250, 300, 450, 200, 500, 400]
    }
    df = pd.DataFrame(sample_data)
    st.dataframe(df)
    st.subheader('Sample data plot')
    fig, ax = plt.subplots(figsize = (8,4))
    ax.plot(df['Month'], df['Sales'], marker = 'o', color = 'b')
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.set_title('Monthly Sales')
    st.pyplot(fig)

    st.markdown("<h6 style = 'text-align': center;> Dashboard development using streamlit</h6>", unsafe_allow_html=True)

