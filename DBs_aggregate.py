import psycopg2
from getting_HH_vacancies import HH
class DB_agregator(HH):
    input('Привет, эта прорамма анализирует вакансии от 10 работодателей, нажмите enter для запуска')
    print('поиск...')
    '''Заполнение таблиц БД данными'''
    conn = psycopg2.connect(host = 'localhost', database = 'HH_jobs', user = 'postgres', password = '150774')
    try:
        with conn:
            with conn.cursor() as cur:
                employers_list = ['ITConstruct', 'Первый Бит', 'WONE IT', 'ЭЛТЕКС СОЛЮШЕНС',
                                  'Элементарные программные решения',
                                  'СДЭК', 'Softline', 'Сбер. IT', 'БКС IT & Digital', 'S7 IT']
                i = HH()
                list_id = i.get_request_employer_id()
                url = i.get_request_employer_url(list_id)
                vacancies = i.get_request_vacancy(url)
                companies = dict(zip(employers_list, list_id))
                for name, company_id in companies.items():
                    cur.execute('INSERT INTO companies VALUES (%s, %s)', (name, company_id))
                for info in vacancies:
                    cur.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)', (info['Company_id'], info['Vacancy_Name'], info['Salary'],
                                                                                          info['Link'], info['Requirement']))

    finally:
        conn.close()