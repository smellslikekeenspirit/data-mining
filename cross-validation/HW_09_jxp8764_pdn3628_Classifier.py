import math
import os
import pandas
import sys

STANDARD_BIN = 2
HEIGHT_BIN = 4


def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 2
	if record['Age'] > 48:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 3
	if record['Reach'] > 209:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 4
	if record['EarLobes'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 5
	if record['BangLn'] <= 1:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 6
	if record['TailLn'] <= 26:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 7
	if record['HairLn'] <= 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 8
	if record['Age'] > 63:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 9
	if record['TailLn'] <= 29:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 10
	if record['BangLn'] <= 5:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 11
	if record['EarLobes'] <= 0:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 12
	if record['TailLn'] > -4:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 13
	if record['HairLn'] <= 12:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 14
	if record['Reach'] <= 136:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 15
	if record['BangLn'] <= 3:
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
	if record['Ht'] > 164:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 19
	if record['EarLobes'] > 2:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 20
	if record['TailLn'] <= 27:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 21
	if record['BangLn'] > 8:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 22
	if record['Age'] > 74:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 23
	if record['Ht'] > 229:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 24
	if record['Reach'] > 224:
		answer = answer - 1
	else:
		answer = answer + 1

	# Decision Stump Number 25
	if record['TailLn'] > 30:
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
