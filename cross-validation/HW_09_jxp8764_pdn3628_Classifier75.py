class Classifier75:
	def classifier(record):
		answer = 0

		# Decision Stump Number 1
		if record['Reach'] <= 100:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 2
		if record['Reach'] <= 109:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 3
		if record['Reach'] > 224:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 4
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 5
		if record['Reach'] > 155:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 6
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 7
		if record['Ht'] <= 119:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 8
		if record['HairLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 9
		if record['Reach'] <= 134:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 10
		if record['Reach'] <= 125:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 11
		if record['TailLn'] > -4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 12
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 13
		if record['HairLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 14
		if record['HairLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 15
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 16
		if record['Age'] > 73:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 17
		if record['Age'] > 41:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 18
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 19
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 20
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 21
		if record['Reach'] > 167:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 22
		if record['Age'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 23
		if record['Age'] > 34:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 24
		if record['Reach'] <= 105:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 25
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 26
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 27
		if record['TailLn'] > 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 28
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 29
		if record['Reach'] > 202:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 30
		if record['Reach'] > 238:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 31
		if record['TailLn'] <= 24:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 32
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 33
		if record['Ht'] <= 131:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 34
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 35
		if record['Reach'] <= 101:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 36
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 37
		if record['TailLn'] > 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 38
		if record['Age'] > 70:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 39
		if record['Reach'] > 228:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 40
		if record['Ht'] > 172:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 41
		if record['TailLn'] <= 27:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 42
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 43
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 44
		if record['Reach'] > 161:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 45
		if record['Reach'] > 161:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 46
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 47
		if record['TailLn'] <= 29:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 48
		if record['Reach'] <= 149:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 49
		if record['HairLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 50
		if record['Age'] > 21:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 51
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 52
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 53
		if record['Age'] > 63:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 54
		if record['HairLn'] <= 14:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 55
		if record['TailLn'] <= 21:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 56
		if record['Ht'] > 211:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 57
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 58
		if record['TailLn'] > 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 59
		if record['HairLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 60
		if record['HairLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 61
		if record['HairLn'] <= 12:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 62
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 63
		if record['TailLn'] <= 26:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 64
		if record['Ht'] > 145:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 65
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 66
		if record['Ht'] <= 94:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 67
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 68
		if record['TailLn'] > -7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 69
		if record['HairLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 70
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 71
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 72
		if record['Age'] > 47:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 73
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 74
		if record['Reach'] <= 139:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 75
		if record['Ht'] > 186:
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
