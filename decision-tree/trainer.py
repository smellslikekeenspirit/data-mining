import pandas
import os.path
import sys
import math
from datetime import date

TRAINED_FILE_NAME = "HW05_jxp8764_pdn3628_Trained_Classifier2.py"
AGE_BIN = 2
HEIGHT_BIN = 4
MIN_NUMBER_IN_NODE = 9
NODE_THRESHOLD = 0.95


class DecisionNode:
    def __init__(self, attribute, threshold, classification, if_group, else_group):
        self.attribute = attribute
        self.threshold = threshold
        self.classification = classification
        self.if_group = if_group
        self.else_group = else_group


def fwrite(string, target_file, tabs=0, newlines=1):
    """Add a number of tab characters to the front of a string."""
    target_file.write('\t' * tabs + string + '\n' * newlines)


def prolog(file_ptr):
    depth = 0
    file_ptr.write("import os.path\nimport sys\nimport pandas\nfrom math import floor\n\n")
    file_ptr.write("AGE_BIN = {0}\nHEIGHT_BIN = {1}\n\n".format(AGE_BIN, HEIGHT_BIN))

    file_ptr.write("def read_data_file(data_file_name):")
    depth += 1
    # function body
    file_ptr.write("\tcwd = os.getcwd()\n")
    file_ptr.write("\tdata_file_path = os.path.join(os.getcwd(), data_file_name)\n\n")
    file_ptr.write("\tdata = pandas.read_csv(data_file_path, delimiter=',')\n\n")

    # Clean the data before using it; quantize or round attributes.
    file_ptr.write("\tclean_data = data[[\'TailLn\', \'HairLn\', \'BangLn\', \'Reach\'"
                   "]].round(decimals=0)\n\n")

    fwrite("\tclean_data[\'Age\'] = data[\'Age\'].apply(lambda x: floor(x / "
           "AGE_BIN_SIZE) * AGE_BIN_SIZE)", file_ptr, depth)
    fwrite("\tclean_data['Ht'] = data['Ht'].apply(lambda x: floor(x / "
           "HEIGHT_BIN_SIZE) * HEIGHT_BIN_SIZE)", file_ptr, depth)
    fwrite("\tclean_data[\'Class\'] = data[\'ClassID\']",
           file_ptr, depth, newlines=2)
    fwrite("# Cast everything to integer.", file_ptr, depth)
    fwrite("return clean_data.astype(int)", file_ptr, depth, newlines=3)


def write_tree(file_ptr, tree, indent):
    """Recursive function for writing a DecisionNode tree into a file as an
    if-else chain.
    :param file_ptr: open file object to write to
    :param tree: <DecisionNode | str> An object representing the classifier to
        write in the trained program file
    :param indent: <int> Current indentation (in tabs) in the output .py file.
    :return: None
    """
    if isinstance(tree, DecisionNode):
        fwrite("if row.{0} >= {1}:".format(tree.attribute, tree.threshold),
               file_ptr, tabs=indent)
        write_tree(file_ptr, tree.if_group, indent + 1)
        fwrite("else:", file_ptr, tabs=indent)
        write_tree(file_ptr, tree.else_group, indent + 1)
    else:
        fwrite("print(row.ClassID, \'{0}\')".format(tree),
               file_ptr, tabs=indent)


def write_body(file_ptr, tree):
    """Write the main function of the trained program, incorporating the
    provided, predetermined attribute in order to guess which people will be
    sick using a One Rule.
    :param file_ptr: open file object to write the program into
    :param tree: <DecisionNode | str> An object representing the classifier to
        write in the trained program file as an if-else chain.
    :return: None
    """
    depth = 0
    # The body will only consist of the main function.
    # Function def
    fwrite("def main(data_file_name):", file_ptr, depth)

    # Docstring
    depth += 1
    fwrite("\"\"\"Read the data from the provided file then attempt to "
           "classify it using", file_ptr, depth)
    fwrite("a decision tree. Each decision node makes a binary split on an "
           "integer threshold.", file_ptr, depth, 2)
    fwrite(":param data_file_name: <str> Name of the CSV file of CDC data to",
           file_ptr, depth)
    fwrite("make predictions for.", file_ptr, depth)
    fwrite(":return: None", file_ptr, depth)
    fwrite("\"\"\"", file_ptr, depth)

    # Code
    fwrite("testing_data = read_data_file(data_file_name)", file_ptr, depth, 2)
    fwrite("for row in testing_data.itertuples(index=False):",
           file_ptr, depth)
    # For loop
    depth += 1
    write_tree(file_ptr, tree, depth)

    # Add another blank line at the end of the function.
    fwrite("", file_ptr, depth, newlines=1)


def epilog(file_ptr):
    """Write the conditional for main programs and close the file.
    :param file_ptr: open file to handle
    :return: None
    """
    fwrite("\nif __name__ == \"__main__\":", file_ptr)
    fwrite("main(sys.argv[1])", file_ptr, 1, 2)
    file_ptr.flush()
    file_ptr.close()


