def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['TailLn'] > -1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 5
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 6
	if record['Ht'] > 156:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 7
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 8
	if record['TailLn'] > -7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 9
	if record['TailLn'] <= 25:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 10
	if record['Age'] > 48:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 11
	if record['Age'] > 28:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 12
	if record['Age'] > 38:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 13
	if record['Age'] > 79:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 14
	if record['TailLn'] > -5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 15
	if record['Age'] > 28:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 16
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 17
	if record['TailLn'] > 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 18
	if record['Age'] > 20:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 19
	if record['Reach'] > 212:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 20
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 21
	if record['TailLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 22
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 23
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 24
	if record['Reach'] <= 94:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 25
	if record['Ht'] <= 130:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 26
	if record['Ht'] > 211:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 27
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 28
	if record['Reach'] > 160:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 29
	if record['Ht'] > 164:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 30
	if record['Ht'] > 212:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 31
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 32
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 33
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 34
	if record['Age'] > 55:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 35
	if record['Reach'] <= 128:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 36
	if record['Age'] > 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 37
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 38
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 39
	if record['Ht'] > 228:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 40
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 41
	if record['TailLn'] > 15:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 42
	if record['Reach'] <= 120:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 43
	if record['TailLn'] > 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 44
	if record['HairLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 45
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 46
	if record['TailLn'] > 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 47
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 48
	if record['TailLn'] <= 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 49
	if record['Ht'] > 187:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 50
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 51
	if record['Reach'] > 188:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 52
	if record['Age'] > 24:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 53
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 54
	if record['Reach'] > 164:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 55
	if record['TailLn'] > 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 56
	if record['Ht'] > 150:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 57
	if record['Reach'] <= 146:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 58
	if record['Age'] > 62:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 59
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 60
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 61
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 62
	if record['Age'] > 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 63
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 64
	if record['HairLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 65
	if record['TailLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 66
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 67
	if record['Ht'] > 152:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 68
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 69
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 70
	if record['Age'] > 78:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 71
	if record['TailLn'] <= 25:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 72
	if record['TailLn'] > 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 73
	if record['Age'] > 57:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 74
	if record['Reach'] > 156:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 75
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 76
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 77
	if record['TailLn'] <= 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 78
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 79
	if record['Ht'] > 203:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 80
	if record['Reach'] > 171:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 81
	if record['TailLn'] <= 20:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 82
	if record['Ht'] > 187:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 83
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 84
	if record['Reach'] <= 131:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 85
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 86
	if record['HairLn'] <= 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 87
	if record['Reach'] > 224:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 88
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 89
	if record['Reach'] <= 149:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 90
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 91
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 92
	if record['TailLn'] > 30:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 93
	if record['Ht'] <= 110:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 94
	if record['TailLn'] > 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 95
	if record['Age'] > 42:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 96
	if record['Age'] > 79:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 97
	if record['TailLn'] > 15:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 98
	if record['Age'] > 37:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 99
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 100
	if record['TailLn'] <= 24:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 101
	if record['Age'] > 66:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 102
	if record['Ht'] > 195:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 103
	if record['Ht'] <= 110:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 104
	if record['Ht'] <= 118:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 105
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 106
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 107
	if record['Ht'] <= 90:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 108
	if record['Reach'] <= 114:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 109
	if record['Ht'] > 180:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 110
	if record['TailLn'] > 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 111
	if record['Reach'] <= 145:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 112
	if record['HairLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 113
	if record['Age'] > 68:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 114
	if record['Age'] > 33:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 115
	if record['TailLn'] > -8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 116
	if record['Age'] > 23:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 117
	if record['Reach'] <= 144:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 118
	if record['TailLn'] > -7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 119
	if record['Reach'] > 216:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 120
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 121
	if record['Age'] > 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 122
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 123
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 124
	if record['Age'] > 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 125
	if record['Age'] > 47:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 126
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 127
	if record['Ht'] > 186:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 128
	if record['TailLn'] > -8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 129
	if record['HairLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 130
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 131
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 132
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 133
	if record['Reach'] > 211:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 134
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 135
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 136
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 137
	if record['Reach'] > 188:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 138
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 139
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 140
	if record['Age'] > 43:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 141
	if record['Ht'] > 158:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 142
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 143
	if record['Age'] > 33:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 144
	if record['HairLn'] <= 10:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 145
	if record['TailLn'] > -6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 146
	if record['Ht'] <= 109:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 147
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 148
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 149
	if record['TailLn'] <= 21:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 150
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 151
	if record['Reach'] <= 115:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 152
	if record['Ht'] <= 99:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 153
	if record['Reach'] <= 98:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 154
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 155
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 156
	if record['Age'] > 55:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 157
	if record['TailLn'] <= 23:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 158
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 159
	if record['Reach'] > 236:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 160
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 161
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 162
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 163
	if record['Age'] > 36:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 164
	if record['HairLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 165
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 166
	if record['Reach'] > 204:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 167
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 168
	if record['Ht'] > 232:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 169
	if record['Ht'] > 209:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 170
	if record['Reach'] > 188:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 171
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 172
	if record['TailLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 173
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 174
	if record['HairLn'] <= 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 175
	if record['Ht'] <= 131:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 176
	if record['TailLn'] > -7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 177
	if record['Ht'] > 143:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 178
	if record['Reach'] <= 99:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 179
	if record['Reach'] <= 144:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 180
	if record['HairLn'] <= 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 181
	if record['TailLn'] > -2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 182
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 183
	if record['Ht'] > 229:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 184
	if record['TailLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 185
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 186
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 187
	if record['HairLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 188
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 189
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 190
	if record['Ht'] > 200:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 191
	if record['Ht'] > 179:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 192
	if record['HairLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 193
	if record['Age'] > 68:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 194
	if record['Age'] > 76:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 195
	if record['TailLn'] <= 25:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 196
	if record['TailLn'] > 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 197
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 198
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 199
	if record['TailLn'] > 19:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 200
	if record['Age'] > 66:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 201
	if record['Ht'] <= 118:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 202
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 203
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 204
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 205
	if record['Ht'] > 168:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 206
	if record['Reach'] > 218:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 207
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 208
	if record['Ht'] > 193:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 209
	if record['HairLn'] <= 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 210
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 211
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 212
	if record['TailLn'] > -3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 213
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 214
	if record['Ht'] <= 119:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 215
	if record['HairLn'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 216
	if record['Ht'] <= 91:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 217
	if record['TailLn'] > -7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 218
	if record['Ht'] <= 142:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 219
	if record['Ht'] > 202:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 220
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 221
	if record['TailLn'] > 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 222
	if record['Age'] > 34:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 223
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 224
	if record['Age'] > 45:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 225
	if record['Age'] > 36:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 226
	if record['Age'] > 65:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 227
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 228
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 229
	if record['TailLn'] <= 24:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 230
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 231
	if record['Age'] > 65:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 232
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 233
	if record['HairLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 234
	if record['Reach'] > 226:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 235
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 236
	if record['Reach'] <= 108:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 237
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 238
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 239
	if record['HairLn'] <= 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 240
	if record['Ht'] <= 105:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 241
	if record['Reach'] > 202:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 242
	if record['TailLn'] > 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 243
	if record['Age'] > 52:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 244
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 245
	if record['Reach'] <= 120:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 246
	if record['Age'] > 54:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 247
	if record['Age'] > 56:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 248
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 249
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 250
	if record['Age'] > 51:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 251
	if record['Age'] > 22:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 252
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 253
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 254
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 255
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 256
	if record['Ht'] <= 102:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 257
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 258
	if record['Reach'] <= 127:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 259
	if record['Ht'] > 197:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 260
	if record['Reach'] <= 123:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 261
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 262
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 263
	if record['TailLn'] <= 20:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 264
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 265
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 266
	if record['Ht'] > 170:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 267
	if record['Ht'] > 151:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 268
	if record['Ht'] > 179:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 269
	if record['Reach'] > 200:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 270
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 271
	if record['Age'] > 52:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 272
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 273
	if record['TailLn'] > 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 274
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 275
	if record['Ht'] > 146:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 276
	if record['Age'] > 69:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 277
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 278
	if record['Reach'] > 164:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 279
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 280
	if record['Reach'] > 180:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 281
	if record['Ht'] <= 108:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 282
	if record['HairLn'] <= 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 283
	if record['Ht'] > 203:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 284
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 285
	if record['Ht'] > 226:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 286
	if record['HairLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 287
	if record['Age'] > 70:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 288
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 289
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 290
	if record['TailLn'] > 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 291
	if record['HairLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 292
	if record['Age'] > 32:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 293
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 294
	if record['Reach'] > 225:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 295
	if record['TailLn'] > -5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 296
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 297
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 298
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 299
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 300
	if record['Reach'] > 214:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 301
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 302
	if record['Ht'] > 184:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 303
	if record['TailLn'] > 30:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 304
	if record['Age'] > 20:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 305
	if record['Age'] > 67:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 306
	if record['TailLn'] > 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 307
	if record['Age'] > 76:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 308
	if record['Reach'] > 200:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 309
	if record['TailLn'] > 30:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 310
	if record['TailLn'] > -9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 311
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 312
	if record['Ht'] > 182:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 313
	if record['Reach'] <= 112:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 314
	if record['Reach'] > 164:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 315
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 316
	if record['Age'] > 70:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 317
	if record['Reach'] > 236:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 318
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 319
	if record['Reach'] <= 138:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 320
	if record['Ht'] > 220:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 321
	if record['Ht'] > 145:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 322
	if record['Age'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 323
	if record['Age'] > 29:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 324
	if record['TailLn'] <= 24:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 325
	if record['Age'] > 47:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 326
	if record['HairLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 327
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 328
	if record['TailLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 329
	if record['Age'] > 41:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 330
	if record['Ht'] > 201:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 331
	if record['HairLn'] > 17:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 332
	if record['Reach'] > 168:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 333
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 334
	if record['TailLn'] > 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 335
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 336
	if record['Age'] > 27:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 337
	if record['Ht'] <= 94:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 338
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 339
	if record['Reach'] > 157:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 340
	if record['Ht'] > 191:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 341
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 342
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 343
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 344
	if record['Reach'] <= 142:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 345
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 346
	if record['Age'] > 18:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 347
	if record['Ht'] > 212:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 348
	if record['Reach'] <= 123:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 349
	if record['Age'] > 57:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 350
	if record['Ht'] <= 125:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 351
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 352
	if record['Ht'] > 194:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 353
	if record['BangLn'] > 9:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 354
	if record['Ht'] <= 121:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 355
	if record['HairLn'] <= 15:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 356
	if record['Ht'] > 179:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 357
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 358
	if record['BangLn'] <= 3:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 359
	if record['BangLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 360
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 361
	if record['TailLn'] > 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 362
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 363
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 364
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 365
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 366
	if record['Reach'] <= 118:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 367
	if record['HairLn'] <= 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 368
	if record['HairLn'] <= 14:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 369
	if record['BangLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 370
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 371
	if record['Reach'] <= 127:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 372
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 373
	if record['HairLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 374
	if record['Reach'] <= 95:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 375
	if record['TailLn'] > 18:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 376
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 377
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 378
	if record['Ht'] <= 113:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 379
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 380
	if record['Age'] > 48:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 381
	if record['Reach'] > 168:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 382
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 383
	if record['Reach'] > 214:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 384
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 385
	if record['EarLobes'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 386
	if record['BangLn'] <= 4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 387
	if record['Ht'] <= 110:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 388
	if record['Age'] > 34:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 389
	if record['Ht'] > 197:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 390
	if record['Reach'] > 227:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 391
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 392
	if record['Ht'] <= 127:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 393
	if record['Ht'] > 188:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 394
	if record['Ht'] <= 134:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 395
	if record['Reach'] <= 101:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 396
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 397
	if record['Ht'] > 172:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 398
	if record['Reach'] > 231:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 399
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 400
	if record['TailLn'] <= 23:
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