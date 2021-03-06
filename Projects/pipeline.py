#!/Users/rohan/opt/anaconda3/bin/python
import numpy as np 
import pandas as pd 
import pickle
from pathlib import Path
import sys
import os
import datetime
# handeling deprecated warnings 
import warnings

warnings.filterwarnings("ignore", category=UserWarning)




def init_report():
    '''

    This will check if report.csv exists in given directory and creates if there isn't 
    then the absolute path of that report is stored in a txt file which is in the application 
    dir, the mode of writing willbe a+ or w+ everytime this pipeline is used for new project update
    the txt will be updated with the abs_path of the report from that project directory

    '''
    pass

        
def state_method():

    stages = '''

preliminary - 

    * create - /Plots and save all the epoch-cycle plots 
    * create Data Overview as using the following 

Step-1 -

import os
path = '../samples/'
overview_path = '../samples/overview.txt'
eval_path  = '../samples/evaluate.txt'

if os.path.exists(path):

    print('samples dir, exists..checking for dictionaries existence..')

    if os.path.exists(overview_path) and os.path.exists(eval_path):
        print('Data exists. no need of overwritting.')
    else:
        print("overview and eval doesn't exist, proceed to step-2")

else:
    print("samples/ dir is non-existent, Establishing one..")
    os.mkdir(path) # samples directory 

Step-2 

# dictionary init
overview_dict = {}
eval_dict = {}

# fill the following - 
# for overview
#string
kind = 'Image Data'
#tuple
dimensions = x_train.shape    
#labels : str(list of unique target values)
targets = list(np.unique(y_train))
#nd.array        
data = x_train[0:3]
#nd.array or class_names
labels = y_train[0:3]

vars0 = ['kind','dimensions', 'targets', 'data', 'labels']

# filling overview_dict 
for x in vars0:
    try:
        overview_dict[x] = eval(x)
    except:
        overview_dict[x] = x

# evaluate_dict 

eval_dict = {'test_cases' : x_test[0:50], 'true': y_test[0:50], 'class_names': None ,'model':'/{model-name}.h5'}


# dump 1 
with open(overview_path,'wb') as f:
    pickle.dump(overview_dict,f)

# dump 2 
with open(eval_path,'wb') as f:
    pickle.dump(eval_dict,f)


        
MAIN- 
step - 1, use ../../pipline -varl with 1 to get the var-dict to show the variables to be filled with 
step - 2 - use the following snippet after fetching ../../pipeline -varl with 2 
    code: 

var = ['desc','project_name', 'framework','prediction_type','network_type',
'architecture','layers','hidden_units','activations','epochs',
'metrics','loss','optimiser','learning_rate','batch_size','train_performance','test_performance','classification_report','elapsed','summary'
,'ipynb','plots']
param = {}
for val in var:

    try: 
        param[val] = eval(val)

    except:
        param[val] = val

    # check if anything is missing

step - 3 - pickle dump 

import pickle
file = open("artefacts.txt", "wb") 
dictionary = param 
pickle.dump(dictionary, file) 
file.close() 

step - 4 - ./pipeline.py -np 

    * relative path to the project dir ex - ./MNIST
    * choose framework 
    * done!
 
    '''

    print(stages)



def sample_collection():

    pass


def docs():

    help ='''

Arguments - Description

    -np [path-to-project]: New project creation
    -nptr [path-to-project]: tranfer learning projects (./Project-name)
    -varl or --var-list [optional] : prints variable/artifact list or dictionary with datatypes 
        * [optional]

            1. --update : update a the dictionary and var-list with new artifacts
            2. --pop : pop an unwanted artifact 

    --status [optional] : prints out catalog with all the projects done until then
        * [optional]

            1. keras : keras portion of catalog
            2. pytorch : pytorch portion of catalog

    --state : prints the actual procedure required to establish a report.csv

    -ar [optional] : prints arifact for a provided framework & project 
        * [optional]
            
            1. -d : (default) displays artefact based on input
            2. --update [optional]: updates an existing artefact with the novel info' provided
                * [optional]
                    1. -f | -file : for atributes like summary and descriptions input is taken from a file.

    -db [optional] : deploys emails to the people who joined the odyssey 
        * [optional]

            1. --status : prints the db of users 
            2. --deploy : deployes preset email and writes a log 
            3. --del : Truncates the Existing db while also backingup the records under assets/bckup 
            and writes a logfile.
            4. --backup : simple backup of the database.

    '''

    print(help)


