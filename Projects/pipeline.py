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


def generate_report(project_path, project_name, fw, report):
    date = datetime.datetime.now().strftime('%d-%A (%Y)')

    # creates an Anchor point for the Application c
    if os.path.exists(project_path+'report.csv'):
        print("report already exists, manually verify if it's the one, else delete it and run the script")
    else:
        report.to_csv(project_path+'report.csv')
        print('report created!')
        print('Updating Catalog .. ')
        if not os.path.exists('../catalog.csv'):
            print('No catalog file in existence, creating one, writing content..')
            with open('../catalog.csv','w') as f:
                f.write('{},{},{},{}\n'.format('date','project','framework','path'))
            # write content
            with open('../catalog.csv','a+') as f:
                f.write('{},{},{},{}\n'.format(date,project_name,fw,'./Projects/'+project_path[2:]+'report.csv'))
                print('Done!')
        
        else:
            with open('../catalog.csv','a+') as f:
                f.write('{},{},{},{}\n'.format(date,project_name,fw,'./Projects/'+project_path[2:]+'report.csv'))
            
            print('Done!')
        
def state_method():

    stages = '''

preliminary - 

        * create - /Plots and save all the epoch-cycle plots 
        * create data for rendering # trail 
        
step - 1, use ../../pipline -varl with 1 to get the var-dict to show the variables to be filled with 
step - 2 - use the following snippet after fetching ../../pipeline -varl with 2 
    example: 
    var = ['desc','project_name', 'framework','prediction_type','network_type',
    'architecture','layers','hidden_units','activations','epochs',
    'metrics','train_accuracy','test_accuracy','classification_report','elapsed','summary'
    ,'ipynb','plots']
    param = {}
    for val in var:

        try: 
            param[val] = eval(val)

        except:
            param[val] = val
step - 3 - pickle dump 

    import pickle
    file = open("artefacts.txt", "wb") 
    dictionary = param 
    pickle.dump(dictionary, file) 
    file.close() 

step - 4 - ./pipeline.py -np 

    * relative path to the project ex - ./MNIST
    * choose framework 
    * done!
 
    '''

    print(stages)



def sample_collection():

    pass


def docs():

    help ='''

Arguments - Description

    -np : New project creation
    -varl or --var-list [optional] : prints variable/artifact list or dictionary with datatypes 
        * [optional]

            1. --update : update a the dictionary and var-list with new artifact
            2. --pop : pop an unwanted artifact 

    --status [optional] : prints out catalog with all the projects done until then
        * [optional]

            1. keras : keras portion of catalog
            2. pytorch : pytorch portion of catalog

    --state : prints the actual procedure required to establish a report.csv

    '''

    print(help)


def meta_collect(project_path,project_name,fw):
    '''


    This function collects all the Data required to create a report.csv file
    control flow will be if-else anchored on framework name, since two-frameworks have two distinct reports 
    generated. 
    if pytorch : {code} else: {keras-code} 

    '''
    print('Meta Data Collection and Organisation')

    meta = os.path.join(project_path,'artefacts.txt')
    if os.path.exists(meta):
        print('artefacts.txt exists, extracting content and remodelling .. ')
        with open(meta, 'rb') as f: 
             data = f.read() 
  
        d = pickle.loads(data) 
        report = pd.DataFrame(pd.Series(d)).T
        
        # report.csv creation
        generate_report(project_path, project_name,fw, report)
        

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




def main():

    if sys.argv[1] == '-np':
        
        try:
            if len(sys.argv) == 3: 
                abs_path = sys.argv[2]
                project_name = sys.argv[2].split('/')[1]
                print('Project Directory - {}'.format(project_name))
                project_path,fw = path_creation(abs_path)
                
                meta_collect(project_path,project_name,fw) # Data collection subroutine 
        
        except:
            print("There's no Absolute Path given in the arguments! ")
            
            while(True):
                abs_path = input('Enter the Name of Directory : ')
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
            meta_collect(project_path,project_name,fw)
                

           
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
                variable = input('Enter variable to add into dictionary: ')
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
        
        catalog = pd.read_csv('../catalog.csv')
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

    elif len(sys.argv) == 1:

        print('This Script Takes in Command-Line Arguments, triggering the functionalitied required, try --help for assistance')
        exit(0)

        

    
            

        
       
        



if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('no command line arguments!, try --help')
        exit(1)
    else:
        main()    










