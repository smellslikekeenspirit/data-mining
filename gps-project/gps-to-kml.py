import sys
import pandas as pd
import pynmea2 as nmea
import geographiclib.geodesic as geo
import datetime
from datetime import tzinfo

df = pd.DataFrame(columns=["ID", "Time", "Latitude", "Longitude", "Altitude"])


def write_to_file(file_name, string_to_append):
    """
    appends given string to the end of given file
    :param file_name: name of file to append to
    :param string_to_append: string to append to file
    :return: None
    """
    file = open(file_name, "a")
    file.write(string_to_append)
    file.close()


def parse_gprmc(sentence):
    """
    parses a GPRMC sentence
    :param sentence: sentence of GPRMC format
    :return: None
    """
    latitude = format(round(sentence.latitude, 6), ".6f")
    longitude = format(round(sentence.longitude, 6), ".6f")
    time = sentence.timestamp

    dataframe_row = ["$GPRMC", time, latitude, longitude, 0]
    # append line to the end of the dataframe
    df.loc[len(df)] = dataframe_row


def parse_gpgga(sentence, kml_file):
    """
    parses a GPGGA sentence
    :param sentence: sentence of GPGGA format
    :param kml_file: file to write sentence to
    :return: None
    """
    latitude = format(round(sentence.latitude, 6), ".6f")
    longitude = format(round(sentence.longitude, 6), ".6f")
    altitude = sentence.altitude  # altitude
    time = sentence.timestamp

    string_to_append_to_kml = str(longitude) + "," + str(latitude) + "," + str(altitude) + "\n"
    dataframe_row = ["$GPGGA", time, latitude, longitude, altitude]

    # append line to the end of the dataframe
    df.loc[len(df)] = dataframe_row
    # append line to end of kml file
    write_to_file(kml_file, string_to_append_to_kml)


# TODO: is this enought for checking before parsing?
def valid_gpgga(sentence):
    if len(sentence) != 15:
        return False
    return True


def valid_gprmc(sentence):
    if len(sentence) != 13:
        return False
    return True

def elapsed_seconds(start, end):
    if len(start) != len(end) != 10:
        # not the proper format
        return -1
    hours = (int(end[0:2]) - int(start[0:2])) * 3600
    minutes = (int(end[2:4]) - int(start[2:4])) * 60
    seconds = int(end[4:6]) - int(start[4:6])
    millis = float(end[6:]) - float(start[6:])
    return ((int(end[0:2]) - int(start[0:2])) * 3600) + ((int(end[2:4]) - int(start[2:4])) * 60) + (int(end[4:6]) - int(start[4:6])) + (float(end[6:]) - float(start[6:]))



# Calcuation the bearings hear and getting the dif
def angle_dif(origin, coord, cur_loc):
    bear_one = geo.Geodesic.WGS84.Inverse(origin[0], origin[1], coord[0], coord[1])['azi1']
    bear_two = geo.Geodesic.WGS84.Inverse(origin[0], origin[1], cur_loc[0], cur_loc[1])['azi1']
    return abs(bear_one - bear_two)


def kml_writer(gps_file, kml_file):
    """
    iterates over records in the GPS file and populates corresponding KML file
    :param gps_file: name of text file containing GPS data
    :param kml_file: name of kml file to produce
    :return: None
    """
    # write header to kml file
    header = open("kml_header.txt", "r").read()
    write_to_file(kml_file, header)
    start_track = False
    stopped = False
    stopped_time = -1
    straight_line = False
    start_loc = []
    second_loc = []
    cur_loc = []
    with open(gps_file) as file:
        # skip introductory lines that do not contain GPS data
        for _ in range(5):
            next(file)
        # for every record in GPS file
        for line in file:
            try:
                sentence = nmea.parse(line)
                line_split = line.split(",")
                # print(str(line_split) + " ", end="")
                if line_split[0] == "$GPGGA":
                    if not valid_gpgga(line_split):
                        continue
                    lat = float(line_split[2])
                    long = float(line_split[6])
                    # print("gpgga")
                    # this method needs the name of the kml file because
                    # we are only using GPGGA sentences to write kml
                    if start_track and (not straight_line and not stopped):
                        parse_gpgga(sentence, kml_file)
                    if stopped:
                        # reset straight line tracking
                        start_loc = []
                        cur_loc = []
                        second_loc = []
                        straight_line = False
                    else:
                        if len(start_loc) == 0:
                            start_loc = [lat, long]
                        elif len(second_loc) == 0:
                            second_loc = [lat, long]
                        else:
                            cur_loc = [lat, long]

                    if len(cur_loc) != 0:
                        if angle_dif(start_loc, second_loc, cur_loc) < 1:
                            straight_line = True
                        else:
                            start_loc = second_loc
                            second_loc = cur_loc
                elif line_split[0] == "$GPRMC":
                    if not valid_gprmc(line_split):
                        continue
                    # print("gprmc")
                    # car has started moving
                    speed = float(line_split[7])
                    if speed >= 1:
                        start_track = True

                    # car has stopped
                    if speed < 1:
                        # weren't stopped until now, car has just stopped
                        if not stopped:
                            stopped = True
                            stopped_time = line_split[1]
                    else:
                        # have been stopped up until now
                        if stopped:
                            stopped = False
                            elapsed = elapsed_seconds(stopped_time, line_split[1])

                            # if stopped for more than 3 minutes
                            if elapsed > 180:
                                print("elapsed: " + str(elapsed) + " from " + stopped_time + " to " + line_split[1])
                    parse_gprmc(sentence)
            except nmea.ParseError as e:
                # if there is an error, report and skip
                print('Error: {}'.format(e))
                continue
    # write footer to kml file
    footer = open("kml_footer.txt", "r").read()
    write_to_file(kml_file, footer)


def main():
    if len(sys.argv) != 3:
        # prompt user to provide a filename with GPS data
        # and a filename under which the kml file will be stored
        print("Usage: python3 gps-to-kml.py gps-input-file.txt kml-output-file.kml")
        exit()
    gps_file, kml_file = sys.argv[1], sys.argv[2]
    kml_writer(gps_file, kml_file)


if __name__ == '__main__':
    main()
