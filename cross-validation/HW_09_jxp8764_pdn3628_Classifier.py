import math
import os
import pandas
import sys

STANDARD_BIN = 2
HEIGHT_BIN = 4


def classifier(record):
	answer = 0

	# Decision Stump Number 1
	if record['Age'] > 27:
		answer = answer - 1
	else:
		answer = answer + 1

	if answer < 0:
		return -1
	else:
		return 1


if __name__ == '__main__':
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

	file = open('HW_09_jxp8764_pdn3628_Classification.csv', 'w')
	for index, record in clean_data.iterrows():
		class_id = classifier(record)
		print(class_id)
		file.write('%s\n' % class_id)
	file.close()
