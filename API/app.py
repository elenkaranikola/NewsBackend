from flask import Flask, render_template, url_for, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL(app)

#Enter here your database informations 
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "eleni123"
app.config["MYSQL_DB"] = "NewsCrawler"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/livesearch",methods=["POST","GET"])
def livesearch():
   searchbox = request.form.get("text")
   cursor = mysql.connection.cursor()
   query = "select article_body from articles where id LIKE '{}%' ".format(searchbox)#This is just example query , you should replace field names with yours
   cursor.execute(query)
   result = cursor.fetchall()
   return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True)
