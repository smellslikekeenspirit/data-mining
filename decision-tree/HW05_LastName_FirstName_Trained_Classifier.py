if __name__ == '__main__':
	data = []

	#reads in the unlabeled data from the csv
	with open('Abominable_VALIDATION_Data_FOR_STUDENTS_v750_2215.csv', 'r') as file:
		file.readline()
		for line in file:
			row = line.strip().split(",")
			for val in row:
				data.append(float(val))

	# classifies the unlabled data
	classification = []
	class_id = 0
	for record in data:
		if data[3] <= 8:
			if data[4] <= 4:
				if data[2] <= 6:
					if data[3] <= 6:
						if data[1] <= 152:
							if data[3] <= 4:
									class_id = -1
							else:
								if data[1] <= 136:
										class_id = -1
								else:
										class_id = -1
						else:
							if data[1] <= 156:
									class_id = 1
							else:
									class_id = -1
					else:
						if data[0] <= 42:
							if data[5] <= 142:
									class_id = 1
							else:
								if data[2] <= 0:
										class_id = 1
								else:
									if data[0] <= 14:
											class_id = -1
									else:
										if data[1] <= 164:
											if data[1] <= 156:
												if data[1] <= 152:
														class_id = 1
												else:
														class_id = -1
											else:
													class_id = 1
										else:
												class_id = -1
						else:
							if data[1] <= 132:
									class_id = 1
							else:
								if data[2] <= -2:
										class_id = 1
								else:
									if data[5] <= 150:
										if data[1] <= 140:
											if data[2] <= 2:
													class_id = 1
											else:
												if data[0] <= 56:
														class_id = -1
												else:
														class_id = -1
										else:
												class_id = -1
									else:
										if data[1] <= 152:
											if data[2] <= 4:
													class_id = 1
											else:
													class_id = -1
										else:
											if data[0] <= 52:
													class_id = -1
											else:
													class_id = 1
				else:
					if data[0] <= 40:
						if data[1] <= 152:
							if data[5] <= 156:
								if data[2] <= 14:
									if data[5] <= 128:
											class_id = -1
									else:
										if data[1] <= 140:
											if data[3] <= 6:
												if data[2] <= 8:
														class_id = 1
												else:
														class_id = -1
											else:
												if data[5] <= 144:
														class_id = -1
												else:
														class_id = 1
										else:
											if data[0] <= 34:
												if data[2] <= 8:
														class_id = -1
												else:
														class_id = -1
											else:
												if data[0] <= 36:
														class_id = -1
												else:
														class_id = -1
								else:
									if data[1] <= 144:
										if data[5] <= 146:
											if data[1] <= 136:
												if data[5] <= 138:
														class_id = -1
												else:
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
							if data[3] <= 6:
									class_id = -1
							else:
								if data[5] <= 166:
									if data[0] <= 30:
										if data[0] <= 26:
												class_id = -1
										else:
												class_id = 1
									else:
										if data[2] <= 12:
												class_id = -1
										else:
											if data[0] <= 34:
													class_id = -1
											else:
												if data[2] <= 16:
														class_id = -1
												else:
														class_id = -1
								else:
										class_id = -1
					else:
						if data[5] <= 146:
							if data[0] <= 52:
								if data[5] <= 132:
										class_id = -1
								else:
									if data[1] <= 124:
											class_id = 1
									else:
										if data[0] <= 46:
											if data[1] <= 136:
												if data[5] <= 140:
														class_id = -1
												else:
														class_id = 1
											else:
												if data[2] <= 10:
														class_id = -1
												else:
														class_id = -1
										else:
											if data[1] <= 136:
													class_id = -1
											else:
												if data[2] <= 8:
														class_id = -1
												else:
														class_id = -1
							else:
									class_id = -1
						else:
							if data[3] <= 6:
								if data[1] <= 140:
										class_id = 1
								else:
									if data[2] <= 10:
										if data[5] <= 154:
											if data[0] <= 50:
												if data[5] <= 148:
														class_id = -1
												else:
														class_id = -1
											else:
													class_id = -1
										else:
												class_id = -1
									else:
											class_id = -1
							else:
								if data[5] <= 164:
									if data[0] <= 56:
										if data[1] <= 156:
											if data[1] <= 144:
												if data[2] <= 12:
														class_id = 1
												else:
														class_id = -1
											else:
												if data[5] <= 162:
														class_id = -1
												else:
														class_id = 1
										else:
												class_id = -1
									else:
										if data[2] <= 20:
												class_id = -1
										else:
												class_id = 1
								else:
									if data[1] <= 164:
										if data[0] <= 44:
												class_id = -1
										else:
											if data[2] <= 10:
													class_id = 1
											else:
													class_id = -1
									else:
										if data[5] <= 174:
												class_id = -1
										else:
												class_id = -1
			else:
				if data[2] <= 6:
					if data[1] <= 132:
							class_id = 1
					else:
						if data[4] <= 6:
							if data[2] <= 0:
								if data[5] <= 158:
										class_id = 1
								else:
										class_id = -1
							else:
								if data[1] <= 156:
									if data[0] <= 62:
										if data[2] <= 2:
											if data[1] <= 148:
												if data[0] <= 46:
														class_id = 1
												else:
														class_id = 1
											else:
													class_id = -1
										else:
											if data[3] <= 4:
													class_id = 1
											else:
												if data[5] <= 160:
														class_id = 1
												else:
														class_id = 1
									else:
										if data[0] <= 64:
												class_id = -1
										else:
												class_id = -1
								else:
									if data[0] <= 46:
										if data[2] <= 4:
												class_id = -1
										else:
												class_id = -1
									else:
										if data[5] <= 166:
												class_id = -1
										else:
												class_id = 1
						else:
							if data[0] <= 44:
								if data[0] <= 34:
										class_id = 1
								else:
									if data[5] <= 142:
											class_id = 1
									else:
										if data[0] <= 36:
												class_id = -1
										else:
											if data[1] <= 140:
													class_id = -1
											else:
													class_id = 1
							else:
									class_id = 1
				else:
					if data[4] <= 6:
						if data[0] <= 44:
							if data[1] <= 152:
								if data[2] <= 10:
									if data[5] <= 156:
										if data[1] <= 144:
											if data[0] <= 32:
												if data[5] <= 146:
														class_id = 1
												else:
														class_id = 1
											else:
												if data[3] <= 6:
														class_id = -1
												else:
														class_id = 1
										else:
											if data[5] <= 152:
												if data[0] <= 18:
														class_id = 1
												else:
														class_id = -1
											else:
												if data[1] <= 148:
														class_id = 1
												else:
														class_id = -1
									else:
											class_id = 1
								else:
									if data[5] <= 156:
										if data[1] <= 144:
											if data[5] <= 148:
												if data[5] <= 138:
														class_id = -1
												else:
														class_id = -1
											else:
													class_id = 1
										else:
											if data[5] <= 154:
												if data[0] <= 36:
														class_id = -1
												else:
														class_id = -1
											else:
												if data[1] <= 148:
														class_id = 1
												else:
														class_id = -1
									else:
										if data[0] <= 40:
												class_id = 1
										else:
												class_id = 1
							else:
								if data[5] <= 158:
										class_id = -1
								else:
									if data[1] <= 164:
										if data[2] <= 14:
											if data[5] <= 160:
												if data[0] <= 42:
														class_id = -1
												else:
														class_id = 1
											else:
												if data[1] <= 156:
														class_id = 1
												else:
														class_id = -1
										else:
											if data[2] <= 16:
													class_id = -1
											else:
												if data[1] <= 156:
														class_id = -1
												else:
														class_id = -1
									else:
										if data[5] <= 172:
												class_id = -1
										else:
											if data[0] <= 34:
													class_id = -1
											else:
													class_id = -1
						else:
							if data[5] <= 140:
								if data[0] <= 52:
									if data[2] <= 10:
										if data[1] <= 132:
											if data[0] <= 46:
													class_id = -1
											else:
													class_id = 1
										else:
											if data[0] <= 48:
													class_id = -1
											else:
													class_id = -1
									else:
											class_id = -1
								else:
										class_id = -1
							else:
								if data[1] <= 136:
										class_id = 1
								else:
									if data[5] <= 158:
										if data[5] <= 142:
											if data[2] <= 8:
													class_id = -1
											else:
													class_id = -1
										else:
											if data[1] <= 140:
												if data[0] <= 60:
														class_id = 1
												else:
														class_id = -1
											else:
												if data[5] <= 148:
														class_id = -1
												else:
														class_id = -1
									else:
										if data[1] <= 156:
											if data[5] <= 160:
												if data[0] <= 54:
														class_id = -1
												else:
														class_id = 1
											else:
													class_id = 1
										else:
											if data[0] <= 46:
													class_id = -1
											else:
												if data[5] <= 166:
														class_id = -1
												else:
														class_id = 1
					else:
						if data[3] <= 6:
							if data[0] <= 32:
									class_id = -1
							else:
								if data[5] <= 140:
										class_id = -1
								else:
									if data[1] <= 136:
											class_id = 1
									else:
										if data[0] <= 38:
												class_id = -1
										else:
											if data[5] <= 142:
													class_id = -1
											else:
												if data[1] <= 148:
														class_id = 1
												else:
														class_id = -1
						else:
							if data[1] <= 156:
								if data[0] <= 48:
									if data[1] <= 140:
											class_id = 1
									else:
										if data[5] <= 148:
											if data[0] <= 42:
													class_id = 1
											else:
													class_id = -1
										else:
											if data[0] <= 42:
												if data[2] <= 16:
														class_id = 1
												else:
														class_id = 1
											else:
													class_id = 1
								else:
									if data[5] <= 140:
											class_id = -1
									else:
										if data[2] <= 8:
												class_id = -1
										else:
											if data[2] <= 16:
												if data[2] <= 14:
														class_id = 1
												else:
														class_id = -1
											else:
													class_id = 1
							else:
								if data[2] <= 14:
									if data[2] <= 12:
										if data[0] <= 48:
												class_id = -1
										else:
												class_id = 1
									else:
											class_id = -1
								else:
										class_id = 1
		else:
			if data[3] <= 10:
				if data[4] <= 4:
					if data[0] <= 48:
						if data[1] <= 156:
							if data[2] <= 6:
								if data[1] <= 132:
										class_id = 1
								else:
									if data[4] <= 2:
											class_id = -1
									else:
										if data[0] <= 46:
											if data[2] <= -2:
													class_id = 1
											else:
												if data[5] <= 160:
														class_id = 1
												else:
														class_id = 1
										else:
												class_id = 1
							else:
								if data[5] <= 130:
										class_id = -1
								else:
									if data[1] <= 132:
										if data[5] <= 134:
											if data[2] <= 10:
													class_id = 1
											else:
													class_id = -1
										else:
												class_id = 1
									else:
										if data[5] <= 140:
											if data[0] <= 34:
													class_id = -1
											else:
												if data[0] <= 42:
														class_id = -1
												else:
														class_id = -1
										else:
											if data[1] <= 136:
													class_id = 1
											else:
												if data[5] <= 144:
														class_id = -1
												else:
														class_id = -1
						else:
							if data[0] <= 36:
									class_id = -1
							else:
								if data[2] <= 18:
									if data[1] <= 160:
										if data[2] <= 2:
												class_id = -1
										else:
											if data[5] <= 162:
												if data[2] <= 12:
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
						if data[5] <= 140:
							if data[2] <= 8:
									class_id = -1
							else:
									class_id = -1
						else:
							if data[2] <= 12:
								if data[1] <= 136:
										class_id = 1
								else:
									if data[5] <= 148:
										if data[0] <= 56:
											if data[2] <= 10:
												if data[0] <= 50:
														class_id = -1
												else:
														class_id = -1
											else:
													class_id = 1
										else:
												class_id = -1
									else:
										if data[1] <= 148:
											if data[1] <= 144:
													class_id = 1
											else:
												if data[2] <= 4:
														class_id = 1
												else:
														class_id = 1
										else:
											if data[0] <= 60:
												if data[0] <= 50:
														class_id = 1
												else:
														class_id = -1
											else:
													class_id = 1
							else:
								if data[2] <= 18:
									if data[0] <= 56:
										if data[0] <= 52:
												class_id = -1
										else:
											if data[2] <= 16:
													class_id = -1
											else:
													class_id = -1
									else:
											class_id = -1
								else:
										class_id = -1
				else:
					if data[2] <= 8:
						if data[1] <= 144:
							if data[0] <= 46:
								if data[0] <= 32:
										class_id = 1
								else:
									if data[1] <= 128:
											class_id = 1
									else:
										if data[0] <= 40:
											if data[2] <= 6:
												if data[0] <= 36:
														class_id = 1
												else:
														class_id = 1
											else:
												if data[5] <= 140:
														class_id = 1
												else:
														class_id = 1
										else:
												class_id = 1
							else:
								if data[0] <= 66:
									if data[5] <= 146:
										if data[1] <= 136:
											if data[0] <= 48:
													class_id = 1
											else:
													class_id = 1
										else:
											if data[5] <= 140:
													class_id = -1
											else:
												if data[0] <= 58:
														class_id = 1
												else:
														class_id = -1
									else:
											class_id = 1
								else:
										class_id = -1
						else:
							if data[4] <= 6:
								if data[2] <= 0:
									if data[0] <= 66:
											class_id = 1
									else:
											class_id = 1
								else:
									if data[1] <= 160:
										if data[5] <= 150:
											if data[0] <= 54:
												if data[2] <= 6:
														class_id = -1
												else:
														class_id = 1
											else:
													class_id = -1
										else:
											if data[2] <= 2:
												if data[5] <= 152:
														class_id = -1
												else:
														class_id = 1
											else:
												if data[0] <= 28:
														class_id = 1
												else:
														class_id = 1
									else:
										if data[2] <= 6:
											if data[0] <= 40:
													class_id = -1
											else:
													class_id = 1
										else:
												class_id = -1
							else:
								if data[1] <= 156:
										class_id = 1
								else:
									if data[5] <= 164:
											class_id = 1
									else:
											class_id = 1
					else:
						if data[5] <= 138:
							if data[0] <= 42:
								if data[2] <= 10:
									if data[0] <= 38:
											class_id = 1
									else:
											class_id = 1
								else:
									if data[0] <= 40:
										if data[2] <= 14:
											if data[4] <= 6:
													class_id = -1
											else:
													class_id = 1
										else:
												class_id = 1
									else:
											class_id = -1
							else:
								if data[0] <= 56:
									if data[1] <= 116:
											class_id = 1
									else:
										if data[5] <= 136:
											if data[1] <= 120:
													class_id = -1
											else:
													class_id = -1
										else:
												class_id = -1
								else:
										class_id = -1
						else:
							if data[4] <= 6:
								if data[1] <= 144:
									if data[5] <= 148:
										if data[0] <= 34:
											if data[5] <= 146:
												if data[0] <= 26:
														class_id = 1
												else:
														class_id = 1
											else:
													class_id = 1
										else:
											if data[0] <= 54:
												if data[5] <= 146:
														class_id = 1
												else:
														class_id = 1
											else:
												if data[0] <= 60:
														class_id = -1
												else:
														class_id = 1
									else:
											class_id = 1
								else:
									if data[5] <= 150:
										if data[0] <= 42:
												class_id = -1
										else:
											if data[2] <= 10:
													class_id = 1
											else:
													class_id = -1
									else:
										if data[1] <= 148:
											if data[0] <= 64:
												if data[2] <= 16:
														class_id = 1
												else:
														class_id = 1
											else:
													class_id = -1
										else:
											if data[5] <= 154:
												if data[2] <= 16:
														class_id = 1
												else:
														class_id = -1
											else:
												if data[1] <= 152:
														class_id = 1
												else:
														class_id = 1
							else:
								if data[0] <= 60:
									if data[1] <= 148:
											class_id = 1
									else:
										if data[5] <= 156:
												class_id = 1
										else:
												class_id = 1
								else:
										class_id = 1
			else:
				if data[0] <= 58:
					if data[4] <= 4:
						if data[2] <= 6:
								class_id = 1
						else:
							if data[5] <= 128:
									class_id = -1
							else:
								if data[5] <= 142:
										class_id = 1
								else:
									if data[1] <= 152:
										if data[4] <= 2:
												class_id = -1
										else:
											if data[0] <= 46:
												if data[0] <= 38:
														class_id = 1
												else:
														class_id = 1
											else:
												if data[0] <= 48:
														class_id = -1
												else:
														class_id = 1
									else:
										if data[2] <= 8:
												class_id = -1
										else:
											if data[2] <= 14:
												if data[5] <= 160:
														class_id = 1
												else:
														class_id = 1
											else:
													class_id = -1
					else:
						if data[1] <= 148:
								class_id = 1
						else:
							if data[2] <= 26:
								if data[5] <= 152:
										class_id = -1
								else:
									if data[4] <= 6:
										if data[3] <= 12:
											if data[2] <= 2:
													class_id = 1
											else:
												if data[5] <= 166:
														class_id = 1
												else:
														class_id = 1
										else:
												class_id = 1
									else:
											class_id = 1
							else:
									class_id = -1
				else:
					if data[5] <= 136:
							class_id = -1
					else:
						if data[1] <= 156:
							if data[4] <= 4:
								if data[0] <= 62:
										class_id = 1
								else:
										class_id = -1
							else:
								if data[0] <= 68:
									if data[2] <= 4:
											class_id = 1
									else:
										if data[2] <= 6:
												class_id = -1
										else:
											if data[1] <= 144:
													class_id = 1
											else:
												if data[5] <= 148:
														class_id = -1
												else:
														class_id = 1
								else:
										class_id = -1
						else:
								class_id = 1
		classification.append(class_id)
	# writes out the classifications to a csv
	fp = open('HW05_LastName_FirstName_MyClassifications.csv', 'w')
	for class_type in classification:
		fp.write('%s\n' % class_type)
	fp.close()
