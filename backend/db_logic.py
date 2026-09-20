#Data already has been ingested, so we just need to write logic to query it

#Our function must import psycopg2 so our function's python code can read/write SQL data, but not pandas or plumberpdf since those two were only used to process the data

#We don't need to do 'from zip_to_state import map_zip_to_state' since we will get our state input when we import map_zip_to_state in server.py

import psycopg2
import os

def get_data(state):
  # conn = connection to PostgreSQL
    conn = psycopg2.connect(os.environ.get("DATABASE_URL"))

    cursor = conn.cursor() #what actually sends SQL commands

    cursor.execute("""
        SELECT year, type, AVG(premium)
        FROM premiums
        WHERE state = %s
        GROUP BY year, type
        ORDER BY year, type
    """, (state,))

    rows = cursor.fetchall()
    conn.close()
    return rows
