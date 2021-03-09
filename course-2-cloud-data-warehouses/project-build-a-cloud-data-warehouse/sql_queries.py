import configparser


# CONFIG

config = configparser.ConfigParser()
config.read('dwh.cfg')
IAM = config['IAM_ROLE']['ARN']
LOG_DATA = config['S3']['LOG_DATA']
SONG_DATA = config['S3']['SONG_DATA']
LOG_JSONPATH = config['S3']['LOG_JSONPATH']

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create = ("""CREATE TABLE IF NOT EXISTS staging_events (
    artist                  VARCHAR, 
    auth                    VARCHAR, 
    firstName               VARCHAR, 
    gender                  VARCHAR, 
    itemInSession           INT,
    lastName                VARCHAR, 
    length                  FLOAT, 
    level                   VARCHAR, 
    location                VARCHAR, 
    method                  VARCHAR,
    page                    VARCHAR, 
    registration            VARCHAR, 
    sessionId               INT, 
    song                    VARCHAR, 
    status                  INT,
    ts                      TIMESTAMP, 
    userAgent               VARCHAR, 
    userId                  INT
    );
""")

staging_songs_table_create = ("""CREATE TABLE IF NOT EXISTS staging_songs (
    song_id                 VARCHAR PRIMARY KEY, 
    artist_id               VARCHAR, 
    artist_latitude         FLOAT,
    artist_longitude        FLOAT, 
    artist_location         VARCHAR, 
    artist_name             VARCHAR,
    duration                FLOAT, 
    num_songs               INT, 
    title                   VARCHAR, 
    year                    INT
    );
""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
    songplay_id             INT IDENTITY(0,1) PRIMARY KEY, 
    start_time              TIMESTAMP NOT NULL,
    user_id                 INT NOT NULL,
    level                   VARCHAR,
    song_id                 VARCHAR,
    artist_id               VARCHAR,
    session_id              INT, 
    location                VARCHAR,
    user_agent              VARCHAR
    );
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
    user_id                 INT PRIMARY KEY NOT NULL, 
    first_name              VARCHAR, 
    last_name               VARCHAR, 
    gender                  VARCHAR, 
    level                   VARCHAR
    );
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
    song_id                 VARCHAR PRIMARY KEY,
    title                   VARCHAR, 
    artist_id               VARCHAR, 
    year                    INT, 
    duration                FLOAT
    );
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
    artist_id               VARCHAR PRIMARY KEY,
    name                    VARCHAR, 
    location                VARCHAR, 
    latitude                FLOAT, 
    longitude               FLOAT
    );
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
    start_time              TIMESTAMP PRIMARY KEY, 
    hour                    INT, 
    day                     INT, 
    week                    INT, 
    month                   INT, 
    year                    INT, 
    weekday                 INT
    );
""")

# STAGING TABLES

staging_events_copy = ("""
    COPY staging_events 
    FROM {} 
    IAM_ROLE {} 
    REGION 'us-west-2'
    COMPUPDATE OFF
    JSON {}
    TIMEFORMAT as 'epochmillisecs';
""").format(LOG_DATA, IAM, LOG_JSONPATH)

staging_songs_copy = ("""
    COPY staging_songs 
    FROM {} 
    IAM_ROLE {}
    REGION 'us-west-2'
    COMPUPDATE OFF
    JSON 'auto';
""").format(SONG_DATA, IAM)

# FINAL TABLES

songplay_table_insert = ("""INSERT INTO songplays (
                                start_time, 
                                user_id, 
                                level, 
                                song_id, 
                                artist_id, 
                                session_id, 
                                location, 
                                user_agent) 
                            SELECT 
                                staging_events.ts AS start_time,
                                staging_events.userId AS user_id,
                                staging_events.level AS level,
                                staging_songs.song_id AS song_id,
                                staging_songs.artist_id AS artist_id,
                                staging_events.sessionId AS session_id,
                                staging_events.location AS location,
                                staging_events.userAgent AS user_agent
                            FROM staging_events
                            JOIN staging_songs
                            ON (staging_events.artist = staging_songs.artist_name)
                            AND (staging_events.song = staging_songs.title)
                            AND (staging_events.length = staging_songs.duration)
                            WHERE staging_events.page = 'NextSong';
""")

user_table_insert = ("""INSERT INTO users (
                            user_id, 
                            first_name, 
                            last_name, 
                            gender, 
                            level) 
                        SELECT DISTINCT 
                            userId AS user_id,
                            firstName AS first_name,
                            lastName AS last_name,
                            gender,
                            level
                        FROM staging_events
                        WHERE page='NextSong';
""")

song_table_insert = ("""INSERT INTO songs (
                            song_id, 
                            title, 
                            artist_id, 
                            year, 
                            duration) 
                        SELECT 
                            song_id,
                            title,
                            artist_id,
                            year,
                            duration
                        FROM staging_songs;
""")

artist_table_insert = ("""INSERT INTO artists (
                            artist_id, 
                            name, 
                            location, 
                            latitude, 
                            longitude) 
                        SELECT 
                            artist_id,
                            artist_name AS name,
                            artist_location AS location,
                            artist_latitude AS latitude,
                            artist_longitude AS longitude
                        FROM staging_songs;
""")

time_table_insert = ("""INSERT INTO time (
                            start_time, 
                            hour, 
                            day, 
                            week, 
                            month, 
                            year, 
                            weekday) 
                        SELECT 
                            start_time,
                            extract(hour from start_time), 
                            extract(day from start_time), 
                            extract(week from start_time), 
                            extract(month from start_time), 
                            extract(year from start_time), 
                            extract(dayofweek from start_time) AS weekday
                        FROM songplays;
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
