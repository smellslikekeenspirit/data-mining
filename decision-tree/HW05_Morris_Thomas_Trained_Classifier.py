"""
Author: Thomas Morris | tcm1998
Written 2022-05-02
"""

import numpy as np
import os.path
import sys
from matplotlib import pyplot as plt
import pandas
from math import floor

AGE_BIN_SIZE = 2
HEIGHT_BIN_SIZE = 4


def read_data_file(data_file_name):
	"""Given a file name, locate, open, and read the file. The file is assumed
	to be a CSV file and its data will be parsed accordingly and returned as a
	pandas dataframe.

	:param: data_file_name - <str> name of CSV file to read data from
	:return: <Pandas.DataFrame> all data read from data_file_name
	"""
	# Assume the data file is in the current working directory.
	cwd = os.getcwd()
	data_file_path = os.path.join(os.getcwd(), data_file_name)

	# If it isn't present, check the parent folder.
	if not os.path.exists(data_file_path):
		super_folder = os.path.dirname(cwd)
		data_file_path = os.path.join(super_folder, data_file_name)

		# If it still can't be found, exit.
		if not os.path.exists(data_file_path):
			sys.exit("Provided data file could not be found.")

	# We have found the file and can extract the data.
	data = pandas.read_csv(data_file_path, delimiter=',')

	# Round TailLn, HairLn, BangLn, Reach
	clean_data = data[['TailLn', 'HairLn', 'BangLn', 'Reach']].round(decimals=0)

	# Quantize the age by their respective bin sizes and save the new columns
	# Into the clean data frame.
	clean_data['Age'] = data['Age'].apply(lambda x: floor(x / AGE_BIN_SIZE) * AGE_BIN_SIZE)
	clean_data['Ht'] = data['Ht'].apply(lambda x: floor(x / HEIGHT_BIN_SIZE) * HEIGHT_BIN_SIZE)
	clean_data['TailLn'] = data['TailLn'].apply(lambda x: floor(x / HEIGHT_BIN_SIZE) * HEIGHT_BIN_SIZE)
	clean_data['HairLn'] = data['HairLn'].apply(lambda x: floor(x / HEIGHT_BIN_SIZE) * HEIGHT_BIN_SIZE)
	clean_data['BangLn'] = data['BangLn'].apply(lambda x: floor(x / HEIGHT_BIN_SIZE) * HEIGHT_BIN_SIZE)
	clean_data['Reach'] = data['Reach'].apply(lambda x: floor(x / HEIGHT_BIN_SIZE) * HEIGHT_BIN_SIZE)
	clean_data['ClassID'] = data['ClassID']

	# Cast everything to integer.
	return clean_data.astype(int)


