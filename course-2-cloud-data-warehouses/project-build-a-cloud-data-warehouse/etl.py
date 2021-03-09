import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    - Opens log file and extracts data, converting time to timestamp format
    - Copies data into 'staging_events' table
    - Opens song file and extracts data
    - Copies data into 'staging_songs' table
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    - Specifies fields to be loaded with data from 'staging_events' and 'staging_songs' tables
    - Filters out records from 'staging_events' table by NextSong to eliminate invalid song plays
    - Inserts records into fact and dimension tables
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Reads configuration file
    - Establishes connection with the Sparkify Redshift database
    - Gets cursor to the Sparkify Redshift database
    - Loads records into staging tables
    - Loads records into fact and dimension tables 
    - Closes the connection 
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()