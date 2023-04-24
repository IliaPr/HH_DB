import psycopg2
from getting_HH_vacancies import HH
class DB_agregator(HH):
    conn = psycopg2.connect(host = 'localhost', database = 'HH_jobs', user = 'postgres', password = '150774')
    try:
        with conn:
            with conn.cursor() as cur:
                i = HH()
                employers_list = i.get_request_employer_name()
                id = i.get_request_employer_id(employers_list)
                employers_links = i.get_request_employer_url(id)
                vacancies = i.get_request_vacancy(employers_links)
                companies = dict(zip(employers_list, id))
                for name, company_id in companies.items():
                    cur.execute('INSERT INTO companies VALUES (%s, %s)', (name, company_id))
                for info in vacancies:
                    cur.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)', (info['Company_id'], info['Vacancy_Name'], info['Salary'],
                                                                                          info['Link'], info['Requirement']))


    finally:
        conn.close()