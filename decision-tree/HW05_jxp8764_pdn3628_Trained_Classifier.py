if __name__ == '__main__':
	data = []

	#reads in the unlabeled data from the csv
	with open('Abominable_VALIDATION_Data_FOR_STUDENTS_v750_2215.csv', 'r') as file:
		file.readline()
		for line in file:
			values = []
			row = line.strip().split(",")
			for index in range(len(row)):
				val = float(row[index])
				if index == 1:
					val = int(round(val / 4.0) * 4)
				elif index == 6:
					val = int(round(val / 2.0, 1) * 4)
				else:
					val = int(round(val / 2.0) * 2)
				values.append(val)
			data.append(values)

	# classifies the unlabled data
	classification = []
	class_id = 0
	for record in data:
		if record[6] <= 0:
			if record[4] <= 6:
				if record[3] <= 10:
					if record[1] <= 136:
						if record[2] <= 6:
							if record[1] <= 132:
									class_id = 1
							else:
								if record[5] <= 140:
									if record[0] <= 46:
											class_id = -1
									else:
										if record[0] <= 56:
												class_id = 1
										else:
												class_id = -1
								else:
										class_id = 1
						else:
							if record[5] <= 140:
								if record[0] <= 40:
									if record[4] <= 4:
										if record[5] <= 138:
												class_id = -1
										else:
											if record[0] <= 36:
													class_id = -1
											else:
													class_id = -1
									else:
										if record[2] <= 10:
											if record[1] <= 132:
												if record[5] <= 126:
														class_id = -1
												else:
														class_id = 1
											else:
												if record[0] <= 34:
														class_id = -1
												else:
														class_id = -1
										else:
											if record[5] <= 134:
													class_id = -1
											else:
												if record[0] <= 30:
														class_id = 1
												else:
														class_id = -1
								else:
										class_id = -1
							else:
								if record[4] <= 4:
									if record[2] <= 12:
											class_id = 1
									else:
											class_id = 1
								else:
										class_id = 1
					else:
						if record[3] <= 8:
								class_id = -1
						else:
							if record[4] <= 4:
									class_id = -1
							else:
								if record[2] <= 14:
									if record[0] <= 54:
										if record[1] <= 144:
											if record[5] <= 144:
												if record[0] <= 30:
														class_id = 1
												else:
														class_id = -1
											else:
												if record[1] <= 140:
														class_id = 1
												else:
														class_id = -1
										else:
											if record[5] <= 152:
													class_id = -1
											else:
												if record[2] <= 12:
														class_id = -1
												else:
														class_id = -1
									else:
											class_id = -1
								else:
									if record[0] <= 56:
										if record[5] <= 142:
												class_id = 1
										else:
											if record[5] <= 146:
												if record[0] <= 28:
														class_id = 1
												else:
														class_id = -1
											else:
												if record[0] <= 44:
														class_id = -1
												else:
														class_id = 1
									else:
											class_id = -1
				else:
					if record[0] <= 46:
						if record[1] <= 140:
							if record[5] <= 124:
									class_id = -1
							else:
								if record[5] <= 132:
										class_id = 1
								else:
										class_id = 1
						else:
							if record[2] <= 14:
								if record[2] <= 6:
										class_id = 1
								else:
										class_id = -1
							else:
								if record[0] <= 42:
										class_id = 1
								else:
										class_id = 1
					else:
						if record[4] <= 4:
							if record[2] <= 16:
									class_id = -1
							else:
									class_id = -1
						else:
							if record[0] <= 68:
								if record[5] <= 136:
										class_id = -1
								else:
									if record[1] <= 132:
											class_id = 1
									else:
										if record[2] <= 14:
											if record[1] <= 148:
													class_id = -1
											else:
													class_id = -1
										else:
												class_id = 1
							else:
									class_id = -1
			else:
				if record[3] <= 6:
					if record[2] <= 6:
							class_id = 1
					else:
						if record[0] <= 52:
							if record[1] <= 136:
									class_id = -1
							else:
									class_id = -1
						else:
								class_id = 1
				else:
					if record[3] <= 10:
						if record[0] <= 52:
							if record[1] <= 132:
									class_id = 1
							else:
								if record[0] <= 44:
									if record[1] <= 148:
										if record[0] <= 30:
												class_id = 1
										else:
											if record[5] <= 150:
												if record[0] <= 38:
														class_id = -1
												else:
														class_id = 1
											else:
													class_id = 1
									else:
										if record[3] <= 8:
												class_id = -1
										else:
												class_id = 1
								else:
									if record[2] <= 10:
											class_id = 1
									else:
										if record[1] <= 152:
												class_id = 1
										else:
												class_id = -1
						else:
							if record[0] <= 64:
								if record[1] <= 136:
										class_id = 1
								else:
										class_id = -1
							else:
									class_id = 1
					else:
						if record[5] <= 138:
								class_id = 1
						else:
								class_id = 1
		else:
			if record[3] <= 8:
				if record[4] <= 4:
					if record[2] <= 14:
						if record[5] <= 138:
							if record[0] <= 46:
								if record[2] <= 8:
									if record[1] <= 132:
											class_id = 1
									else:
											class_id = -1
								else:
									if record[0] <= 30:
											class_id = 1
									else:
										if record[1] <= 132:
												class_id = -1
										else:
												class_id = 1
							else:
								if record[2] <= 6:
										class_id = -1
								else:
										class_id = -1
						else:
							if record[4] <= 2:
									class_id = -1
							else:
								if record[0] <= 22:
										class_id = -1
								else:
									if record[5] <= 142:
										if record[0] <= 52:
											if record[2] <= 4:
													class_id = 1
											else:
												if record[1] <= 136:
														class_id = 1
												else:
														class_id = -1
										else:
												class_id = -1
									else:
										if record[3] <= 6:
											if record[1] <= 156:
												if record[0] <= 46:
														class_id = 1
												else:
														class_id = 1
											else:
													class_id = -1
										else:
											if record[0] <= 50:
												if record[1] <= 144:
														class_id = 1
												else:
														class_id = 1
											else:
													class_id = 1
					else:
						if record[0] <= 56:
							if record[0] <= 30:
									class_id = -1
							else:
								if record[5] <= 146:
									if record[3] <= 6:
											class_id = -1
									else:
											class_id = -1
								else:
									if record[1] <= 144:
											class_id = 1
									else:
										if record[2] <= 20:
											if record[0] <= 50:
												if record[0] <= 44:
														class_id = -1
												else:
														class_id = -1
											else:
													class_id = 1
										else:
												class_id = 1
						else:
								class_id = -1
				else:
					if record[2] <= 6:
							class_id = 1
					else:
						if record[5] <= 140:
							if record[0] <= 44:
								if record[0] <= 34:
										class_id = 1
								else:
									if record[5] <= 138:
										if record[2] <= 10:
												class_id = 1
										else:
												class_id = -1
									else:
											class_id = 1
							else:
								if record[0] <= 52:
									if record[2] <= 10:
											class_id = 1
									else:
										if record[1] <= 128:
												class_id = -1
										else:
												class_id = -1
								else:
										class_id = -1
						else:
							if record[2] <= 14:
								if record[4] <= 6:
										class_id = 1
								else:
									if record[0] <= 30:
											class_id = -1
									else:
										if record[2] <= 10:
												class_id = 1
										else:
											if record[2] <= 12:
												if record[0] <= 60:
														class_id = 1
												else:
														class_id = -1
											else:
													class_id = 1
							else:
								if record[0] <= 52:
									if record[1] <= 144:
										if record[5] <= 142:
												class_id = 1
										else:
												class_id = 1
									else:
										if record[5] <= 150:
												class_id = -1
										else:
											if record[1] <= 148:
													class_id = 1
											else:
												if record[5] <= 160:
														class_id = 1
												else:
														class_id = 1
								else:
									if record[5] <= 156:
										if record[1] <= 140:
												class_id = 1
										else:
											if record[2] <= 20:
												if record[3] <= 4:
														class_id = 1
												else:
														class_id = -1
											else:
													class_id = 1
									else:
										if record[3] <= 6:
												class_id = -1
										else:
											if record[0] <= 54:
													class_id = 1
											else:
													class_id = 1
			else:
				if record[2] <= 8:
						class_id = 1
				else:
					if record[5] <= 138:
						if record[0] <= 52:
							if record[2] <= 10:
									class_id = 1
							else:
								if record[3] <= 10:
									if record[4] <= 6:
										if record[2] <= 12:
												class_id = 1
										else:
												class_id = -1
									else:
											class_id = 1
								else:
										class_id = 1
						else:
							if record[0] <= 56:
									class_id = -1
							else:
									class_id = -1
					else:
						if record[2] <= 14:
								class_id = 1
						else:
							if record[4] <= 6:
								if record[0] <= 52:
									if record[1] <= 148:
										if record[5] <= 144:
											if record[1] <= 136:
													class_id = 1
											else:
												if record[5] <= 142:
														class_id = -1
												else:
														class_id = 1
										else:
												class_id = 1
									else:
										if record[2] <= 16:
											if record[4] <= 4:
													class_id = -1
											else:
												if record[1] <= 156:
														class_id = 1
												else:
														class_id = 1
										else:
											if record[5] <= 154:
													class_id = -1
											else:
												if record[2] <= 18:
														class_id = 1
												else:
														class_id = 1
								else:
									if record[3] <= 10:
										if record[5] <= 154:
											if record[0] <= 64:
												if record[0] <= 60:
														class_id = 1
												else:
														class_id = -1
											else:
													class_id = 1
										else:
											if record[0] <= 62:
												if record[1] <= 168:
														class_id = 1
												else:
														class_id = 1
											else:
													class_id = -1
									else:
										if record[1] <= 144:
												class_id = 1
										else:
											if record[5] <= 162:
													class_id = 1
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
