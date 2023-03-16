-- create database hbtn_0d_tvshows in you mysql
-- import the table using : mysql -uroot -p hbtn_0d_tvshows < hbtn_0d_tvshows.sql
-- join infomation of tv_shows and tv_show_genres
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
