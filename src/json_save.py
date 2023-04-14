from abc import ABC, abstractmethod

from src.uploading import HeadHunterAPI, SuperJobAPI
import json


class JSONSaver(ABC):
    @abstractmethod
    def add_vacancy(self):
        pass


class JSONSaverHH(JSONSaver):
    def __init__(self):
        self.test = None
        self.discharge = None

    def add_vacancy(self, word):
        self.discharge = HeadHunterAPI()
        self.test = self.discharge.uploading(word)
        with open('hhData.json', 'w', encoding='utf-8') as file:
            json.dump(self.test, file, indent=4, ensure_ascii=False)
            print("Данные выгружены")


class JSONSaverSJ(JSONSaver):
    def __init__(self):
        self.test = None
        self.discharge = None

    def add_vacancy(self, word):
        self.discharge = SuperJobAPI()
        self.test = self.discharge.uploading(word)
        with open('sjData.json', 'w', encoding='utf-8') as file:
            json.dump(self.test, file, indent=4, ensure_ascii=False)
            print("Данные выгружены")


