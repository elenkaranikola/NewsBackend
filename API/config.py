import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('mysql://root:eleni123@localhost/NewsCrawler')
    SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://"+ os.environ['DB_USER'] + ":" 
                                         + os.environ['DB_PASSWORD']+ "@" 
                                         + os.environ['DB_HOST'] 
                                         + ":3306/NewsCrawler")
