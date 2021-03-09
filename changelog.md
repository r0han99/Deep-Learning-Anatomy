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

- **[2nd Feb, 2021]** _new patches and front-end improvements_ 

    - pipeline script can now edit artefact files directly 
    - added icon and tab name for the application
    - added iteration log in the application
    
- **[6th Feb, 2021]** _CIFAR-10 Keras, Deployment Ready_
  
    - patches for pipeline script on --state
    - completed cifar-10 keras 
    - edited app.py to incorporate changes
    - added requirements.txt 
    - *DEPLOYED ON STREAMLIT SHARE*
    
***

## Post Deployment ChangeLog 

- **[11 Feb, 2021]** _Transfer Learning Section + Galaxy-Classifier-InceptionV3_
  
    - patched pipeline to incorporate transfer learning project creations 
    - implemented galaxy classifier using transfer learning on pretrained network inceptionV3_ 
    - pdf url creation is now completely dynamic based on the artefacts dict

* **[23 Feb, 2021]** _Iteration-0 Elapsed + Dogs and Cats - MobileNetV2_

    * Pipeline patch with Doc String updates, fixed --state typo
    * Dogs & Cats Classifier with MobileNetv2 Under Transfer Learning Section 
    * Application Updated to handle one-hot encoding of y vector and predict vector shapes 

* **[28 Feb, 2021]** _Active SMTP system, Join the Odyssey_
    * SignUp Section to receive periodic emails of ChangeLog and Updated Project Information
    * Pipeline patch to deploy emails and view status
    * Added Banner Image
    * Obfuscated & binary encoded user-db ( currently empty )


* **[3 Mar, 2021]** _db Management_

    * pipeline can now truncate and make backups of userdb 
    * application now has a register button for the signup page
    * pipeline doc updated 

* **[6 Mar, 2021]** _abandoned the idea of db and signup_

    * rolled back to the older version without signup and db integration 
    * cleaned up the repository, moved prompt_list and catalog to /assets 
    * made necessary changes to paths in the application to anticipate changes in the repository 

* **[8 Mar, 2021]** _pipeline patch_
  * pipeline now can --update artefacts like summary and desc by taking formatted information from files
    * updated doc-string
    * fixed formatting for Dogs-Cats Summary

* **[10 Mar, 2021]** _Upload-test case functionality_

    * People can now uploaded an Image concerning the project and get a real-time classification
        of the model.
    *  Category is now a expander section with two sub-categories Projects and Information
        * Information holds all the references, the simulated intermediate activations, pytorch tensor application 
        * Project section is unchanged

    * Application now has multiple page functionality with all the additional/miscellaneous scripts set under `/src`