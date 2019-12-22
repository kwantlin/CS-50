SELECT AVG(movie_id) FROM ratings WHERE movie_id IN (SELECT id FROM movies WHERE year = 2012);
-- #6