def meta_collect(project_path,project_name,fw,nntype):
    date = datetime.datetime.now().strftime('%d-%A (%Y)')
    '''

    This function collects all the Data required to create a report.csv file
    control flow will be if-else anchored on framework name, since two-frameworks have two distinct reports 
    generated. 
    if pytorch : {code} else: {keras-code} 

    '''
    print('Meta Data Collection and Organisation')

    meta = os.path.join(project_path,'artefacts.txt')
    if os.path.exists(meta):
        print('artefacts.txt exists..')
        with open(meta, 'rb') as f: 
             data = f.read() 
  
        d = pickle.loads(data) 
        # report = pd.DataFrame(pd.Series(d)).T

        # dev = '../catalog1.csv'
        main= '../assets/catalog.csv'

        print('Updating Catalog .. ')
        if not os.path.exists(main):
            print('No catalog file in existence, creating one, writing content..')
            with open(main,'w') as f:
                f.write('{},{},{},{},{}\n'.format('date','project','framework','type','path'))
            # write content
            with open(main,'a+') as f:
                f.write('{},{},{},{},{}\n'.format(date,project_name,fw,nntype,'./Projects/'+project_path[2:]+'artefacts.txt'))
                print('Done!')
        
        else:
            with open(main,'a+') as f:
                f.write('{},{},{},{},{}\n'.format(date,project_name,fw,nntype,'./Projects/'+project_path[2:]+'artefacts.txt'))
            
            print('Done!')


        
        # report.csv creation
        # generate_report(project_path, project_name,fw, report)
        

    else:
        print('artefacts.txt is non-existent, create network-metadata before triggering pipeline')


    '''
    
    After the inputs taken, all the inputs will then be packaged and parameterized into other subroutine called 
    validate_meta() which comprehensively checks for all the data with the user

    Then comes the generate_report() which creates a pandas dataframes from all the stuff and generates two 
    csv files which

    '''

def path_creation(project_path):
    while(True):
        fw = input('Select Framework : 1. Pytorch, 2. Keras >> Enter: ')
        if fw == '1':
            fw = 'Pytorch/'
            break
        elif fw == '2':
            fw = 'Keras/'
            break
        else:
            print('Invalid!')
            continue
        
    path_url = os.path.join(project_path,fw)
    print('Project Path ~ ', path_url)
    return path_url,fw



def pickle_handle(file_path,method,d=None):

    if method == 'dump':
        print('Dumping records!')
        with open(file_path,'wb') as f:
            pickle.dump(d,f)
        print(f'byte-code dump created at {file_path}')
    
    elif method == 'load':

        print('Loading Byte-code text!')
        with open(file_path, 'rb') as f:
            data = f.read() 
        d = pickle.loads(data)

        return d


def artefact_edit(flag='-d'):

    
    '''
    catalog read and select path pivoting on framwework and project name 

    '''
    catalog_path = '../assets/catalog.csv'
    catalog = pd.read_csv(catalog_path)
    
    while True:
        fw = input('select framework 1) Keras 2) Pytorch  >> Enter: ') 
        fw = 'Keras/' if fw == '1' else 'Pytorch/' if fw == '2' else 'Invalid'
        
        if fw in list(catalog['framework']):
            catalog = catalog[catalog['framework'] == fw]
            print(f'{fw} Catalog ')
            print(catalog)
            break
        else:
            print('invalid framework name')
            continue
    print()
    print('Project-List : ',list(catalog['project']))
    while True:
        prj = input('Enter project name : ')
        if prj in list(catalog['project']):
            catalog = catalog[catalog['project'] == prj]
            print(f'{prj} Catalog')
            print(catalog)
            break
        else:
            print('Invalid Project Name (spell-check) : ') 
            continue

    path = catalog['path'].values[0].split('/')[2:]
    path = os.path.join('./',*path)


    print(f'\nAccessing Artefact archive of {fw}-{prj}')

    artefact = pickle_handle(path,'load')
    
    if flag == '-d':
        print(list(artefact.keys()))
        while True:
            art_name = input('Enter Artifact to retreive info : ')
            if art_name in list(artefact.keys()):
                print('ARTEFACT - INFO')
                print(f"{art_name} >> ",artefact[art_name])
                break
            else:
                print()
                print(f'Artefact - {art_name} is non-existent!')
                continue

    elif flag[2] == '--update':
        
        print(list(artefact.keys()))
        while True:
            art_name = input('Enter Artifact to retreive info : ')
            if art_name in list(artefact.keys()):
                print('ARTEFACT - INFO ( current ) ')
                print(f"{art_name} >> ",artefact[art_name])
                break
            else:
                print()
                print(f'Artefact - {art_name} is non-existent!')
                continue
            
        print(f'Updating Artefact Info for >> {art_name}')

        if flag[3] == '-f' or flag[3] == '-file':

            print()
            print('File Input')
            print()
            while True:
                filename = input('Enter FILE Relative-PATH : ')
                if os.path.exists(filename):
                    break
                else:
                    print('invalid filepath!')
                    continue
            
            with open(filename,'r') as f:
                content = f.readlines()

            text = ''
            for line in content:
                text += line
            
            print('PREVIEW\n')
            print(text)

            print('\nVariable Added to the Dictionary! -- saving state .. ')
            artefact[art_name] = text
            pickle_handle(file_path=path,method='dump',d=artefact)
            
            print('ARTEFACT - INFO ( Updated ) ')
            print(f"{art_name} >> ",artefact[art_name])
            
        
        else:
            info = input('New info : ')
            artefact[art_name] = info
            print('Variable Added to the Dictionary! -- saving state .. ')
            pickle_handle(file_path=path,method='dump',d=artefact)

            print('ARTEFACT - INFO ( Updated ) ')
            print(f"{art_name} >> ",artefact[art_name])
 

