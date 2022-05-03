# Prionti Nasir, Justin Palmer
import os
import sys
import numpy as np
import math
import pandas
import HW05_jxp8764_pdn3628_Trained_Classifier

"""
The cost function to determine the minimum weighted entropy
possible for an attribute
"""

STANDARD_BIN = 2
HEIGHT_BIN = 4


def best_min_entropy_threshold(points, class_id, bin_size, attr_index):
    # the entropy can at most be 1, so 1.1 is a good max value to start at
    best_entropy = 1.1
    # determine range of thresholds to check
    attr_vals = []
    for index, record in points.iterrows():
        attr_vals.append(record[attr_index])
    np_arr = np.array(attr_vals)
    threshold = np_arr.min()
    max = np_arr.max()
    best_threshold = 0
    while threshold < max:
        # splits up the classes into left and right nodes
        left_class = []
        right_class = []
        for index in range(len(attr_vals)):
            if attr_vals[index] <= threshold:
                left_class.append(class_id[index])
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


def build_classification(file_pointer, data, classification, level):
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
        majority_class = 1
        # prevent diving my zero, data set have an even balance of classes
        if purity != 0:
            majority_class = purity / abs(purity)
        file_pointer.write('%s\tclass_id = %d\n' % (tabs, majority_class))
        return
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
    right_partition = pandas.DataFrame(right_partition)
    # left split of the data
    file_pointer.write('%sif record[\'%s\'] <= %d:\n' % (tabs, attr_index, best_rule_thresh))
    build_classification(file_pointer, left_partition, left_class, level + 1)

    # right split of the data
    file_pointer.write('%selse:\n' % tabs)
    build_classification(file_pointer, right_partition, right_class, level + 1)
    return


"""
The libraries and global variable needed in the trained program
"""


def file_header(file_pointer):
    file_pointer.write('import math\n')
    file_pointer.write('import os\n')
    file_pointer.write('import pandas\n')
    file_pointer.write('import sys\n\n')

    file_pointer.write('STANDARD_BIN = 2\n')
    file_pointer.write('HEIGHT_BIN = 4\n')


"""
Reads in the unlabeled data and stores the columns in an array
"""


def read_input(file_pointer):
    file_pointer.write('def read_data_file(data_file_name):\n')
    file_pointer.write('\tdata_file_path = os.path.join(os.getcwd(), data_file_name)\n')
    file_pointer.write('\tdata = pandas.read_csv(data_file_path, delimiter=\',\')\n')
    file_pointer.write('\tclean_data = data[[\'TailLn\', \'HairLn\', \'BangLn\', \'Reach\', \'EarLobes\', \'Age\']].round(decimals=0)\n')
    file_pointer.write('\tclassification = []\n')
    file_pointer.write('\t# quantize the data\n')
    file_pointer.write('\tclean_data[\'Age\'] = data[\'Age\'].apply(\n')
    file_pointer.write('\t\tlambda x: math.floor(x / STANDARD_BIN) * STANDARD_BIN)\n')
    file_pointer.write('\tclean_data[\'TailLn\'] = data[\'TailLn\'].apply(\n')
    file_pointer.write('\t\tlambda x: math.floor(x / STANDARD_BIN) * STANDARD_BIN)\n')
    file_pointer.write('\tclean_data[\'HairLn\'] = data[\'HairLn\'].apply(\n')
    file_pointer.write('\t\tlambda x: math.floor(x / STANDARD_BIN) * STANDARD_BIN)\n')
    file_pointer.write('\tclean_data[\'BangLn\'] = data[\'BangLn\'].apply(\n')
    file_pointer.write('\t\tlambda x: math.floor(x / STANDARD_BIN) * STANDARD_BIN)\n')
    file_pointer.write('\tclean_data[\'Reach\'] = data[\'Reach\'].apply(\n')
    file_pointer.write('\t\tlambda x: math.floor(x / STANDARD_BIN) * STANDARD_BIN)\n')
    file_pointer.write('\tclean_data[\'EarLobes\'] = data[\'EarLobes\'].apply(\n')
    file_pointer.write('\t\tlambda x: math.ceil(x / STANDARD_BIN) * STANDARD_BIN)\n')
    file_pointer.write('\tclean_data[\'Ht\'] = data[\'Ht\'].apply(\n')
    file_pointer.write('\t\tlambda x: math.floor(x / HEIGHT_BIN) * HEIGHT_BIN)\n')
    file_pointer.write('\tfor index, row in data.iterrows():\n')
    file_pointer.write('\t\tclassification.append(row[\'ClassID\'])\n')
    file_pointer.write('\treturn clean_data.astype(int), classification\n\n\n')


