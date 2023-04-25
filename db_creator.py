import psycopg2
'''Создание таблиц в БД'''
conn = psycopg2.connect(host='localhost', database='HH_jobs', user='postgres', password='150774')
try:
    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE companies (company_name text, company_id int PRIMARY KEY)")
            cur.execute('CREATE TABLE vacancies (company_id int REFERENCES companies(company_id), Vacancy_Name varchar, Salary int, v_Link text, Requirement text)')

finally:
    conn.close()
