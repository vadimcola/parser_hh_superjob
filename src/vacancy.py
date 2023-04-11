from abc import ABC, abstractmethod

from src.uploading import HeadHunterAPI


class Vacancy(ABC):
    @abstractmethod
    def vacances(self):
        pass


class VacancyHH(Vacancy):

    def __init__(self, *args):
        self.vacancy_hh = HeadHunterAPI().uploading(args)
        self.job_title = self.vacancy_hh[0]['name']
        self.salary_max = self.vacancy_hh[0]['salary']['to']
        self.salary_min = self.vacancy_hh[0]['salary']['from']
        self.employee_requirement = self.vacancy_hh[0]['snippet']['requirement']
        self.id_vacancy = self.vacancy_hh[0]['id']
        self.url_vacancy = f'https://hh.ru/vacancy/{self.id_vacancy}'

    def vacances(self, *args):
        return self.vacancy_hh


class VacancySJ(Vacancy):

    def vacances(self):
        pass


vc = VacancyHH()
print(vc.vacances("Водитель"))
