"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить
среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""

from collections import defaultdict

n_companies = int(input('По какому количеству компаний вы хотите вести данные? Введите целое число: '))

company_data = defaultdict(int)
for _ in range(n_companies):
    company_name = input('Введите название компании: ')
    print('Введите прибыль компании за каждый квартал прошлого года: ')
    for _ in range(4):
        company_data[company_name] += int(input())


avg_income = sum(company_data.values()) / len(company_data)
company_ratings = defaultdict(list)
for company in company_data:
    if company_data[company] > avg_income:
        company_ratings['above_avg'].append(company)
    elif company_data[company] < avg_income:
        company_ratings['below_avg'].append(company)
print(f'Компании с доходом выше среднего: {", ".join(company_ratings["above_avg"])}')
print(f'Компании с доходом ниже среднего: {", ".join(company_ratings["below_avg"])}')

