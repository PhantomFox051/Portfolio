import csv
data = [
['Name', 'Age', 'Money', 'lvl', 'hp'],
['Tunis', 16, 10000000000, 100, 345435654 ],
['Ivan', 17, -100000, 504, 646823298383264329]
]
with open('test.csv', 'w', encoding = 'utf-8', newline = '') as file:
	writer  = csv.writer(file)
	writer.writerows(data)

print('File created')

with open('test.csv', 'r', encoding = 'utf-8') as CSV:
	reder = csv.reader(CSV)
	header = next(reder)
	lst = list(reder)
	print(lst)
	max_age = 0
	max_money = 0
	max_lvl = 0
	sred_hp = 0
	for i in lst:
		if int(i[3]) > max_lvl:
			max_lvl = int(i[3])

		if int(i[1]) > max_age:
			max_age = int(i[1])

		if int(i[2]) > max_money:
			max_money = int(i[2])

	for i in lst:
		sred_hp += int(i[4])

	print(f'Самый внушительный возраст: {max_age}\nСамое большое состояние: {max_money}\nСамый большой уровень: {max_lvl}\n Среднее hp: {sred_hp / len(lst)}')
