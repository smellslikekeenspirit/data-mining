import random
import numpy as np
import pandas as pd

from HW_09_jxp8764_pdn3628_Classifier1 import Classifier1
from HW_09_jxp8764_pdn3628_Classifier2 import Classifier2
from HW_09_jxp8764_pdn3628_Classifier4 import Classifier4
from HW_09_jxp8764_pdn3628_Classifier8 import Classifier8
from HW_09_jxp8764_pdn3628_Classifier10 import Classifier10
from HW_09_jxp8764_pdn3628_Classifier20 import Classifier20
from HW_09_jxp8764_pdn3628_Classifier25 import Classifier25
from HW_09_jxp8764_pdn3628_Classifier35 import Classifier35
from HW_09_jxp8764_pdn3628_Classifier50 import Classifier50
from HW_09_jxp8764_pdn3628_Classifier75 import Classifier75
from HW_09_jxp8764_pdn3628_Classifier100 import Classifier100
from HW_09_jxp8764_pdn3628_Classifier150 import Classifier150
from HW_09_jxp8764_pdn3628_Classifier200 import Classifier200
from HW_09_jxp8764_pdn3628_Classifier250 import Classifier250
from HW_09_jxp8764_pdn3628_Classifier300 import Classifier300
from HW_09_jxp8764_pdn3628_Classifier400 import Classifier400

classifiers = {
    1: Classifier1,
    2: Classifier2,
    4: Classifier4,
    8: Classifier8,
    10: Classifier10,
    20: Classifier20,
    25: Classifier25,
    35: Classifier35,
    50: Classifier50,
    100: Classifier100,
    150: Classifier150,
    200: Classifier200,
    250: Classifier250,
    300: Classifier300,
    400: Classifier400
}

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


def create_classifier(fp, data, class_ids, stump_count, number=""):
    fp.write('class Classifier%s:\n' % stump_count)
    fp.write('\tdef classifier(record):\n')
    fp.write('\t\tanswer = 0\n\n')

    attr_range = []
    for column in data.columns.drop('ClassID'):
        column_values = data[column]
        print(column)
        print(column_values.min())
        print(column_values.max())
        attr_range.append([column_values.min(), column_values.max()])
    # Decision Stumps
    for stump in range(stump_count):
        attrs = data.columns.drop('ClassID')
        idx = random.randint(0, (len(attrs) - 1))
        attr_index = attrs[idx]
        [min_val, max_val] = attr_range[idx]
        threshold = random.randint(int(min_val), int(max_val))
        print("YOOO", attr_range[idx], threshold)
        # Determine majority case
        hit = 0
        miss = 0
        values = data[attr_index]
        print(values)
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
        fp.write('\t\t# Decision Stump Number %s\n' % (stump + 1))
        fp.write('\t\tif record[\'%s\'] %s %s:\n' % (attr_index, sign, threshold))
        fp.write('\t\t\tanswer = answer - 1\n')
        fp.write('\t\telse:\n')
        fp.write('\t\t\tanswer = answer + 1\n\n')

    # TODO: is it < or <= ... the doc shows both
    # Return result
    fp.write('\t\tif answer < 0:\n')
    fp.write('\t\t\treturn -1\n')
    fp.write('\t\telse:\n')
    fp.write('\t\t\treturn 1\n\n\n')


def call_classifier(fp, count):
    fp.write('\tfor record in data:\n')
    fp.write('\t\tprint(Classifier%s.classifier(record))\n' % count)
    # TODO: what to do with the classifications


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

    for count in n_stumps:
        file = open('HW_09_jxp8764_pdn3628_Classifier{0}.py'.format(count), 'w')

        create_classifier(file, data, class_ids, count)
        read_input(file)
        call_classifier(file, count)

        file.close()

    for count in n_stumps:
        class_name = 'Classifier%s' % count
        # call the function to classify to determine the fold
        classify = getattr(classifiers[count], 'classifier')
        print(classify([0, 0, 0, 0, 0, 0, 0, 0]))
    return 0


if __name__ == '__main__':
    n_stumps = [1, 2, 4, 8, 10, 20, 25, 35, 50, 75, 100, 150, 200, 250, 300, 400]
    # files should do nothing for now
    for count in n_stumps:
        file = open('HW_09_jxp8764_pdn3628_Classifier{0}.py'.format(count), 'w')
        file.write('class Classifier%s:\n' % count)
        file.write('\tdef classifier(record):\n')
        file.write('\t\traise Exception(\'Sorry, no numbers below zero\')\n\n')
        file.close()
    # Note: can run this in a for loop to get data for all n_stumps
    fp = open('HW_09_jxp8764_pdn3628_Classifier.py', 'w')
    # TODO: quantize
    labeled_data = pd.read_csv("Abominable_Data_HW_LABELED_TRAINING_DATA__v770_2215.csv")\
        .drop(columns=['ClassName']).astype(int)
    class_ids = labeled_data['ClassID']
    best_number_of_stumps = cross_validation(n_stumps, labeled_data)

    fp.close()
