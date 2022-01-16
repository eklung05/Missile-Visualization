import csv

header = ['Month', 'var1', 'var2']
data = [
	['Jan', 0, 1],
	['Feb', 0, 11],
	['Mar', 0, 20],
	['Apr', 4, 13],
	['May', 6, 13],
	['Jun', 2, 6],
	['Jul', 15, 13],
	['Aug', 1, 10],
	['Sep', 3, 10],
	['Oct', 0, 5],
	['Nov', 0, 3],
	['Dec', 0, 2]
]

with open('KimLaunch.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(header)
	writer.writerows(data)