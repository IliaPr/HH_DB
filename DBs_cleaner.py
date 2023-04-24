import psycopg2
class DB_agregator():
    conn = psycopg2.connect(host = 'localhost', database = 'HH_jobs', user = 'postgres', password = '150774')
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute('DELETE FROM vacancies')
                cur.execute('DELETE FROM companies')

    finally:
        conn.close()