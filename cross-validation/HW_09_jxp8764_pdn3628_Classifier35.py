def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record['HairLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record['TailLn'] <= 21:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 5
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 6
	if record['TailLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 7
	if record['Ht'] <= 134:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 8
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 9
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 10
	if record['Age'] > 32:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 11
	if record['TailLn'] <= 28:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 12
	if record['HairLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 13
	if record['Age'] > 73:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 14
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 15
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 16
	if record['Age'] > 21:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 17
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 18
	if record['HairLn'] <= 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 19
	if record['Ht'] <= 103:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 20
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 21
	if record['Age'] > 36:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 22
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 23
	if record['Reach'] > 162:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 24
	if record['Ht'] <= 141:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 25
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 26
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 27
	if record['Ht'] > 161:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 28
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 29
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 30
	if record['TailLn'] > 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 31
	if record['Reach'] <= 104:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 32
	if record['Age'] > 49:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 33
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 34
	if record['Age'] > 21:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 35
	if record['EarLobes'] <= 0:
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
