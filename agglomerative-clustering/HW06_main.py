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


def calc_center_of_mass(attributes):
    return attributes.mean()


def agglomerate(distances, clusters):
    merged_cluster_sizes = []
    while len(clusters) > 1:
        lowest_distance = sys.float_info.max
        this_index = 0
        other_index = 0

        # compare every cluster against every other cluster and
        # find the two closest to each other
        for start in clusters.keys():
            for end in clusters.keys():
                # ensure start smaller than end for consistent merging
                if start >= end:
                    continue
                # if distance is lower than the current lowest value, save it
                if distances[start][end] < lowest_distance:
                    lowest_distance = distances[start][end]
                    this_index = start
                    other_index = end

        # merge the clusters by combining their records
        # start/this_index which is the smaller number represents the updated cluster
        # save the size of the smaller cluster being merged
        merged_cluster_sizes.append(min(clusters[other_index].shape[0], clusters[this_index].shape[0]))
        clusters[this_index] = pandas.concat([clusters[this_index], clusters[other_index]], ignore_index=True)
        # remove the merged cluster
        del clusters[other_index]

        # recompute distances of updated cluster to all remaining clusters
        for other_index in clusters.keys():
            linkage = calculate_linkage(calc_center_of_mass(clusters[other_index]),
                                        calc_center_of_mass(clusters[this_index]))
            distances[this_index][other_index] = linkage
            distances[other_index][this_index] = linkage

        if len(clusters) == 2:
            for k, v in clusters.items():
                print(v.shape[0])
                print(calc_center_of_mass(clusters[k]))

    print(merged_cluster_sizes)


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
    pandas.set_option('display.max_rows', 20)
    pandas.set_option('display.max_columns', 20)
    pandas.set_option('display.width', 250)

    data = read_data_file("HW_CLUSTERING_SHOPPING_CART_v2215H.csv")

    cross_correlation = data.corr().round(2)
    print(cross_correlation)
    distance_matrix, clusters = initialize(data)
    agglomerate(distance_matrix, clusters)


if __name__ == "__main__":
    main()
