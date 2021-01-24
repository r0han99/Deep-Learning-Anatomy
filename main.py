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

# @st.cache(persist=True)
def read_catalog():
    
    catalog = pd.read_csv('./catalog.csv')
    paths = list(catalog['path'])
    projects = list(catalog['project'].unique())
    
    return catalog, paths, projects

# @st.cache(persist=True,allow_output_mutation=True)
def read_meta(df_slice):

    
    try: 
        report = pd.read_csv(df_slice['path'].values[0])
        try:
            report = report.drop('Unnamed: 0',axis=1)
        except:
            pass
        return report
    except:
        
        return 'Crude'


def model_eval(model):

    st.markdown('***Real-Time Model Evaluation***')
    
    
   
    
def cs_body(report):

    # st.code(report.columns)

    st.markdown("<h3 style='font-family: Avenir; font-weight:bold; font-size:30px;'>Project Artefacts</h3>",unsafe_allow_html=True)
    st.markdown('***')
    
    # Network Type 

    st.markdown('*Network Type : *')
    st.code(report['network_type'].values[0])
    # st.markdown("<p style='font-family: century gothic;'>Network Type : {}<p>".format(),unsafe_allow_html=True)


    # Prediction Type 
    st.markdown('*Prediction Type : *')
    st.code(report['prediction_type'].values[0])

    


    # Network Architecture Pytorch
    st.markdown('*Network Architecture : *')
    st.code(report['framework'].values[0]+'\n'+report['Architecture'].values[0])


    # Number of Layers
    st.markdown('*Number of  Layers: *')
    st.code(report['layers'].values[0])

    # Number of Hidden Units
    st.markdown('*Number of Hidden Units: *')
    if str(report['hidden_units'].values[0]) == 'nan':
        st.code('None')
    else:
        st.code(report['hidden_units'].values[0])

    # activations used
    st.markdown('*Activations Used: *')
    st.code(report['Activations'].values[0])

    # Number of Epochs:
    st.markdown('*Number of Epochs: *')
    st.code(report['epochs'].values[0])

    # Metrics
    st.markdown('*Metrics: *')
    st.code(report['metrics'].values[0])
    
    # Train_Accuracy and Test Accuracy 
    st.markdown('*Train and Test Accuracy : *')
    st.code('Train - {:.2f}, Test - {:.2f}'.format(report['Train_Accuracy'].values[0],report['Test_Accuracy'].values[0]))

    # Elapsed 
    st.markdown('*Elapsed Time for Training : *')
    st.code(report['elapsed'].values[0])


    st.markdown('***')
        

    




def cs_main():

    '''
    A line to read the report paths
    
    '''

    tagline = 'A comprehensive approach to attain the Deep Learning Knowledge'
    st.markdown('''<h1>Deep Learning Anatomy  <img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64><br><p style='font-style: italic; font-size:15px; text-align:left;'>{}</p></h1>'''.format(img_to_bytes("deep-learning.png"),tagline),unsafe_allow_html=True)
    
    st.sidebar.markdown("<h2 style='font-family:century gothic;'>Project Catalog 📓</h2>",unsafe_allow_html=True)
    st.sidebar.markdown('***')
    


    catalog, paths, projects = read_catalog() # read paths 
    
    project = st.sidebar.selectbox('Project',projects, key='project-name')  
    framework  = st.sidebar.radio("Framework", ("Pytorch", "Keras"), key='Deep-Learning-frameworks')
    
     
    st.sidebar.markdown('***') 
    
    # catalog according to framework
    catalog_fw = catalog[catalog['framework'] == framework+'/']
    
    # report df 
    report = read_meta(catalog_fw[catalog_fw['project'] == project])
    

    st.markdown('***')
    
    if not isinstance(report, pd.DataFrame):
        st.markdown("There are no traces of a report.csv file under the **{}** implementation in the project _dir_, There's a possibility that the project is unfinished or missing files required to render the subject. until then try other projects.".format(framework))
    else:
        temp_desc = report['Desc'][0]
        st.markdown("<h3 style='font-family: century gothic'>Project Title : <bold><strong>{}</strong></bold></h3>".format(project),unsafe_allow_html=True)
        st.markdown('**Description** ~ _{}_'.format(temp_desc))
        st.markdown('**Implementation** ~ ___{}___'.format(framework))
        
        st.markdown('***')
        cs_body(report)


    model_eval('model')
   
    

        
        
    
    
        




if __name__ == '__main__':
    cs_main()
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64>](https://github.com/r0han99/) <small><i>Database of My Knowledge</i></small>'''.format(img_to_bytes('./tesseract.png')), unsafe_allow_html=True)
