from src.json_save import JSONSaverSJ, JSONSaverHH
from src.vacancy import VacancyHH, VacancySJ


def main():
    while True:
        web_platform = input(f"Выберите платформу для загрузки данных\n"
                             f"Введите 'SJ', для загрузки из SuperJob\n"
                             f"Введите 'HH', для загрузки из HeadHunter\n"
                             f"Сделайте ввод ...")
        if web_platform.upper() == 'HH':
            vac = JSONSaverHH()
        elif web_platform.upper() == 'SJ':
            vac = JSONSaverSJ()
        else:
            print("Ошибка ввода!!!")
            continue
        profession = input("Введите название профессии ... ")
        vac.add_vacancy(profession)

        if web_platform.upper() == 'HH':
            print_vac = VacancyHH()
        elif web_platform.upper() == 'SJ':
            print_vac = VacancySJ()
        print_vac.vacances()
        while True:
            answer = input(f"Теперь вам доступны следующие команды для отображения полученной информации:\n"
                           f"1: Получить расширенную информацию о вакансии по ID\n"
                           f"2: Показать топ 10 вакансий по заработной плате\n"
                           f"3: Возврат к выбору платформы\n"
                           f"4: Выход из программы\n"
                           f"   Введите цифру команды ...")
            if answer not in ('1', '2', '3', '4'):
                print("!!!! Ошибка ввода !!!!")
                continue
            elif answer == '1':
                id_vac = input("Введите ID вакансии ...")
                print_vac.vacances_id(id_vac)
            elif answer == '2':
                print_vac.vacances_top()
            elif answer == "3":
                break
            else:
                exit("Спасибо !!!!")

if __name__ == "__main__":
    main()
