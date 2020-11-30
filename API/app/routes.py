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
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('home', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('home', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('home.html', title='All Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)


@app.route('/world')
def world():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='World').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('world', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('world', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('world.html', title='All Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)

    #article_dicts = {}
    #index = 0
    #articles_list = []
    #for article in articles:
    #    articles_list.append(article)

    #return render_template('ArticleSizePerCategory.html')
    #return render_template('home.html', title='All Articles',articles = articles_list)

@app.route("/article/<id>")
def article(id):
    article = Articles.query.filter_by(id=id).first_or_404()
    similar_articles =  SimilarArticles.query.filter_by(id=id).first()
    first_article = Articles.query.filter_by(id=similar_articles.first_article).first_or_404()
    second_article = Articles.query.filter_by(id=similar_articles.second_article).first_or_404()
    third_article = Articles.query.filter_by(id=similar_articles.third_article).first_or_404()
    return render_template('article.html', article=article, first_article=first_article, second_article=second_article, third_article=third_article)


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