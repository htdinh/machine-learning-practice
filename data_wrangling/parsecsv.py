#!/usr/bin/env python
"""
Your task is to process the supplied file and use the csv module to extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. You should extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
You can use the csv modules "reader" method to get data in such format.
Another useful method is next() - to get the next line from the iterator.
You should only change the parse_file function.
"""
import csv
import os

DATADIR = ""
DATAFILE = "745090.csv"


def parse_file(datafile):
    name = ""
    data = []
    first_line_been_read = False # First line has not been read
    with open(datafile,'rb') as f:
        # Reference: https://docs.python.org/2/library/csv.html
        filereader = csv.reader(f, delimiter=',')
        line_index = 0
        for line in filereader: # Each line is now a list
            # "print line", line
            if line_index == 0:
                name = line[1] # Check the CSV file to know the position of the station name
                first_line_been_read = True  # To indicate that the first line has been read
            elif line_index >= 2:  # Only store data from 2nd line (1st line is the header)
                data.append(line)
            line_index += 1

    # Do not change the line below
    return (name, data)


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)
    # print list(name), list("MOUNTAIN VIEW MOFFETT FLD NAS") # To check the characters of the string
    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    # print data[0] # To check what is the data returned by the method parse_file
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()