# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists
    (artist_id text PRIMARY KEY,
     name text NOT NULL, 
     location text, 
     lattitude float, 
     longitude float)
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users
    (user_id int PRIMARY KEY, 
    first_name text NOT NULL, 
    last_name text NOT NULL, 
    gender text, 
    level text)
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs
    (song_id text PRIMARY KEY, 
    title text NOT NULL, 
    artist_id text NOT NULL REFERENCES artists(artist_id), 
    year int, 
    duration float NOT NULL)
""")


time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time
    (start_time timestamp,
     hour int, 
     day int, 
     week int, 
     month int, 
     year int, 
     weekday text)
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays
    (songplay_id SERIAL,
    start_time timestamp, 
    user_id int NOT NULL, 
    level text, 
    song_id text, 
    artist_id text, 
    session_id int, 
    location text, 
    user_agent text,
    PRIMARY KEY (songplay_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (song_id) REFERENCES songs (song_id),
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
    )
""")



# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays
    (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO users
    (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO NOTHING;
""")

song_table_insert = ("""
    INSERT INTO songs
    (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
    INSERT INTO artists
    (artist_id, name, location, lattitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO time
    (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
    SELECT song_id, artists.artist_id
    FROM songs JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s
""")

# QUERY LISTS
create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, artist_table_drop, song_table_drop, time_table_drop, songplay_table_drop]