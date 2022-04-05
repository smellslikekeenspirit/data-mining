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


def write_decision_tree():
   print('tmp')


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

    build_classification(data, classification)
