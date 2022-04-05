# Prionti Nasir, Justin Palmer
import sys


def best_thresh(points, class_id, bin_size, attr_index):
    # need to return weighted entropy, index to split, value to split at
    return 0


def build_classification(data, classification, level):
    best_rule_thresh = sys.float_info.max
    best_rule_index = -1

    purity = 0.0
    for class_id in classification:
        purity += class_id
    purity /= len(classification)

    if level > 10 or abs(purity) > .95 or len(data) < 9:
        majority_class = 1
        if purity != 0:
            majority_class = purity/purity
        # write class = ... statement
        return

    for index in range(len(data[0])):
        bin = 2
        if index == 1:
            bin = 4
        attr_eval = best_thresh(data, classification, bin, index)
        if attr_eval[2] < best_rule_thresh:
            best_rule_thresh = attr_eval[0]
            best_rule_index = attr_eval[1]

    left_partition = data[:best_rule_index+1]
    left_class = classification[:best_rule_index+1]
    build_classification(left_partition, left_class, level + 1)

    right_partition = data[best_rule_index+1:]
    right_class = classification[best_rule_index+1:]
    build_classification(right_partition, right_class, level + 1)
    return


# Reads in the unlabeled data and stores the columns in an array
def read_input(fp):
    fp.write('if __name__ == \'__main__\':\n')
    fp.write('\tdata = [[], []]\n\n')
    fp.write('\t#reads in the unlabeled data from the csv\n')
    fp.write('\twith open(\'Abominable_VALIDATION_Data_FOR_STUDENTS_v750_2215.csv\', \'r\') as file:\n')
    fp.write('\t\tfile.readline()\n')
    fp.write('\t\tfor line in file:\n')
    fp.write('\t\t\trow = line.strip().split(",")\n')
    fp.write('\t\t\tdata[0].append(float(row[0]))\n')
    fp.write('\t\t\tdata[1].append(float(row[1]))\n\n')


# The one rule classification for unlabeled data
def classify_data(fp, threshold, left_class, right_class, attr):
    fp.write('\t# classifies the unlabled data\n')
    fp.write('\tclassification = []\n')
    fp.write('\tfor attr in data[%d]:\n' % attr)
    # this needs to be changes to use the classifier build by the decision tree
    # fp.write('\t\tif attr <= %d:\n' % threshold)
    # fp.write('\t\t\tclass_id = \'%s\'\n' % left_class)
    # fp.write('\t\telse:\n')
    # fp.write('\t\t\tclass_id = \'%s\'\n' % right_class)
    # fp.write('\t\tprint(class_id)\n')
    # fp.write('\t\tclassification.append(class_id)\n\n')


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
    classify_data(fp, threshold, left_class, right_class, attr)
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
                val = int(attributes[index])
                if index == 1:
                    val = int(round(val / 4.0) * 4)
                else:
                    val = int(round(val / 2.0) * 2)
                values.append(val)
            classification.append(int(attributes[-1]))
            data.append(values)

    write_decision_tree(data, classification)
