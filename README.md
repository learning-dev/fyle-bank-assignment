# fyle-bank-assignment
fyle assignment - Rest API using Django Rest Framework

### Description 
Web api that does the following- 
- Takes in a **IFSC code** and returns the bank details 
- Takes in a **bank name** and a **city** which returns a list of bank branches in that city. 

### Instructions to run
- #### Deployed App - Application is deployed on heroku 
  - **Curl commands** are included in **commands.txt** to test the APIs

- #### To run locally 
    **Install the packages** 

    ```pip install -r requirements.txt```

    **Populate the DB**
    
    Make sure you have posgres installed and create db with name provided in the settings.py
    You can either populate the db using **bankdb.dump** or using the csv file **bank_branches.csv**. I prefer the latter one i.e. using the csv file in python shell.
    There is also large csv file and jupyter notebook, incase you want to add more branches or play with csv file using pandas 

    **Run the application**
    
      python manage.py runserver