def read_data_file(data_file_name):
    """Given a file name, locate, open, and read the file. The file is assumed
    to be a CSV file and its data will be parsed accordingly and returned as a
    pandas dataframe.
    :param data_file_name: <str> name of CSV file to read data from
    :return: <Pandas.DataFrame> all data read from data_file_name
    """
    # Assume the data file is in the current working directory.
    cwd = os.getcwd()
    data_file_path = os.path.join(os.getcwd(), data_file_name)

    # If it isn't present, check the parent folder.
    if not os.path.exists(data_file_path):
        super_folder = os.path.dirname(cwd)
        data_file_path = os.path.join(super_folder, data_file_name)

        # If it still can't be found, exit.
        if not os.path.exists(data_file_path):
            sys.exit("Provided data file could not be found.")

    # We have found the file and can extract the data.
    data = pandas.read_csv(data_file_path, delimiter=',')

    # Round TailLn, HairLn, BangLn, Reach
    clean_data = data[['TailLn', 'HairLn', 'BangLn', 'Reach']].round(decimals=0)

    # Quantize the age by their respective bin sizes and save the new columns
    # Into the clean data frame.
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
    clean_data['Class'] = data['ClassName']

    # Exchange Assam for 1 and Bhuttan for -1.
    clean_data = clean_data.replace({'Class': {'Assam': -1, 'Bhuttan': +1}})

    # Cast everything to integer.
    return clean_data.astype(int)


def gini(dataframe):
    """Calculate the GINI index for a given Pandas dataframe.
    :param dataframe: <Pandas.DataFrame> The set of records.
    :returns: <float> the GINI index
    """
    total_records = dataframe.shape[0]
    positive_count = dataframe[dataframe['Class'] > 0].shape[0]

    # Relative probability of Assam (a) or Bhutan (b).
    probability_a = positive_count / total_records
    probability_b = (total_records - positive_count) / total_records

    return 1 - math.pow(probability_a, 2) - math.pow(probability_b, 2)


def build_classifier(training_data, depth=0):
    """Recursively construct a decision tree comprised of DecisionNode objects
    and strings representing the classification or, in terms of a tree, a leaf
    node.
    :param training_data: <Pandas.DataFrame> Data to learn a decision tree for.
    :param depth: <int> Current depth of the decision tree.
    :return: <DecisionNode | str> A decision tree for classifying abominable
        snow folk.
    """
    # Number of rows in the current dataframe.
    parent_record_count = training_data.shape[0]

    # Number of rows with Class == +1
    positive_count = training_data[training_data['Class'] > 0].shape[0]
    print(parent_record_count)
    print(positive_count)

    # Base case conditions.
    # If the node is very small...
    if parent_record_count < MIN_NUMBER_IN_NODE:
        if positive_count / parent_record_count >= 0.5:
            return '+1'
        else:
            return '-1'
    # If most of the nodes belong to one class...
    elif positive_count / parent_record_count >= NODE_THRESHOLD:
        return '+1'
    elif positive_count / parent_record_count < (1 - NODE_THRESHOLD):
        return '-1'
    # If the tree is becoming too complex...
    elif depth >= 10:
        if positive_count / parent_record_count >= 0.5:
            return '+1'
        else:
            return '-1'

    best_attribute = None
    best_threshold = None
    associated_class = None
    best_gini = 1.0

    # For each column/attribute in the dataframe...
    for attribute in training_data.columns.drop('Class'):

        # For every integer value between the min and max values for this
        # attribute...
        for threshold in range(training_data[attribute].min() + 1,
                               training_data[attribute].max() + 1):

            # All records for which this attribute is greater than or equal to
            # the threshold.
            meets_thresh = \
                training_data[training_data[attribute] >= threshold]

            # All records for which this attribute is below the threshold.
            below_thresh = \
                training_data[training_data[attribute] < threshold]

            # Weighted GINI index for the records at the threshold and above.
            weighted_gini = (meets_thresh.shape[0] / parent_record_count) * \
                            gini(meets_thresh)

            # Add in the weighted GINI index for the remaining records.
            weighted_gini += (below_thresh.shape[0] / parent_record_count) * \
                             gini(below_thresh)

            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_attribute = attribute
                best_threshold = threshold

    # What goes into the if body in the decision tree.
    ingroup = build_classifier(
        training_data[training_data[best_attribute] >= best_threshold],
        depth + 1)

    # What goes into the else body in the decision tree.
    outgroup = build_classifier(
        training_data[training_data[best_attribute] < best_threshold],
        depth + 1)

    # Return an object containing all the necessary information for printing
    # the code of the corresponding decision tree node, and its children.
    return DecisionNode(best_attribute, best_threshold, associated_class,
                        ingroup, outgroup)


def main(training_file_name):
    """Main function.
    Determine the best classification attribute and threshold, then write the
    training program using this information.
    :param training_file_name: <str> name of the training data file
    :return: None
    """
    data = read_data_file(training_file_name)
    print(data)
    classifier = build_classifier(data)
    print(classifier)
    trained_file = open(TRAINED_FILE_NAME, mode='w')
    prolog(trained_file)
    write_body(trained_file, classifier)
    epilog(trained_file)


if __name__ == "__main__":
    main(sys.argv[1])
