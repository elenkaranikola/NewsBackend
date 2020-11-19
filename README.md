# NewsBackend

## Project Stucture:
  - utilities.py: Contains all the functions that are being used in this project.
  - stop_words.py: Scans a given text and creates the *filter_words.txt* file in the dependencies folder.
  - dependencies/filter_words.txt: Contains the set of the first 118 most common words and the 500 hundred shortest words of the text.
   - dependencies/imported_stop_words.txt: Contains extra stop words found on the internet and some more based on my observations.
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
[NewBackend](https://github.com/elenisproject/NewsBackend.git)
to fill your database with data.

4. Go back to your terminal and run:
```bash
$ python3 stop_words.py     
$ python3 text_preprocessing.py
```
