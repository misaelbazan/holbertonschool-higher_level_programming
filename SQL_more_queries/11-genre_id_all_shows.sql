-- lists all shows contained in the database hbtn_0d_tvshows
-- each record should display: tv_show.title  - tv_show_genres.genre_id
-- results must be sorted by ASC order by tv_shows.title
-- and tv_show_genres.genre_id
-- if a show doesn't have a genre, display NULL
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
