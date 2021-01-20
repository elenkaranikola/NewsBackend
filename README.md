# NewsBackend

## Project Stucture:

  - API: This folder is for everyhting that has to do with website
    - requirements.txt : All the programs needed to run the project.
    - config.py : Basic configuration for our website, use as is, no modifications needed.
    - classifier.py : Code for our classifier.
    - app.py : Part of flask structure for running the website.
    - venv : Folder used to activate our virtual environment.
    - app/static/img : Folder of images used in the website.
    - app/static/style.css : Personalized stylesheet.
    - app/static/templates : All the html pages.
    - app/__ init__ .py : First file to start up the flask project
    - app/classifier.py : Classifier as used and called from the website.
    - app/forms.py : In this file we structure the forms that will be used to get the user data from our web pages.
    - app/models.py : Contains the objects flask recongizes and accepts.
    - app/routes.py : Is the main body code of the website with the fucntions and endpoint the website uses.

  - ChartFunctions : In This folder are all the python scripts used to calculate the data used for the javascript charts.
  - Database_Configurations : As the name indicates, this folder has all the sql commands needed for the project. 
    - commands.sql : Usefull sql commands to control and test the database
    - create_table_articles.sql : Creates the table in which we will save our articles
    - similar_articles.sql : Creates the table where we save the similar articles information
  
  - TextPreprocessor: Folder with the python scripts used to edit our text data.
    - clean_input.py : For the input given it retuns the text in the wanted formula.
    - common_articles_finder.py : Code used to calculate the similar articles and fill the similar_articles table in the database
    - stop_words.py : Scans a given text and creates the *filter_words.txt* file in the dependencies folder.
    
  - utilities.py: Contains all the functions that are being used in this project.
  - dependencies/filter_words.txt: Contains the set of the first 118 most common words and the 500 hundred shortest words of the text.
  - dependencies/imported_stop_words.txt: Contains extra stop words found on the internet and some more based on my observations.
  - dependencies/api_charts : Containes the data used in the javascript files.
  - text_preprocessing.py: Used to keep only the usefull words from a text.
  - commands.sql: Sql commands to control tha data on the database.
  - create_table_articles.sql: Sql commands used to create our database.
  
  
### Steps to run this project:

1. Open your terminal and run:

```bash
$ git clone https://github.com/elenisproject/NewsBackend.git
$ cd NewsBackend
$ pip3 install -r requirements.txt

```
*Now we have in our computer, the code we need to start this project. Time to create our database. I used MySQLWorkbench.* 

2. Create a new schema and run the sql command:
[create_table_article.sql](Database_Configuration/create_table_articles.sql)

3. Run the project as explained in
[NewsBackend](https://github.com/elenisproject/NewsBackend.git)
to fill your database with data.

4. Go back to your terminal and run:
```bash
$ python3 stop_words.py     
$ python3 text_preprocessing.py
```
