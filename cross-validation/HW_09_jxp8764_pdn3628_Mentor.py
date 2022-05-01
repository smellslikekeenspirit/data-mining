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
    fp.write('\t\t\tfor index in range(len(row)):\n')
    fp.write('\t\t\t\tval = float(row[index])\n')
    fp.write('\t\t\t\tif index == 1:\n')
    fp.write('\t\t\t\t\tval = int(round(val / 4.0) * 4)\n')
    fp.write('\t\t\t\telif index == 6:\n')
    fp.write('\t\t\t\t\tval = int(round(val / 2.0, 1) * 4)\n')
    fp.write('\t\t\t\telse:\n')
    fp.write('\t\t\t\t\tval = int(round(val / 2.0) * 2)\n')
    fp.write('\t\t\t\tdata.append(val)\n\n')


def create_classifier(fp, data, class_ids, stump_count):
    fp.write('def classifier(record):\n')
    fp.write('\tanswer = 0\n\n')

    attr_range = []
    for index in range(len(data)):
        np_arr = np.array(data[index])
        print(data[index])
        attr_range.append([np_arr.min(), np_arr.max()])

    # Decision Stumps
    for stump in range(stump_count):
        attr_index = random.randint(0, len(data) - 1)
        [min_val, max_val] = attr_range[attr_index]
        threshold = random.randint(int(min_val), int(max_val))
        # Determine majority case
        hit = 0
        miss = 0
        values = data[attr_index]
        for index in range(len(values)):
            if values[index] <= threshold:
                if int(class_ids[index]) == -1:
                    hit = hit + 1
                else:
                    miss = miss + 1
            else:
                if int(class_ids[index] == 1):
                    hit = hit + 1
                else:
                    miss = miss + 1

        sign = ''
        if hit > miss:
            sign = '<='
        else:
            sign = '>'
        fp.write('\t# Decision Stump Number %s\n' % (stump + 1))
        fp.write('\tif record[%s] %s %s:\n' % (attr_index, sign, threshold))
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
                val = float(attributes[index])
                if index == 1:
                    val = int(round(val / 4.0) * 4)
                elif index == 6:
                    # need a round earlobes different, because default rounding function has 0.5 become 0
                    val = int(round(val / 2.0, 1) * 4)
                else:
                    val = int(round(val / 2.0) * 2)
                data[index].append(val)
            class_ids.append(int(attributes[-1]))

    # Note: can run this in a for loop to get data for all n_stumps
    fp = open('HW_09_jxp8764_pdn3628_Classifier.py', 'w')

    # TODO: determine how many stumps we need to use
    create_classifier(fp, data, class_ids, n_stumps[2])
    read_input(fp)
    call_classifier(fp)

    fp.close()
