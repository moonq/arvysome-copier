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
    return filtered


def file_matches(fname, ids, acronyms):
    """ Return True if file parses to predefined format, and matches found in IDs and acronyms """
    parsed = parse.parse("{id}_{acronym} {the_rest}", os.path.basename(fname))
    if not parsed:
        # file name does not match our parsing format!
        print("Not parsed! {}".format(fname))
        return False
    id_matches = parsed["id"] in ids
    acronym_matches = parsed["acronym"] in acronyms
    print(f"'{fname}' id:{str(id_matches)[0]} acr:{str(acronym_matches)[0]}")
    return id_matches and acronym_matches


def copy_files(filtered_files, output_folder):
    """ Copy list of files to a folder """

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
 
    for input_file in filtered_files:
        output_file = os.path.join(output_folder, os.path.basename(input_file))
        shutil.copy2(input_file,output_file)
        print(".", end="")
    print("")

                     
def main():
    """ Performs all the steps """

    options = get_options()
    all_files = get_filelist(options.input)
    ids = read_csv(options.ids)
    acronyms = read_csv(options.acronyms)
    filtered_files = filter_filelist(
        all_files,
        ids,
        acronyms
    )
    copy_files(
        filtered_files,
        options.output
    )


if __name__ == "__main__":
    main()
