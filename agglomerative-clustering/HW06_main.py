
import pandas
import os.path
import sys
import numpy


def read_data_file(data_file_name):
    data_file_path = os.path.join(os.getcwd(), data_file_name)
    if not os.path.exists(data_file_path):
        sys.exit("Provided data file could not be found.")
    data = pandas.read_csv(data_file_path, delimiter=',', index_col='ID')
    return data.astype(int)


def calculate_linkage(center1, center2):
    """
    calculate the Euclidean distance between two cluster centroids
    """
    # convert the Series to numpy.ndarray
    array1 = center1.to_numpy(dtype=float, copy=True)
    array2 = center2.to_numpy(dtype=float, copy=True)
    # square root of the sum of squared differences
    difference = array1 - array2
    squared = difference * difference
    squared_sum = squared.sum()
    return numpy.sqrt(squared_sum)


def initialize(dataframe):
    row_count = dataframe.shape[0]
    # an n-by-n matrix where cell (x, y) represents the distance between cluster x and cluster y
    # (x, x) cells will contain 0
    distances = [[0 for _ in range(row_count + 1)] for _ in range(row_count + 1)]
    clusters = {}
    for index, row in dataframe.iterrows():
        # make a dataframe out of a single row in the dataframe
        clusters[index] = pandas.DataFrame([row])
        # for every row otherRow except the current one,
        # calculate the distance from it to the current row
        for otherIndex, otherRow in dataframe.iterrows():
            if otherIndex > index:
                linkage = calculate_linkage(row, otherRow)
                distances[index][otherIndex] = linkage
                distances[otherIndex][index] = linkage
    return distances, clusters


def main():
    pandas.set_option('display.max_rows', 10)
    pandas.set_option('display.max_columns', 10)
    pandas.set_option('display.width', 100)

    data = read_data_file("HW_CLUSTERING_SHOPPING_CART_v2215H_test.csv")

    cross_correlation = data.corr()
    print(cross_correlation)
    distanceMatrix, clusters = initialize(data)


if __name__ == "__main__":
    main()
