def classifier(record):
	answer = 0
	# Decision Stump Number 1
	if record[4] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record[1] <= 137:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record[5] <= 129:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record[4] <= 8:
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
			for val in row:
				data.append(float(val))

	for record in data:
		print(classifier(record))
