from abc import ABC, abstractmethod
import requests
import time

class Engine(ABC):
    word = input()

    @abstractmethod
    def get_request_employer_name(self):
        pass
    @abstractmethod
    def get_request_employer_id(self, employers_list):
        pass

    @abstractmethod
    def get_request_employer_url(self, employers_list):
        pass
    @abstractmethod
    def get_request_vacancy(self, employers_list):
        pass


class HH(Engine):

    def get_request_employer_name(self):
        '''Получение списка работодателей'''
        url = 'https://api.hh.ru/vacancies?text=' + self.word
        employers_list = []
        for item in range(10):
            request_hh = requests.get(url, params={"keywords": self.word, 'page': item}).json()['items']
            for item2 in request_hh:
                if len(employers_list) == 10:
                    break
                if item2 in employers_list:
                    continue
                employers_list.append(item2['employer']['name'])
                time.sleep(0.2)
        return employers_list

    def get_request_employer_id(self, employers_list):
        '''Полуение списка id работодателей'''
        list_id = []
        for i in employers_list:
            response = requests.get(f"https://api.hh.ru/employers?text={i}").json()['items']
            company_id = response[0]['id']
            list_id.append(company_id)
            time.sleep(0.2)
        return list_id
    def get_request_employer_url(self, list_id):
        '''Полуение списка id работодателей'''
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
                        job['Salary'] = {'from': 0, 'to': 0}
                    elif i['salary']['from'] == None:
                        if i['salary']['currency'] == 'RUR':
                            job['Salary'] = {'from': 0, 'to': i['salary']['to']}
                    elif i['salary']['to'] == None:
                        if i['salary']['currency'] == 'RUR':
                            job['Salary'] = {'from': i['salary']['from'], 'to': 0}
                    else:
                        if i['salary']['currency'] == 'RUR':
                            job['Salary'] = {'from': i['salary']['from'],
                                             'to': i['salary']['to']}
                    job["Link"] = i['alternate_url']
                    job['Requirement'] = i['snippet']['requirement']
                    job['Company_name'] = i['employer']['name']
                    job['Company_id'] = i['employer']['id']
                    jobs.append(job)
                    time.sleep(0.2)
        return jobs

if __name__ == '__main__':
    i = HH()
    employers_list = i.get_request_employer_name()
    print(employers_list)
    list_id = i.get_request_employer_id(employers_list)
    print(list_id)
    url = i.get_request_employer_url(list_id)
    print(url)
    vacants = i.get_request_vacancy(url)
    print(vacants)