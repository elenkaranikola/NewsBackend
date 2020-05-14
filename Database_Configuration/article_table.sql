USE NewsCrawler;
CREATE TABLE articles(
	id INT NOT NULL AUTO_INCREMENT,
    subtopic VARCHAR(50) NOT NULL,
    website VARCHAR(20) NOT NULL,
    title TEXT NOT NULL,
    article_date DATE,
    author VARCHAR(50) NOT NULL,
    article_body LONGTEXT NOT NULL,
    url VARCHAR(200) NOT NULL,
    PRIMARY KEY (id)
);