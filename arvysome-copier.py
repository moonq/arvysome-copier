#!/usr/bin/env python3

import csv
import os
import sys
import shutil
import parse
import argparse


def get_options():
    """ Reads user options, and returns as object """
    parser = argparse.ArgumentParser()
    parser.add_argument(
               "--input",
                action="store",
                help="Path to input data",
                required = True
            )
    parser.add_argument(
               "--output",
                action="store",
                help="Path to output data",
                required = True
            )
    parser.add_argument(
               "--ids",
                action="store",
                help="file name with IDs",
                required = True
            )
    parser.add_argument(
               "--acronyms",
                action="store",
                help= "file name with acronyms",
                required = True
            )
    options = parser.parse_args()
    # input folder, output folder, file of ids, file of acronyms
    #print(options)
    return options


def get_filelist(input_folder):
    """ Recursively create list of all files with paths """
    
    filelist = []
    for root, dirs, files in os.walk(input_folder):
        for file in files:
	        filelist.append(os.path.join(root,file))
    
    #print(filelist)
    return filelist


def read_csv(path):
    """ Reads a file and returns its contents as a list """
    
    read_data = []
    with open(path,'rt') as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            read_data.append(row[0]) 
       
    #print(read_data)
    return read_data


def filter_filelist(all_files, ids, acronyms):
    """ Removes non-matching entries from a file list """

    filtered = []
    for f in all_files:
        if file_matches(f, ids, acronyms):
            filtered.append(f)
    print(filtered)
    return filtered


def file_matches(fname, ids, acronyms):
    """ Return True if file parses to predefined format, and matches found in IDs and acronyms """
    parsed = parse.parse("parsing-format", os.path.basename(fname))
    return parsed["id"] in ids and parsed["acronym"] in acronyms


def copy_files(filtered_files, output_folder):
    """ Copy list of files to a folder """
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    pass


def main():
    """ Performs all the steps """

    options = get_options()
    all_files = get_filelist(options.input)
    ids = read_csv(options.ids)
    acronyms = read_csv(options.acronyms)
    # filtered_files = filter_filelist(
    #    all_files,
    #    ids,
    #    acronyms
    # )
    # copy_files(
    #    filtered_files,
    #    options.output
    # )


if __name__ == "__main__":
    main()
