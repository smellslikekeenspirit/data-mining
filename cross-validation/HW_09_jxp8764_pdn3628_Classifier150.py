def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['HairLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record['Age'] > 24:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 5
	if record['TailLn'] <= 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 6
	if record['TailLn'] > 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 7
	if record['Ht'] > 187:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 8
	if record['Ht'] > 199:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 9
	if record['Ht'] > 152:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 10
	if record['Ht'] > 203:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 11
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 12
	if record['Reach'] > 155:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 13
	if record['TailLn'] > 15:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 14
	if record['Ht'] > 215:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 15
	if record['Reach'] > 220:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 16
	if record['TailLn'] > 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 17
	if record['TailLn'] > -1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 18
	if record['Reach'] > 224:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 19
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 20
	if record['Reach'] <= 98:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 21
	if record['Age'] > 79:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 22
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 23
	if record['Ht'] <= 101:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 24
	if record['HairLn'] <= 2:
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
	if record['TailLn'] > 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 28
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 29
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 30
	if record['Age'] > 65:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 31
	if record['Age'] > 23:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 32
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 33
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 34
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 35
	if record['Reach'] > 226:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 36
	if record['Reach'] > 159:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 37
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 38
	if record['Age'] > 75:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 39
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 40
	if record['HairLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 41
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 42
	if record['TailLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 43
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 44
	if record['TailLn'] <= 25:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 45
	if record['Ht'] <= 89:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 46
	if record['Reach'] > 173:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 47
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 48
	if record['Ht'] > 188:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 49
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 50
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 51
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 52
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 53
	if record['Reach'] > 216:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 54
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 55
	if record['Age'] > 40:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 56
	if record['Reach'] <= 101:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 57
	if record['Reach'] > 196:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 58
	if record['Age'] > 28:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 59
	if record['Reach'] <= 105:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 60
	if record['TailLn'] > 30:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 61
	if record['Age'] > 56:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 62
	if record['Reach'] <= 95:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 63
	if record['HairLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 64
	if record['Ht'] > 199:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 65
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 66
	if record['Age'] > 48:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 67
	if record['Ht'] > 209:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 68
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 69
	if record['Reach'] <= 144:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 70
	if record['Age'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 71
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 72
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 73
	if record['Reach'] > 155:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 74
	if record['Ht'] > 230:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 75
	if record['TailLn'] > -5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 76
	if record['Ht'] <= 140:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 77
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 78
	if record['Age'] > 18:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 79
	if record['Reach'] > 213:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 80
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 81
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 82
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 83
	if record['Reach'] > 226:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 84
	if record['Ht'] > 227:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 85
	if record['TailLn'] > 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 86
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 87
	if record['Age'] > 30:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 88
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 89
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 90
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 91
	if record['TailLn'] > 30:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 92
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 93
	if record['TailLn'] > 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 94
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 95
	if record['Reach'] <= 146:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 96
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 97
	if record['Ht'] <= 119:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 98
	if record['TailLn'] > 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 99
	if record['Age'] > 28:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 100
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 101
	if record['Ht'] > 145:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 102
	if record['Reach'] > 183:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 103
	if record['HairLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 104
	if record['TailLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 105
	if record['Ht'] > 156:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 106
	if record['Age'] > 23:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 107
	if record['Reach'] > 186:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 108
	if record['Age'] > 25:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 109
	if record['TailLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 110
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 111
	if record['Age'] > 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 112
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 113
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 114
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 115
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 116
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 117
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 118
	if record['Age'] > 55:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 119
	if record['HairLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 120
	if record['TailLn'] > 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 121
	if record['Reach'] > 237:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 122
	if record['HairLn'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 123
	if record['TailLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 124
	if record['Reach'] > 227:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 125
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 126
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 127
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 128
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 129
	if record['Age'] > 25:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 130
	if record['Reach'] <= 101:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 131
	if record['Ht'] > 147:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 132
	if record['Ht'] <= 140:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 133
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 134
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 135
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 136
	if record['Ht'] <= 102:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 137
	if record['HairLn'] <= 15:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 138
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 139
	if record['Age'] > 40:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 140
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 141
	if record['Reach'] <= 120:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 142
	if record['Reach'] > 232:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 143
	if record['HairLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 144
	if record['Age'] > 30:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 145
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 146
	if record['Age'] > 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 147
	if record['Age'] > 22:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 148
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 149
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 150
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
