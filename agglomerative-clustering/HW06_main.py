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
    array1 = numpy.array(center1) # center1.to_numpy(dtype=float, copy=True)
    array2 = numpy.array(center2) # center2.to_numpy(dtype=float, copy=True)
    # square root of the sum of squared differences
    difference = array1 - array2
    squared = difference * difference
    squared_sum = squared.sum()
    return numpy.sqrt(squared_sum)


def calc_center_of_mass(attributes):
    result = [0 for _ in range(len(attributes[0]))]
    for record in attributes:
        for i in range(len(record)):
            result[i] += record[i]

    for i in range(len(result)):
        result[i] /= len(attributes)

    return result


def initialize(dataframe):
    row_count = dataframe.shape[0]
    # an n-by-n matrix where cell (x, y) represents the distance between cluster x and cluster y
    # (x, x) cells will contain 0
    distances = [[calc_center_of_mass([row.tolist()]), [row.tolist()]] for _, row in dataframe.iterrows()]
    clusters = {}
    merged_clusters = []

    while len(distances) > 1:
        cluster_one = 0
        cluster_two = 1
        best_dist = sys.float_info.max
        for c1_index in range(len(distances) - 1):
            for c2_index in range(c1_index + 1, len(distances)):
                cluster_dist = calculate_linkage(distances[c1_index][0], distances[c2_index][0])
                if cluster_dist < best_dist:
                    best_dist = cluster_dist
                    cluster_one = c1_index
                    cluster_two = c2_index
        removed = distances.pop(cluster_two)
        merged_clusters.append(min(len(distances[cluster_one][1]), len(removed[1])))
        attributes = distances[cluster_one][1]
        attributes.extend(removed[1])
        distances[cluster_one] = [calc_center_of_mass(attributes), attributes]
    print(merged_clusters)
    return distances, clusters


def main():
    pandas.set_option('display.max_rows', 10)
    pandas.set_option('display.max_columns', 10)
    pandas.set_option('display.width', 100)

    data = read_data_file("HW_CLUSTERING_SHOPPING_CART_v2215H_test.csv")

    print(data)
    print("did the data")
    cross_correlation = data.corr()
    # print(cross_correlation)
    distanceMatrix, clusters = initialize(data)


if __name__ == "__main__":
    main()
