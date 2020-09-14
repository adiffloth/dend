# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

songplay_table_create = ("""
create table if not exists songplays
 (songplay_id int primary key,
  ts_dt date references time(ts_dt),
  user_id varchar references users(user_id),
  level varchar,
  song_id varchar references songs(song_id),
  artist_id varchar references artists(artist_id),
  session_id varchar,
  location varchar,
  user_agent varchar);
""")

user_table_create = ("""
create table if not exists users
 (user_id varchar primary key,
  firstname varchar,
  lastname varchar,
  gender varchar(1),
  level varchar);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
 (song_id varchar primary key,
  title varchar,
  artist_id varchar references artists(artist_id),
  year int,
  duration real);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
 (artist_id varchar PRIMARY KEY,
  name text NOT NULL,
  location text,
  latitude real,
  longitude real);
""")

time_table_create = ("""
create table if not exists time
 (ts_dt date primary key,
  hour integer,
  day integer,
  week integer,
  month integer,
  year integer,
  weekday integer);
""")

# INSERT RECORDS

songplay_table_insert = ("""
insert into songplays (songplay_id, ts_dt, user_id, level, song_id, artist_id, session_id, location, user_agent)
 values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
 on conflict (songplay_id) do nothing;
""")

user_table_insert = ("""
insert into users (user_id, firstname, lastname, gender, level)
 values (%s, %s, %s, %s, %s)
 on conflict (user_id) do nothing;
""")

song_table_insert = ("""
insert into songs (song_id, title, artist_id, year, duration)
 values (%s, %s, %s, %s, %s)
 on conflict (song_id) do nothing;
""")

artist_table_insert = ("""
insert into artists (artist_id, name, location, latitude, longitude)
 values (%s, %s, %s, %s, %s)
 on conflict (artist_id) do nothing;
""")

time_table_insert = ("""
insert into time (ts_dt, hour, day, week, month, year, weekday)
 values (%s, %s, %s, %s, %s, %s, %s)
 on conflict (ts_dt) do nothing;
""")

# FIND SONGS

song_select = ("""
select song_id, songs.artist_id
 from songs join artists on songs.artist_id = artists.artist_id
 where title = %s
 and artists.name = %s
 and songs.duration = %s;
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
