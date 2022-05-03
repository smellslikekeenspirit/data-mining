def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['Age'] > 31:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record['Ht'] > 214:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record['Age'] > 78:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record['Ht'] > 217:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 5
	if record['TailLn'] <= 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 6
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 7
	if record['TailLn'] > 30:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 8
	if record['Age'] > 72:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 9
	if record['Age'] > 67:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 10
	if record['Ht'] > 235:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 11
	if record['Reach'] <= 142:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 12
	if record['Ht'] > 176:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 13
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 14
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 15
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 16
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 17
	if record['Reach'] > 173:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 18
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 19
	if record['HairLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 20
	if record['TailLn'] <= 25:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 21
	if record['TailLn'] > 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 22
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 23
	if record['TailLn'] <= 20:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 24
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 25
	if record['TailLn'] > 30:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 26
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 27
	if record['Ht'] > 215:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 28
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 29
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 30
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 31
	if record['Age'] > 51:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 32
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 33
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 34
	if record['Ht'] > 183:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 35
	if record['TailLn'] > -1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 36
	if record['Ht'] > 191:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 37
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 38
	if record['TailLn'] <= 20:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 39
	if record['Ht'] <= 133:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 40
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 41
	if record['TailLn'] > 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 42
	if record['Ht'] > 173:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 43
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 44
	if record['Ht'] > 188:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 45
	if record['Age'] > 70:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 46
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 47
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 48
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 49
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 50
	if record['Age'] > 55:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 51
	if record['HairLn'] <= 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 52
	if record['Reach'] > 186:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 53
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 54
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 55
	if record['HairLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 56
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 57
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 58
	if record['Reach'] > 211:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 59
	if record['Ht'] <= 129:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 60
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 61
	if record['Age'] > 57:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 62
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 63
	if record['Ht'] > 193:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 64
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 65
	if record['Reach'] > 184:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 66
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 67
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 68
	if record['Ht'] > 169:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 69
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 70
	if record['TailLn'] > 10:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 71
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 72
	if record['Ht'] > 204:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 73
	if record['Age'] > 41:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 74
	if record['TailLn'] > 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 75
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 76
	if record['Reach'] > 169:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 77
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 78
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 79
	if record['Age'] > 76:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 80
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 81
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 82
	if record['Ht'] <= 114:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 83
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 84
	if record['Age'] > 21:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 85
	if record['Reach'] <= 107:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 86
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 87
	if record['TailLn'] > 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 88
	if record['Reach'] <= 94:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 89
	if record['Ht'] > 184:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 90
	if record['HairLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 91
	if record['Reach'] > 161:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 92
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 93
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 94
	if record['Reach'] > 239:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 95
	if record['Age'] > 22:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 96
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 97
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 98
	if record['Reach'] > 228:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 99
	if record['Age'] > 63:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 100
	if record['Reach'] > 158:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 101
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 102
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 103
	if record['Ht'] > 154:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 104
	if record['Ht'] > 227:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 105
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 106
	if record['Reach'] > 238:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 107
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 108
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 109
	if record['Ht'] > 145:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 110
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 111
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 112
	if record['Reach'] > 229:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 113
	if record['Reach'] > 219:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 114
	if record['TailLn'] > 18:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 115
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 116
	if record['Reach'] > 163:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 117
	if record['Ht'] <= 91:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 118
	if record['Reach'] <= 101:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 119
	if record['Reach'] > 231:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 120
	if record['Age'] > 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 121
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 122
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 123
	if record['Ht'] <= 121:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 124
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 125
	if record['Reach'] <= 122:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 126
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 127
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 128
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 129
	if record['Ht'] > 220:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 130
	if record['Ht'] <= 138:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 131
	if record['Reach'] <= 106:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 132
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 133
	if record['Reach'] > 215:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 134
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 135
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 136
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 137
	if record['Reach'] > 174:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 138
	if record['Ht'] > 225:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 139
	if record['Reach'] > 157:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 140
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 141
	if record['Reach'] > 188:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 142
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 143
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 144
	if record['Ht'] <= 91:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 145
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 146
	if record['TailLn'] > 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 147
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 148
	if record['TailLn'] > -1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 149
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 150
	if record['Reach'] > 233:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 151
	if record['Reach'] > 233:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 152
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 153
	if record['Reach'] <= 114:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 154
	if record['Age'] > 23:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 155
	if record['Age'] > 75:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 156
	if record['Reach'] > 217:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 157
	if record['Ht'] <= 132:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 158
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 159
	if record['TailLn'] <= 21:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 160
	if record['Age'] > 64:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 161
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 162
	if record['Age'] > 33:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 163
	if record['Reach'] > 194:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 164
	if record['TailLn'] > 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 165
	if record['Reach'] <= 140:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 166
	if record['Age'] > 58:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 167
	if record['Age'] > 21:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 168
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 169
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 170
	if record['Age'] > 58:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 171
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 172
	if record['Ht'] > 234:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 173
	if record['TailLn'] > -5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 174
	if record['Reach'] > 196:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 175
	if record['Age'] > 27:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 176
	if record['Ht'] > 148:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 177
	if record['Age'] > 66:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 178
	if record['Reach'] <= 95:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 179
	if record['Age'] > 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 180
	if record['Ht'] > 208:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 181
	if record['TailLn'] > -4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 182
	if record['TailLn'] > -6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 183
	if record['Ht'] > 228:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 184
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 185
	if record['Ht'] <= 121:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 186
	if record['Reach'] <= 127:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 187
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 188
	if record['TailLn'] > 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 189
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 190
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 191
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 192
	if record['Reach'] > 161:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 193
	if record['Reach'] > 236:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 194
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 195
	if record['Reach'] > 167:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 196
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 197
	if record['Ht'] > 193:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 198
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 199
	if record['TailLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 200
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 201
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 202
	if record['Reach'] > 193:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 203
	if record['HairLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 204
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 205
	if record['Age'] > 54:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 206
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 207
	if record['TailLn'] <= 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 208
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 209
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 210
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 211
	if record['Age'] > 35:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 212
	if record['TailLn'] > 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 213
	if record['Reach'] <= 110:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 214
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 215
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 216
	if record['Ht'] > 155:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 217
	if record['TailLn'] <= 29:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 218
	if record['HairLn'] <= 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 219
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 220
	if record['Reach'] > 164:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 221
	if record['Ht'] > 194:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 222
	if record['Reach'] <= 128:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 223
	if record['Age'] > 77:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 224
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 225
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 226
	if record['HairLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 227
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 228
	if record['TailLn'] > 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 229
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 230
	if record['Age'] > 27:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 231
	if record['HairLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 232
	if record['HairLn'] <= 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 233
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 234
	if record['HairLn'] <= 10:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 235
	if record['TailLn'] > -2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 236
	if record['Reach'] > 180:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 237
	if record['TailLn'] > -7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 238
	if record['Reach'] <= 126:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 239
	if record['Ht'] > 183:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 240
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 241
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 242
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 243
	if record['TailLn'] > -6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 244
	if record['Age'] > 69:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 245
	if record['Age'] > 68:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 246
	if record['Ht'] > 194:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 247
	if record['HairLn'] <= 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 248
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 249
	if record['HairLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 250
	if record['BangLn'] <= 7:
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
