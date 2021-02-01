# The Deep Learning Anatomy <img src="./deep-learning.png" width="32">


A Comprehensive **Deep Learning** _Project Catalogue_ holding sophisticated details of a project implmented using both _Pytorch_
and _Keras_ 

![dl-banner](https://user-images.githubusercontent.com/45916202/105623232-3aa7f080-5e3e-11eb-8caa-478302027063.jpg)



```A Deep Neural Network```

***


## Project Abstract 

_A progressive web application which holds all the Deep Learning projects that I work on, during the timeline. Post every project's completion all the meta-data regarding the deep learning model unique to that particular problem statement is dynamically collected, organised and made into a report file to establish the parameters of the project for future reference and a better understanding of the project itself. This organised information is then rendered on the web application deployed on the cloud for anyone to briefly absorb the concept behind the implementation. The application will also include a section, to allow  manual intervention of a user to try out the model in real-time with their input concerning the project. The entire front-end aesthetics were facilitated by the Streamlit Library with python codebase._

[Abstract Communication Model](https://github.com/r0han99/Deep-Learning-Anatomy/blob/main/DL-Anatomy-comms.png), which represents the sequence of actions and comms between the _scripts_ before a project ends up in the _Application catalogue_.


## Project Catalogue 

### _Pytorch & Keras_ 

( Pre-Deployment ) 

  - ___MNIST___
  - ___CIFAR-10___

( Post-Deployment )

  - ___Dogs-&-Cats___
  
  
 
## Pipeline Script Testing Ideology

- MNIST : Anchores the process of establishing the comprehensive report sheet which is to be rendered on the web-page.
- CIFAR-10 : Facilitates the process of Constructing and Testing a robust pipeline script which dynamically creates report-sheets with minimal human intervention.
- Cats-&-Dogs : Validates the report generation process and pipeline robustness post-deployment

Note, These 3 projects were the support structures to _test_ and _automate_ the process to fill the project catalogue dynamically.

## Deployment Log 

- _None_


## Change Log

- **[24th Jan, 2021]**  _init_

  - Developed a pipeline script which is executed post project development, this gathers all the meta information from the project such as The Neural Network     Architecture ( _layers_, _Hidden Units_ ), Type of Prediction ( _Classification_, _Regression_), Type of Network ( _Convolutional_, _Recurrent_ ) etc. The meta info is organised and a report file is created, which is then processed by the application from the project _dir_ to be rendered on the Web Page.
  - Partially developed Application codebase. Front-End Project Artefacts are laid down 
  
  
- **[26th Jan, 2021]** _new patches_ 
  - created variable_dict and prompt_dict
  - Added commandline functionalities to the pipeline script to handle var-dicts and prompt-list
  - now the prompts under the project artefacts are predefined and dynamically generated
  - segmented artefacts and plots into radios
  - added download-link to the source-code pdf
  - cs_plots() will render the plots related/included in a particular project
  
- **[27th Jan, 2021]** _Keras MNIST and Patches_
  - _Keras_ MNIST is added into Catalog 
  - Pipeline script is now more verbose with integrated documentation
  - catalog status can be fetched by pipeline script with provided args 
  
- **[30th Jan, 2021]** _pipeline patch-3, application dev++_
  - report.csv creation is now deprecated, byte encoded artefacts are used for rendering information
  - pipeline modified to the above criteria
  - added network 4 missed out network artifacts - Loss, batch_size, learning_rate, optimizer
  - changed logo to iteration3
   
- **[1st Feb, 2021]** _data-overview, model-eval, patch-4_

  - Script Name changed to app.py following the streamlit convention
  - Added Data collection procedure required for both Data Overview section and Model Evaluation
  - added doc string to pipeline script for the data collection procecure


  
