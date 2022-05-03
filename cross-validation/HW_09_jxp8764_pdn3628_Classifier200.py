class Classifier200:
	def classifier(record):
		answer = 0

		# Decision Stump Number 1
		if record['Ht'] <= 98:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 2
		if record['Age'] > 75:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 3
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 4
		if record['Age'] > 46:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 5
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 6
		if record['TailLn'] <= 24:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 7
		if record['Ht'] > 147:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 8
		if record['BangLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 9
		if record['Ht'] <= 128:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 10
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 11
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 12
		if record['Age'] > 36:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 13
		if record['HairLn'] <= 14:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 14
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 15
		if record['Reach'] > 233:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 16
		if record['Age'] > 53:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 17
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 18
		if record['Ht'] > 157:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 19
		if record['Ht'] <= 91:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 20
		if record['HairLn'] <= 14:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 21
		if record['Age'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 22
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 23
		if record['Reach'] > 173:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 24
		if record['Ht'] <= 135:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 25
		if record['Age'] > 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 26
		if record['Age'] > 79:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 27
		if record['HairLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 28
		if record['HairLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 29
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 30
		if record['Ht'] <= 112:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 31
		if record['TailLn'] > 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 32
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 33
		if record['HairLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 34
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 35
		if record['TailLn'] <= 20:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 36
		if record['TailLn'] > 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 37
		if record['Age'] > 21:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 38
		if record['TailLn'] > 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 39
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 40
		if record['Reach'] > 175:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 41
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 42
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 43
		if record['Ht'] > 151:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 44
		if record['Ht'] <= 124:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 45
		if record['Ht'] > 218:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 46
		if record['HairLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 47
		if record['Reach'] > 209:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 48
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 49
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 50
		if record['TailLn'] > -5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 51
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 52
		if record['Reach'] <= 121:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 53
		if record['Reach'] <= 142:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 54
		if record['Reach'] > 200:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 55
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 56
		if record['TailLn'] > 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 57
		if record['TailLn'] > 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 58
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 59
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 60
		if record['Ht'] <= 89:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 61
		if record['Age'] > 66:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 62
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 63
		if record['HairLn'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 64
		if record['Age'] > 61:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 65
		if record['Ht'] > 190:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 66
		if record['Ht'] > 146:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 67
		if record['TailLn'] > 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 68
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 69
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 70
		if record['TailLn'] <= 27:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 71
		if record['Ht'] > 176:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 72
		if record['Age'] > 40:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 73
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 74
		if record['Reach'] > 206:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 75
		if record['Reach'] > 214:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 76
		if record['Age'] > 53:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 77
		if record['TailLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 78
		if record['Ht'] <= 141:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 79
		if record['BangLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 80
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 81
		if record['TailLn'] > 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 82
		if record['HairLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 83
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 84
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 85
		if record['Reach'] <= 141:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 86
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 87
		if record['BangLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 88
		if record['HairLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 89
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 90
		if record['Ht'] > 183:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 91
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 92
		if record['BangLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 93
		if record['Age'] > 69:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 94
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 95
		if record['TailLn'] > -8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 96
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 97
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 98
		if record['Reach'] <= 108:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 99
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 100
		if record['TailLn'] > 19:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 101
		if record['Ht'] > 176:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 102
		if record['Age'] > 60:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 103
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 104
		if record['Ht'] > 222:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 105
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 106
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 107
		if record['TailLn'] <= 24:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 108
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 109
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 110
		if record['Reach'] <= 112:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 111
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 112
		if record['Reach'] <= 121:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 113
		if record['TailLn'] > 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 114
		if record['Ht'] > 224:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 115
		if record['Reach'] <= 147:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 116
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 117
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 118
		if record['TailLn'] > 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 119
		if record['Reach'] > 204:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 120
		if record['Reach'] > 236:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 121
		if record['Reach'] <= 100:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 122
		if record['HairLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 123
		if record['Ht'] > 217:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 124
		if record['TailLn'] <= 25:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 125
		if record['Reach'] <= 132:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 126
		if record['Ht'] <= 119:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 127
		if record['Reach'] > 209:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 128
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 129
		if record['Age'] > 20:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 130
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 131
		if record['Ht'] > 223:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 132
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 133
		if record['Reach'] > 155:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 134
		if record['TailLn'] > 19:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 135
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 136
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 137
		if record['HairLn'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 138
		if record['Reach'] > 207:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 139
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 140
		if record['Age'] > 61:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 141
		if record['Age'] > 23:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 142
		if record['Reach'] > 210:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 143
		if record['TailLn'] > 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 144
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 145
		if record['TailLn'] > -4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 146
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 147
		if record['Ht'] > 233:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 148
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 149
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 150
		if record['Reach'] > 201:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 151
		if record['Age'] > 54:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 152
		if record['Reach'] <= 97:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 153
		if record['Reach'] > 212:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 154
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 155
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 156
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 157
		if record['Ht'] > 196:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 158
		if record['TailLn'] > -4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 159
		if record['TailLn'] > -1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 160
		if record['TailLn'] > -1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 161
		if record['HairLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 162
		if record['Reach'] > 213:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 163
		if record['Reach'] > 155:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 164
		if record['Ht'] <= 101:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 165
		if record['Reach'] > 153:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 166
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 167
		if record['HairLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 168
		if record['Reach'] > 215:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 169
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 170
		if record['Reach'] > 233:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 171
		if record['Ht'] <= 99:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 172
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 173
		if record['TailLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 174
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 175
		if record['Ht'] <= 136:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 176
		if record['TailLn'] > 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 177
		if record['Ht'] <= 136:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 178
		if record['Reach'] <= 139:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 179
		if record['TailLn'] > 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 180
		if record['Reach'] <= 123:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 181
		if record['TailLn'] > -7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 182
		if record['Ht'] > 184:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 183
		if record['Ht'] > 227:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 184
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 185
		if record['Reach'] <= 151:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 186
		if record['Age'] > 34:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 187
		if record['Ht'] > 163:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 188
		if record['TailLn'] > -7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 189
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 190
		if record['TailLn'] > -6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 191
		if record['Reach'] > 184:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 192
		if record['HairLn'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 193
		if record['Ht'] <= 138:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 194
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 195
		if record['Age'] > 80:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 196
		if record['TailLn'] > -1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 197
		if record['Ht'] <= 136:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 198
		if record['Ht'] <= 124:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 199
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 200
		if record['EarLobes'] > 1:
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
		print(Classifier200.classifier(record))
