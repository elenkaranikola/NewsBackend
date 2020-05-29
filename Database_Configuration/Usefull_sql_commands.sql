-- specify the schema used
USE NewsCrawler;

-- select all articles extracted
SELECT * FROM articles;

-- count the number of articles per site
SELECT COUNT(*) FROM articles WHERE website="tanea.gr";

-- Return the different websites articles have been extracted
SELECT DISTINCT website FROM articles;

-- Delete articles from a specific site 
DELETE FROM articles WHERE topic = "World" AND website = "efsyn.gr";