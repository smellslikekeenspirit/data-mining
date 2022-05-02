# Prionti Nasir, Justin Palmer
import os
import sys
import numpy as np
import math

import pandas


"""
The cost function to determine the minimum weighted entropy
possible for an attribute
"""

AGE_BIN = 2
HEIGHT_BIN = 4


def best_min_entropy_threshold(points, class_id, bin_size, attr_index):
    # the entropy can at most be 1, so 1.1 is a good max value to start at
    best_entropy = 1.1
    # determine range of thresholds to check
    attr_vals = []
    print(points)
    for index, record in points.iterrows():
        attr_vals.append(record[attr_index])
    print(attr_vals)
    np_arr = np.array(attr_vals)
    threshold = np_arr.min()
    max = np_arr.max()
    best_threshold = 0
    while threshold < max:
        # splits up the classes into left and right nodes
        left_class = []
        right_class = []
        print("YOO!", len(left_class))
        print("YOO!", len(right_class))
        print("YOO!", len(class_id))
        print("YOO!", len(attr_vals))
        for index in range(len(attr_vals)):
            if attr_vals[index] <= threshold:
                left_class.append(class_id[index])
                print(class_id[index])
            else:
                right_class.append(class_id[index])

        if len(left_class) == 0 or len(right_class) == 0:
            threshold = threshold + bin_size
            continue
        # calculate weighted entropy for left nodes
        assam_count = 0
        bhuttan_count = 0
        for index in range(len(left_class)):
            if left_class[index] == 1:
                bhuttan_count = bhuttan_count + 1
            else:
                assam_count = assam_count + 1

        prob_b = bhuttan_count / len(left_class)
        prob_a = assam_count / len(left_class)
        left_entropy = 0
        # the log base 2 function throws an error when the probability is 0
        if prob_b == 0:
            left_entropy = 0 - (prob_a * math.log2(prob_a))
        elif prob_a == 0:
            left_entropy = 0 - (prob_b * math.log2(prob_b))
        else:
            left_entropy = 0 - (prob_b * math.log2(prob_b)) - (prob_a * math.log2(prob_a))

        # calculate weighted entropy for right nodes
        assam_count = 0
        bhuttan_count = 0
        for index in range(len(right_class)):
            if right_class[index] == 1:
                bhuttan_count = bhuttan_count + 1
            else:
                assam_count = assam_count + 1

        prob_b = bhuttan_count / len(right_class)
        prob_a = assam_count / len(right_class)
        right_entropy = 0
        # the log base 2 function throws an error when the probability is 0
        if prob_b == 0:
            right_entropy = 0 - (prob_a * math.log2(prob_a))
        elif prob_a == 0:
            right_entropy = 0 - (prob_b * math.log2(prob_b))
        else:
            right_entropy = 0 - (prob_b * math.log2(prob_b)) - (prob_a * math.log2(prob_a))

        # use best weighted_entropy
        weighted_entropy = ((len(left_class) / len(attr_vals)) * left_entropy) \
                           + (len(right_class) / len(attr_vals) * right_entropy)
        if weighted_entropy < best_entropy:
            best_entropy = weighted_entropy
            best_threshold = threshold
        threshold = threshold + bin_size
    return [best_threshold, best_entropy]


"""
Builds the decision tree classifier.
Writes out each decision as the decision is made
"""


def build_classification(fp, data, classification, level):
    best_rule_thresh = sys.float_info.max
    best_weighted_entropy = sys.float_info.max
    attr_index = -1

    # cases when to stop building the decision tree
    purity = 0.0
    for class_id in classification:
        purity += class_id

    if len(classification) > 0:
        purity /= len(classification)

    tabs = "\t" * (level + 2)

    if level > 10 or abs(purity) > .95 or len(data) < 9:
        # TODO: check that 1 should be the default class
        majority_class = 1
        if purity != 0:
            majority_class = purity / abs(purity)
        fp.write('%s\tclass_id = %d\n' % (tabs, majority_class))
        return
    print("OK", data)
    for attribute in data.columns:
        bin = 2
        if attribute == 'Ht':
            bin = 4
        # select attribute with the smallest weighted entropy

        [thresh, entropy] = best_min_entropy_threshold(data, classification, bin, attribute)
        if entropy < best_weighted_entropy:
            best_rule_thresh = thresh
            best_weighted_entropy = entropy
            attr_index = attribute

    left_partition = []
    left_class = []
    right_partition = []
    right_class = []
    print("YOO3", data, len(classification))

    # split the data along the threshold
    idx = 0
    for index, record in data.iterrows():
        if record[attr_index] <= best_rule_thresh:
            left_partition.append(record)
            left_class.append(classification[idx])
        else:
            right_partition.append(record)
            right_class.append(classification[idx])
        idx += 1

    left_partition = pandas.DataFrame(left_partition)
    print("OK", left_partition)
    right_partition = pandas.DataFrame(right_partition)
    # left split of the data
    fp.write('%sif record[\'%s\'] <= %d:\n' % (tabs, attr_index, best_rule_thresh))
    print("YOO", len(left_partition), len(left_class))
    build_classification(fp, left_partition, left_class, level + 1)

    # right split of the data
    fp.write('%selse:\n' % tabs)
    build_classification(fp, right_partition, right_class, level + 1)
    return


