Steps to install and run the the webapp
Requirements : 
 a.OS - ubuntu, b. browser - Chrome c. Python 2.7

Follow the below steps to create a virtual environment in the assignmnet(Final_Assignment) folder
 Creating a virtual environment 
 1. pip install virtualenv --user
 2.virtualenv -p python2.7 py-2
 3.source py-2/bin/activate
 
1. Then run this command in the pip install -r requirements.txt  in Final_Assignment
2. Run this command in the terminal 'export FLASK_APP=main_code.py'
3. Then run this command 'flask run'
3. Then run command 'flask run'. The webapp will start running  on localhost:5000.
4. Load the chrome exteion by going to 'chrome://extensions' and unpacking the chrome  AW_user_tracker_extension package.
5. Once the AW_user_tracker_extension is successfully installed, run the webapp and through the webapp, navigate to Stackoverflow. The activites will start logging and entering the database.
