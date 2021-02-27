# Libraries 

import streamlit as st 
# dataset dependencies 
import numpy as np
import pandas as pd
# os dependencies
from pathlib import Path
import datetime
import base64
import pickle
import glob
import re
import os 
# model evaluation
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical


 



# image encoding 
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def validate(details):

    # load db
    with open('./db.txt', 'rb') as f:
        data = f.read() 
    db = pickle.loads(data)
    npeeps = db.shape[0]
    #unpack details 
    name, email = details

    names = list(db['Names'])
    emails = list(db['Emails'])

    # name can be same but not email
    status = (name in names and email in emails)

    return status,npeeps


def userdb(details):

    # access db
    with open('./db.txt', 'rb') as f:
        data = f.read() 
    db = pickle.loads(data)
    
    # add row 
    db.loc[len(db.index)] = details
    
    # write changes
    with open('./db.txt','wb') as f:
        pickle.dump(db,f)
        

    




def model_predict(model_path,x,true,class_names,nn_type,report):
    

    try:
        model = load_model(model_path)
    except:
        if not nn_type == 'Transfer Learning':
            st.error('Keras does not exist!')
        else:
            st.warning('___Saved Model states (.h5 file) for any transfer learning project is huge compared to the normal ones. Large files cannot be pushed on to GitHub repositories in a normal git-commit workflow. Working on Alternatives to make this section up and running.___')

    else:
        predict = model.predict_classes(x)
        predict = predict.reshape(1)
        
    
        
        if class_names == None:
            st.markdown('Model Classifies this to be - `{}`'.format(predict[0]))
        else:
            st.markdown('Model Classifies this to be - `{}`, class - `{}`'.format(predict[0],class_names[predict[0]]))
        if predict[0] == true.argmax():
            st.success('___Which is True!___')
        else:
            st.error('___Which is False___')


def model_eval(evaluate_path,project,nn_type,report):


    
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
        
        # st.write(test_data['test_cases'][0].shape)
        
        # x,y,model = test_data.values()
        # x = test_data['']
        x = test_data['test_cases']
        y = test_data['true']
        model = test_data['model']

        # st.write(test_data.keys())
        if not nn_type == 'Transfer Learning':
            model_path = './Projects/' +project+'/'+'samples'+model
        else:
            model_path = './Projects/'+'Transfer-Learning/'+project+'/'+'samples'+model

        
        try: 
            shape = y.shape[1]
        except:
            shape = len(y.shape)
            if shape ==1:
                y = to_categorical(y)
        
        

        try:
            class_names = test_data['class_names']
        except:
            class_names = None

        # expander = st.beta_expander('Evaluation type')

        control = st.selectbox('Test Case type',('Random Test-Set Sample', 'Upload Test-Case'),key='eval-type')
        
        if control == 'Random Test-Set Sample':
            st.markdown('***')
            header, generator = st.beta_columns(2)
            header.markdown(f'___{control}___')
            if generator.button('Generate random sample'):
            
                image_col, prompt_col = st.beta_columns(2)
                rn_index = np.random.randint(0,50,1)
                image_col.image(x[rn_index],caption='random sample', width=220)
                if class_names == None:
                    ans = prompt_col.markdown(f'True Target Class = `{y[rn_index].argmax()}`')
                else:
                    ans = prompt_col.markdown(f'True Target Class = `{y[rn_index].argmax()}`, a `{class_names[y[rn_index].argmax()]}`')
                

                st.markdown('***')
                st.write('___Model Classification___')

                # in future the eval_dict will contain paths to both keras model and pytorch model 
                # so user can pick one from here 
                
                
                model_predict(model_path,x[rn_index],y[rn_index],class_names,nn_type,report)
                  

        elif control == 'Upload Test-Case':
            st.warning('_Currently under development!_')
            image_file = st.file_uploader("Upload Image",type=['jpg', 'png', 'jpeg'])
            
            if not image_file is None:
                st.image(image_file,width=220)
            
    
    st.markdown('***')
    if st.checkbox('Note',False):
        st.markdown('_Note, This Model evaluation block uses only keras encoded models for predictions, because it’s simpler to save model and reuse in Keras than in Pytorch -- which uses pretty unorthodox methodology to save and reuse models;_')

    
   
    
