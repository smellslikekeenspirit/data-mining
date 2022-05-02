"""
Authors: Prionti Nasir
HW07
"""

import pandas
import os.path
import sys
import numpy
from numpy.linalg import eig
from matplotlib import pyplot as plt
from scipy import cluster


def read_data_file(data_file_name):
    """
    reads csv file and converts into dataframe
    :param data_file_name: file name
    :return: data in int
    """
    data_file_path = os.path.join(os.getcwd(), data_file_name)
    if not os.path.exists(data_file_path):
        sys.exit("Provided data file could not be found.")
    data = pandas.read_csv(data_file_path, delimiter=',', index_col='ID')
    return data.astype(int)


def main():
    pandas.set_option('display.max_rows', 20)
    pandas.set_option('display.max_columns', 20)
    pandas.set_option('display.width', 250)

    data = read_data_file("HW_CLUSTERING_SHOPPING_CART_v2215H.csv")

    covariance_matrix = data.cov().round(2)
    print(covariance_matrix)
    eigenvalues, eigenvectors = eig(covariance_matrix)
    print(eigenvectors.round(2))


if __name__ == "__main__":
    main()
