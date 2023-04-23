import psycopg2
from getting_HH_vacancies import HH
class DB_agregator(HH):
    conn = psycopg2.connect(host = 'localhost', database = 'HH_jobs', user = 'postgres', password = '150774')
    try:
        with conn:
            with conn.cursor() as cur:
                hh = HH()
                employers_list = hh.get_request_employer()
                list_vacancies = hh.get_request_vacancy(employers_list)
                for job in list_vacancies:
                    cur.execute('INSERT INTO companies DISTINCT VALUES (%s, %s)', (job['Company_id'], job['Company_name'],))


    finally:
        conn.close()