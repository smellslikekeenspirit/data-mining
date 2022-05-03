import random
import numpy as np
import pandas as pd


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


def write_classifier(fp, decision_stumps):
    fp.write('def classifier(record):\n')
    fp.write('\tanswer = 0\n\n')
    print(decision_stumps)

    # Decision Stumps
    for index in range(len(decision_stumps)):
        [attr_index, sign, threshold] = decision_stumps[index]
        fp.write('\t# Decision Stump Number %s\n' % (index + 1))
        fp.write('\tif record[\'%s\'] %s %s:\n' % (attr_index, sign, threshold))
        fp.write('\t\tanswer = answer - 1\n')
        fp.write('\telse:\n')
        fp.write('\t\tanswer = answer + 1\n\n')

    # TODO: is it < or <= ... the doc shows both
    # Return result
    fp.write('\tif answer < 0:\n')
    fp.write('\t\treturn -1\n')
    fp.write('\telse:\n')
    fp.write('\t\treturn 1\n\n\n')


def call_classifier(fp, count):
    fp.write('\tfor record in data:\n')
    fp.write('\t\tprint(classifier(record))\n')
    # TODO: what to do with the classifications


def create_classifiers(data, class_ids, n_stumps):
    attr_range = []
    for column in data.columns.drop('ClassID'):
        column_values = data[column]
        attr_range.append([column_values.min(), column_values.max()])

    # Decisions for all the stumps stumps
    stump_decisions = {}
    for stump_count in n_stumps:
        decisions = []
        for stump in range(stump_count):
            attrs = data.columns.drop('ClassID')
            idx = random.randint(0, (len(attrs) - 1))
            attr_index = attrs[idx]
            [min_val, max_val] = attr_range[idx]
            threshold = random.randint(int(min_val), int(max_val))
            # Determine majority case
            hit = 0
            miss = 0
            values = data[attr_index]
            for index in range(len(values)):
                if values[index] <= threshold:
                    # print(values[index], threshold)
                    if int(class_ids[index]) == -1:
                        hit = hit + 1
                    else:
                        miss = miss + 1
                else:
                    if int(class_ids[index] == 1):
                        hit = hit + 1
                    else:
                        miss = miss + 1

            if hit > miss:
                sign = '<='
            else:
                sign = '>'
            decisions.append([attr_index, sign, threshold])
        stump_decisions[stump_count] = decisions
    return stump_decisions


def classify_data(decisions, record):
    answer = 0

    for stump in decisions:
        [attr_index, sign, threshold] = stump
        if sign == '<=':
            if record[attr_index] <= threshold:
                answer = answer - 1
            else:
                answer = answer + 1
        else:
            if record[attr_index] > threshold:
                answer = answer - 1
            else:
                answer = answer + 1

    if answer < 0:
        return -1
    else:
        return 1


def cross_validation(n_stumps, data, n_folds=10):
    number_of_records_per_fold = int(len(data) / n_folds)
    folds = {}
    data_assam = data[data['ClassID'] == -1]
    data_bhutan = data[data['ClassID'] == 1]
    toggle = 0

    for num_fold in range(n_folds):
        fold = []
        for record_index in range(number_of_records_per_fold):
            if toggle == 0:
                fold.append(data_assam)
                toggle = 1
            else:
                fold.append(data_bhutan)
                toggle = 0

    decision_stumps = create_classifiers(data, class_ids, n_stumps)

    for count in n_stumps:
        class_name = 'Classifier%s' % count
        # call the function to classify to determine the fold
        # classify_data(decision_stumps[count], record)

    file = open('HW_09_jxp8764_pdn3628_Classifier.py', 'w')

    write_classifier(file, decision_stumps[1])
    read_input(file)
    call_classifier(file, count)

    file.close()
    return 0


if __name__ == '__main__':
    n_stumps = [1, 2, 4, 8, 10, 20, 25, 35, 50, 75, 100, 150, 200, 250, 300, 400]
    # files should do nothing for now
    file = open('HW_09_jxp8764_pdn3628_Classifier.py', 'w')
    file.write('def classifier(record):\n')
    file.write('\traise Exception(\'Sorry, no numbers below zero\')\n\n')
    file.close()
    # Note: can run this in a for loop to get data for all n_stumps
    fp = open('HW_09_jxp8764_pdn3628_Classifier.py', 'w')
    # TODO: quantize
    labeled_data = pd.read_csv("Abominable_Data_HW_LABELED_TRAINING_DATA__v770_2215.csv")\
        .drop(columns=['ClassName']).astype(int)
    class_ids = labeled_data['ClassID']
    best_number_of_stumps = cross_validation(n_stumps, labeled_data)

    fp.close()
