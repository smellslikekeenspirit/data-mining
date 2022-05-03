def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record['Ht'] > 160:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 5
	if record['Ht'] > 193:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 6
	if record['Age'] > 62:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 7
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 8
	if record['Age'] > 81:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 9
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 10
	if record['Age'] > 29:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 11
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 12
	if record['Reach'] <= 123:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 13
	if record['Ht'] > 174:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 14
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 15
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 16
	if record['Ht'] > 175:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 17
	if record['Age'] > 67:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 18
	if record['Reach'] > 206:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 19
	if record['TailLn'] > 19:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 20
	if record['Ht'] <= 137:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 21
	if record['Ht'] <= 125:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 22
	if record['Ht'] <= 124:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 23
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 24
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 25
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 26
	if record['TailLn'] > -5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 27
	if record['Ht'] > 203:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 28
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 29
	if record['TailLn'] > -9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 30
	if record['Age'] > 47:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 31
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 32
	if record['Reach'] <= 139:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 33
	if record['Reach'] <= 145:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 34
	if record['Reach'] <= 151:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 35
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 36
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 37
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 38
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 39
	if record['HairLn'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 40
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 41
	if record['TailLn'] > -4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 42
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 43
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 44
	if record['Reach'] > 229:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 45
	if record['Age'] > 65:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 46
	if record['Age'] > 73:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 47
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 48
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 49
	if record['Ht'] > 157:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 50
	if record['TailLn'] <= 27:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 51
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 52
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 53
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 54
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 55
	if record['Age'] > 30:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 56
	if record['Ht'] <= 119:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 57
	if record['Ht'] > 207:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 58
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 59
	if record['Age'] > 79:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 60
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 61
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 62
	if record['Age'] > 23:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 63
	if record['Ht'] > 146:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 64
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 65
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 66
	if record['Reach'] > 183:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 67
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 68
	if record['Reach'] > 226:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 69
	if record['Age'] > 73:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 70
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 71
	if record['Reach'] > 232:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 72
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 73
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 74
	if record['Ht'] > 183:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 75
	if record['Reach'] <= 109:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 76
	if record['Reach'] > 232:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 77
	if record['TailLn'] <= 24:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 78
	if record['TailLn'] <= 24:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 79
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 80
	if record['Reach'] > 205:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 81
	if record['TailLn'] > 30:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 82
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 83
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 84
	if record['Reach'] <= 112:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 85
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 86
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 87
	if record['Age'] > 20:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 88
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 89
	if record['Ht'] <= 129:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 90
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 91
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 92
	if record['Age'] > 81:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 93
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 94
	if record['Ht'] > 159:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 95
	if record['TailLn'] > 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 96
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 97
	if record['Ht'] <= 141:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 98
	if record['Ht'] <= 141:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 99
	if record['Ht'] > 155:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 100
	if record['TailLn'] > 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 101
	if record['TailLn'] > 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 102
	if record['Ht'] > 187:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 103
	if record['Ht'] > 235:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 104
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 105
	if record['TailLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 106
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 107
	if record['Ht'] <= 95:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 108
	if record['Reach'] > 163:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 109
	if record['TailLn'] > 19:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 110
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 111
	if record['Age'] > 60:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 112
	if record['Age'] > 76:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 113
	if record['Reach'] > 160:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 114
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 115
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 116
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 117
	if record['TailLn'] > 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 118
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 119
	if record['HairLn'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 120
	if record['Reach'] <= 136:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 121
	if record['TailLn'] > 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 122
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 123
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 124
	if record['Ht'] > 229:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 125
	if record['Ht'] <= 100:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 126
	if record['Ht'] > 172:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 127
	if record['Age'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 128
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 129
	if record['Reach'] > 234:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 130
	if record['Ht'] > 155:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 131
	if record['HairLn'] <= 10:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 132
	if record['TailLn'] > -5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 133
	if record['HairLn'] <= 10:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 134
	if record['Reach'] > 200:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 135
	if record['Ht'] > 189:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 136
	if record['TailLn'] <= 20:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 137
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 138
	if record['Ht'] > 186:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 139
	if record['TailLn'] <= 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 140
	if record['Age'] > 33:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 141
	if record['Age'] > 45:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 142
	if record['Reach'] <= 151:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 143
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 144
	if record['TailLn'] <= 23:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 145
	if record['Reach'] > 196:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 146
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 147
	if record['Age'] > 19:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 148
	if record['Reach'] > 175:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 149
	if record['Ht'] <= 89:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 150
	if record['Reach'] > 218:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 151
	if record['Age'] > 49:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 152
	if record['TailLn'] <= 23:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 153
	if record['Reach'] > 158:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 154
	if record['Age'] > 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 155
	if record['Reach'] <= 150:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 156
	if record['Age'] > 64:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 157
	if record['Age'] > 75:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 158
	if record['Ht'] > 180:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 159
	if record['TailLn'] > 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 160
	if record['Age'] > 59:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 161
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 162
	if record['Reach'] <= 110:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 163
	if record['Age'] > 65:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 164
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 165
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 166
	if record['HairLn'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 167
	if record['Ht'] <= 109:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 168
	if record['Age'] > 74:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 169
	if record['Age'] > 21:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 170
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 171
	if record['Reach'] <= 143:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 172
	if record['HairLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 173
	if record['TailLn'] <= 29:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 174
	if record['Ht'] <= 134:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 175
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 176
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 177
	if record['Age'] > 57:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 178
	if record['Reach'] <= 115:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 179
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 180
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 181
	if record['TailLn'] > -5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 182
	if record['Reach'] <= 108:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 183
	if record['Age'] > 61:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 184
	if record['TailLn'] > -3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 185
	if record['Age'] > 48:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 186
	if record['Age'] > 80:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 187
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 188
	if record['Ht'] <= 128:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 189
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 190
	if record['Reach'] > 200:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 191
	if record['Reach'] <= 128:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 192
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 193
	if record['HairLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 194
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 195
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 196
	if record['Age'] > 40:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 197
	if record['HairLn'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 198
	if record['Ht'] <= 90:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 199
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 200
	if record['HairLn'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 201
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 202
	if record['Age'] > 48:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 203
	if record['Age'] > 15:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 204
	if record['Ht'] > 165:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 205
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 206
	if record['HairLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 207
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 208
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 209
	if record['HairLn'] <= 15:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 210
	if record['TailLn'] > 18:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 211
	if record['Ht'] > 222:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 212
	if record['TailLn'] <= 28:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 213
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 214
	if record['TailLn'] > -1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 215
	if record['Reach'] <= 113:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 216
	if record['Age'] > 75:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 217
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 218
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 219
	if record['TailLn'] > 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 220
	if record['Reach'] <= 139:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 221
	if record['Age'] > 61:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 222
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 223
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 224
	if record['HairLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 225
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 226
	if record['Ht'] <= 134:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 227
	if record['TailLn'] > 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 228
	if record['Ht'] <= 92:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 229
	if record['Ht'] <= 92:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 230
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 231
	if record['Reach'] <= 119:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 232
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 233
	if record['Reach'] > 195:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 234
	if record['Age'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 235
	if record['HairLn'] <= 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 236
	if record['HairLn'] <= 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 237
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 238
	if record['Ht'] > 228:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 239
	if record['Ht'] <= 134:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 240
	if record['HairLn'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 241
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 242
	if record['Ht'] > 203:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 243
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 244
	if record['Age'] > 20:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 245
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 246
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 247
	if record['Ht'] <= 102:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 248
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 249
	if record['Ht'] <= 135:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 250
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 251
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 252
	if record['TailLn'] <= 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 253
	if record['HairLn'] <= 15:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 254
	if record['Age'] > 40:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 255
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 256
	if record['TailLn'] > 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 257
	if record['Age'] > 78:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 258
	if record['Age'] > 54:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 259
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 260
	if record['Age'] > 47:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 261
	if record['TailLn'] <= 25:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 262
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 263
	if record['Reach'] > 220:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 264
	if record['TailLn'] <= 27:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 265
	if record['Ht'] > 159:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 266
	if record['HairLn'] <= 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 267
	if record['TailLn'] > 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 268
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 269
	if record['TailLn'] > 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 270
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 271
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 272
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 273
	if record['TailLn'] > 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 274
	if record['Age'] > 74:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 275
	if record['Age'] > 78:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 276
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 277
	if record['Ht'] > 159:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 278
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 279
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 280
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 281
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 282
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 283
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 284
	if record['Reach'] > 182:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 285
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 286
	if record['Ht'] > 199:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 287
	if record['Ht'] <= 112:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 288
	if record['Age'] > 76:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 289
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 290
	if record['TailLn'] > 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 291
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 292
	if record['HairLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 293
	if record['Age'] > 53:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 294
	if record['TailLn'] > 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 295
	if record['Age'] > 65:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 296
	if record['Ht'] > 202:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 297
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 298
	if record['TailLn'] > -2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 299
	if record['Age'] > 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 300
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
		print(classifier(record))
