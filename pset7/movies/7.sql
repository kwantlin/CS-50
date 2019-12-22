SELECT title, rating FROM movies JOIN ratings ON id = movie_id WHERE rating IS NOT NULL AND year IS 2010 ORDER BY rating DESC, title;
-- #7