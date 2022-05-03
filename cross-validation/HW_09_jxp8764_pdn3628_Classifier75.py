def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['TailLn'] > 18:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record['TailLn'] > -2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record['TailLn'] > -4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 5
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 6
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 7
	if record['Ht'] <= 125:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 8
	if record['Ht'] <= 118:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 9
	if record['Ht'] > 175:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 10
	if record['Age'] > 79:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 11
	if record['Reach'] <= 123:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 12
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 13
	if record['Ht'] <= 138:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 14
	if record['Age'] > 56:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 15
	if record['Reach'] > 189:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 16
	if record['TailLn'] <= 27:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 17
	if record['Reach'] > 198:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 18
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 19
	if record['TailLn'] > 10:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 20
	if record['TailLn'] > -6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 21
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 22
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 23
	if record['Reach'] > 231:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 24
	if record['TailLn'] > -5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 25
	if record['Reach'] > 237:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 26
	if record['Ht'] <= 130:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 27
	if record['Reach'] > 197:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 28
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 29
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 30
	if record['Reach'] > 218:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 31
	if record['Ht'] > 165:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 32
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 33
	if record['TailLn'] <= 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 34
	if record['TailLn'] <= 29:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 35
	if record['Reach'] > 188:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 36
	if record['Age'] > 43:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 37
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 38
	if record['Age'] > 43:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 39
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 40
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 41
	if record['HairLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 42
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 43
	if record['Reach'] > 163:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 44
	if record['Ht'] > 231:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 45
	if record['Ht'] > 222:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 46
	if record['Reach'] > 181:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 47
	if record['HairLn'] <= 15:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 48
	if record['Ht'] <= 122:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 49
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 50
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 51
	if record['Ht'] <= 142:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 52
	if record['Ht'] > 212:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 53
	if record['Ht'] > 206:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 54
	if record['Age'] > 80:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 55
	if record['TailLn'] > 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 56
	if record['Reach'] > 229:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 57
	if record['Ht'] <= 130:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 58
	if record['Age'] > 43:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 59
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 60
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 61
	if record['Age'] > 69:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 62
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 63
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 64
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 65
	if record['Age'] > 30:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 66
	if record['HairLn'] <= 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 67
	if record['Reach'] > 163:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 68
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 69
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 70
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 71
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 72
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 73
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 74
	if record['Age'] > 25:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 75
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
