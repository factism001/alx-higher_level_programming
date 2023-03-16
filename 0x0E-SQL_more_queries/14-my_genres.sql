-- double JOIN using 3 different tables
-- the idea is always get relations table-table and in that way
-- get the information that we need
-- the important thing is relate both JOINs
SELECT tv_genres.name FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC;
