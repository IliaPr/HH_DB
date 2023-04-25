import psycopg2


class DBManager:
    def connection(self):
        '''Подклюение к БД'''
        self.conn = psycopg2.connect(host='localhost', database='HH_jobs', user='postgres', password='150774')
        return self.conn

    def get_companies_and_vacancies_count(self):
        '''Получение названий компаний с количестовм вакансий'''
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('SELECT companies.company_name, COUNT(*) FROM vacancies INNER JOIN companies USING(company_id) GROUP BY company_name')
                    data = cur.fetchall()
                    return data
        finally:
            self.conn.close()

    def get_all_vacancies(self):
        '''Получение информации по вакансиям с названиями компаний'''
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('SELECT companies.company_name, vacancy_name, salary, v_link, requirement FROM vacancies INNER JOIN companies USING(company_id)')
                    data = cur.fetchall()
                    return data
        finally:
            self.conn.close()

    def get_avg_salary(self):
        '''Получение средней зарплаты'''
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('SELECT vacancy_name, CEILING(AVG(salary)) FROM vacancies GROUP BY vacancy_name')
                    data = cur.fetchall()
                    return data

        finally:
            self.conn.close()

    def get_vacancies_with_higher_salary(self):
        '''Получение вакансий с зарплатой выше средней'''
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('SELECT vacancy_name, salary, v_link FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies WHERE salary <>0)')
                    data = cur.fetchall()
                    return data

        finally:
            self.conn.close()

    def get_vacancies_with_keyword(self, keyword):
        '''Получение списка вакансий, содержащих ключевое слово в названии'''
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute(f"SELECT vacancy_name, salary, v_link FROM vacancies WHERE vacancy_name LIKE '%{keyword}%'")
                    data = cur.fetchall()
                    return data
        finally:
            self.conn.close()