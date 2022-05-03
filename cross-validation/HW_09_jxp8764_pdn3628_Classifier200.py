class Classifier200:
	def classifier(record):
		answer = 0

		# Decision Stump Number 1
		if record['TailLn'] <= 25:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 2
		if record['HairLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 3
		if record['Reach'] > 197:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 4
		if record['Reach'] > 199:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 5
		if record['Ht'] <= 115:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 6
		if record['Ht'] > 230:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 7
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 8
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 9
		if record['Reach'] <= 111:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 10
		if record['Ht'] <= 125:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 11
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 12
		if record['Ht'] <= 106:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 13
		if record['Age'] > 79:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 14
		if record['HairLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 15
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 16
		if record['HairLn'] <= 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 17
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 18
		if record['Age'] > 29:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 19
		if record['HairLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 20
		if record['Ht'] > 189:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 21
		if record['Ht'] > 203:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 22
		if record['TailLn'] > -9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 23
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 24
		if record['Age'] > 23:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 25
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 26
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 27
		if record['TailLn'] > 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 28
		if record['Ht'] <= 112:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 29
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 30
		if record['Ht'] > 230:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 31
		if record['TailLn'] > 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 32
		if record['Ht'] > 190:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 33
		if record['Reach'] > 210:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 34
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 35
		if record['TailLn'] > 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 36
		if record['Age'] > 71:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 37
		if record['Age'] > 42:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 38
		if record['Ht'] > 209:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 39
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 40
		if record['Ht'] <= 105:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 41
		if record['HairLn'] <= 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 42
		if record['BangLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 43
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 44
		if record['Ht'] <= 107:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 45
		if record['Ht'] > 153:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 46
		if record['Age'] > 60:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 47
		if record['Ht'] > 213:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 48
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 49
		if record['Ht'] > 166:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 50
		if record['Reach'] <= 104:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 51
		if record['HairLn'] <= 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 52
		if record['TailLn'] > 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 53
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 54
		if record['HairLn'] <= 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 55
		if record['Age'] > 53:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 56
		if record['Reach'] > 154:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 57
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 58
		if record['Ht'] > 175:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 59
		if record['Ht'] > 217:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 60
		if record['BangLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 61
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 62
		if record['TailLn'] > 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 63
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 64
		if record['Ht'] > 144:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 65
		if record['HairLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 66
		if record['Age'] > 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 67
		if record['Reach'] > 170:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 68
		if record['HairLn'] <= 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 69
		if record['TailLn'] > -4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 70
		if record['Ht'] > 226:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 71
		if record['Age'] > 78:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 72
		if record['Age'] > 19:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 73
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 74
		if record['TailLn'] > 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 75
		if record['Age'] > 71:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 76
		if record['HairLn'] <= 12:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 77
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 78
		if record['Ht'] > 226:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 79
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 80
		if record['Reach'] <= 144:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 81
		if record['Age'] > 29:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 82
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 83
		if record['Ht'] <= 142:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 84
		if record['Ht'] > 186:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 85
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 86
		if record['Reach'] > 201:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 87
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 88
		if record['Age'] > 61:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 89
		if record['Ht'] > 206:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 90
		if record['Reach'] <= 111:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 91
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 92
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 93
		if record['Ht'] > 216:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 94
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 95
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 96
		if record['Age'] > 79:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 97
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 98
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 99
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 100
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 101
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 102
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 103
		if record['HairLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 104
		if record['HairLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 105
		if record['Ht'] > 172:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 106
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 107
		if record['Age'] > 49:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 108
		if record['Ht'] > 199:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 109
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 110
		if record['Age'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 111
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 112
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 113
		if record['Reach'] > 198:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 114
		if record['HairLn'] <= 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 115
		if record['Ht'] <= 142:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 116
		if record['TailLn'] > 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 117
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 118
		if record['Reach'] <= 117:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 119
		if record['TailLn'] <= 28:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 120
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 121
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 122
		if record['Reach'] > 201:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 123
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 124
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 125
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 126
		if record['TailLn'] > 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 127
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 128
		if record['Ht'] > 169:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 129
		if record['TailLn'] > 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 130
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 131
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 132
		if record['TailLn'] <= 23:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 133
		if record['TailLn'] > -1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 134
		if record['HairLn'] <= 12:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 135
		if record['TailLn'] > 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 136
		if record['Reach'] <= 138:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 137
		if record['Ht'] > 148:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 138
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 139
		if record['Age'] > 44:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 140
		if record['Age'] > 80:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 141
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 142
		if record['HairLn'] <= 14:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 143
		if record['TailLn'] <= 25:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 144
		if record['TailLn'] > 30:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 145
		if record['Reach'] <= 131:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 146
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 147
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 148
		if record['Age'] > 36:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 149
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 150
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 151
		if record['HairLn'] <= 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 152
		if record['Ht'] <= 97:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 153
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 154
		if record['Ht'] <= 105:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 155
		if record['Reach'] > 195:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 156
		if record['Ht'] <= 130:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 157
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 158
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 159
		if record['Reach'] > 172:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 160
		if record['Ht'] > 146:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 161
		if record['Age'] > 29:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 162
		if record['Reach'] > 222:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 163
		if record['Age'] > 48:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 164
		if record['TailLn'] > 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 165
		if record['Ht'] > 160:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 166
		if record['HairLn'] <= 13:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 167
		if record['Ht'] > 221:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 168
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 169
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 170
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 171
		if record['TailLn'] <= 21:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 172
		if record['HairLn'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 173
		if record['TailLn'] > -8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 174
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 175
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 176
		if record['Age'] > 25:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 177
		if record['Ht'] <= 133:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 178
		if record['TailLn'] <= 24:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 179
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 180
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 181
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 182
		if record['Age'] > 56:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 183
		if record['Ht'] <= 140:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 184
		if record['Ht'] > 149:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 185
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 186
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 187
		if record['Reach'] <= 119:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 188
		if record['Ht'] > 201:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 189
		if record['HairLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 190
		if record['Ht'] <= 102:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 191
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 192
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 193
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 194
		if record['Ht'] > 220:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 195
		if record['Age'] > 57:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 196
		if record['Reach'] > 172:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 197
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 198
		if record['TailLn'] <= 29:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 199
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 200
		if record['Age'] > 55:
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
