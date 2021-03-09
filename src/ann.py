import streamlit as st 

def app():

    st.title('Multi-Layered Perceptrons (ANN)')
    st.write('Numerical Analysis')

    option = st.sidebar.radio('choose',['EDA','MODEL EVAL','ARCH'])

    st.markdown(option)