import psycopg2
class DB_agregator:
    def connection(self):
        '''Подклюение к БД'''
        self.conn = psycopg2.connect(host='localhost', database='HH_jobs', user='postgres', password='150774')
        return self.conn
    def filling_table_data(self, list_id, employers_list, vacancies):
        '''Заполнение таблиц БД данными'''
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    companies = dict(zip(employers_list, list_id))
                    for name, company_id in companies.items():
                        cur.execute('INSERT INTO companies VALUES (%s, %s)', (name, company_id))
                    for info in vacancies:
                        cur.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)', (info['Company_id'], info['Vacancy_Name'], info['Salary'],
                                                                                          info['Link'], info['Requirement']))

        finally:
            self.conn.close()