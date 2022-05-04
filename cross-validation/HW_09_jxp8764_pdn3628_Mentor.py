import random
import numpy as np
import pandas
import pandas as pd
import os
import math
import matplotlib.pyplot as plot

STANDARD_BIN = 2
HEIGHT_BIN = 4

"""
The libraries and global variable needed in the trained program
"""


def file_header(file_pointer):
    file_pointer.write('import math\n')
    file_pointer.write('import os\n')
    file_pointer.write('import pandas\n')
    file_pointer.write('import sys\n\n')

    file_pointer.write('STANDARD_BIN = 2\n')
    file_pointer.write('HEIGHT_BIN = 4\n\n\n')


"""
Reads in the data in the train program and quantizes the data
"""


def read_input(file_pointer):
    # TODO: What should the data be rounded to?
    file_pointer.write('if __name__ == \'__main__\':\n')
    file_pointer.write('\t# reads in the data\n')
    file_pointer.write('\tdata_file_name = \'Abominable_VALIDATION_Data_FOR_STUDENTS_v770_2215.csv\'\n')
    file_pointer.write('\tdata_file_path = os.path.join(os.getcwd(), data_file_name)\n')
    file_pointer.write('\tdata = pandas.read_csv(data_file_path, delimiter=\',\')\n')
    file_pointer.write(
        '\tclean_data = data[[\'TailLn\', \'HairLn\', \'BangLn\', \'Reach\', \'EarLobes\', \'Age\']].round(decimals=0)\n')
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
    file_pointer.write('\t\tlambda x: math.floor(x / HEIGHT_BIN) * HEIGHT_BIN)\n\n')


"""
The classifier function, which has the decisions stumps to determine what class a record is
"""


def write_classifier(file_pointer, decision_stumps):
    file_pointer.write('def classifier(record):\n')
    file_pointer.write('\tanswer = 0\n\n')

    # Decision Stumps
    for index in range(len(decision_stumps)):
        [attr_index, sign, threshold] = decision_stumps[index]
        file_pointer.write('\t# Decision Stump Number %s\n' % (index + 1))
        file_pointer.write('\tif record[\'%s\'] %s %s:\n' % (attr_index, sign, threshold))
        file_pointer.write('\t\tanswer = answer - 1\n')
        file_pointer.write('\telse:\n')
        file_pointer.write('\t\tanswer = answer + 1\n\n')

    # Return result
    file_pointer.write('\tif answer < 0:\n')
    file_pointer.write('\t\treturn -1\n')
    file_pointer.write('\telse:\n')
    file_pointer.write('\t\treturn 1\n\n\n')


"""
Prints and writes out the classifications of the data
"""


def call_classifier(file_pointer):
    file_pointer.write('\t# Writes and prints out the classification results\n')
    file_pointer.write('\tfile = open(\'HW_09_jxp8764_pdn3628_Classification.csv\', \'w\')\n')
    file_pointer.write('\tfor index, record in clean_data.iterrows():\n')
    file_pointer.write('\t\tclass_id = classifier(record)\n')
    file_pointer.write('\t\tprint(class_id)\n')
    file_pointer.write('\t\tfile.write(\'%s\\n\' % class_id)\n')
    file_pointer.write('\tfile.close()\n')


"""
Generates of the decisions for all of the stumps
"""


def create_classifiers(data, class_ids, stump_count):
    # The range of each of the attributes
    attr_range = []
    for column in data.columns.drop('ClassID'):
        column_values = data[column]
        attr_range.append([column_values.min(), column_values.max()])

    # Decisions for n stumps
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
            if values.iloc[index] <= threshold:
                if int(class_ids.iloc[index]) == -1:
                    hit = hit + 1
                else:
                    miss = miss + 1
            else:
                if int(class_ids.iloc[index] == 1):
                    hit = hit + 1
                else:
                    miss = miss + 1

        if hit > miss:
            sign = '<='
        else:
            sign = '>'
        decisions.append([attr_index, sign, threshold])

    return decisions


"""
Classifies the data based on the decision stumps
"""


def classify_data(decisions, record):
    answer = 0
    # classify by using all the stumps
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


def plot_mistakes(mistakes):
    plot.plot(mistakes.keys(), mistakes.values())
    plot.show()


"""
Determines which number of stumps to use based on n-fold cross validation
"""


