class Classifier50:
	def classifier(record):
		answer = 0

		# Decision Stump Number 1
		if record['Ht'] > 218:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 2
		if record['Ht'] > 171:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 3
		if record['Reach'] <= 118:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 4
		if record['Reach'] > 193:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 5
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 6
		if record['Reach'] <= 98:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 7
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 8
		if record['Reach'] <= 129:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 9
		if record['Reach'] <= 119:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 10
		if record['Ht'] > 195:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 11
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 12
		if record['Ht'] > 159:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 13
		if record['Reach'] <= 135:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 14
		if record['Reach'] > 181:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 15
		if record['Ht'] <= 95:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 16
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 17
		if record['Age'] > 46:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 18
		if record['TailLn'] > 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 19
		if record['Ht'] > 203:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 20
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 21
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 22
		if record['TailLn'] <= 29:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 23
		if record['Ht'] > 194:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 24
		if record['HairLn'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 25
		if record['Ht'] > 214:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 26
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 27
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 28
		if record['TailLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 29
		if record['TailLn'] <= 28:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 30
		if record['Reach'] > 206:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 31
		if record['Age'] > 43:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 32
		if record['Ht'] > 197:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 33
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 34
		if record['Ht'] > 144:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 35
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 36
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 37
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 38
		if record['TailLn'] <= 28:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 39
		if record['Reach'] > 170:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 40
		if record['Age'] > 72:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 41
		if record['TailLn'] > 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 42
		if record['Ht'] > 222:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 43
		if record['Age'] > 27:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 44
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 45
		if record['Age'] > 64:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 46
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 47
		if record['Ht'] > 169:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 48
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 49
		if record['Ht'] <= 127:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 50
		if record['TailLn'] > 15:
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
