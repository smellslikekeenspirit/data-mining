import math
import os
import pandas
import sys

STANDARD_BIN = 2
HEIGHT_BIN = 4


def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record['Ht'] <= 109:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record['EarLobes'] > 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record['EarLobes'] > 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 5
	if record['Age'] > 53:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 6
	if record['Ht'] > 142:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 7
	if record['HairLn'] > 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 8
	if record['Reach'] <= 139:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 9
	if record['Ht'] <= 115:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 10
	if record['Age'] > 42:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 11
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 12
	if record['HairLn'] <= 11:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 13
	if record['EarLobes'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 14
	if record['EarLobes'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 15
	if record['BangLn'] <= 7:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 16
	if record['Reach'] <= 104:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 17
	if record['Age'] > 38:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 18
	if record['Age'] > 66:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 19
	if record['EarLobes'] > 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 20
	if record['Age'] > 19:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 21
	if record['Ht'] <= 135:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 22
	if record['Age'] > 52:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 23
	if record['EarLobes'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 24
	if record['TailLn'] > 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 25
	if record['Reach'] <= 121:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 26
	if record['HairLn'] <= 10:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 27
	if record['Ht'] > 198:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 28
	if record['Ht'] <= 99:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 29
	if record['Reach'] > 195:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 30
	if record['Ht'] > 204:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 31
	if record['BangLn'] <= 6:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 32
	if record['EarLobes'] <= 1:
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
	if record['TailLn'] > 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 36
	if record['Age'] > 79:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 37
	if record['Ht'] <= 98:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 38
	if record['Age'] > 13:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 39
	if record['Reach'] <= 101:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 40
	if record['EarLobes'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 41
	if record['Age'] > 22:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 42
	if record['Ht'] > 203:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 43
	if record['HairLn'] > 16:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 44
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 45
	if record['Ht'] > 168:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 46
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 47
	if record['Age'] > 52:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 48
	if record['Ht'] > 180:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 49
	if record['Ht'] > 182:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 50
	if record['HairLn'] <= 2:
		answer = answer - 1
	else:
		answer = answer + 1

	if answer < 0:
		return -1
	else:
		return 1


if __name__ == '__main__':
	# reads in the data
	data_file_name = 'Abominable_VALIDATION_Data_FOR_STUDENTS_v770_2215.csv'
	data_file_path = os.path.join(os.getcwd(), data_file_name)
	data = pandas.read_csv(data_file_path, delimiter=',')
	clean_data = data[['TailLn', 'HairLn', 'BangLn', 'Reach', 'EarLobes', 'Age']].round(decimals=0)
	classification = []
	# quantize the data
	clean_data['Age'] = data['Age'].apply(
		lambda x: math.floor(x / STANDARD_BIN) * STANDARD_BIN)
	clean_data['TailLn'] = data['TailLn'].apply(
		lambda x: math.floor(x / STANDARD_BIN) * STANDARD_BIN)
	clean_data['HairLn'] = data['HairLn'].apply(
		lambda x: math.floor(x / STANDARD_BIN) * STANDARD_BIN)
	clean_data['BangLn'] = data['BangLn'].apply(
		lambda x: math.floor(x / STANDARD_BIN) * STANDARD_BIN)
	clean_data['Reach'] = data['Reach'].apply(
		lambda x: math.floor(x / STANDARD_BIN) * STANDARD_BIN)
	clean_data['EarLobes'] = data['EarLobes'].apply(
		lambda x: math.ceil(x / STANDARD_BIN) * STANDARD_BIN)
	clean_data['Ht'] = data['Ht'].apply(
		lambda x: math.floor(x / HEIGHT_BIN) * HEIGHT_BIN)

	# Writes and prints out the classification results
	file = open('HW_09_jxp8764_pdn3628_Classification.csv', 'w')
	for index, record in clean_data.iterrows():
		class_id = classifier(record)
		print(class_id)
		file.write('%s\n' % class_id)
	file.close()
