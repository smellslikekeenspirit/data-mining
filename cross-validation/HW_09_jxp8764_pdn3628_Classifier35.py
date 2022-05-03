def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['HairLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record['TailLn'] > -4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record['Age'] > 62:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record['Age'] > 38:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 5
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 6
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 7
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 8
	if record['HairLn'] <= 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 9
	if record['Age'] > 42:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 10
	if record['TailLn'] > 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 11
	if record['TailLn'] > 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 12
	if record['Age'] > 67:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 13
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 14
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 15
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 16
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 17
	if record['Age'] > 21:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 18
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 19
	if record['TailLn'] <= 25:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 20
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 21
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 22
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 23
	if record['TailLn'] > 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 24
	if record['Age'] > 24:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 25
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 26
	if record['Age'] > 58:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 27
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 28
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 29
	if record['TailLn'] > -7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 30
	if record['TailLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 31
	if record['Age'] > 39:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 32
	if record['TailLn'] > 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 33
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 34
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 35
	if record['Reach'] > 207:
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