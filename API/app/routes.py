 # -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, jsonify, Response, request
import random
import time
from app import app
from app.forms import LoginForm,SearchForm
from app.models import SimilarArticles,Articles
from functools import wraps
import os

@app.route('/',methods=["POST","GET"])
@app.route('/home')
def home():
    articles = Articles.query.limit(10).all()
    #article_dicts = {}
    #index = 0
    articles_list = []
    for article in articles:
        articles_list.append(article)
        #article_dicts[article.id] = [article.topic,article.article_body]
        #index += 1
    #return  jsonify(article_dicts)
    if request.args:
        index = int(request.args.get('index'))
        limit = int(request.args.get('limit'))
    

        return render_template('home.html', title='All Articles',articles = articles_list[index:limit + index])
    else:
        return render_template('home.html', title='All Articles',articles = articles_list[:10])

    #return render_template('home.html', title='All Articles',articles = articles_list)


@app.route("/search",methods=["POST","GET"])
def search(): 
    form = SearchForm()
    if form.validate_on_submit():
        article = SimilarArticles.query.filter_by(id=form.index.data).first()
        return render_template('results.html', title='Search Results', article=article)
        #return (article.first_article)
        flash('Login requested for index {}'.format(
            form.index.data))
        return redirect(url_for('index'))
    return render_template('search.html', title='Search Article', form=form)

@app.route("/results")
def results():
    return render_template('results.html', title='Search Results', article=article)


@app.route("/load")
def load():
    """ Route to return the posts """

    time.sleep(0.2)  # Used to simulate delay

    if request.args:
        counter = int(request.args.get("c"))  # The 'counter' value sent in the QS
        res = Articles.query.limit(counter).all()
        #if counter == 0:
        #    print(f"Returning posts 0 to {quantity}")
        #    # Slice 0 -> quantity from the db
        #    res = make_response(jsonify(db[0: quantity]), 200)
#
        #elif counter == posts:
        #    print("No more posts")
        #    res = make_response(jsonify({}), 200)
#
        #else:
        #    print(f"Returning posts {counter} to {counter + quantity}")
        #    # Slice counter -> quantity from the db
        #    res = make_response(jsonify(db[counter: counter + quantity]), 200)

    return res

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)