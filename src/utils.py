def sort_salary_hh(vacancy):
    return sorted(vacancy, key=lambda data: (data["salary"]["to"] is None, data["salary"]["to"]),
                  reverse=True)
