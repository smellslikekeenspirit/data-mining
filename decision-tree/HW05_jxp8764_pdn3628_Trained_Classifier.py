import math
import os
import pandas
import sys

AGE_BIN = 2
HEIGHT_BIN = 4
def read_data_file(data_file_name):
	data_file_path = os.path.join(os.getcwd(), data_file_name)
	data = pandas.read_csv(data_file_path, delimiter=',')
	clean_data = data[['TailLn', 'HairLn', 'BangLn', 'Reach']].round(decimals=0)
	classification = []
	clean_data['Age'] = data['Age'].apply(
		lambda x: math.floor(x / AGE_BIN) * AGE_BIN)
	clean_data['TailLn'] = data['TailLn'].apply(
		lambda x: math.floor(x / AGE_BIN) * AGE_BIN)
	clean_data['HairLn'] = data['HairLn'].apply(
		lambda x: math.floor(x / AGE_BIN) * AGE_BIN)
	clean_data['BangLn'] = data['BangLn'].apply(
		lambda x: math.floor(x / AGE_BIN) * AGE_BIN)
	clean_data['Reach'] = data['Reach'].apply(
		lambda x: math.floor(x / AGE_BIN) * AGE_BIN)
	clean_data['EarLobes'] = data['EarLobes'].apply(
		lambda x: math.floor(x / AGE_BIN) * AGE_BIN)
	clean_data['Ht'] = data['Ht'].apply(
		lambda x: math.floor(x / HEIGHT_BIN) * HEIGHT_BIN)
	for index, row in data.iterrows():
		classification.append(row['ClassID'])
	return clean_data.astype(int), classification


def classify(filename):
	data, labels = read_data_file('Abominable_Data_HW_LABELED_TRAINING_DATA__v750_2215.csv')
	# classifies the unlabled data
	classification = []
	class_id = 0
	for index, record in data.iterrows():
		if record['Age'] <= 40:
				class_id = 1
		else:
			if record['BangLn'] <= 4:
				if record['HairLn'] <= 8:
						class_id = -1
				else:
						class_id = 1
			else:
					class_id = 1
		classification.append(class_id)
		# Print out here for the grader
		print(class_id)

	# writes out the classifications to a csv
	fp = open('HW05_jxp8764_pdn3628_MyClassifications.csv', 'w')
	for class_type in classification:
		fp.write('%s\n' % class_type)
	fp.close()


if __name__ == '__main__':
	classify(sys.argv[1])
