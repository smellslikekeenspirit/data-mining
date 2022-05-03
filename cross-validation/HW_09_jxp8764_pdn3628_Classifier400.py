class Classifier400:
	def classifier(record):
		answer = 0

		# Decision Stump Number 1
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 2
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 3
		if record['Ht'] > 235:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 4
		if record['Reach'] <= 106:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 5
		if record['Age'] > 78:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 6
		if record['Ht'] <= 120:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 7
		if record['Ht'] > 215:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 8
		if record['Reach'] <= 111:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 9
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 10
		if record['HairLn'] <= 12:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 11
		if record['TailLn'] > 19:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 12
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 13
		if record['Age'] > 42:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 14
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 15
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 16
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 17
		if record['Ht'] <= 141:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 18
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 19
		if record['Reach'] > 239:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 20
		if record['Reach'] <= 108:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 21
		if record['Ht'] <= 132:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 22
		if record['Ht'] > 187:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 23
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 24
		if record['Ht'] > 218:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 25
		if record['Ht'] <= 98:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 26
		if record['TailLn'] > -8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 27
		if record['TailLn'] > 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 28
		if record['TailLn'] > -5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 29
		if record['Ht'] <= 130:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 30
		if record['Reach'] > 180:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 31
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 32
		if record['HairLn'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 33
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 34
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 35
		if record['Ht'] > 143:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 36
		if record['Reach'] <= 133:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 37
		if record['Reach'] <= 131:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 38
		if record['Ht'] > 226:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 39
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 40
		if record['TailLn'] > 19:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 41
		if record['Ht'] > 235:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 42
		if record['TailLn'] > -7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 43
		if record['HairLn'] <= 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 44
		if record['TailLn'] > 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 45
		if record['Age'] > 77:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 46
		if record['Ht'] > 146:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 47
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 48
		if record['Ht'] > 164:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 49
		if record['HairLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 50
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 51
		if record['TailLn'] > -2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 52
		if record['TailLn'] > -4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 53
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 54
		if record['HairLn'] <= 12:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 55
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 56
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 57
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 58
		if record['Ht'] <= 110:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 59
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 60
		if record['TailLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 61
		if record['Age'] > 38:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 62
		if record['Reach'] > 174:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 63
		if record['Reach'] <= 129:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 64
		if record['HairLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 65
		if record['Age'] > 44:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 66
		if record['HairLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 67
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 68
		if record['Reach'] > 178:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 69
		if record['Reach'] <= 96:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 70
		if record['Age'] > 53:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 71
		if record['Reach'] > 226:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 72
		if record['HairLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 73
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 74
		if record['Reach'] <= 125:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 75
		if record['Reach'] > 192:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 76
		if record['Ht'] > 167:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 77
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 78
		if record['Ht'] > 157:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 79
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 80
		if record['Ht'] > 185:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 81
		if record['Reach'] > 195:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 82
		if record['Age'] > 27:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 83
		if record['Age'] > 75:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 84
		if record['Reach'] <= 149:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 85
		if record['TailLn'] > 13:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 86
		if record['Age'] > 18:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 87
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 88
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 89
		if record['HairLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 90
		if record['Ht'] <= 112:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 91
		if record['Ht'] <= 124:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 92
		if record['Age'] > 59:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 93
		if record['Ht'] <= 129:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 94
		if record['TailLn'] > 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 95
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 96
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 97
		if record['Age'] > 55:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 98
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 99
		if record['BangLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 100
		if record['Age'] > 41:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 101
		if record['Age'] > 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 102
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 103
		if record['Reach'] > 157:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 104
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 105
		if record['HairLn'] <= 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 106
		if record['Age'] > 37:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 107
		if record['Reach'] <= 128:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 108
		if record['Ht'] > 164:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 109
		if record['TailLn'] <= 27:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 110
		if record['TailLn'] <= 27:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 111
		if record['Ht'] > 233:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 112
		if record['Age'] > 81:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 113
		if record['Age'] > 32:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 114
		if record['Age'] > 36:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 115
		if record['Reach'] > 161:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 116
		if record['HairLn'] <= 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 117
		if record['Ht'] <= 125:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 118
		if record['Reach'] <= 119:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 119
		if record['TailLn'] > -4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 120
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 121
		if record['Reach'] <= 118:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 122
		if record['Age'] > 29:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 123
		if record['Reach'] > 230:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 124
		if record['Ht'] > 194:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 125
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 126
		if record['HairLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 127
		if record['Reach'] > 155:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 128
		if record['Age'] > 13:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 129
		if record['Ht'] <= 98:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 130
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 131
		if record['Age'] > 64:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 132
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 133
		if record['Age'] > 39:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 134
		if record['Ht'] > 151:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 135
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 136
		if record['BangLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 137
		if record['Age'] > 66:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 138
		if record['Age'] > 76:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 139
		if record['Age'] > 49:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 140
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 141
		if record['Ht'] > 144:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 142
		if record['BangLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 143
		if record['Reach'] > 166:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 144
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 145
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 146
		if record['Reach'] > 185:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 147
		if record['TailLn'] > 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 148
		if record['Age'] > 69:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 149
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 150
		if record['Ht'] <= 131:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 151
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 152
		if record['Ht'] <= 121:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 153
		if record['Age'] > 56:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 154
		if record['Reach'] > 239:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 155
		if record['Age'] > 76:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 156
		if record['TailLn'] <= 20:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 157
		if record['TailLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 158
		if record['Ht'] > 193:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 159
		if record['Reach'] > 193:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 160
		if record['Reach'] <= 120:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 161
		if record['HairLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 162
		if record['TailLn'] > 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 163
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 164
		if record['Reach'] > 167:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 165
		if record['TailLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 166
		if record['TailLn'] > 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 167
		if record['Reach'] <= 129:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 168
		if record['HairLn'] <= 12:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 169
		if record['Reach'] > 167:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 170
		if record['Ht'] > 165:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 171
		if record['HairLn'] <= 13:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 172
		if record['TailLn'] > -8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 173
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 174
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 175
		if record['Age'] > 66:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 176
		if record['HairLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 177
		if record['HairLn'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 178
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 179
		if record['HairLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 180
		if record['Ht'] <= 114:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 181
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 182
		if record['TailLn'] > 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 183
		if record['Ht'] <= 139:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 184
		if record['Age'] <= 12:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 185
		if record['Age'] > 54:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 186
		if record['HairLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 187
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 188
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 189
		if record['Age'] > 48:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 190
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 191
		if record['Reach'] <= 125:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 192
		if record['Reach'] > 225:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 193
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 194
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 195
		if record['HairLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 196
		if record['Ht'] > 158:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 197
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 198
		if record['TailLn'] > 18:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 199
		if record['Ht'] > 225:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 200
		if record['TailLn'] <= 27:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 201
		if record['Age'] > 28:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 202
		if record['Ht'] > 205:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 203
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 204
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 205
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 206
		if record['Ht'] > 153:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 207
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 208
		if record['Ht'] > 225:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 209
		if record['TailLn'] <= 22:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 210
		if record['TailLn'] <= 23:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 211
		if record['Reach'] <= 147:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 212
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 213
		if record['Ht'] > 215:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 214
		if record['TailLn'] <= 29:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 215
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 216
		if record['Reach'] <= 106:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 217
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 218
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 219
		if record['Ht'] > 188:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 220
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 221
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 222
		if record['Reach'] > 207:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 223
		if record['Reach'] > 162:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 224
		if record['HairLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 225
		if record['Reach'] > 157:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 226
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 227
		if record['Reach'] > 193:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 228
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 229
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 230
		if record['Age'] > 77:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 231
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 232
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 233
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 234
		if record['Age'] > 31:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 235
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 236
		if record['Age'] > 81:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 237
		if record['Reach'] <= 123:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 238
		if record['HairLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 239
		if record['TailLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 240
		if record['TailLn'] <= 24:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 241
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 242
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 243
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 244
		if record['TailLn'] <= 27:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 245
		if record['Ht'] <= 97:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 246
		if record['HairLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 247
		if record['Reach'] > 181:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 248
		if record['TailLn'] > 12:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 249
		if record['Ht'] <= 130:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 250
		if record['HairLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 251
		if record['HairLn'] <= 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 252
		if record['Reach'] > 169:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 253
		if record['TailLn'] > 13:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 254
		if record['BangLn'] <= 8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 255
		if record['Age'] > 14:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 256
		if record['HairLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 257
		if record['Ht'] > 173:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 258
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 259
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 260
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 261
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 262
		if record['Age'] > 66:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 263
		if record['TailLn'] > -8:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 264
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 265
		if record['Age'] > 36:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 266
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 267
		if record['HairLn'] <= 16:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 268
		if record['TailLn'] <= 22:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 269
		if record['Ht'] > 198:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 270
		if record['Reach'] <= 134:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 271
		if record['HairLn'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 272
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 273
		if record['HairLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 274
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 275
		if record['Age'] > 45:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 276
		if record['Ht'] <= 117:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 277
		if record['Age'] > 60:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 278
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 279
		if record['HairLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 280
		if record['TailLn'] > -9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 281
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 282
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 283
		if record['Reach'] > 235:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 284
		if record['Age'] > 57:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 285
		if record['Reach'] > 217:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 286
		if record['Reach'] > 233:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 287
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 288
		if record['Reach'] <= 140:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 289
		if record['Reach'] > 159:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 290
		if record['Ht'] > 213:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 291
		if record['Reach'] > 228:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 292
		if record['Ht'] > 168:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 293
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 294
		if record['TailLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 295
		if record['TailLn'] > -2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 296
		if record['TailLn'] > 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 297
		if record['Ht'] > 228:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 298
		if record['TailLn'] <= 28:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 299
		if record['Age'] > 30:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 300
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 301
		if record['TailLn'] > 19:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 302
		if record['HairLn'] <= 14:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 303
		if record['Age'] > 35:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 304
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 305
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 306
		if record['Reach'] > 191:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 307
		if record['HairLn'] <= 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 308
		if record['Age'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 309
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 310
		if record['Reach'] > 186:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 311
		if record['Ht'] <= 114:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 312
		if record['Ht'] <= 91:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 313
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 314
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 315
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 316
		if record['Reach'] > 234:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 317
		if record['Ht'] > 222:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 318
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 319
		if record['HairLn'] <= 11:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 320
		if record['TailLn'] > -4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 321
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 322
		if record['Age'] > 75:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 323
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 324
		if record['Reach'] <= 143:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 325
		if record['Age'] > 63:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 326
		if record['BangLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 327
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 328
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 329
		if record['HairLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 330
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 331
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 332
		if record['Reach'] <= 95:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 333
		if record['Ht'] <= 140:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 334
		if record['TailLn'] > 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 335
		if record['HairLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 336
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 337
		if record['Age'] > 53:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 338
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 339
		if record['TailLn'] <= 24:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 340
		if record['BangLn'] <= 7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 341
		if record['TailLn'] > -4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 342
		if record['BangLn'] <= 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 343
		if record['HairLn'] <= 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 344
		if record['Age'] > 44:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 345
		if record['Reach'] <= 144:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 346
		if record['Reach'] > 201:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 347
		if record['TailLn'] <= 21:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 348
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 349
		if record['BangLn'] <= 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 350
		if record['Reach'] > 198:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 351
		if record['Age'] > 32:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 352
		if record['TailLn'] > 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 353
		if record['Ht'] > 172:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 354
		if record['TailLn'] <= 20:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 355
		if record['Reach'] > 231:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 356
		if record['TailLn'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 357
		if record['Ht'] > 163:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 358
		if record['TailLn'] > 13:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 359
		if record['Age'] > 69:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 360
		if record['Age'] > 20:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 361
		if record['TailLn'] > -3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 362
		if record['Ht'] > 189:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 363
		if record['Age'] > 24:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 364
		if record['BangLn'] <= 5:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 365
		if record['HairLn'] <= 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 366
		if record['Age'] > 50:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 367
		if record['Ht'] > 215:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 368
		if record['TailLn'] > 3:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 369
		if record['Age'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 370
		if record['Reach'] <= 125:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 371
		if record['HairLn'] <= 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 372
		if record['Age'] > 62:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 373
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 374
		if record['Age'] > 71:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 375
		if record['Age'] > 59:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 376
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 377
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 378
		if record['Age'] > 26:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 379
		if record['BangLn'] <= 6:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 380
		if record['BangLn'] <= 2:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 381
		if record['TailLn'] > 10:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 382
		if record['Ht'] > 176:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 383
		if record['TailLn'] > -7:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 384
		if record['Reach'] <= 137:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 385
		if record['Age'] > 70:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 386
		if record['Reach'] <= 101:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 387
		if record['Ht'] > 174:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 388
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 389
		if record['HairLn'] <= 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 390
		if record['Age'] > 68:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 391
		if record['TailLn'] > 15:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 392
		if record['TailLn'] > 4:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 393
		if record['EarLobes'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 394
		if record['Ht'] > 157:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 395
		if record['Age'] > 22:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 396
		if record['BangLn'] > 9:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 397
		if record['EarLobes'] <= 0:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 398
		if record['HairLn'] > 1:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 399
		if record['HairLn'] > 17:
			answer = answer - 1
		else:
			answer = answer + 1

		# Decision Stump Number 400
		if record['HairLn'] <= 12:
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