def cross_validation(n_stumps, data, n_folds=10):
    # number of records to have in each fold
    number_of_records_per_fold = int(len(data) / n_folds)
    # dictionary of data subsets, this will have n_folds number of folds
    folds = {}
    # separating assam data
    data_assam = data[data['ClassID'] == -1]
    # separate bhutan data
    data_bhutan = data[data['ClassID'] == 1]
    # flag for inserting assam and bhutan records alternatively
    toggle = 0

    # do this n_folds times
    for num_fold in range(n_folds):
        # make a new fold
        fold = []
        # insert number_of_records_per_fold number of records into it
        # with about 50% random assam data and 50% random bhutan data
        for record_index in range(number_of_records_per_fold):
            if toggle == 0:
                r = random.randint(0, len(data_assam)-1)
                fold.append(data_assam.iloc[r])
                toggle = 1
            else:
                r = random.randint(0, len(data_bhutan)-1)
                fold.append(data_bhutan.iloc[r])
                toggle = 0
        # convert the list of records back to a dataframe
        fold = pandas.DataFrame(fold)
        # add this dataframe to the "shelf" labeled with the appropriate fold_number
        folds[num_fold] = fold

    # make a dictionary that will have the number of mistakes per stump number
    mistakes = {}
    # for every stump number
    for count in n_stumps:
        # initialize mistakes count to 0
        mistakes[count] = 0
        # for 10 folds
        for test_fold in range(0, n_folds):
            # initialize training dataset
            training_data = []
            # for all folds in the folds dictionary
            for fold_number in folds.keys():
                # as long as this fold is not the nth fold (which will be set aside as testing data)
                if fold_number != test_fold:
                    # add fold to training data
                    training_data.append(folds[fold_number])
            # merge the list of folds into a single dataframe of training data for convenience
            training_data = pandas.concat(training_data, axis=0)
            # create classifier of the current stump number using training data
            decision_stumps = create_classifiers(training_data, training_data['ClassID'], count)
            # for every record in the testing set which is kept in the nth position of the folds dictionary
            for index, record in folds[test_fold].iterrows():
                # let classifier with the current stump number decide its class
                classifier_decision = classify_data(decision_stumps, record)
                # if the decision does not match the record's actual label
                if record['ClassID'] != classifier_decision:
                    # increment mistakes for classifier with the current stump number
                    mistakes[count] += 1

    for count in n_stumps:
        mistakes[count] /= len(data)
    print(mistakes)
    plot_mistakes(mistakes)

    least_mistakes = 1
    for stump in n_stumps:
        if mistakes[stump] < mistakes[least_mistakes]:
            least_mistakes = stump
    return least_mistakes


"""
Reads in and quantizes the data
"""


def read_data_file(data_file_name):
    data_file_path = os.path.join(os.getcwd(), data_file_name)
    data = pd.read_csv(data_file_path, delimiter=',') \
        .drop(columns=['ClassName']).astype(int)
    clean_data = data[['TailLn', 'HairLn', 'BangLn', 'Reach', 'EarLobes', 'Age', 'ClassID']].round(decimals=0)
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
    # Cast everything to integer.
    return clean_data.astype(int)


"""
Clears the Classifier, then writes out a new one with the best number of stumps to use
"""

if __name__ == '__main__':
    n_stumps = [1, 2, 4, 8, 10, 20, 25, 35, 50, 75, 100, 150, 200, 250, 300, 400]
    # the classifier should do nothing for now
    file_clear = open('HW_09_jxp8764_pdn3628_Classifier.py', 'w')
    file_clear.write('def classifier(record):\n')
    file_clear.write('\traise Exception(\'Sorry, file not done\')\n\n')
    file_clear.close()

    labeled_data = read_data_file('Abominable_Data_HW_LABELED_TRAINING_DATA__v770_2215.csv')
    best_number_of_stumps = cross_validation(n_stumps, labeled_data)
    print('Best Number of Stumps: %s\n' % best_number_of_stumps)

    decision_stumps = create_classifiers(labeled_data, labeled_data['ClassID'], best_number_of_stumps)
    file_classify = open('HW_09_jxp8764_pdn3628_Classifier.py', 'w')

    file_header(file_classify)
    write_classifier(file_classify, decision_stumps)
    read_data_file(file_classify)
    call_classifier(file_classify)

    file_classify.close()
