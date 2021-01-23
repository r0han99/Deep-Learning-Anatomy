# Libraries 

import streamlit as st 
# dataset dependencies 
import numpy as np
import pandas as pd 
# os dependencies
from pathlib import Path
import base64

# '''
# paths to the report files 
# pytorch = ?
# keras = ?  

# '''

# image encoding 
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

@st.cache(persist=True)
def read_catalog():
    
    catalog = pd.read_csv('./catalog.csv')
    paths = list(catalog['path'])
    projects = list(catalog['project'])
    
    return catalog, paths, projects

@st.cache(persist=True)
def read_meta(df_slice):

    report = pd.read_csv(df_slice['path'][0])
    
    return report

    
def cs_body(report):

    st.write(report)
    st.markdown('Report progress')

    






def cs_main():

    '''
    A line to read the report paths
    
    '''
    


    tagline = 'A comprehensive approach to attain the Deep Learning Knowledge'
    st.markdown('''<h1>Deep Learning Anatomy  <img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64><br><p style='font-style: italic; font-size:15px; text-align:left;'>{}</p></h1>'''.format(img_to_bytes("deep-learning.png"),tagline),unsafe_allow_html=True)
    
    st.sidebar.markdown("<h2 style='font-family:century gothic;'>Project Catalog 📓</h2>",unsafe_allow_html=True)
    st.sidebar.markdown('***')
    
    # '''
    # here lies a function call which reads the report.csv -> dataframe 
    # variable decompositon for the application:
    #     - project-name column is decomposed or translated into a list to feed it to the select-box 
        
    # addtional functions:
    #     - subroutine to extract summary and framworks from the two csv after the project selection and radio selection has been done

    
    # Type, project-name, Framework ,Architecture, Layers, Hidden Units, Activations: list, Epochs, Metric, Score, summary

    # '''

    catalog, paths, projects = read_catalog() # read paths 
    
    project = st.sidebar.selectbox('Project',projects, key='project-name')  
    framework  = st.sidebar.radio("Framework", ("Pytorch", "Keras"), key='Deep-Learning-frameworks')
    
     # slice according to the project name 

    st.sidebar.markdown('***') 

    
    
    
    
    

    # --> function call which extracts and returns the summary of the project-name from the two framework reports <--
    
    # '''
    # The Options in this selectbox needs to be dynamic in-order to employ a pipeline which is able to 
    # automate the process of updating it after each project.
            # '''

    report = read_meta(catalog[catalog['project'] == project]) # contents of report 
    
    st.markdown('***')
    

    # remove the following line 
    temp_desc = report['Desc'][0]

    st.markdown("<h3 style='font-family: century gothic'>Project Title : <bold><strong>{}</strong></bold></h3>".format(project),unsafe_allow_html=True)
    st.markdown('*Description* ~ _{}_'.format(temp_desc))

    st.markdown("<p style='font-family: century gothic;'>Implemtentation : <b><i>{}</i></b></p>".format(framework),unsafe_allow_html=True)

    st.markdown('***')

    st.markdown("<p style='font-family: century gothic;'>Network Architechture<p>",unsafe_allow_html=True)
    
    
    cs_body(report)





if __name__ == '__main__':
    cs_main()
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64>](https://github.com/r0han99/) <small><i>Database of My Knowledge</i></small>'''.format(img_to_bytes('./tesseract.png')), unsafe_allow_html=True)