"""
Reads in the unlabeled data and stores the columns in an array
"""


def read_input(fp):
    fp.write('import sys\n\n')
    fp.write('def classify(filename):\n')
    fp.write('\tdata = []\n\n')
    fp.write('\t#reads in the unlabeled data from the csv\n')
    fp.write('\twith open(filename) as file:\n')
    fp.write('\t\tfile.readline()\n')
    fp.write('\t\tfor line in file:\n')
    fp.write('\t\t\tvalues = []\n')
    fp.write('\t\t\trow = line.strip().split(",")\n')
    fp.write('\t\t\tfor index in range(len(row)):\n')
    fp.write('\t\t\t\tval = float(row[index])\n')
    fp.write('\t\t\t\tif index == 1:\n')
    fp.write('\t\t\t\t\tval = int(round(val / 4.0) * 4)\n')
    fp.write('\t\t\t\telif index == 6:\n')
    fp.write('\t\t\t\t\tval = int(round(val / 2.0, 1) * 4)\n')
    fp.write('\t\t\t\telse:\n')
    fp.write('\t\t\t\t\tval = int(round(val / 2.0) * 2)\n')
    fp.write('\t\t\t\tvalues.append(val)\n')
    fp.write('\t\t\tdata.append(values)\n\n')


"""
The one rule classification for unlabeled data
"""


def classify_data(fp, data, classification):
    fp.write('\t# classifies the unlabled data\n')
    fp.write('\tclassification = []\n')
    fp.write('\tclass_id = 0\n')
    fp.write('\tfor record in data:\n')
    build_classification(fp, data, classification, 0)
    fp.write('\t\tclassification.append(class_id)\n')
    fp.write('\t\t# Print out here for the grader\n')
    fp.write('\t\tprint(class_id)\n')


"""
Writes the now classified data to a csv file
The order of the elements is the order the data was read in
"""


def output_classification(fp):
    fp.write('\t# writes out the classifications to a csv\n')
    fp.write('\tfp = open(\'HW05_jxp8764_pdn3628_MyClassifications.csv\', \'w\')\n')
    fp.write('\tfor class_type in classification:\n')
    fp.write('\t\tfp.write(\'%s\\n\' % class_type)\n')
    fp.write('\tfp.close()\n')
    fp.write('if __name__ == \'__main__\':\n')
    fp.write('\tclassify(sys.argv[1])\n')


"""
Opens up the file to write out the classification. Then starts writting to it
"""


def write_decision_tree(data, classification):
    fp = open('HW05_jxp8764_pdn3628_Trained_Classifier2.py', 'w')

    read_input(fp)
    classify_data(fp, data, classification)
    output_classification(fp)

    fp.close()


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
    clean_data['Ht'] = data['Ht'].apply(
        lambda x: math.floor(x / HEIGHT_BIN) * HEIGHT_BIN)
    for index, row in data.iterrows():
        classification.append(row['ClassID'])
    # Cast everything to integer.
    return clean_data.astype(int), classification


"""
Reads in the training data and quantizes the data
"""
if __name__ == '__main__':
    df, classification = read_data_file('Abominable_Data_HW_LABELED_TRAINING_DATA__v750_2215.csv')
    write_decision_tree(df, classification)
    # HW05_jxp8764_pdn3628_Trained_Classifier.classify('Abominable_Data_HW_LABELED_TRAINING_DATA__v750_2215.csv')
