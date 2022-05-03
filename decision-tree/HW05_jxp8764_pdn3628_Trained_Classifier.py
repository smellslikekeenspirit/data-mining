import math
import os
import pandas
import sys

STANDARD_BIN = 2
HEIGHT_BIN = 4


def read_data_file(data_file_name):
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
	for index, row in data.iterrows():
		classification.append(row['ClassID'])
	return clean_data.astype(int), classification


def classify():
	data, labels = read_data_file('Abominable_Data_HW_LABELED_TRAINING_DATA__v750_2215.csv')
	# classifies the unlabled data
	classification = []
	class_id = 0
	for index, record in data.iterrows():
		if record['EarLobes'] <= 0:
			if record['BangLn'] <= 4:
				if record['HairLn'] <= 8:
					if record['Ht'] <= 136:
						if record['Age'] <= 42:
							if record['TailLn'] <= 6:
								if record['Ht'] <= 132:
									if record['BangLn'] <= 2:
											class_id = -1
									else:
										if record['HairLn'] <= 6:
												class_id = 1
										else:
												class_id = 1
								else:
									if record['HairLn'] <= 6:
											class_id = -1
									else:
											class_id = -1
							else:
								if record['Reach'] <= 134:
										class_id = -1
								else:
									if record['Reach'] <= 140:
										if record['Age'] <= 38:
											if record['HairLn'] <= 6:
													class_id = -1
											else:
												if record['TailLn'] <= 10:
														class_id = -1
												else:
														class_id = -1
										else:
											if record['TailLn'] <= 8:
													class_id = -1
											else:
												if record['HairLn'] <= 4:
														class_id = -1
												else:
														class_id = -1
									else:
										if record['TailLn'] <= 12:
											if record['Ht'] <= 132:
													class_id = 1
											else:
													class_id = -1
										else:
												class_id = 1
						else:
								class_id = -1
					else:
							class_id = -1
				else:
					if record['Ht'] <= 136:
						if record['Age'] <= 46:
							if record['TailLn'] <= 8:
								if record['Ht'] <= 132:
										class_id = 1
								else:
										class_id = -1
							else:
								if record['Reach'] <= 138:
									if record['Age'] <= 26:
											class_id = 1
									else:
											class_id = -1
								else:
									if record['TailLn'] <= 12:
											class_id = -1
									else:
											class_id = 1
						else:
							if record['Reach'] <= 140:
								if record['TailLn'] <= 4:
										class_id = 1
								else:
										class_id = -1
							else:
									class_id = 1
					else:
						if record['TailLn'] <= 12:
								class_id = -1
						else:
							if record['BangLn'] <= 2:
									class_id = -1
							else:
								if record['Reach'] <= 146:
										class_id = -1
								else:
									if record['Reach'] <= 162:
										if record['TailLn'] <= 14:
											if record['Age'] <= 38:
													class_id = 1
											else:
													class_id = -1
										else:
											if record['Age'] <= 56:
												if record['Reach'] <= 156:
														class_id = 1
												else:
														class_id = -1
											else:
													class_id = 1
									else:
											class_id = 1
			else:
				if record['HairLn'] <= 8:
					if record['TailLn'] <= 6:
						if record['Ht'] <= 132:
							if record['Age'] <= 54:
									class_id = 1
							else:
									class_id = -1
						else:
							if record['TailLn'] <= 0:
								if record['HairLn'] <= 6:
										class_id = -1
								else:
									if record['Reach'] <= 164:
											class_id = 1
									else:
											class_id = -1
							else:
								if record['Age'] <= 56:
									if record['Ht'] <= 156:
										if record['BangLn'] <= 6:
											if record['Reach'] <= 160:
												if record['Age'] <= 18:
														class_id = 1
												else:
														class_id = -1
											else:
													class_id = 1
										else:
												class_id = 1
									else:
											class_id = -1
								else:
										class_id = -1
					else:
						if record['BangLn'] <= 6:
							if record['TailLn'] <= 18:
								if record['Age'] <= 46:
									if record['Ht'] <= 136:
										if record['TailLn'] <= 8:
											if record['HairLn'] <= 6:
													class_id = -1
											else:
													class_id = 1
										else:
											if record['Reach'] <= 142:
												if record['Age'] <= 44:
														class_id = -1
												else:
														class_id = -1
											else:
													class_id = 1
									else:
										if record['Age'] <= 38:
											if record['TailLn'] <= 12:
													class_id = -1
											else:
												if record['HairLn'] <= 6:
														class_id = -1
												else:
														class_id = -1
										else:
											if record['Reach'] <= 148:
												if record['HairLn'] <= 6:
														class_id = -1
												else:
														class_id = -1
											else:
												if record['Ht'] <= 144:
														class_id = 1
												else:
														class_id = -1
								else:
									if record['Age'] <= 72:
										if record['Reach'] <= 138:
												class_id = -1
										else:
											if record['TailLn'] <= 10:
												if record['TailLn'] <= 8:
														class_id = -1
												else:
														class_id = -1
											else:
												if record['Reach'] <= 172:
														class_id = -1
												else:
														class_id = -1
									else:
											class_id = 1
							else:
								if record['Age'] <= 40:
										class_id = -1
								else:
									if record['Reach'] <= 138:
											class_id = -1
									else:
										if record['Ht'] <= 156:
											if record['TailLn'] <= 20:
													class_id = 1
											else:
													class_id = 1
										else:
												class_id = -1
						else:
								class_id = 1
				else:
					if record['Ht'] <= 152:
						if record['Age'] <= 34:
								class_id = 1
						else:
							if record['TailLn'] <= 2:
									class_id = 1
							else:
								if record['Age'] <= 56:
									if record['HairLn'] <= 10:
										if record['TailLn'] <= 14:
											if record['Reach'] <= 154:
												if record['Ht'] <= 148:
														class_id = 1
												else:
														class_id = -1
											else:
													class_id = 1
										else:
												class_id = 1
									else:
										if record['Reach'] <= 152:
												class_id = 1
										else:
												class_id = 1
								else:
									if record['Age'] <= 60:
											class_id = -1
									else:
											class_id = 1
					else:
						if record['Reach'] <= 162:
								class_id = -1
						else:
								class_id = 1
		else:
			if record['HairLn'] <= 8:
				if record['TailLn'] <= 8:
					if record['BangLn'] <= 2:
						if record['Age'] <= 48:
							if record['HairLn'] <= 6:
								if record['TailLn'] <= 2:
										class_id = 1
								else:
									if record['TailLn'] <= 4:
											class_id = -1
									else:
											class_id = -1
							else:
								if record['Reach'] <= 164:
									if record['Reach'] <= 140:
											class_id = 1
									else:
											class_id = 1
								else:
										class_id = -1
						else:
								class_id = -1
					else:
						if record['Reach'] <= 138:
							if record['Age'] <= 44:
									class_id = 1
							else:
								if record['TailLn'] <= 4:
									if record['Reach'] <= 136:
											class_id = 1
									else:
											class_id = 1
								else:
									if record['Age'] <= 50:
										if record['HairLn'] <= 4:
												class_id = -1
										else:
											if record['Age'] <= 46:
													class_id = 1
											else:
													class_id = 1
									else:
										if record['TailLn'] <= 6:
											if record['Ht'] <= 132:
													class_id = 1
											else:
													class_id = -1
										else:
												class_id = -1
						else:
								class_id = 1
				else:
					if record['Reach'] <= 136:
						if record['Age'] <= 46:
							if record['Ht'] <= 128:
								if record['BangLn'] <= 4:
									if record['HairLn'] <= 6:
											class_id = -1
									else:
										if record['TailLn'] <= 10:
												class_id = -1
										else:
												class_id = 1
								else:
										class_id = 1
							else:
									class_id = -1
						else:
								class_id = -1
					else:
						if record['TailLn'] <= 12:
							if record['BangLn'] <= 2:
								if record['HairLn'] <= 4:
										class_id = -1
								else:
									if record['Age'] <= 48:
										if record['Reach'] <= 140:
												class_id = -1
										else:
											if record['Age'] <= 16:
													class_id = -1
											else:
												if record['Age'] <= 36:
														class_id = 1
												else:
														class_id = 1
									else:
											class_id = -1
							else:
								if record['Reach'] <= 140:
									if record['Age'] <= 46:
										if record['Ht'] <= 132:
												class_id = 1
										else:
											if record['Reach'] <= 138:
													class_id = -1
											else:
												if record['BangLn'] <= 4:
														class_id = 1
												else:
														class_id = 1
									else:
											class_id = -1
								else:
									if record['Age'] <= 28:
										if record['Reach'] <= 166:
											if record['Reach'] <= 152:
												if record['Reach'] <= 150:
														class_id = 1
												else:
														class_id = -1
											else:
													class_id = 1
										else:
												class_id = -1
									else:
											class_id = 1
						else:
							if record['BangLn'] <= 4:
								if record['Age'] <= 50:
									if record['Age'] <= 22:
											class_id = -1
									else:
										if record['Reach'] <= 140:
											if record['HairLn'] <= 4:
													class_id = 1
											else:
												if record['Age'] <= 44:
														class_id = -1
												else:
														class_id = -1
										else:
											if record['Ht'] <= 136:
												if record['Age'] <= 44:
														class_id = 1
												else:
														class_id = 1
											else:
												if record['Ht'] <= 156:
														class_id = 1
												else:
														class_id = -1
								else:
									if record['Reach'] <= 152:
										if record['Reach'] <= 142:
												class_id = -1
										else:
											if record['Age'] <= 52:
													class_id = 1
											else:
												if record['BangLn'] <= 2:
														class_id = -1
												else:
														class_id = -1
									else:
										if record['HairLn'] <= 6:
												class_id = -1
										else:
											if record['TailLn'] <= 16:
												if record['Age'] <= 52:
														class_id = 1
												else:
														class_id = 1
											else:
													class_id = -1
							else:
								if record['TailLn'] <= 16:
									if record['Reach'] <= 138:
											class_id = -1
									else:
										if record['HairLn'] <= 4:
												class_id = -1
										else:
											if record['Reach'] <= 140:
													class_id = 1
											else:
												if record['Age'] <= 38:
														class_id = 1
												else:
														class_id = 1
								else:
									if record['Age'] <= 54:
										if record['Reach'] <= 158:
											if record['Ht'] <= 152:
												if record['Reach'] <= 148:
														class_id = 1
												else:
														class_id = 1
											else:
													class_id = -1
										else:
												class_id = 1
									else:
										if record['TailLn'] <= 18:
												class_id = -1
										else:
												class_id = 1
			else:
					class_id = 1
		classification.append(class_id)
		# Print out here for the grader
		print(class_id)

	# writes out the classifications to a csv
	file_pointer = open('HW05_jxp8764_pdn3628_MyClassifications.csv', 'w')
	for class_type in classification:
		file_pointer.write('%s\n' % class_type)
	file_pointer.close()


if __name__ == '__main__':
	classify()
