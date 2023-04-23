import psycopg2

conn = psycopg2.connect(host='localhost', database='HH_jobs', user='postgres', password='150774')
try:
    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE companies (company_id int PRIMARY KEY , company_name text)")
            cur.execute('CREATE TABLE vacancies (company_id int REFERENCES companies(company_id), Vacancy_Name varchar, Salary_from int, Salary_to int, Link text, Requirement text)')

finally:
    conn.close()
