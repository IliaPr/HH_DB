import psycopg2
class DB_agregator:
    '''Заполнение таблиц БД данными'''
    def filling_table_data(self, list_id, employers_list, vacancies):
        conn = psycopg2.connect(host = 'localhost', database = 'HH_jobs', user = 'postgres', password = '150774')
        try:
            with conn:
                with conn.cursor() as cur:
                    companies = dict(zip(employers_list, list_id))
                    for name, company_id in companies.items():
                        cur.execute('INSERT INTO companies VALUES (%s, %s)', (name, company_id))
                    for info in vacancies:
                        cur.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)', (info['Company_id'], info['Vacancy_Name'], info['Salary'],
                                                                                          info['Link'], info['Requirement']))

        finally:
            conn.close()