def main(data_file_name):
	"""Read the data from the provided file then attempt to classify it using
	a decision tree. Each decision node makes a binary split on an integer threshold.

	:param data_file_name: <str> Name of the CSV file of CDC data to
	make predictions for.
	:return: None
	"""
	testing_data = read_data_file(data_file_name)

	for row in testing_data.itertuples(index=False):
		if row.HairLn >= 9:
			if row.BangLn >= 3:
				if row.BangLn >= 5:
					if row.Reach >= 117:
						if row.Age >= 57:
							if row.Reach >= 141:
								if row.Ht >= 169:
									print(row.ClassID, '+1')
								else:
									if row.TailLn >= 7:
										if row.Ht >= 141:
											if row.Reach >= 149:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
										else:
											print(row.ClassID, '+1')
									else:
										print(row.ClassID, '+1')
							else:
								print(row.ClassID, '+1')
						else:
							print(row.ClassID, '+1')
					else:
						print(row.ClassID, '-1')
				else:
					if row.TailLn >= 7:
						if row.Reach >= 133:
							if row.HairLn >= 11:
								print(row.ClassID, '+1')
							else:
								if row.Age >= 47:
									if row.Reach >= 139:
										if row.Ht >= 153:
											if row.TailLn >= 19:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
										else:
											if row.Reach >= 149:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
									else:
										print(row.ClassID, '-1')
								else:
									if row.Ht >= 145:
										if row.Reach >= 151:
											if row.Ht >= 149:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
										else:
											print(row.ClassID, '-1')
									else:
										if row.TailLn >= 11:
											if row.Reach >= 139:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
										else:
											print(row.ClassID, '+1')
						else:
							if row.Age >= 35:
								print(row.ClassID, '-1')
							else:
								print(row.ClassID, '+1')
					else:
						if row.Age >= 65:
							print(row.ClassID, '-1')
						else:
							if row.Ht >= 149:
								if row.Reach >= 155:
									if row.Age >= 21:
										if row.Age >= 53:
											print(row.ClassID, '+1')
										else:
											if row.Age >= 51:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
									else:
										print(row.ClassID, '-1')
								else:
									print(row.ClassID, '-1')
							else:
								print(row.ClassID, '+1')
			else:
				if row.HairLn >= 11:
					print(row.ClassID, '+1')
				else:
					if row.TailLn >= 17:
						if row.Reach >= 155:
							print(row.ClassID, '+1')
						else:
							print(row.ClassID, '+1')
					else:
						if row.TailLn >= 1:
							if row.Age >= 35:
								if row.Age >= 51:
									if row.Reach >= 149:
										print(row.ClassID, '-1')
									else:
										print(row.ClassID, '-1')
								else:
									if row.Ht >= 137:
										if row.Age >= 41:
											if row.TailLn >= 11:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '+1')
										else:
											print(row.ClassID, '-1')
									else:
										print(row.ClassID, '+1')
							else:
								print(row.ClassID, '-1')
						else:
							print(row.ClassID, '+1')
		else:
			if row.BangLn >= 5:
				if row.TailLn >= 7:
					if row.HairLn >= 7:
						if row.Age >= 51:
							if row.Reach >= 141:
								if row.BangLn >= 7:
									print(row.ClassID, '+1')
								else:
									if row.Reach >= 163:
										if row.Reach >= 171:
											print(row.ClassID, '-1')
										else:
											print(row.ClassID, '+1')
									else:
										if row.TailLn >= 19:
											print(row.ClassID, '+1')
										else:
											if row.Ht >= 137:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '+1')
							else:
								print(row.ClassID, '-1')
						else:
							if row.Ht >= 153:
								if row.Reach >= 159:
									if row.Ht >= 161:
										if row.Reach >= 169:
											print(row.ClassID, '+1')
										else:
											print(row.ClassID, '-1')
									else:
										if row.Reach >= 163:
											print(row.ClassID, '+1')
										else:
											if row.TailLn >= 15:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
								else:
									print(row.ClassID, '-1')
							else:
								if row.Reach >= 135:
									if row.TailLn >= 15:
										if row.Reach >= 143:
											if row.Age >= 47:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '+1')
										else:
											print(row.ClassID, '+1')
									else:
										if row.TailLn >= 9:
											if row.Reach >= 139:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
										else:
											if row.Ht >= 137:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
								else:
									if row.Age >= 39:
										if row.Age >= 49:
											print(row.ClassID, '+1')
										else:
											print(row.ClassID, '-1')
									else:
										if row.Reach >= 133:
											print(row.ClassID, '-1')
										else:
											if row.TailLn >= 9:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
					else:
						if row.BangLn >= 7:
							print(row.ClassID, '+1')
						else:
							if row.Age >= 45:
								if row.Reach >= 149:
									if row.Ht >= 145:
										if row.HairLn >= 5:
											if row.Reach >= 153:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
										else:
											print(row.ClassID, '-1')
									else:
										print(row.ClassID, '+1')
								else:
									if row.Age >= 49:
										print(row.ClassID, '-1')
									else:
										if row.Ht >= 137:
											print(row.ClassID, '-1')
										else:
											if row.Reach >= 141:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
							else:
								if row.Ht >= 157:
									if row.Age >= 43:
										print(row.ClassID, '+1')
									else:
										print(row.ClassID, '-1')
								else:
									if row.Reach >= 147:
										if row.Age >= 39:
											if row.TailLn >= 15:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
										else:
											if row.Ht >= 145:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '+1')
									else:
										if row.Ht >= 137:
											if row.Reach >= 145:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '-1')
										else:
											if row.Age >= 39:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '+1')
				else:
					if row.Ht >= 133:
						if row.HairLn >= 7:
							if row.Reach >= 139:
								if row.TailLn >= 1:
									if row.Age >= 59:
										if row.TailLn >= 3:
											if row.Reach >= 165:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
										else:
											print(row.ClassID, '+1')
									else:
										if row.Reach >= 173:
											print(row.ClassID, '-1')
										else:
											if row.Age >= 35:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
								else:
									if row.Ht >= 161:
										print(row.ClassID, '+1')
									else:
										print(row.ClassID, '+1')
							else:
								print(row.ClassID, '-1')
						else:
							if row.TailLn >= 3:
								if row.Age >= 49:
									if row.Reach >= 153:
										print(row.ClassID, '+1')
									else:
										if row.Age >= 61:
											print(row.ClassID, '+1')
										else:
											print(row.ClassID, '-1')
								else:
									if row.Reach >= 159:
										print(row.ClassID, '-1')
									else:
										if row.Reach >= 149:
											if row.Reach >= 153:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
										else:
											if row.Age >= 39:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '+1')
							else:
								if row.Age >= 39:
									if row.Age >= 53:
										print(row.ClassID, '+1')
									else:
										print(row.ClassID, '+1')
								else:
									if row.Reach >= 149:
										print(row.ClassID, '+1')
									else:
										print(row.ClassID, '+1')
					else:
						print(row.ClassID, '+1')
			else:
				if row.TailLn >= 7:
					if row.Age >= 45:
						if row.Reach >= 147:
							if row.HairLn >= 7:
								if row.BangLn >= 3:
									if row.Reach >= 167:
										if row.TailLn >= 15:
											print(row.ClassID, '+1')
										else:
											if row.Age >= 51:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
									else:
										if row.Ht >= 153:
											if row.Age >= 65:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
										else:
											if row.Reach >= 159:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
								else:
									print(row.ClassID, '-1')
							else:
								if row.Reach >= 161:
									if row.Ht >= 157:
										if row.Age >= 59:
											if row.TailLn >= 13:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '+1')
										else:
											if row.Reach >= 165:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '-1')
									else:
										print(row.ClassID, '+1')
								else:
									if row.Ht >= 145:
										print(row.ClassID, '-1')
									else:
										if row.Age >= 71:
											print(row.ClassID, '+1')
										else:
											if row.Age >= 55:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '-1')
						else:
							print(row.ClassID, '-1')
					else:
						if row.Ht >= 149:
							if row.Ht >= 157:
								if row.HairLn >= 7:
									if row.Reach >= 163:
										if row.Ht >= 161:
											if row.TailLn >= 17:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '-1')
										else:
											if row.Age >= 43:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
									else:
										print(row.ClassID, '-1')
								else:
									print(row.ClassID, '-1')
							else:
								if row.Reach >= 161:
									if row.HairLn >= 7:
										if row.TailLn >= 15:
											print(row.ClassID, '-1')
										else:
											if row.TailLn >= 9:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
									else:
										print(row.ClassID, '-1')
								else:
									if row.Reach >= 157:
										if row.Ht >= 153:
											if row.Age >= 43:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '-1')
										else:
											if row.Reach >= 159:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
									else:
										if row.TailLn >= 21:
											print(row.ClassID, '+1')
										else:
											if row.Age >= 35:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '-1')
						else:
							if row.TailLn >= 9:
								if row.Reach >= 137:
									if row.Ht >= 137:
										if row.Reach >= 155:
											print(row.ClassID, '+1')
										else:
											if row.Reach >= 143:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '-1')
									else:
										if row.Reach >= 141:
											if row.HairLn >= 5:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
										else:
											if row.Ht >= 133:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '+1')
								else:
									if row.Ht >= 113:
										print(row.ClassID, '-1')
									else:
										print(row.ClassID, '+1')
							else:
								if row.Reach >= 153:
									print(row.ClassID, '+1')
								else:
									if row.Ht >= 129:
										if row.Reach >= 139:
											if row.Ht >= 145:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '+1')
										else:
											print(row.ClassID, '-1')
									else:
										if row.Reach >= 131:
											if row.Reach >= 135:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
										else:
											print(row.ClassID, '-1')
				else:
					if row.Ht >= 133:
						if row.TailLn >= 3:
							if row.HairLn >= 7:
								if row.TailLn >= 5:
									if row.Age >= 53:
										if row.Age >= 57:
											print(row.ClassID, '-1')
										else:
											if row.Reach >= 153:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
									else:
										if row.Ht >= 157:
											print(row.ClassID, '-1')
										else:
											if row.BangLn >= 3:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
								else:
									if row.Reach >= 141:
										if row.Age >= 25:
											if row.Ht >= 165:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '+1')
										else:
											print(row.ClassID, '-1')
									else:
										print(row.ClassID, '-1')
							else:
								if row.Reach >= 153:
									if row.Ht >= 149:
										if row.Ht >= 153:
											if row.Age >= 39:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '-1')
										else:
											if row.Reach >= 155:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
									else:
										print(row.ClassID, '+1')
								else:
									if row.Age >= 39:
										if row.HairLn >= 5:
											if row.TailLn >= 5:
												print(row.ClassID, '-1')
											else:
												print(row.ClassID, '-1')
										else:
											if row.Reach >= 149:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
									else:
										if row.Ht >= 145:
											print(row.ClassID, '-1')
										else:
											if row.Reach >= 149:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
						else:
							if row.Ht >= 153:
								if row.Age >= 51:
									if row.Reach >= 165:
										print(row.ClassID, '+1')
									else:
										print(row.ClassID, '-1')
								else:
									if row.Ht >= 157:
										print(row.ClassID, '-1')
									else:
										print(row.ClassID, '-1')
							else:
								if row.TailLn >= 1:
									if row.BangLn >= 3:
										if row.Age >= 63:
											print(row.ClassID, '-1')
										else:
											if row.Age >= 35:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '-1')
									else:
										print(row.ClassID, '-1')
								else:
									if row.Reach >= 139:
										if row.Age >= 49:
											if row.Reach >= 153:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
										else:
											if row.Reach >= 147:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
									else:
										print(row.ClassID, '-1')
					else:
						if row.BangLn >= 3:
							if row.Age >= 45:
								if row.HairLn >= 5:
									if row.Reach >= 129:
										if row.Age >= 53:
											print(row.ClassID, '+1')
										else:
											if row.Ht >= 125:
												print(row.ClassID, '+1')
											else:
												print(row.ClassID, '+1')
									else:
										print(row.ClassID, '-1')
								else:
									print(row.ClassID, '-1')
							else:
								print(row.ClassID, '+1')
						else:
							print(row.ClassID, '-1')
		

if __name__ == "__main__":
	main(sys.argv[1])

