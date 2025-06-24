-- Lists all genres with the number of shows linked to each
-- Excludes genres with no linked shows
-- Output: genre | number_of_shows
-- Ordered by number_of_shows in descending order
SELECT tv_genres.name AS genre,
COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC
