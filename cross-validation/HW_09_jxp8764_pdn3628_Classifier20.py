class Classifier20:
	def classifier(record):
		answer = 0

		# Decision Stump Number 1
		if record['Age'] > 33:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 2
		if record['Age'] > 46:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 3
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 4
		if record['Ht'] > 165:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 5
		if record['BangLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 6
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 7
		if record['Reach'] <= 93:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 8
		if record['Ht'] <= 111:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 9
		if record['Reach'] > 188:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 10
		if record['Ht'] > 154:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 11
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 12
		if record['Reach'] > 167:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 13
		if record['Ht'] > 153:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 14
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 15
		if record['Age'] > 37:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 16
		if record['HairLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 17
		if record['Ht'] > 155:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 18
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 19
		if record['TailLn'] > 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 20
		if record['Reach'] > 226:
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
		print(Classifier20.classifier(record))
