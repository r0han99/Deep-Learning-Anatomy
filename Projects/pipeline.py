#!/Users/rohan/opt/anaconda3/bin/python
import numpy as np 
import pandas as pd 
import pickle
from pathlib import Path
import sys
import os
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


def generate_report(project_path, project_name,report):

    # creates an Anchor point for the Application c
    if os.path.exists(project_path+'report.csv'):
        print("report already exists, manually verify if it's the one, else delete it and run the script")
    else:
        report.to_csv(project_path+'report.csv')
        print('report created!')
        print('filling catalog .. ')
        with open('../catalog.csv','a+') as f:
            f.write('{},{}\n'.format(project_name,'./Projects/'+project_path[2:]+'report.csv'))
        
        print('Done!')
        

def validate_meta():

    # invoked only when the user's argument demands to 

    pass 



def meta_collect(project_path,project_name):
    '''


    This function collects all the Data required to create a report.csv file
    control flow will be if-else anchored on framework name, since two-frameworks have two distinct reports 
    generated. 
    if pytorch : {code} else: {keras-code} 

    '''
    print('Meta Data Collection and Organisation')

    meta = os.path.join(project_path,'state_dict.txt')
    if os.path.exists(meta):
        print('state_dict.txt exists, extracting content and remodelling .. ')
        with open('./MNIST/Pytorch/state_dict.txt', 'rb') as f: 
             data = f.read() 
  
        d = pickle.loads(data) 
        report = pd.DataFrame(pd.Series(d)).T
        
        # report.csv creation
        generate_report(project_path, project_name, report)
        

    else:
        print('state_dict is not found, create network-metadata before triggering pipeline')


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
    return path_url


def main():

    if sys.argv[1] == '-np':
        
        try:
            if sys.argv[2]: 
                abs_path = sys.argv[2]
                project_name = sys.argv[2].split('/')[1]
                print('Project Directory - {}'.format(project_name))
                project_path = path_creation(abs_path)
                
                meta_collect(project_path,project_name) # Data collection subroutine 
        
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
            project_path = path_creation(abs_path)
            meta_collect(project_path,project_name)
                

           

   

    
            

        
       
        










if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('no command line arguments!, try --help')
        exit(1)
    else:
        main()    










