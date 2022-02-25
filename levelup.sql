CREATE VIEW EVENTS_BY_USER AS
SELECT
    gr.id as gamer_id,
    e.id, 
    e.description,
    e.date,
    e.time,
    g.title,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_event e
JOIN
    levelupapi_game g on g.id = e.game_id
JOIN
    levelupapi_gamer gr ON g.gamer_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id
;