def main():

     

    if sys.argv[1] == '-np':
        
        try:
            if len(sys.argv) == 3: 
                abs_path = sys.argv[2]
                project_name = sys.argv[2].split('/')[1]
                print('Project Directory - {}'.format(project_name))
                project_path,fw = path_creation(abs_path)
                nntype = input('Enter Approach Type >>  ')

                meta_collect(project_path,project_name,fw,nntype) # Data collection subroutine 
        
        except:
            print("There's no Absolute Path given in the arguments! ")
            
            while(True):
                abs_path = input('Enter the Name of Directory : ')
                nntype = input('Enter Approach Type >>  ')
                if os.path.isdir(abs_path):
                    try:
                        project_name = abs_path.split('/')[1]
                        print('Project Directory - ./{}'.format(project_name))
                        
                    except:
                        project_name = abs_path
                        abs_path = './'+abs_path
                        print('Project Directory - {}'.format(abs_path))
                    break
                else:
                    print('Invalid Path!')
                    print('Here are the list of neighbouring dirs : {}'.format(list(os.listdir('./'))))
                    continue

                # Data collection subroutine 
            project_path,fw = path_creation(abs_path)
            meta_collect(project_path,project_name,fw,nntype)
                
    elif sys.argv[1] == '-nptr':
        print('Transfer-Learning')
        if len(sys.argv) == 3: 
                abs_path = sys.argv[2]
                project_name = sys.argv[2].split('/')[1]
                print('Project Directory - {}'.format(project_name))
                prj_path = os.path.join('./Transfer-Learning',project_name+'/')
                if os.path.exists(prj_path):
                    print(f'Relative Path {prj_path}')
                    nntype = input('Enter Approach Type >>  ')
                    fw = input('select framework 1) Keras 2) Pytorch  >> Enter: ') 
                    fw = 'Keras/' if fw == '1' else 'Pytorch/' if fw == '2' else 'Invalid'
                else:
                    print("project directory doesn't exist! [check-dir-name]")
                    exit(1)               
                
                meta_collect(prj_path,project_name,fw,nntype)

           
    elif sys.argv[1] == '-varl' or sys.argv[1] == '--var-list':

        # read here 
        d = pickle_handle(file_path='./var-dict.txt',method='load')

        if len(sys.argv) == 2:

            print('Default Variable List : ')
            inp = input('1. For Entire Dict, 2. For Var-List >> Enter : ')
            if inp == '1':
                for var,dtype in zip(d.keys(), d.values()):
                    print('{:}-----{:}'.format(var,dtype))
            elif inp == '2':
                print(list(d.keys()))
            else:

                print('Invalid arg')

            # display it 
        else:
            if sys.argv[2] == '--update':
                # Load the pickled prompt_list, display it 
                # update with new prompts required
                print('Adding new variable and dtype to var-dict')
                variable = input('Enter variable to add into dictionary: ')
                d[variable] = input('Enter Dtype of that variable: ')
                print('Variable Added to the Dictionary! -- saving state .. ')
                pickle_handle(file_path='./var-dict.txt',method='dump',d=d)

            elif sys.argv[2] == '--pop':
                # popping variable 
                print('Popping Existing variable and dtype from var-dict')
                variable = input('Enter variable to pop outof the dictionary: ')
                try:
                    d.pop(variable)
                    print(f'{variable} deleted from the records! -- saving state..')
                    pickle_handle(file_path='./var-dict.txt',method='dump',d=d)

                except:
                    print('Invalid var-name')
                    exit(1)


            else:
                print('Invalid follow up argument detect, -varl is followed by --update')
                exit(1)

    elif sys.argv[1] == '--status':
        
        catalog = pd.read_csv('../assets/catalog.csv')
        keras = catalog[catalog['framework'] == 'Keras/']
        pytorch = catalog[catalog['framework'] == 'Pytorch/']

        if len(sys.argv) == 3:
            
            if sys.argv[2] == 'keras':
                print('prints the catalog, segmented according to the framework')
                print('Keras')
                print(keras)
                print()
                print('Number projects done {}'.format(sum(keras['project'].value_counts())))

            elif sys.argv[2] == 'pytorch':
                print('prints the catalog, segmented according to the framework')
                print('Pytorch')
                print(pytorch)
                print()
                print('Number projects done {}'.format(sum(pytorch['project'].value_counts())))

            else:
                print('Invalid arg!')

        else:
            print('Catalog')
            print(catalog)
    
    elif sys.argv[1] == '--state':
        state_method()
        

    
    elif sys.argv[1] == '-sample' or sys.argv[1] == '-sc':
        print('Sample Collection to display the type of data handeled ')


    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        docs()

    
    elif sys.argv[1] == '-ar':
        
        if len(sys.argv) >= 3:
            if sys.argv[2] == '-d':
                artefact_edit()
            elif sys.argv[2] == '--update':
                artefact_edit(flag=sys.argv)
            else:
                print('Invalid arg, try --help')
        else:
            artefact_edit()    

    elif sys.argv[1] == '-db':
        db_path = '../assets/db.txt'
        if len(sys.argv) == 3:
            if sys.argv[2] == '--status':
                while True:
                    db_type = input('--status of 1. db, 2. bckup_db  >> Enter : ')
                    if db_type == '1':
                        break
                    elif db_type == '2':
                        break
                    else:
                        print('Invalid re-enter')
                        continue

                status_path = db_path if db_type == '1' else '../assets/bckup/bckup.txt'
                print(status_path)              
                db = pickle_handle(status_path,'load')
                print(db)
                print()
                print('Number of users who joined odyssey : {}'.format(db.shape[0]))
            
    
            elif sys.argv[2] == '--deploy':

                '''
                1. checks the env, if its /dev goes to path git and runs a subprocess git pull and copies the content of db.txt to this db.txt 
                2. Reads an already writen file potentially MD, and edits positions with names
                3. Sends the mails iteratively to every user who enrolled
                4. writes a log --> fmt [date][users][summary]
                
                '''
                print('DEPLOYMENT')
            
            elif sys.argv[2] == '--del':
                
                print()
                initial_state = pickle_handle(db_path, 'load')
                if not initial_state.empty:
                    
                    if not os.path.exists(os.path.join('../assets','bckup/')):
                        os.mkdir(os.path.join('../assets','bckup/'))
                    else:
                        print('Backing Up db...')
                        bckup_path = os.path.join('../assets','bckup/')
                        bckup_file = os.path.join('../assets/','bckup/','bckup.txt')
                        log_file = os.path.join('../assets/','bckup/','backup.log')
                        db_state = pickle_handle(db_path, 'load')
                        # writing bckup
                        pickle_handle('../assets/bckup/bckup.txt', 'dump',d=db_state)
                        print('Number of Records backed-up {}'.format(db_state.shape[0]))
                        
                        print('Writing Log ..')
                        with open(log_file,'a') as log:
                            log.write(f'[{datetime.datetime.now()} records backed-up : {db_state.shape[0]}]')
                            log.write('\n')

                        print('Truncating db ...')
                        user_db = pd.DataFrame({"Names":[], "Emails":[]})
                        with open(db_path,'wb') as f:
                            pickle.dump(user_db,f)  
                        print('Done!')

                else:
                    print('Database is already Empty!')

            elif sys.argv[2] == '--backup':
                
                print('Backing Up db...')
                bckup_path = os.path.join('../assets','bckup/')
                bckup_file = os.path.join('../assets/','bckup/','bckup.txt')
                log_file = os.path.join('../assets/','bckup/','backup.log')
                db_state = pickle_handle(db_path, 'load')
                # writing bckup
                pickle_handle('../assets/bckup/bckup.txt', 'dump',d=db_state)
                print('Number of Records backed-up {}'.format(db_state.shape[0]))
                
                print('Writing Log ..')
                with open(log_file,'a') as log:
                    log.write(f'[{datetime.datetime.now()} records backed-up : {db_state.shape[0]}]')
                    log.write('\n')
                print('Done!')



                

                                 
                
                    
        else:
            db = pickle_handle('../assets/db.txt','load')
            print(db)
            print()
            print('Number of users who joined the odyssey : {}'.format(db.shape[0]))






if __name__ == '__main__':

    

    if len(sys.argv) == 1:
        print('This Script Takes in Command-Line Arguments to trigger the functionalitied required,\nfetching ```doc-string```')
        docs()
        exit(1)
    else:
        main()    










