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

@app.route('/politics')
def politics():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Politics').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('politics', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('politics', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('politics.html', title='Politics Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)

@app.route('/culture')
def culture():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Culture').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('culture', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('culture', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('culture.html', title='Culture Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)

@app.route('/economics')
def economics():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Economics').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('economics', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('economics', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('economics.html', title='Economics Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)


@app.route('/env')
def env():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Environment').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('env', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('env', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('env.html', title='Environment Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)


@app.route('/food')
def food():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Food').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('food', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('food', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('food.html', title='Food Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)



@app.route('/society')
def society():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Society').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('society', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('society', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('society.html', title='Society Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)



@app.route('/sport')
def sport():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Sport').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('sport', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('sport', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('sport.html', title='Sport Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)


@app.route('/style')
def style():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Style').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('style', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('style', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('style.html', title='Style Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)


@app.route('/tech')
def tech():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Tech').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('tech', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('tech', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('tech.html', title='Technology Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)



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