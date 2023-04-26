import psycopg2
class DB_cleaner:
    def connection(self):
        '''Подклюение к БД'''
        self.conn = psycopg2.connect(host='localhost', database='HH_jobs', user='postgres', password='150774')
        return self.conn
    def cleaner(self):
        '''Удаление данных из таблиц'''
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('DELETE FROM vacancies')
                    cur.execute('DELETE FROM companies')

        finally:
            self.conn.close()
