# Prionti Nasir, Justin Palmer
import sys
import numpy as np
import math


def best_min_entropy_threshold(points, class_id, bin_size, attr_index):
    best_entropy = 1.1
    attr_vals = []
    for record in points:
        attr_vals.append(record[attr_index])
    np_arr = np.array(attr_vals)
    threshold = np_arr.min()
    max = np_arr.max()
    best_threshold = 0

    while threshold < max:
        left_class = []
        right_class = []
        for index in range(len(attr_vals)):
            if attr_vals[index] <= threshold:
                left_class.append(class_id[index])
            else:
                right_class.append(class_id[index])
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
        if prob_b == 0:
            right_entropy = 0 - (prob_a * math.log2(prob_a))
        elif prob_a == 0:
            right_entropy = 0 - (prob_b * math.log2(prob_b))
        else:
            right_entropy = 0 - (prob_b * math.log2(prob_b)) - (prob_a * math.log2(prob_a))

        weighted_entropy = ((len(left_class)/len(attr_vals)) * left_entropy)\
                           + (len(right_class)/len(attr_vals) * right_entropy)
        if weighted_entropy < best_entropy:
            best_entropy = weighted_entropy
            best_threshold = threshold
        threshold = threshold + bin_size
    # need to return weighted entropy, index to split, value to split at
    return [best_threshold, best_entropy]


def build_classification(fp, data, classification, level):
    best_rule_thresh = sys.float_info.max
    best_weighted_entropy = sys.float_info.max
    attr_index = -1

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
            majority_class = purity/abs(purity)
        fp.write('%s\tclass_id = %d\n' % (tabs, majority_class))
        return

    for index in range(len(data[0])):
        bin = 2
        if index == 1:
            bin = 4
        [thresh, entropy] = best_min_entropy_threshold(data, classification, bin, index)
        if entropy < best_weighted_entropy:
            best_rule_thresh = thresh
            best_weighted_entropy = entropy
            attr_index = index

    left_partition = []
    left_class = []
    right_partition = []
    right_class = []
    for row_index in range(len(data)):
        if data[row_index][attr_index] <= best_rule_thresh:
            left_partition.append(data[row_index])
            left_class.append(classification[row_index])
        else:
            right_partition.append(data[row_index])
            right_class.append(classification[row_index])
    fp.write('%sif data[%d] <= %d:\n' % (tabs, attr_index, best_rule_thresh))
    build_classification(fp, left_partition, left_class, level + 1)

    fp.write('%selse:\n' % tabs)
    build_classification(fp, right_partition, right_class, level + 1)
    return


# TODO: check that this is the way we want to store data
# Reads in the unlabeled data and stores the columns in an array
def read_input(fp):
    fp.write('if __name__ == \'__main__\':\n')
    fp.write('\tdata = []\n\n')
    fp.write('\t#reads in the unlabeled data from the csv\n')
    fp.write('\twith open(\'Abominable_VALIDATION_Data_FOR_STUDENTS_v750_2215.csv\', \'r\') as file:\n')
    fp.write('\t\tfile.readline()\n')
    fp.write('\t\tfor line in file:\n')
    fp.write('\t\t\trow = line.strip().split(",")\n')
    fp.write('\t\t\tfor val in row:\n')
    fp.write('\t\t\t\tdata.append(float(val))\n\n')


# The one rule classification for unlabeled data
def classify_data(fp, data, classification):
    fp.write('\t# classifies the unlabled data\n')
    fp.write('\tclassification = []\n')
    fp.write('\tclass_id = 0\n')
    fp.write('\tfor record in data:\n')
    build_classification(fp, data, classification, 0)
    fp.write('\t\tclassification.append(class_id)\n')


# Writes the now classified data to a csv file
# The order of the elements is the order the data was read in
def output_classification(fp):
    fp.write('\t# writes out the classifications to a csv\n')
    fp.write('\tfp = open(\'HW05_LastName_FirstName_MyClassifications.csv\', \'w\')\n')
    fp.write('\tfor class_type in classification:\n')
    fp.write('\t\tfp.write(\'%s\\n\' % class_type)\n')
    fp.write('\tfp.close()\n')


def write_decision_tree(data, classification):
    fp = open('HW05_LastName_FirstName_Trained_Classifier.py', 'w')

    read_input(fp)
    classify_data(fp, data, classification)
    output_classification(fp)

    fp.close()


if __name__ == '__main__':
    data = []
    classification = []
    with open('./Abominable_Data_HW_LABELED_TRAINING_DATA__v750_2215.csv', 'r') as dataFile:
        dataFile.readline()
        for line in dataFile:
            attributes = line.strip().split(",")
            values = []
            # quantize height to nearest 4 cm, every other attribute to nearest 2 value
            for index in range(0, len(attributes) - 2):
                val = float(attributes[index])
                if index == 1:
                    val = int(round(val / 4.0) * 4)
                else:
                    val = int(round(val / 2.0) * 2)
                values.append(val)
            classification.append(int(attributes[-1]))
            data.append(values)

    write_decision_tree(data, classification)
