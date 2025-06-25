-- List all TV shows along with their associated genres
-- Shows with no genre are also included using LEFT JOINs
-- Results are sorted by show title (ascending), then genre name (ascending)
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
