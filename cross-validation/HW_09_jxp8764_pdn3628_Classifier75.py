class Classifier75:
	def classifier(record):
		answer = 0

		# Decision Stump Number 1
		if record['Reach'] <= 122:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 2
		if record['HairLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 3
		if record['Ht'] <= 93:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 4
		if record['Ht'] <= 128:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 5
		if record['HairLn'] <= 13:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 6
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 7
		if record['TailLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 8
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 9
		if record['TailLn'] > 13:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 10
		if record['Ht'] <= 140:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 11
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 12
		if record['Age'] > 44:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 13
		if record['Age'] > 30:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 14
		if record['Reach'] <= 116:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 15
		if record['Age'] > 25:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 16
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 17
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 18
		if record['TailLn'] > -7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 19
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 20
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 21
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 22
		if record['Age'] > 73:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 23
		if record['Ht'] > 167:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 24
		if record['Reach'] <= 103:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 25
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 26
		if record['Ht'] <= 133:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 27
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 28
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 29
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 30
		if record['HairLn'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 31
		if record['HairLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 32
		if record['Age'] > 32:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 33
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 34
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 35
		if record['TailLn'] > -9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 36
		if record['Age'] <= 12:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 37
		if record['TailLn'] > -8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 38
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 39
		if record['HairLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 40
		if record['HairLn'] <= 13:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 41
		if record['TailLn'] <= 23:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 42
		if record['Reach'] > 178:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 43
		if record['Reach'] <= 134:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 44
		if record['Ht'] > 208:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 45
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 46
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 47
		if record['HairLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 48
		if record['HairLn'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 49
		if record['Ht'] > 224:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 50
		if record['HairLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 51
		if record['Reach'] > 158:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 52
		if record['Ht'] > 156:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 53
		if record['Ht'] > 204:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 54
		if record['Ht'] <= 112:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 55
		if record['Age'] > 65:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 56
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 57
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 58
		if record['TailLn'] <= 24:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 59
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 60
		if record['TailLn'] <= 26:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 61
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 62
		if record['Age'] > 18:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 63
		if record['Ht'] <= 118:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 64
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 65
		if record['TailLn'] > 18:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 66
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 67
		if record['TailLn'] <= 22:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 68
		if record['Age'] > 44:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 69
		if record['Age'] > 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 70
		if record['Age'] <= 12:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 71
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 72
		if record['TailLn'] > -2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 73
		if record['TailLn'] > -9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 74
		if record['Age'] > 35:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 75
		if record['Age'] > 69:
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
		print(Classifier75.classifier(record))
