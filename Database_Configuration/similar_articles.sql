USE NewsCrawler;
create table similar_articles(
   id INT NOT NULL,
   first_article INT NOT NULL,
   second_article INT NOT NULL,
   third_article INT NOT NULL,
   fourth_article INT NOT NULL,
   fifth_article INT NOT NULL,
   PRIMARY KEY ( id ),
   FOREIGN KEY (id) REFERENCES articles(id)
	ON DELETE CASCADE
);