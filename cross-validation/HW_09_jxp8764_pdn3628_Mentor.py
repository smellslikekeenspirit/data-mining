import random
import numpy as np

def read_input(fp):
    # TODO: What should the data be rounded to?
    fp.write('if __name__ == \'__main__\':\n')
    fp.write('\tdata = []\n\n')
    fp.write('\t# reads in the unlabeled data from the csv\n')
    fp.write('\twith open(\'Abominable_VALIDATION_Data_FOR_STUDENTS_v770_2215.csv\', \'r\') as file:\n')
    fp.write('\t\tfile.readline()\n')
    fp.write('\t\tfor line in file:\n')
    fp.write('\t\t\trow = line.strip().split(",")\n')
    fp.write('\t\t\tfor val in row:\n')
    fp.write('\t\t\t\tdata.append(float(val))\n\n')


def create_classifier(fp, data, class_ids, n_stumps):
    fp.write('def classifier(record):\n')
    fp.write('\tanswer = 0\n\n')

    attr_range = []
    for index in range(len(data)):
        np_arr = np.array(data[index])
        print(data[index])
        attr_range.append([np_arr.min(), np_arr.max()])

    # TODO: Determine how many stumps to use
    stump_count = n_stumps[2]
    # Decision Stumps
    for stump in range(stump_count):
        attr_index = random.randint(0, len(data) - 1)
        [min_val, max_val] = attr_range[attr_index]
        threshold = random.randint(int(min_val), int(max_val))
        print(threshold, min_val, max_val)
        fp.write('\t# Decision Stump Number %s\n' % (stump + 1))
        fp.write('\tif record[%s] <= %s:\n' % (attr_index, threshold))
        fp.write('\t\tanswer = answer - 1\n')
        fp.write('\telse:\n')
        fp.write('\t\tanswer = answer + 1\n\n')

    # TODO: is it < or <= ... the doc shows both
    # Return result
    fp.write('\tif answer < 0:\n')
    fp.write('\t\treturn -1\n')
    fp.write('\telse:\n')
    fp.write('\t\treturn 1\n\n\n')


def call_classifier(fp):
    fp.write('\tfor record in data:\n')
    fp.write('\t\tprint(classifier(record))\n')
    # TODO: what to do with the classifications


if __name__ == '__main__':
    n_stumps = [1, 2, 4, 8, 10, 20, 25, 35, 50, 75, 100, 150, 200, 250, 300, 400]
    data = []
    class_ids = []
    with open('Abominable_Data_HW_LABELED_TRAINING_DATA__v770_2215.csv') as dataFile:
        for _tmp in range(len(dataFile.readline().strip().split(",")) - 2):
            data.append([])
        for line in dataFile:
            attributes = line.strip().split(",")
            for index in range(len(attributes) - 2):
                data[index].append(float(attributes[index]))
            class_ids.append(int(attributes[-1]))
    fp = open('HW_09_jxp8764_pdn3628_Classifier.py', 'w')

    create_classifier(fp, data, class_ids, n_stumps)
    read_input(fp)
    call_classifier(fp)

    fp.close()
