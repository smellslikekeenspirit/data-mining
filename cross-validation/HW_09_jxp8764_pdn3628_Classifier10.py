def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['Ht'] > 230:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record['TailLn'] > -5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record['Age'] > 31:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record['TailLn'] <= 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 5
	if record['TailLn'] > 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 6
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 7
	if record['Age'] > 29:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 8
	if record['Reach'] <= 121:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 9
	if record['Reach'] > 196:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 10
	if record['Reach'] > 225:
		answer = answer - 1
	else:
		answer = answer + 1

	if answer < 0:
		return -1
	else:
		return 1


if __name__ == '__main__':
	data = []

	# reads in the unlabeled data from the csv
	with open('Abominable_VALIDATION_Data_FOR_STUDENTS_v770_2215.csv', 'r') as file:
		file.readline()
		for line in file:
			row = line.strip().split(",")
			for index in range(len(row)):
				val = float(row[index])
				if index == 1:
					val = int(round(val / 4.0) * 4)
				elif index == 6:
					val = int(round(val / 2.0, 1) * 4)
				else:
					val = int(round(val / 2.0) * 2)
				data.append(val)

	for record in data:
		print(classifier(record))
