from src.uploading import HeadHunterAPI
import json


class JSONSaver:
    def __init__(self):
        self.test = None
        self.discharge = None

    def add_vacancy(self, word):
        self.discharge = HeadHunterAPI()
        self.test = self.discharge.uploading(word)
        with open('hhData.json', 'w', encoding='utf-8') as file:
            json.dump(self.test, file, indent=4, ensure_ascii=False)


vac = JSONSaver()
vac.add_vacancy("Python")
