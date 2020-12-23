 # -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, jsonify, Response, request, g
import random
import time
from app import app
from app.classifier import Classifier
from app.forms import LoginForm,SearchForm,ClassifierForm
from app.models import SimilarArticles,Articles
from flask_login import login_required
from flask_babel import _, get_locale
from flask_babel import lazy_gettext as _l
from functools import wraps
from sqlalchemy import and_, or_, not_, desc
from sqlalchemy.sql.expression import func
import runpy
import re
import os

@app.route('/',methods=["POST","GET"])

@app.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.order_by(func.rand()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('home', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('home', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('home.html', title='All Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)


@app.route('/classifier',methods=["POST","GET"])
def classifier():
    form = ClassifierForm()
    if form.validate_on_submit():
        text = form.index.data
        category = Classifier(form.index.data)
        articles = Articles.query.filter_by(topic=category).limit(10)
        #article = SimilarArticles.query.filter_by(id=form.index.data).first()
        return render_template('results.html', title='Search Results', category=category, text=text[0:100], articles = articles)
    return render_template('classifier.html', title='Search Article', form=form)


@app.route('/alphabetical')
def alphabetical():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.order_by(Articles.title).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('alphabetical', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('alphabetical', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('alphabetical.html', title='Alphabetical order', articles=articles.items, next_url=next_url, prev_url=prev_url)

@app.route('/alphabeticalDesc')
def alphabeticalDesc():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.order_by(desc(Articles.title)).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('alphabeticalDesc', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('alphabeticalDesc', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('alphabeticalDesc.html', title='Alphabetical order desc', articles=articles.items, next_url=next_url, prev_url=prev_url)

@app.route('/newest')
def newest():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.order_by(desc(Articles.article_date)).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('newest', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('newest', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('newest.html', title='Newest Publishes', articles=articles.items, next_url=next_url, prev_url=prev_url)

@app.route('/oldest')
def oldest():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.order_by(Articles.article_date).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('oldest', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('oldest', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('oldest.html', title='Oldest Publishes', articles=articles.items, next_url=next_url, prev_url=prev_url)

@app.route('/alphabeticalCat')
def alphabeticalCat():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.order_by(Articles.subtopic).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('alphabeticalCat', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('alphabeticalCat', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('alphabeticalCat.html', title='Alphabetical Category order', articles=articles.items, next_url=next_url, prev_url=prev_url)

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/articles_available_from_each_year')
def articles_available_from_each_year():
    return render_template('charts/articles_available_from_each_year.html')    

@app.route('/beginner_reading')
def beginner_reading():
    return render_template('charts/beginner_reading.html')   

@app.route('/categorize_sites')
def categorize_sites():
    return render_template('charts/categorize_sites.html')   

@app.route('/analytics')
def analytics():
    return render_template('notebooks.html')

@app.route('/article_size_per_category')
def article_size_per_category():
    return render_template('notebooks/article_size.html')

@app.route('/goodnews_badnews')
def goodnews_badnews():
    return render_template('notebooks/goodnews_badnews.html')

@app.route('/most_common_countries')
def most_common_countries():
    return render_template('notebooks/most_common_countries.html')    

@app.route('/most_common_per_category')
def most_common_per_category():
    return render_template('notebooks/most_common_per_category.html')

@app.route('/most_news_source')
def most_news_source():
    return render_template('notebooks/most_news_source.html')

@app.route('/most_popular_authors')
def most_popular_authors():
    return render_template('notebooks/most_popular_authors.html') 

@app.route('/percentage_top_authors')
def percentage_top_authors():
    return render_template('notebooks/percentage_top_authors.html')    

@app.route('/popular_word_per_year')
def popular_word_per_year():
    return render_template('notebooks/popular_word_per_year.html')

@app.route('/quality_of_articles')
def quality_of_articles():
    return render_template('notebooks/quality_of_articles.html')

@app.route('/word_popularity_in_time')
def word_popularity_in_time():
    return render_template('notebooks/word_popularity_in_time.html') 

@app.before_request
def before_request():
    g.search_form = SearchForm()
    g.locale = str(get_locale())

@app.route('/search',methods=["POST","GET"])
def search():
    page = request.args.get('page', 1, type=int)
    form_input = g.search_form.q.data
    search = '%{}%'.format(form_input)

    articles = Articles.query.filter(Articles.article_body.like(search)).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('search', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('search', page=articles.prev_num) \
        if articles.has_prev else None
    return render_template('search.html', title='All Articles', articles=articles.items, search=form_input, next_url=next_url, prev_url=prev_url)


@app.route('/World')
def World():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='World').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('World', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('World', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('World.html', title='All Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)

@app.route('/Politics')
def Politics():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Politics').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('Politics', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('Politics', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('Politics.html', title='Politics Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)

@app.route('/Culture')
def Culture():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Culture').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('Culture', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('Culture', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('Culture.html', title='Culture Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)

@app.route('/Economics')
def Economics():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Economics').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('Economics', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('Economics', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('Economics.html', title='Economics Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)


@app.route('/Environment')
def Environment():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Environment').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('Environment', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('Environment', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('Environment.html', title='Environment Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)


@app.route('/Food')
def Food():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Food').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('Food', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('Food', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('Food.html', title='Food Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)



@app.route('/Society')
def Society():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Society').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('Society', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('Society', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('Society.html', title='Society Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)



@app.route('/Sport')
def Sport():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Sport').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('Sport', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('Sport', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('Sport.html', title='Sport Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)


@app.route('/Style')
def Style():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Style').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('Style', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('Style', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('Style.html', title='Style Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)


@app.route('/Tech')
def Tech():
    page = request.args.get('page', 1, type=int)
    articles = Articles.query.filter_by(topic='Tech').paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('Tech', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('Tech', page=articles.prev_num) \
        if articles.has_prev else None

    return render_template('Tech.html', title='Technology Articles', articles=articles.items, next_url=next_url, prev_url=prev_url)




@app.route("/article/<id>")
def article(id):
    article = Articles.query.filter_by(id=id).first_or_404()
    similar_articles =  SimilarArticles.query.filter_by(id=id).first()
    first_article = Articles.query.filter_by(id=similar_articles.first_article).first_or_404()
    second_article = Articles.query.filter_by(id=similar_articles.second_article).first_or_404()
    third_article = Articles.query.filter_by(id=similar_articles.third_article).first_or_404()
    return render_template('article.html', article=article, first_article=first_article, second_article=second_article, third_article=third_article)


@app.route("/articlesFromSearch/<id>/<search>")
def articlesFromSearch(id,search):
    article = Articles.query.filter_by(id=id).first_or_404()
    similar_articles =  SimilarArticles.query.filter_by(id=id).first()
    first_article = Articles.query.filter_by(id=similar_articles.first_article).first_or_404()
    second_article = Articles.query.filter_by(id=similar_articles.second_article).first_or_404()
    third_article = Articles.query.filter_by(id=similar_articles.third_article).first_or_404()
    return render_template('articlesFromSearch.html', article=article, first_article=first_article, second_article=second_article, third_article=third_article, search=search)



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

@app.route('/go_back/<string:topic>',methods=['GET'])
def go_back(topic):
    return redirect(url_for(topic))

@app.route('/back_to_search/<string:search>',methods=['GET','POST'])
def back_to_search(search):
    page = request.args.get('page', 1, type=int)
    my_input = '%{}%'.format(search)

    articles = Articles.query.filter(Articles.article_body.like(my_input)).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('search', page=articles.next_num) \
        if articles.has_next else None
    prev_url = url_for('search', page=articles.prev_num) \
        if articles.has_prev else None
    return render_template('search.html', title='All Articles', articles=articles.items, search=search, next_url=next_url, prev_url=prev_url)
