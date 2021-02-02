# Libraries 

import streamlit as st 
# dataset dependencies 
import numpy as np
import pandas as pd
# os dependencies
from pathlib import Path
# import datetime
import base64
import pickle
import glob
import re
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
def read_catalog(path):
    
    catalog = pd.read_csv(path)
    paths = list(catalog['path'])
    projects = list(catalog['project'].unique())
    
    return catalog, paths, projects


def model_eval(evaluate_path):

    
    st.markdown("<h3 style='font-family: BioRhyme; font-weight:bold; font-size:25px;'>Real-Time Model Evaluation</h3>",unsafe_allow_html=True)

    st.markdown('***')
    try:
        path = evaluate_path
        with open(path,'rb') as f:
            temp = f.read()
        test_data = pickle.loads(temp)

    except:
        st.warning('The file encapsulating the required sample data for the overview block is non-existent, try again later;')

    else:
        rn_index = np.random.randint(0,50,1)
        x,y,model = test_data.values()
        
        expander = st.beta_expander('Evaluation type')
        control = expander.radio('choose',('Random Test-Case', 'Upload Test-Case'))
        st.markdown('***')
        st.markdown(f'___{control}___')
        
        image_col, prompt_col = st.beta_columns(2)
        
        if control == 'Random Test-Case':
            image_col.image(np.invert(x[rn_index]),caption='Label - ?', width=220)
            ans = prompt_col.selectbox('What do you think this is?',("I don't know",f"It is target - {y[rn_index]}"))
            
            st.markdown('***')
            st.write('___Model Classification___')

            # in future the eval_dict will contain paths to both keras model and pytorch model 
            # so user can pick one from here 

            st.write(model)

        else:
            image_file = st.file_uploader("Upload Image",type=['jpg', 'png', 'jpeg'])
            st.image(image_file,width=220)
            # st.write(model)
    
        

    
   
    
def cs_body(report,project,framework):

    pdf_url = 'https://github.com/r0han99/Deep-Learning-Anatomy/raw/main/Projects/' + project + '/' + framework + '/' + project+'-'+framework + '.pdf'

    cols = list(report.keys())[3:-3]
    # report.fillna('None',inplace=True)
    st.markdown("<h3 style='font-family: BioRhyme; font-weight:bold; font-size:25px;'>Project Artefacts</h3>",unsafe_allow_html=True)
    st.markdown('***')

    with open('./prompt-list.txt', 'rb') as f:
        data = f.read() 
    d = pickle.loads(data)

    # st.write(cols)
    

    for i,col in enumerate(cols):
        st.markdown(d[i])
        st.code(report[col])


    st.markdown('***')

    st.markdown('Summary: ')
    st.markdown('_'+report['summary']+'_')



    st.markdown('***')

    expander = st.beta_expander('Source-Code')
    expander.markdown('_Ipynb_ translated into _PDF_ using _LaTeX_')
    expander.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64>]({}) <small style='color:blue;'><i>Download</i></small>'''.format(img_to_bytes('./ipynb.png'),pdf_url), unsafe_allow_html=True)
    if expander.checkbox('Note'):
        expander.markdown('_"This link is a dynamically generated link, if this is a non-existent url, it is possible to traceback a 404 error, please visit the main repository for more info."_')
        

def cs_plots(report):

    st.markdown("<h3 style='font-family: BioRhyme; font-weight:bold; font-size:25px;'>Visualisation of Train Cycle ( Epoch vs Metric/Loss )</h3>",unsafe_allow_html=True)
    
    
    st.markdown('***')
    path = report['plots']

    
    for name in glob.glob(path+'/*.png'):
        st.image(name)
        
def cs_data(overview_path):
    st.markdown("<h3 style='font-family: BioRhyme; font-weight:bold; font-size:25px;'>Data Characteristics and Overview</h3>",unsafe_allow_html=True)

    st.markdown('***')
    
    
    try:
        path = overview_path
        with open(path,'rb') as f:
            temp = f.read()
        data = pickle.loads(temp)

    except:
        st.warning('The file encapsulating the required sample data for the overview block is non-existent, try again later;')

    else:
        # st.write(data)
        if re.search(r'[Ii]mage',data['kind']):
            st.markdown('___Training-set Dimensions:___ `{}`'.format(data['dimensions']))
            
            st.markdown('* _Number of Samples: `{}`_'.format(data['dimensions'][0]))
            st.markdown('* _What kind of Data?:_ `{}`'.format(data['kind']))
            st.markdown('* _Image Dimensions (H x W) pixels : `({}x{})`_'.format(data['dimensions'][1],data['dimensions'][2]))
            st.markdown('* _Number of Color Channels: `{}`_'.format(data['dimensions'][3]))
            st.markdown('* _Target Labels_:  `{}`'.format(data['targets']))

            st.markdown('***')

            st.markdown('___Image Data Exemplified : ___')
            cols = st.beta_columns(3)
            cols[0].image(data['data'][0],caption='Label - '+str(data['labels'][0]),width=175)
            cols[1].image(data['data'][1],caption='Label - '+str(data['labels'][1]),width=175)
            cols[2].image(data['data'][2],caption='Label - '+str(data['labels'][2]),width=175)

            st.markdown('***')
            if st.checkbox('Note',False):

                st.markdown('_Only 3 randomly selected samples are displayed here, to fit the aesthetics._')
            # if st.checkbox('Note')
        else:
            # '''
            # Structured Data, --> Title
            # * Traininng_set Dims 
            # * Feature Columns
            # * Target column 
            # * Data.info() as code block 
            # * Data.head at the end

            # '''

            pass

    
    




