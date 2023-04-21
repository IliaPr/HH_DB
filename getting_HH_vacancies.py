from abc import ABC, abstractmethod
import requests


class Engine(ABC):
    word = 'IT'

    @abstractmethod
    def get_request_employer(self):
        pass

    @abstractmethod
    def get_request_vacancy(self, employers_list):
        pass


class HH(Engine):

    def get_request_employer(self):
        """
        Парсим компании с ресурса HeadHunter
        """
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
        return employers_list

    def get_request_vacancy(self, employers_list):
        """
        Парсим данные по комнанияс с ресурса HeadHunter
        """
        jobs = []
        for word in employers_list:
            job = {}
            url = 'https://api.hh.ru/vacancies?text=' + word
            job['Company_name'] = word
            for item in range(1):
                request = requests.get(url, params={"keywords": word, 'page': item}).json()['items']
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
                    jobs.append(job)
        return jobs
