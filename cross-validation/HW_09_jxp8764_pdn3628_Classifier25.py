def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['Reach'] > 219:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record['TailLn'] <= 24:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record['TailLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 5
	if record['Ht'] <= 138:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 6
	if record['TailLn'] <= 29:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 7
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 8
	if record['HairLn'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 9
	if record['Age'] > 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 10
	if record['TailLn'] > -4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 11
	if record['Reach'] <= 127:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 12
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 13
	if record['HairLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 14
	if record['Age'] > 69:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 15
	if record['Age'] > 25:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 16
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 17
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 18
	if record['Reach'] <= 139:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 19
	if record['Ht'] <= 132:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 20
	if record['Ht'] <= 131:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 21
	if record['Age'] > 72:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 22
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 23
	if record['TailLn'] <= 25:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 24
	if record['Reach'] <= 93:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 25
	if record['HairLn'] <= 16:
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