"""
The one rule classification for unlabeled data
"""


def classify_data(file_pointer, data, classification):
    file_pointer.write('def classify(filename):\n')
    file_pointer.write('\tdata, labels = read_data_file(\'Abominable_Data_HW_LABELED_TRAINING_DATA__v750_2215.csv\')\n')
    file_pointer.write('\t# classifies the unlabled data\n')
    file_pointer.write('\tclassification = []\n')
    file_pointer.write('\tclass_id = 0\n')
    file_pointer.write('\tfor index, record in data.iterrows():\n')
    build_classification(file_pointer, data, classification, 0)
    file_pointer.write('\t\tclassification.append(class_id)\n')
    file_pointer.write('\t\t# Print out here for the grader\n')
    file_pointer.write('\t\tprint(class_id)\n\n')
    file_pointer.write('\t# writes out the classifications to a csv\n')
    file_pointer.write('\tfile_pointer = open(\'HW05_jxp8764_pdn3628_MyClassifications.csv\', \'w\')\n')
    file_pointer.write('\tfor class_type in classification:\n')
    file_pointer.write('\t\tfile_pointer.write(\'%s\\n\' % class_type)\n')
    file_pointer.write('\tfile_pointer.close()\n\n\n')

    file_pointer.write('if __name__ == \'__main__\':\n')
    file_pointer.write('\tclassify(sys.argv[1])\n')


"""
Opens up the file to write out the classification. Then starts writting to it
"""


def write_decision_tree(data, classification):
    file_pointer = open('HW05_jxp8764_pdn3628_Trained_Classifier.py', 'w')

    file_header(file_pointer)
    read_input(file_pointer)
    classify_data(file_pointer, data, classification)

    file_pointer.close()


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
    # Cast everything to integer.
    return clean_data.astype(int), classification


"""
Reads in the training data and quantizes the data
"""
if __name__ == '__main__':
    data_frame, classification = read_data_file('Abominable_Data_HW_LABELED_TRAINING_DATA__v750_2215.csv')
    write_decision_tree(data_frame, classification)
    HW05_jxp8764_pdn3628_Trained_Classifier.classify('Abominable_Data_HW_LABELED_TRAINING_DATA__v750_2215.csv')
    with open('HW05_jxp8764_pdn3628_MyClassifications.csv', 'r') as f:
        # assuming target class is Assam
        records = []
        for class_id in classification:
            classifier_decision = int(f.readline().strip())
            outcome = ""
            if class_id == -1 and classifier_decision == -1:
                outcome = "TP"
            elif class_id == -1 and classifier_decision == 1:
                outcome = "FN"
            elif class_id == 1 and classifier_decision == 1:
                outcome = "TN"
            elif class_id == 1 and classifier_decision == -1:
                outcome = "FP"
            records.append([class_id, classifier_decision, outcome])
        data_frame = pandas.DataFrame(records, columns=['Actual Class', 'Classified Class', 'Outcome'])
        frequency_table = df['Outcome'].value_counts()
        print(frequency_table)
        print("Accurate guesses (TP+TN): ", frequency_table.TP+frequency_table.TN)
        print("Mistakes (FP+FN): ", frequency_table.FP+frequency_table.FN)