def cs_body(report,project,framework,nn_type):


    pdf_url = 'https://github.com/r0han99/Deep-Learning-Anatomy/raw/main/' + report['ipynb'][2:]


    cols = list(report.keys())[3:-3]
    # report.fillna('None',inplace=True)
    st.markdown("<h3 style='font-family: BioRhyme; font-weight:bold; font-size:25px;'>Project Artefacts</h3>",unsafe_allow_html=True)
    st.markdown('***')

    with open('./prompt-list.txt', 'rb') as f:
        data = f.read() 
    d = pickle.loads(data)
    
    
    # st.write(report.keys())
    # st.write(d)

    for i,col in enumerate(cols):
        st.markdown(d[i])
        st.code(report[col])


    st.markdown('***')

    st.markdown('Summary: ')
    st.markdown('_'+report['summary']+'_')



    st.markdown('***')

    expander = st.beta_expander('Source-Code')
    expander.markdown('_Ipynb_ translated into _PDF_ using _LaTeX_')
    expander.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64>]({}) <small style='color:blue;'><i>Download</i></small>'''.format(img_to_bytes('./pngs/ipynb.png'),pdf_url), unsafe_allow_html=True)
    expander.markdown('***')
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
    
    st.set_page_config(page_title="Deep Learning Anatomy",page_icon="./pngs/brain.png",layout="centered",initial_sidebar_state="auto",)
   
    tagline = 'My odyssey of attaining Deep Learning knowledge'
    st.markdown('''<h1 style='text-align:center; font-weight:bold; color:black;'>Deep Learning Anatomy  <img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64><br><p style='font-style: italic; font-size:15px; text-align:center; padding-right:60px'>{}</p></h1>'''.format(img_to_bytes("./pngs/deep-learning.png"),tagline),unsafe_allow_html=True)
    # st.image('./banner.png',width=700)
    st.markdown('<hr style="height:2px;border-width:0;color:gray;background-color:gray">',unsafe_allow_html=True)
    st.sidebar.markdown("<h2 style='font-family:BioRhyme; '>Project Catalog 📓</h2>",unsafe_allow_html=True)
    st.sidebar.markdown('***')
    

    catalog_path = './catalog.csv'
    if os.path.exists(catalog_path):
        
        catalog = pd.read_csv(catalog_path)
        types = list(catalog['type'].unique())
        all_list = list(catalog['project'].unique())
        date = list(catalog['date'])[-1:]
        nn_type = st.sidebar.selectbox('Category',types,key='nn-type')
        catalog = catalog[catalog['type'] == nn_type]
        paths = list(catalog['path'])
        projects = list(catalog['project'].unique())
        # catalog, paths, projects, types = read_catalog(catalog_path,nn_type) # read paths 
        
    

        
        

        if nn_type == 'CNN':
            
            catalog = catalog[catalog['type'] == nn_type]
            project = st.sidebar.selectbox('Project Name',projects, key='project-name')  
            framework  = st.sidebar.radio("Framework", ("Keras", "Pytorch"), key='Deep-Learning-frameworks')

            

           
            # for data-overview and eval
            overview = os.path.join('./Projects', project, 'samples','overview.txt')
            evaluate = os.path.join('./Projects', project, 'samples','evaluate.txt')


            # catalog according to framework
            catalog_fw = catalog[catalog['framework'] == framework+'/']
            
            # st.write(catalog_fw)

            if not catalog_fw.empty:
                slice_ = catalog_fw[catalog_fw['project'] == project]
                if not slice_.empty:
                    # st.write(slice_)
                    #  report df 
                    with open(slice_['path'].values[0],'rb') as f:
                        data = f.read()
                    
                    report = pickle.loads(data)
                    
                    project_name = report['project_name']
                    temp_desc = report['desc']
                    st.markdown("<h3 style='font-family: BioRhyme'>Project Title : <bold><strong style='color:#E45E18; padding-left:20px;'>{}</strong></bold></h3>".format(project_name),unsafe_allow_html=True)
                    st.markdown('''<h3 style='font-family: BioRhyme'> Description :</h3> <i>{}<i>'''.format(temp_desc),unsafe_allow_html=True)
                    
                    if framework == 'Keras':
                        st.markdown('''<h3 style='font-family: BioRhyme;'>Implementation : <b style='color:#EB8E26; padding-left:20px;'>{}</b> <img src='data:image/png;base64,{}' class='img-fluid' width=30 height=30></h3>'''.format(framework,img_to_bytes('./pngs/Tensorflow.png')),unsafe_allow_html=True)
                    else:
                        st.markdown('''<h3 style='font-family: BioRhyme;'>Implementation : <b style='color:#EE4C2C; padding-left:20px;'>{}</b> <img src='data:image/png;base64,{}' class='img-fluid' width=40 height=40></h3>'''.format(framework,img_to_bytes('./pngs/pytorch.png')),unsafe_allow_html=True)
                    # st.markdown('**Implementation** ~ ___{}___'.format(framework))
                    
                    st.markdown('***')

                    radios = ('Project Artefacts','Data Overview','Plots','Model Evaluation')

                    st.sidebar.markdown('***') # sidebar section break

                    options = st.sidebar.radio('Specifics', radios, key='web-page-definition')

                    if options == 'Project Artefacts':
                        cs_body(report,project,framework,nn_type)
                    elif options == 'Plots':
                        cs_plots(report)
                    elif options == 'Data Overview':
                        cs_data(overview)
                    elif options == 'Model Evaluation':
                        
                        model_eval(evaluate,project,nn_type,report)
                
                else:
                    st.error(f"{framework}'s Version of {project} doesn't exist in the catalog.")



                
            else:
                st.markdown("There are no traces of a _Artefacts.txt_ file under the ***{}*** implementation in the project _dir_, There's a possibility that the project is unfinished or missing files required to render the subject. until then try other projects.".format(framework))

        
            

            st.markdown('***')
        
       
        elif nn_type == 'Transfer Learning':
            catalog = catalog[catalog['type'] == nn_type]

            # st.write(catalog)
            projects = list(catalog['project'])
            
            # projects list
            project = st.sidebar.selectbox('Project Name',projects, key='project-name')  
            framework = catalog['framework'].values[0][:-1]
            
            


            # for data-overview and eval
            overview = os.path.join('./Projects','Transfer-Learning' ,project, 'samples','overview.txt')
            evaluate = os.path.join('./Projects','Transfer-Learning' ,project, 'samples','evaluate.txt')
            
            
            slice_ = catalog[catalog['project'] == project]
            if not slice_.empty:
                # st.write(slice_)
                #  report df 
                with open(slice_['path'].values[0],'rb') as f:
                    data = f.read()
                
                report = pickle.loads(data)
                
                project_name = report['project_name']
                temp_desc = report['desc']
                st.markdown("<h3 style='font-family: Lexend Mega;'>Project Title : <bold><strong style='color:#E45E18; padding-left:20px;'>{}</strong></bold></h3>".format(project_name),unsafe_allow_html=True)
                st.markdown('''<h3 style='font-family: BioRhyme'> Description :</h3> <i>{}<i>'''.format(temp_desc),unsafe_allow_html=True)
                    
                    
                if framework == 'Keras':
                        st.markdown('''<h3 style='font-family: BioRhyme;'>Implementation : <b style='color:#EB8E26; padding-left:20px;'>{}</b> <img src='data:image/png;base64,{}' class='img-fluid' width=30 height=30></h3>'''.format(framework,img_to_bytes('./pngs/Tensorflow.png')),unsafe_allow_html=True)
                else:
                        st.markdown('''<h3 style='font-family: BioRhyme;'>Implementation : <b style='color:#EE4C2C; padding-left:20px;'>{}</b> <img src='data:image/png;base64,{}' class='img-fluid' width=40 height=40></h3>'''.format(framework,img_to_bytes('./pngs/pytorch.png')),unsafe_allow_html=True)
                    
#                 if framework == 'Keras':
#                     st.markdown('''<h3 style='font-family: BioRhyme;'>Implementation : <b>{}</b> <img src='data:image/png;base64,{}' class='img-fluid' width=30 height=30></h3>'''.format(framework,img_to_bytes('./pngs/Tensorflow.png')),unsafe_allow_html=True)
#                 else:
#                     st.markdown('''<h3 style='font-family: BioRhyme;'>Implementation : <b>{}</b> <img src='data:image/png;base64,{}' class='img-fluid' width=40 height=40></h3>'''.format(framework,img_to_bytes('./pngs/pytorch.png')),unsafe_allow_html=True)
                
                st.markdown('***')

                # st.write(report)

                

                radios = ('Project Artefacts','Data Overview','Plots','Model Evaluation')

                st.sidebar.markdown('***') # sidebar section break
                

                options = st.sidebar.radio('Specifics', radios, key='web-page-definition')

                if options == 'Project Artefacts':
                    cs_body(report,project,framework,nn_type)
                elif options == 'Plots':
                    cs_plots(report)
                elif options == 'Data Overview':
                    cs_data(overview)
                elif options == 'Model Evaluation':
                    
                    model_eval(evaluate,project,nn_type,report)
            

        st.sidebar.markdown('***')
        all_proj = st.sidebar.beta_expander('All projects')
        all_proj.code('** Current List **')
        all_proj.write(all_list)
        
        


    # if catalog.csv doesn't exist
    else:
        st.warning("There's a possibility that the repository is corrupted -- required catalog for app-initiation is non-existent. run pipline script to establish catalog.")
    
    
    
def page(expander):
    
    
    # st.sidebar.beta_expandertitle('Explore ✨')

    r_name = r"^\w+$"
    r_email = r"^[a-z0-9\._]+@[a-z]+\.[a-z]{1,3}"


    name = expander.text_input('Enter your Name:')
    status = True if re.fullmatch(r_name,name) else False
    email = expander.text_input('Enter your Email ID:')
    status_e = True if re.fullmatch(r_email,email) else False

    if (status and status_e):
        expander.success("___Thank you!, I'll keep you posted___")
        return 'Done', (name,email)

    elif not name == '' and not email == '':
        expander.error('Name or Email are in an unorthodox format, please re-enter.')
    
    

    if expander.checkbox('why?', False):
        expander.info('_Signing up here, will enable you to periodically get Automated-Emails about the ChangeLog and any new projects that are added into this ***Catalog***._')
    



if __name__ == '__main__':
    

    cs_main()
    

    expander = st.sidebar.beta_expander('Sign-Up?')
    expander.markdown('''<p style='font-size:14.5px; color:#E74A2B; font-family:poppins; font-weight:bold; text-align:center; padding-right:42px;'>Join my odyssey ✨</p>''',unsafe_allow_html=True)
    expander.image('./banner.png',width=300)
    try:
        status,(name,email) = page(expander)
        if status == 'Done':
            # expander.code(f"{name}, {email}")
            details = list([name,email])
            # another function to validate if the user already exists in the db
            status,npeeps = validate(details)

            if status == False:
                userdb(details)
            else:
                expander.markdown('''<p style='font-size:14.5px; color:green; font-family:poppins; font-weight:bold; text-align:center; padding-right:42px;'>Already Registered for the Odyssey</p>''',unsafe_allow_html=True)
                # expander.code('People joined {:,}'.format(npeeps)) Number of People Joined

            
    except:
        pass

   

    # expander.markdown('***')

    st.sidebar.markdown('***')
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=40 height=40>](https://github.com/r0han99/Deep-Learning-Anatomy) <b style='font-family: BioRhyme; font-weight:bold; font-size:18px; text-transform: capitalize;' >Developed & Deployed by <i style='text-transform: lowercase; font-family: courier; color: crimson;'>r0han</i></b> [<img src='data:image/png;base64,{}' class='img-fluid' width=33 height=33>](https://github.com/r0han99/) '''.format(img_to_bytes("./pngs/GitHub.png"),img_to_bytes('./pngs/tesseract.png')), unsafe_allow_html=True)
    
    st.sidebar.markdown('***')
    # st.sidebar.markdown('''''')
    
    
