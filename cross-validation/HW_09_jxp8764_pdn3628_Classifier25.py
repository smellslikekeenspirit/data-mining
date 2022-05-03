class Classifier25:
	def classifier(record):
		answer = 0

		# Decision Stump Number 1
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 2
		if record['HairLn'] <= 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 3
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 4
		if record['Reach'] <= 140:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 5
		if record['Ht'] > 176:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 6
		if record['TailLn'] <= 22:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 7
		if record['Ht'] <= 111:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 8
		if record['Ht'] > 227:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 9
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 10
		if record['Ht'] > 176:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 11
		if record['TailLn'] > 14:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 12
		if record['Age'] > 74:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 13
		if record['TailLn'] <= 23:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 14
		if record['Age'] > 34:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 15
		if record['HairLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 16
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 17
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 18
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 19
		if record['TailLn'] > 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 20
		if record['Reach'] > 156:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 21
		if record['Reach'] <= 143:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 22
		if record['Ht'] <= 92:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 23
		if record['Ht'] > 225:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 24
		if record['Reach'] > 156:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 25
		if record['Age'] > 71:
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
