import json
from abc import ABC, abstractmethod


from src.utils import sort_salary_hh, sort_salary_sj


class Vacancy(ABC):
    '''
    абстрактный класс, который обязывает реализовать метод трибутов вакансий
    '''

    @abstractmethod
    def vacances(self):
        '''
        метод выводит список выгруженных вакансий в отсортированном виде от большого к меньшему
        '''
        pass

    @abstractmethod
    def vacances_top(self):
        '''
        метод выводит ТОП-10 вакансий по максимальной зарплате
        '''
        pass

    @abstractmethod
    def vacances_id(self):
        """
        метод выводит по id данные по вакансии
        """
        pass


class VacancyHH(Vacancy):
    '''
    В классе определены следующие атрибуты ваканий Название компании, Название должности,
    Зарплата ОТ и ДО, а так же ссылка на вакансию также класс выводит вокансии
    в отсортированном виде от меньшего к большему
    '''

    def __init__(self):
        self.sorted_list = None
        self.vacancy_hh = None
        self.vacancy = None

    def vacances(self):
        with open('hhData.json', 'r', encoding='utf-8') as file:
            self.vacancy = json.load(file)
            self.vacancy_hh = sort_salary_hh(self.vacancy)
            for vac in self.vacancy_hh:
                if vac["salary"]["currency"] != "RUR":
                    continue
                if vac["salary"]["from"] is None:
                    vac["salary"]["from"] = "<не указано>"
                else:
                    vac["salary"]["from"] = vac["salary"]["from"]
                if vac["salary"]["to"] is None:
                    vac["salary"]["to"] = "<не указано>"
                else:
                    vac["salary"]["to"] = vac["salary"]["to"]
                print(f'{vac["employer"]["name"]} ---- {vac["name"]} \n'
                      f'Оплата от {vac["salary"]["from"]} до {vac["salary"]["to"]} '
                      f'{vac["salary"]["currency"]} \n'
                      f'Ссылка {vac["alternate_url"]} \n'
                      f'ID {vac["id"]}\n {("=" * 200)}')

    def vacances_top(self):
        vac_list = []
        with open('hhData.json', 'r', encoding='utf-8') as file:
            self.vacancy = json.load(file)
            for i in self.vacancy:
                if i["salary"]["to"] is None:
                    continue
                if i["salary"]["currency"] != "RUR":
                    continue
                vac_list.append(i)
        self.sorted_list = sorted(vac_list, key=lambda data: (data["salary"]["to"]),
                                  reverse=True)[:10]
        for vac in self.sorted_list:
            print(f'{vac["employer"]["name"]} ---- {vac["name"]} \n'
                  f'Оплата от {vac["salary"]["from"]} до {vac["salary"]["to"]} '
                  f'{vac["salary"]["currency"]} \n'
                  f'Ссылка {vac["alternate_url"]} \n'
                  f'ID {vac["id"]}\n {("~" * 200)}')

    def vacances_id(self, id_vac):
        with open('hhData.json', 'r', encoding='utf-8') as file:
            self.vacancy = json.load(file)
            for vac in self.vacancy:
                if vac["id"] == str(id_vac):
                    if vac["salary"]["from"] is None:
                        vac["salary"]["from"] = "<не указано>"
                    else:
                        vac["salary"]["from"] = vac["salary"]["from"]
                    if vac["salary"]["to"] is None:
                        vac["salary"]["to"] = "<не указано>"
                    else:
                        vac["salary"]["to"] = vac["salary"]["to"]
                    print(f'{("*" * 200)}\n'
                          f'{vac["employer"]["name"]} ---- {vac["name"]} \n'                   
                          f'Оплата от {vac["salary"]["from"]} до {vac["salary"]["to"]} '
                          f'{vac["salary"]["currency"]} \n'
                          f'Требования: {vac["snippet"]["requirement"]}\n'
                          f'            {vac["snippet"]["responsibility"]}\n'
                          f'Ссылка {vac["alternate_url"]}\n{("*" * 200)}')


class VacancySJ(Vacancy):
    '''
        В классе определены следующие атрибуты ваканий Название компании, Название должности,
        Зарплата ОТ и ДО, а так же ссылка на вакансию также класс выводит вокансии
        в отсортированном виде от меньшего к большему
        '''

    def __init__(self):
        self.sorted_list = None
        self.vacancy_sj = None
        self.vacancy = None

    def vacances(self):
        with open('sjData.json', 'r', encoding='utf-8') as file:
            self.vacancy = json.load(file)
            self.vacancy_sj = sort_salary_sj(self.vacancy)
            for vac in self.vacancy_sj:
                if vac['payment_from'] == 0:
                    vac['payment_from'] = '<не указано>'
                if vac['payment_to'] == 0:
                    vac['payment_to'] = '<не указано>'
                print(f"{vac['firm_name']} ---- {vac['profession']}\n"
                      f"Оплата от {vac['payment_from']} до {vac['payment_to']} {vac['currency']}\n"
                      f"Ссылка {vac['link']}\n"
                      f"ID {vac['id']}\n{('=' * 200)}")

    def vacances_top(self):
        vac_list = []
        with open('sjData.json', 'r', encoding='utf-8') as file:
            self.vacancy = json.load(file)
            for i in self.vacancy:
                if i['payment_to'] == 0:
                    continue
                vac_list.append(i)
        self.sorted_list = sorted(vac_list, key=lambda data: (data['payment_to']),
                                  reverse=True)[:10]
        for vac in self.sorted_list:
            print(f"{vac['firm_name']} ---- {vac['profession']}\n"
                  f"Оплата от {vac['payment_from']} до {vac['payment_to']} {vac['currency']}\n"
                  f"Ссылка {vac['link']}\n"
                  f"ID {vac['id']}\n{('~' * 200)}")

    def vacances_id(self, id_vac):
        with open('sjData.json', 'r', encoding='utf-8') as file:
            self.vacancy = json.load(file)
            for vac in self.vacancy:
                if vac["id"] == int(id_vac):
                    if vac['payment_from'] == 0:
                        vac['payment_from'] = '<не указано>'
                    if vac['payment_to'] == 0:
                        vac['payment_to'] = '<не указано>'
                    print(f"{('*' * 200)}\n"
                          f"{vac['firm_name']} ---- {vac['profession']}\n"
                          f"Оплата от {vac['payment_from']} до {vac['payment_to']} {vac['currency']}\n"
                          f"Требования: {vac['candidat']}\n"
                          f"Ссылка {vac['link']}\n{('*' * 200)}")





