class Classifier150:
	def classifier(record):
		answer = 0

		# Decision Stump Number 1
		if record['HairLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 2
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 3
		if record['HairLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 4
		if record['Reach'] > 182:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 5
		if record['Ht'] > 219:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 6
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 7
		if record['Reach'] > 166:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 8
		if record['Ht'] > 219:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 9
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 10
		if record['TailLn'] <= 25:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 11
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 12
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 13
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 14
		if record['Ht'] > 164:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 15
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 16
		if record['Age'] > 43:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 17
		if record['TailLn'] <= 23:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 18
		if record['HairLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 19
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 20
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 21
		if record['HairLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 22
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 23
		if record['TailLn'] > 18:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 24
		if record['Ht'] > 233:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 25
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 26
		if record['Ht'] > 231:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 27
		if record['Reach'] <= 112:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 28
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 29
		if record['TailLn'] > 30:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 30
		if record['TailLn'] > 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 31
		if record['TailLn'] > 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 32
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 33
		if record['Age'] > 57:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 34
		if record['Ht'] <= 108:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 35
		if record['Reach'] <= 141:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 36
		if record['Ht'] <= 101:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 37
		if record['HairLn'] <= 14:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 38
		if record['TailLn'] > 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 39
		if record['Age'] > 41:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 40
		if record['HairLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 41
		if record['Age'] > 24:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 42
		if record['Age'] > 63:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 43
		if record['Ht'] > 209:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 44
		if record['Ht'] > 207:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 45
		if record['HairLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 46
		if record['HairLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 47
		if record['Ht'] > 203:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 48
		if record['TailLn'] > 13:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 49
		if record['HairLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 50
		if record['Reach'] <= 98:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 51
		if record['HairLn'] <= 14:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 52
		if record['TailLn'] > -9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 53
		if record['Ht'] > 194:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 54
		if record['HairLn'] <= 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 55
		if record['TailLn'] > 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 56
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 57
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 58
		if record['TailLn'] <= 26:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 59
		if record['TailLn'] > -4:
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
		if record['Ht'] > 222:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 63
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 64
		if record['Age'] > 40:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 65
		if record['TailLn'] > 19:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 66
		if record['Ht'] <= 109:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 67
		if record['Reach'] > 186:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 68
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 69
		if record['Age'] > 37:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 70
		if record['Ht'] > 199:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 71
		if record['Ht'] > 191:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 72
		if record['Reach'] <= 105:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 73
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 74
		if record['HairLn'] <= 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 75
		if record['Age'] > 56:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 76
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 77
		if record['Reach'] <= 127:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 78
		if record['Ht'] > 152:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 79
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 80
		if record['Reach'] <= 102:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 81
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 82
		if record['TailLn'] > 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 83
		if record['Reach'] <= 114:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 84
		if record['Ht'] > 218:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 85
		if record['Reach'] > 201:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 86
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 87
		if record['Age'] > 60:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 88
		if record['HairLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 89
		if record['Reach'] > 234:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 90
		if record['Ht'] <= 106:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 91
		if record['Ht'] <= 130:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 92
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 93
		if record['Age'] > 61:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 94
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 95
		if record['TailLn'] > -7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 96
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 97
		if record['Reach'] > 239:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 98
		if record['Reach'] <= 147:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 99
		if record['Ht'] <= 133:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 100
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 101
		if record['Age'] > 29:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 102
		if record['HairLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 103
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 104
		if record['TailLn'] > 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 105
		if record['TailLn'] > 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 106
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 107
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 108
		if record['Age'] > 28:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 109
		if record['TailLn'] > 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 110
		if record['TailLn'] > 18:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 111
		if record['Reach'] > 154:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 112
		if record['HairLn'] <= 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 113
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 114
		if record['Age'] > 14:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 115
		if record['HairLn'] <= 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 116
		if record['Reach'] <= 146:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 117
		if record['HairLn'] <= 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 118
		if record['Age'] > 37:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 119
		if record['Age'] > 52:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 120
		if record['Ht'] > 166:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 121
		if record['Age'] > 66:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 122
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 123
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 124
		if record['Ht'] <= 118:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 125
		if record['Ht'] <= 108:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 126
		if record['Age'] > 70:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 127
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 128
		if record['Age'] > 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 129
		if record['HairLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 130
		if record['TailLn'] > 13:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 131
		if record['Reach'] > 211:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 132
		if record['Age'] > 68:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 133
		if record['Ht'] <= 137:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 134
		if record['Ht'] > 211:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 135
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 136
		if record['Reach'] > 210:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 137
		if record['Reach'] <= 96:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 138
		if record['Reach'] > 217:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 139
		if record['Ht'] > 163:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 140
		if record['HairLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 141
		if record['Reach'] > 186:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 142
		if record['TailLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 143
		if record['Age'] > 32:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 144
		if record['Reach'] > 176:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 145
		if record['Age'] > 14:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 146
		if record['Age'] > 46:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 147
		if record['Reach'] > 230:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 148
		if record['Ht'] > 218:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 149
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 150
		if record['BangLn'] <= 8:
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
		print(Classifier150.classifier(record))
