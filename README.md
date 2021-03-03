<img width="1150" alt="banner-trans-l" src="https://user-images.githubusercontent.com/45916202/109449517-ac431200-7a6e-11eb-8e7d-d59c26d475b9.png">


[<img src="./pngs/Streamlit.png" width="64" style="float:right border:5px solid black">](https://share.streamlit.io/r0han99/deep-learning-anatomy/main/app.py)

***


## Project Abstract 

_A progressive web application which holds all the Deep Learning Projects that I work on during the subsequent timeline. After every project's completion all the meta-data unique to that deep learning model of a particular problem statement is dynamically collected, organised and byte-encoded into a file to establish the parameters of the project for future reference and a better comprehension of the project. This organised information from the file is then accessed and rendered on the web application deployed on the cloud for anyone to briefly absorb the concept behind the implementation. The application will also include a section, to allow  manual intervention of a user to try out the model in real-time, with their input concerning the project. This entire application is a responsive catalog fairly can be even considered as an ensemled deployment of every project that I do. The front-end aesthetics were facilitated by the Streamlit Library with absolute python codebase._

[Flowchart](https://github.com/r0han99/Deep-Learning-Anatomy/blob/main/Deep-Learning-Anatomy.png) elucidating the _Sequence of Actions and Comms_ between the scripts inorder to fill this catalog with proper details.

 
## Pipeline Script Testing Ideology


( Pre-Deployment ) 

  - ___MNIST___
  - ___CIFAR-10___

( Post-Deployment )

  - ___Dogs-&-Cats___
  

- MNIST : Anchores the process of establishing the comprehensive report sheet which is to be rendered on the web-page.
- CIFAR-10 : Facilitates the process of Constructing and Testing a robust pipeline script which dynamically creates report-sheets with minimal human intervention.
- Dogs-&-Cats : Validates the report generation process and pipeline robustness post-deployment

Note, These 3 projects were the support structures to _test_ and _automate_ the process to fill the project catalogue dynamically.

***

## List of Projects in the Catalogue

**Convolutional Neural Networks**

  `Iteration-0`
   * MNIST
   * CIFAR10

**Transfer Learning** 

   `Iteration-0`
   * Galaxy Classifier ( _InceptionV3_ )
   * Dogs and Cats Classifier (_MobileNetV2_)

***

## Deployment Log 

- **[6th Feb, 2021]** _Deployed_
  - A seamless automated deployment on streamlit-share
  
  
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

[continuation...](https://github.com/r0han99/Deep-Learning-Anatomy/blob/main/changelog.md) ( _last-date in changelog - [3rd March, 2021]_ )


***

  
