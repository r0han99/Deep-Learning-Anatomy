# Libraries 

import streamlit as st 
# dataset dependencies 
import numpy as np
import pandas as pd 
# os dependencies
from pathlib import Path
import base64
import pickle
import glob
import os 

# '''
# paths to the report files -- Dynamic 
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

    # st.write("df_slice['path'].values[0])",df_slice['path'].values[0])
    
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
    
    
    
   
    
def cs_body(report,project,framework):

    pdf_url = 'https://github.com/r0han99/Deep-Learning-Anatomy/raw/main/Projects/' + project + '/' + framework + '/' + project+'-'+framework + '.pdf'

    cols = report.columns[3:-1]
    report.fillna('None',inplace=True)
    st.markdown("<h3 style='font-family: Avenir; font-weight:bold; font-size:30px;'>Project Artefacts</h3>",unsafe_allow_html=True)
    st.markdown('***')

    with open('./prompt-list.txt', 'rb') as f:
        data = f.read() 
    d = pickle.loads(data)

    
    for i in range(len(d)-1):
        st.markdown(d[i])
        st.code(report[cols[i]].values[0])


    st.markdown('***')

    st.markdown('Summary: ')
    st.markdown('_'+report['summary'].values[0]+'_')



    st.markdown('***')

    expander = st.beta_expander('Source-Code')
    expander.markdown('_Ipynb_ translated into _PDF_ using _LaTeX_')
    expander.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64>]({}) <small style='color:blue;'><i>Download</i></small>'''.format(img_to_bytes('./ipynb.png'),pdf_url), unsafe_allow_html=True)
    if expander.checkbox('Note'):
        expander.markdown('_"This link is dynamically generated, so in the case of non-existent url to pdf, it is possible to traceback a 404 error, please visit the main repository for more info."_')
        

def cs_plots(report):

    st.markdown("<h3 style='font-family: Avenir; font-weight:bold; font-size:30px;'>Visualisation of Train Cycle <br>( Epoch vs Metric/Loss )</h3>",unsafe_allow_html=True)
    
    path = report['plots'].values[0]

    
    for name in glob.glob(path+'/*.png'):
        st.image(name)
        

    




def cs_main():

    '''
    A line to read the report paths
    
    '''

    tagline = 'A comprehensive approach to attain the Deep Learning Knowledge'
    st.markdown('''<h1>Deep Learning Anatomy  <img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64><br><p style='font-style: italic; font-size:15px; text-align:left;'>{}</p></h1>'''.format(img_to_bytes("deep-learning.png"),tagline),unsafe_allow_html=True)
    
    st.sidebar.markdown("<h2 style='font-family:century gothic;'>Project Catalog 📓</h2>",unsafe_allow_html=True)
    st.sidebar.markdown('***')
    


    if os.path.exists('./catalog.csv'):
        catalog, paths, projects = read_catalog() # read paths 
        project = st.sidebar.selectbox('Project',projects, key='project-name')  
        framework  = st.sidebar.radio("Framework", ("Pytorch", "Keras"), key='Deep-Learning-frameworks') 



        # catalog according to framework
        catalog_fw = catalog[catalog['framework'] == framework+'/']
        
       
        slice_ = catalog_fw[catalog_fw['project'] == project]
        

        # report df 
        report = read_meta(slice_)
        

        st.markdown('***')
        
        if not isinstance(report, pd.DataFrame):
            st.markdown("There are no traces of a _report.csv_ file under the ***{}*** implementation in the project _dir_, There's a possibility that the project is unfinished or missing files required to render the subject. until then try other projects.".format(framework))

        
        else:
            temp_desc = report['desc'][0]
            st.markdown("<h3 style='font-family: century gothic'>Project Title : <bold><strong>{}</strong></bold></h3>".format(project),unsafe_allow_html=True)
            st.markdown('**Description** ~ _{}_'.format(temp_desc))
            st.markdown('**Implementation** ~ ___{}___'.format(framework))
            
            st.markdown('***')

            options = st.sidebar.radio('View', ('Project Artefacts','Plots'), key='web-page-definition')
            if options == 'Project Artefacts':
                cs_body(report,project,framework)
            if options == 'Plots':
                cs_plots(report)
            

            st.sidebar.markdown('***')
            expander = st.sidebar.beta_expander('Want to try?')
            expander.warning('Currently Under-Beta')
            if expander.checkbox('yes?'):
                model_eval('model')



    # if catalog.csv doesn't exist
    else:
        st.warning("There's a possibility that the repository is corrupted -- required catalog for initiation is non-existent.")
    
    
    st.sidebar.markdown('***') 
    
    
        
        
    
    
        




if __name__ == '__main__':
    cs_main()
    st.sidebar.markdown('***')
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64>](https://github.com/r0han99/) <small><i>Database of My Knowledge</i></small>'''.format(img_to_bytes('./tesseract.png')), unsafe_allow_html=True)