def cs_main():
    
    st.set_page_config(page_title="Deep Learning Anatomy",page_icon="./brain.png",layout="centered",initial_sidebar_state="auto",)
   
    tagline = 'A pragmatic approach to attain the Deep Learning Knowledge'
    st.markdown('''<h1 style='text-align:center;'>Deep Learning Anatomy  <img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64><br><p style='font-style: italic; font-size:15px; text-align:center; padding-right:60px'>{}</p></h1>'''.format(img_to_bytes("deep-learning.png"),tagline),unsafe_allow_html=True)
    st.markdown('<hr style="height:2px;border-width:0;color:gray;background-color:gray">',unsafe_allow_html=True)
    st.sidebar.markdown("<h2 style='font-family:BioRhyme; '>Project Catalog 📓</h2>",unsafe_allow_html=True)
    st.sidebar.markdown('***')
    

    catalog_path = './catalog.csv'
    if os.path.exists(catalog_path):
        catalog, paths, projects = read_catalog(catalog_path) # read paths 
        project = st.sidebar.selectbox('Project',projects, key='project-name')  
        framework  = st.sidebar.radio("Framework", ("Pytorch", "Keras"), key='Deep-Learning-frameworks') 

        # for data-overview and eval
        overview = os.path.join('./Projects', project, 'samples','overview.txt')
        
        evaluate = os.path.join('./Projects', project, 'samples','evaluate.txt')


        # catalog according to framework
        catalog_fw = catalog[catalog['framework'] == framework+'/']
        
        # st.write(catalog_fw)

        if not catalog_fw.empty:
            slice_ = catalog_fw[catalog_fw['project'] == project]
             # report df 
            with open(slice_['path'].values[0],'rb') as f:
                data = f.read()
            
            report = pickle.loads(data)


            temp_desc = report['desc']
            st.markdown("<h3 style='font-family: century gothic'>Project Title : <bold><strong>{}</strong></bold></h3>".format(project),unsafe_allow_html=True)
            st.markdown('**Description** ~ _{}_'.format(temp_desc))
            st.markdown('**Implementation** ~ ___{}___'.format(framework))
            
            st.markdown('***')

            radios = ('Project Artefacts','Data Overview','Plots','Model Evaluation')

            st.sidebar.markdown('***') # sidebar section break

            options = st.sidebar.radio('Specifics', radios, key='web-page-definition')

            

            if options == 'Project Artefacts':
                cs_body(report,project,framework)
            elif options == 'Plots':
                cs_plots(report)
            elif options == 'Data Overview':
                cs_data(overview)
            elif options == 'Model Evaluation':
                # later copy this piece of code and convert it into a subroutine
                model_eval(evaluate)
        
        else:
            st.markdown("There are no traces of a _report.csv_ file under the ***{}*** implementation in the project _dir_, There's a possibility that the project is unfinished or missing files required to render the subject. until then try other projects.".format(framework))

       
        

        st.markdown('***')
        
       
        
       


    # if catalog.csv doesn't exist
    else:
        st.warning("There's a possibility that the repository is corrupted -- required catalog for initiation is non-existent. run pipline script to establish catalog.")
    
    
    
    
    
        
        
    
    
        




if __name__ == '__main__':
    

    cs_main()
    st.sidebar.markdown('***')
    
    st.sidebar.markdown("<h5 style='font-family: BioRhyme; font-weight:bold; font-size:18px; text-transform: capitalize; '> ∑ Developed & Deployed by <i style='text-transform: lowercase; font-family: courier; color: green;'>r0han<i></h5>",unsafe_allow_html=True)
    st.sidebar.markdown('***')
    expander = st.sidebar.beta_expander('Iteration?')
    expander.markdown(' * `Iteration-0 | 2nd Feb, 2021;`')
    expander.markdown('***')
    
    expander.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=45 height=45>](https://github.com/r0han99/) <small><i>My Mind Palace </i></small>'''.format(img_to_bytes('./tesseract.png')), unsafe_allow_html=True)
    # st.sidebar.markdown('''''')
    
    
