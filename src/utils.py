def sort_salary_hh(vacancy):
    '''
    метод сортировки списка вакансий по максимальной зарплате
    '''
    return sorted(vacancy, key=lambda data: (data["salary"]["to"] is None, data["salary"]["to"]),
                  reverse=True)


def sort_salary_sj(vacancy):
    '''
    метод сортировки списка вакансий по максимальной зарплате
    '''
    return sorted(vacancy, key=lambda data: (data['payment_to'] == 0, data['payment_to']),
                  reverse=True)
