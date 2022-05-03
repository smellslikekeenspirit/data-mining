def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record['Reach'] > 231:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 5
	if record['Ht'] <= 110:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 6
	if record['Age'] > 67:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 7
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 8
	if record['Age'] > 32:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 9
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 10
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 11
	if record['Ht'] > 145:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 12
	if record['TailLn'] > 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 13
	if record['TailLn'] > 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 14
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 15
	if record['Age'] > 53:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 16
	if record['Ht'] > 201:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 17
	if record['Reach'] > 185:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 18
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 19
	if record['Reach'] <= 133:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 20
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 21
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 22
	if record['Ht'] > 158:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 23
	if record['Reach'] <= 118:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 24
	if record['TailLn'] > 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 25
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 26
	if record['TailLn'] > 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 27
	if record['Reach'] > 226:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 28
	if record['Reach'] <= 128:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 29
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 30
	if record['Reach'] > 228:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 31
	if record['HairLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 32
	if record['HairLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 33
	if record['Age'] > 20:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 34
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 35
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 36
	if record['Reach'] > 192:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 37
	if record['Age'] > 79:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 38
	if record['Age'] > 69:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 39
	if record['Reach'] > 234:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 40
	if record['Age'] > 19:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 41
	if record['HairLn'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 42
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 43
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 44
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 45
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 46
	if record['Age'] > 29:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 47
	if record['Ht'] > 153:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 48
	if record['Ht'] > 186:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 49
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 50
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 51
	if record['Age'] > 19:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 52
	if record['Age'] > 24:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 53
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 54
	if record['Age'] > 35:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 55
	if record['HairLn'] <= 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 56
	if record['Ht'] > 232:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 57
	if record['Age'] > 66:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 58
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 59
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 60
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 61
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 62
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 63
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 64
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 65
	if record['TailLn'] > 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 66
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 67
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 68
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 69
	if record['Ht'] <= 110:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 70
	if record['Reach'] > 161:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 71
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 72
	if record['Age'] > 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 73
	if record['HairLn'] <= 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 74
	if record['Ht'] <= 139:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 75
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 76
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 77
	if record['Age'] > 61:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 78
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 79
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 80
	if record['TailLn'] > 10:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 81
	if record['Ht'] > 223:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 82
	if record['Age'] > 31:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 83
	if record['TailLn'] > 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 84
	if record['TailLn'] > 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 85
	if record['Age'] > 42:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 86
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 87
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 88
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 89
	if record['Ht'] > 161:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 90
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 91
	if record['Reach'] > 226:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 92
	if record['Reach'] <= 96:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 93
	if record['Ht'] > 159:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 94
	if record['Reach'] > 239:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 95
	if record['Ht'] <= 128:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 96
	if record['Reach'] <= 139:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 97
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 98
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 99
	if record['Reach'] <= 135:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 100
	if record['Reach'] > 204:
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
