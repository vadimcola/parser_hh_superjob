import json
from abc import ABC, abstractmethod
from operator import itemgetter

class Vacancy(ABC):
    @abstractmethod
    def vacances(self):
        pass


class VacancyHH(Vacancy):

    def vacances(self):
        with open('hhData.json', 'r', encoding='utf-8') as file:
            self.vacancy = json.load(file)
            #self.vacancy_hh = sorted(self.vacancy, key=lambda data: (data["salary"]["to"] is None, data["salary"]["to"]), reverse = True)
            self.vacancy_hh
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
                      f'ID {vacancy["id"]}\n'
                      f'{("="*200)}')


class VacancySJ(Vacancy):

    def vacances(self):
        pass


vac = VacancyHH()
print(vac.vacances())

