import time
import requests
class HH:
    def get_request_employer_id(self, companies_list):
        '''Полуение списка id работодателей'''
        list_id = []
        for i in companies_list:
            response = requests.get(f"https://api.hh.ru/employers?text={i}").json()['items']
            company_id = response[0]['id']
            list_id.append(company_id)
            time.sleep(0.2)
        return list_id
    def get_request_employer_url(self, list_id):
        '''Полуение списка url работодателей'''
        vacancies_link_list = []
        for i in list_id:
            id_response = requests.get(f"https://api.hh.ru/employers/{i}").json()
            vacancies_url = id_response['vacancies_url']
            vacancies_link_list.append(vacancies_url)
            time.sleep(0.2)
        return vacancies_link_list

    def get_request_vacancy(self, vacancies_link_list):
        '''Получение списка вакансий с данными'''
        jobs = []
        for word in vacancies_link_list:
            job = {}
            url = word
            for item in range(1):
                request = requests.get(url, params={'page': item}).json()['items']
                for i in request:
                        job["Vacancy_Name"] = i['name']
                        if i['salary'] == None:
                            job['Salary'] = 0
                        elif i['salary']['from'] == None:
                                job['Salary'] = i['salary']['to']
                        elif i['salary']['to'] == None:
                                job['Salary'] = i['salary']['from']
                        else:
                                job['Salary'] = i['salary']['from']
                        job["Link"] = i['alternate_url']
                        job['Requirement'] = i['snippet']['requirement']
                        job['Company_name'] = i['employer']['name']
                        job['Company_id'] = i['employer']['id']
                        jobs.append(job)
                        time.sleep(0.2)
        return jobs
