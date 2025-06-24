-- List all shows from tv_shows that do not have any genre linked
-- Results are sorted by title in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC
