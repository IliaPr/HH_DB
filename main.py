from DBs_cleaner import DB_cleaner
from DBs_manager import DBManager
from DBs_aggregate import DB_agregator

'''Основна логика программы'''
program_start = DB_agregator()
print('Вакансии записаны в базу данных!')
print('Для продолжения работы введите номер одной из следующих команд:\n '
      '1. Вывести список всех компаний и количество вакансий у каждой компании.\n'
      '2. Вывести список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.\n'
      '3. Вывести среднюю зарплату по вакансиям.\n'
      '4. Вывести список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n'
      '5. Вывести список всех вакансий, в названии которых содержатся переданные в метод слова\n'
      'Введите "s" для выхода из программы')
user_choose = input('Команда: ')
while user_choose != 's':
      if user_choose == '1':
            data = DBManager()
            conn = data.connection()
            result = data.get_companies_and_vacancies_count()
            for i in result:
                  print(i)
            user_choose = input('Команда: ')
      elif user_choose == '2':
            data = DBManager()
            conn = data.connection()
            result = data.get_all_vacancies()
            for i in result:
                  print(i)
            user_choose = input('Команда: ')
      elif user_choose == '3':
            data = DBManager()
            conn = data.connection()
            result = data.get_avg_salary()
            for i in result:
                  print(i)
            user_choose = input('Команда: ')
      elif user_choose == '4':
            data = DBManager()
            conn = data.connection()
            result = data.get_vacancies_with_higher_salary()
            for i in result:
                  print(i)
            user_choose = input('Команда: ')
      elif user_choose == '5':
            keyword = str(input('Введите ключевое слово '))
            data = DBManager()
            conn = data.connection()
            result = data.get_vacancies_with_keyword(keyword)
            for i in result:
                  print(i)
            user_choose = input('Команда: ')

if user_choose == 's':
      clean = DB_cleaner()
      print('Программа завершила работу!')



