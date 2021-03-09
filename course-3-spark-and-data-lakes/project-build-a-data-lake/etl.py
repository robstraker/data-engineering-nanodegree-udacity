import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format
from pyspark.sql.types import DateType, TimestampType


config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS']['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    """
    - Creates Spark session
    """
    print("Creating Spark Session...")
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    """
    - Opens S3 or local song file
    - Extracts song data and inserts new song data into 'songs' table
    - Extracts artist data and inserts new artist data into 'artists' table
    """
    # get filepath to S3 or local song data file
    song_data = input_data + 'song_data/*/*/*/*.json' # full S3 dataset or local dataset
    #song_data = input_data + 'song_data/A/A/A/*.json' # subset of S3 dataset
    
    # read song data file
    print("Reading song data files...")
    df = spark.read.json(song_data)

    # create a temporary view against which SQL queries can be run
    df.createOrReplaceTempView('songs_table')
    
    # extract columns to create songs table
    print("Extracting columns to create songs table...")
    songs_table = spark.sql("""
                            SELECT DISTINCT song_id, 
                                             title, 
                                             artist_id, 
                                             year, 
                                             duration, 
                                             artist_name
                            FROM songs_table
                            WHERE song_id IS NOT NULL
                            """)
    
    # write songs table to parquet files partitioned by year and artist
    print("Writing songs table to parquet files...")
    songs_table.write.parquet(os.path.join(output_data, 'songs_table/'), \
                              mode='overwrite', partitionBy=['year', 'artist_id'])
    
    # extract columns to create artists table
    print("Extracting columns to create artists table...")
    artists_table = spark.sql("""
                              SELECT DISTINCT artist_id, 
                                              artist_name as name, 
                                              artist_location as location, 
                                              artist_latitude as latitude, 
                                              artist_longitude as longitude
                              FROM songs_table
                              WHERE artist_id IS NOT NULL
                              """)
    
    # write artists table to parquet files
    print("Writing artists table to parquet files...")
    artists_table.write.parquet(os.path.join(output_data, 'artists_table/'), mode='overwrite')
    

def process_log_data(spark, input_data, output_data):
    """
    - Opens S3 or local log file
    - Filters out by NextSong to eliminate invalid song plays
    - Extracts user data and inserts new user data into 'users' table
    - Extracts time data, converts to timestamp and datetime, inserts new time data into 'time' table
    - Extracts songplay data and inserts new songplay data into 'songplays' table
    """
    # get filepath to S3 or local log data file
    #log_data = input_data + 'log_data/*.json'        # local dataset
    log_data = input_data + 'log_data/*/*/*.json'     # S3 dataset

    # read log data file
    print("Reading log data files...")
    df = spark.read.json(log_data)
    
    # filter by actions for song plays
    df = df.filter(df.page == 'NextSong')

    # create a temporary view against which SQL queries can be run
    df.createOrReplaceTempView('log_table')
    
    # extract columns for users table   
    print("Extracting columns to create users table...")
    users_table = spark.sql("""
                            SELECT DISTINCT userId as user_id, 
                                            firstName as first_name, 
                                            lastName as last_name, 
                                            gender, 
                                            level
                            FROM log_table
                            WHERE userId IS NOT NULL
                            """)
    
    # write users table to parquet files
    print("Writing users table to parquet files...")
    users_table.write.parquet(os.path.join(output_data, 'users/'), mode='overwrite')

    # create timestamp column from original timestamp column
    get_timestamp = udf(lambda x:  datetime.fromtimestamp((x/1000.0)), TimestampType())
    df = df.withColumn('timestamp', get_timestamp(df.ts))
    
    # create datetime column from original timestamp column
    get_datetime = udf(lambda x: datetime.fromtimestamp((x/1000.0)), DateType())
    df = df.withColumn('datetime', get_datetime(df.ts))

    # create a temporary view against which SQL queries can be run
    df.createOrReplaceTempView('time_table')
    
    # extract columns to create time table
    print("Extracting columns to create time table...")
    time_table = spark.sql("""
                           SELECT DISTINCT timestamp as start_time,  
                                           hour(timestamp) as hour, 
                                           day(timestamp) as day, 
                                           weekofyear(timestamp) as week,  
                                           month(timestamp) as month, 
                                           year(timestamp) as year, 
                                           dayofweek(timestamp) as weekday 
                           FROM time_table
                           WHERE timestamp IS NOT NULL
                           ORDER BY timestamp
                           """)
    
    # write time table to parquet files partitioned by year and month
    print("Writing time table to parquet files...")
    time_table.write.parquet(os.path.join(output_data, 'time_table/'), \
                             mode='overwrite', partitionBy=['year', 'month'])

    # read in song data to use for songplays table
    print("Reading song data files...")
    song_df = spark.read.parquet(output_data + 'songs_table/')

    # create a temporary view against which SQL queries can be run
    song_df.createOrReplaceTempView('song_table')
    
    # extract columns from joined song and log datasets to create songplays table 
    print("Extracting columns to create songplays table...")
    songplays_table = df.join(song_df, (df.song == song_df.title) & (df.artist == song_df.artist_name) \
                              & (df.length == song_df.duration), 'left_outer').select(
                                 df.timestamp,
                                 col("userId").alias('user_id'),
                                 df.level,
                                 song_df.song_id,
                                 song_df.artist_id,
                                 col("sessionId").alias("session_id"),
                                 df.location,
                                 col("useragent").alias("user_agent"),
                                 year('datetime').alias('year'),
                                 month('datetime').alias('month')) 
    
    # write songplays table to parquet files partitioned by year and month
    print("Writing songplays table to parquet files...")
    songplays_table.write.parquet(os.path.join(output_data, 'songplays_table/'),\
                                  mode='overwrite', partitionBy=['year', 'month'])
                             

def main():
    """
    - Creates Spark session
    - Loads, transforms, and extracts records into song and artist tables
    - Loads, transforms, and extracts records into users, time and songplays tables
    """
    spark = create_spark_session()
    #input_data = "data/"        # running on local dataset
    #output_data = "output/"     # running on local dataset
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://my-emr-cluster/"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
