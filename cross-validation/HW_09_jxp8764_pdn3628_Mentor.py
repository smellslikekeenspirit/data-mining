

def read_input(fp):
    # TODO: What should the data be rounded to?
    fp.write('if __name__ == \'__main__\':\n')
    fp.write('\tdata = []\n\n')
    fp.write('\t#reads in the unlabeled data from the csv\n')
    fp.write('\twith open(\'Abominable_VALIDATION_Data_FOR_STUDENTS_v770_2215.csv\', \'r\') as file:\n')
    fp.write('\t\tfile.readline()\n')
    fp.write('\t\tfor line in file:\n')
    fp.write('\t\t\trow = line.strip().split(",")\n')
    fp.write('\t\t\tfor val in row:\n')
    fp.write('\t\t\t\tdata.append(float(val))\n\n')


def create_classifier(fp, n_stumps):
    fp.write('def classifier(record)\n')
    fp.write('\tanswer = 0\n')

    # Decision Stumps


    # Return result
    fp.write('\tif answer < 0:\n')
    fp.write('\t\t return -1\n')
    fp.write('\telse:\n')
    fp.write('\t\treturn 1')


def call_classifier(fp):
    fp.write('\tfor record in data:\n')
    fp.write('\t\tprint(classifier(record))\n')
    # TODO: what to do with the classifications


if __name__ == '__main__':
    n_stumps = [1, 2, 4, 8, 10, 20, 25, 35, 50, 75, 100, 150, 200, 250, 300, 400]
    fp = open('HW_09_jxp8764_pdn3628_Classifier.py', 'w')

    create_classifier(fp, n_stumps)
    read_input(fp)
    call_classifier(fp)

    fp.close()
