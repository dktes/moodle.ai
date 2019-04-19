# moodle.ai
DKTES one stop for Machine Learning resources of Python, ML, DL resources and more...
Thanks to open source community for providing awesome content on internet. Notebooks are prepared using online references gathered from appliedai, Corey Schefar, StatQuest, medium blogs, etc.
OK

# Usage:
A. Learn the basics of Jupyter Notebook here:- 
[Jupyter Basics](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html)

B. More information about using colaboratory here:-  [Using Colab](https://colab.research.google.com/notebooks/welcome.ipynb)

C . To try out Notebooks in Google Colab click here:-  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dktes/moodle.ai/)
  1. This is the best method to access our resources without having the hectic of installation of packages
  2. Google Colab provides free GPU/TPU instance
  3. Your selected notebook is first opened in playground mode where you can play with code written by us. And when you reopen the notebook changes won't be persistent.
  4. To make persistent changes save a copy of notebook save it to your drive.

D. To try out Notebooks in Microsoft Azure click here:-   [![Open in Azure](https://notebooks.azure.com/launch.svg)](https://notebooks.azure.com/dktescse/projects/moodle-ai)
  1. Another option for google colab
  2. You need to have sign up first to play with notebooks.
  3. Unless you clone the notebooks you cannot execute the code.

E. To create similar environment on your local machine:-

 <b> 1. Windows Users:</b><br>
    (Uninstall any previous python installations to prevent conflicts)<br>
    a. If it is your first time to run the code of this book, you need to complete the following 4 steps. Next time you can jump directly to Step 3 and Step 4.<br><br>
      Step 1: is to download and install Miniconda according to the operating system in use. During the installation, it is required to choose the option “Add Anaconda to the system PATH environment variable”.<br><br>
      Step 2: is to create a virtual (running) environment using conda to install the libraries needed. Type in cmd:-
      `conda env create -f ML.yml` <br><br>
      Step 3: is to activate the environment that is created earlier.To exit the environment, use the command `conda deactivate` (if the conda version is lower than 4.4, use the command `deactivate`). If the conda version is lower than 4.4, use the command `activate ML` else  `conda activate ML`<br><br>
      Step 4: Open jupyter notebook `jupyter notebook`. Make sure your environment is activated and you are in correct directory.<br><br>
  
  <b>2. Linux/macOS Users:</b><br>
    Step 1: is to download and install Miniconda according to the operating system in use. It is a sh file. Open the Terminal application and enter the command to execute the sh file, such as<br>
 `# The file name is subject to change, always use the one downloaded from the Miniconda website
  sh Miniconda3-latest-Linux-x86_64.sh`<br><br>
  The terms of use will be displayed during installation. Press “↓” to continue reading, press “Q” to exit reading. After that, answer the following questions:<br>
`Do you accept the license terms? [yes|no]
[no] >>> yes
Do you wish the installer to prepend the Miniconda3 install location
to PATH in your /home/your_name/your_file ? [yes|no]
[no] >>> yes`<br><br>
After the installation is complete, conda should be made to take effect. Linux users need to run source ~/.bashrc or restart the command line application; macOS users need to run source ~/.bash_profile or restart the command line application.
<br><br>
Step 2: refer to the such steps for Windows users as described earlier. If the conda version is lower than 4.4, replace the command in Step 3 with `source activate ML` and exit the virtual environment using the command `source deactivate`.<br><br>
      
# Updating Code and Running Environment
update the running environment with the command<br>
`conda env update -f ML.yml`<br>
The subsequent steps for activating the environment and running Jupyter are the same as those described earlier.<br>
 
