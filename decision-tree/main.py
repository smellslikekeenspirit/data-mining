# Prionti Nasir, Justin Palmer
import sys


# TODO
def best_thresh(points, class_id, bin_size, attr_index):
    # need to return weighted entropy, index to split, value to split at
    return [0, int(len(points)/2), 5.0]


def build_classification(fp, data, classification, level):
    best_rule_thresh = sys.float_info.max
    best_rule_index = -1

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
        attr_eval = best_thresh(data, classification, bin, index)
        if attr_eval[2] < best_rule_thresh:
            best_rule_thresh = attr_eval[0]
            best_rule_index = index
            split_index = attr_eval[1]

    fp.write('%sif data[%d] <= %d:\n' % (tabs, best_rule_index, best_rule_thresh))
    left_partition = data[:split_index+1]
    left_class = classification[:split_index+1]
    build_classification(fp, left_partition, left_class, level + 1)

    fp.write('%selse:\n' % tabs)
    right_partition = data[split_index:]
    right_class = classification[split_index+1:]
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
