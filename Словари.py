словарь = {"city": "Москва", "temperature": "20"}
print(словарь['city'])
словарь['temperature'] = '15'
print(словарь)
print(словарь.get('country'))
словарь.get('country', 'Россия')
print(словарь.get('country', 'Россия'))
словарь['date'] = '27.05.2019'
print(словарь)
print(len(словарь))