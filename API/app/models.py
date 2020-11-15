from app import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subtopic = db.Column(db.String(50), index=True)
    website = db.Column(db.String(20), index=True)
    title = db.Column(db.Text, index=True)
    article_date = db.Column(db.DateTime, index=True)
    author = db.Column(db.String(50), index=True)
    article_body = db.Column(db.Text, index=True)
    url = db.Column(db.String(200), index=True)

    def __repr__(self):
        return '<Article {}>'.format(self.title)

class SimilarArticles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_article = db.Column(db.Integer, index=True)
    second_article = db.Column(db.Integer, index=True)
    third_article = db.Column(db.Integer, index=True)
    fourth_article = db.Column(db.Integer, index=True)
    fifth_article = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<SimilarArticles {}>'.format(self.id)

#@login.article_loader
#def load_article(id):
#    return Article.query.get(int(id))