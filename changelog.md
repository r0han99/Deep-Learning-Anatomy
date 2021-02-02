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

