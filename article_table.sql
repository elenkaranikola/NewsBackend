USE NewsCrawler;
CREATE TABLE articles(
	subtopic VARCHAR(50),
    website CHAR(20),
	title TEXT,
    article_date VARCHAR(50),
    author VARCHAR(50),
    article_body LONGTEXT,
    url TEXT,
);