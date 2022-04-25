import sys
import pandas as pd
import pynmea2 as nmea

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
    with open(gps_file) as file:
        # skip introductory lines that do not contain GPS data
        for _ in range(5):
            next(file)
        # for every record in GPS file
        for line in file:
            try:
                sentence = nmea.parse(line)
                line_split = line.split(",")
                if line_split[0] == "$GPGGA":
                    print("gpgga")
                    # this method needs the name of the kml file because
                    # we are only using GPGGA sentences to write kml
                    parse_gpgga(sentence, kml_file)
                elif line_split[0] == "$GPRMC":
                    print("gprmc")
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
