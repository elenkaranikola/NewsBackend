USE NewsCrawler;
create table similar_articles(
   id INT NOT NULL,
   similar_articles VARCHAR(100) NOT NULL,
   PRIMARY KEY ( id ),
   FOREIGN KEY (id) REFERENCES articles(id)
	ON DELETE CASCADE
);