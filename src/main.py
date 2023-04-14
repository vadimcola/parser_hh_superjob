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
        profession = input("Введите название профессии ... ")
        vac.add_vacancy(profession)

        if web_platform.upper() == 'HH':
            print_vac = VacancyHH()
        elif web_platform.upper() == 'SJ':
            print_vac = VacancySJ()
        print_vac.vacances()
        print(f"{'~' * 200}\n{'~' * 200}")
        answer = input("Если хотите продолжить введите 'Y', если нет введите 'N' ...")
        if answer.upper() == 'Y':
            continue
        elif answer.upper() == 'N':
            print("Спасибо !!!")
            break


if __name__ == "__main__":
    main()
