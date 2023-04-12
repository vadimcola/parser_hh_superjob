import json
from abc import ABC, abstractmethod


class Vacancy(ABC):
    @abstractmethod
    def vacances(self):
        pass


class VacancyHH(Vacancy):

    def vacances(self):
        with open('hhData.json', 'r') as file:
            self.vacancy_hh = json.load(file)
            for vacancy in self.vacancy_hh:
                if vacancy["salary"]["currency"] != "RUR":
                    continue
                if vacancy["salary"]["from"] is None:
                    vacancy["salary"]["from"] = "<не указано>"
                else:
                    vacancy["salary"]["from"] = vacancy["salary"]["from"]
                if vacancy["salary"]["to"] is None:
                    vacancy["salary"]["to"] = "<не указано>"
                else:
                    vacancy["salary"]["to"] = vacancy["salary"]["to"]
                print(f'{vacancy["employer"]["name"]} ---- {vacancy["name"]} \n'
                      f'Оплата от {vacancy["salary"]["from"]} до {vacancy["salary"]["to"]} '
                      f'{vacancy["salary"]["currency"]} \n'
                      f'Ссылка {vacancy["alternate_url"]} \n'
                      f'\n'
                      f'{("="*200)}')


class VacancySJ(Vacancy):

    def vacances(self):
        pass


vac = VacancyHH()
print(vac.vacances())
