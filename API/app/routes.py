from flask import render_template, flash, redirect, url_for, jsonify
from app import app
from app.forms import LoginForm,SearchForm
from app.models import SimilarArticles

@app.route('/',methods=["POST","GET"])
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