#!/usr/bin/env python3

import csv
import os
import sys
import shutil
import parse
import argparse


def get_options():

    print(options)
    return options


def get_filelist(input_folder):

    # print(filelist)
    pass


def read_csv():
    # print(read_data)
    pass


def filter_filelist(all_files, ids, acronyms):

    filtered = []
    for f in all_files:
        if file_matches(f, ids, acronyms):
            filtered.append(f)
    print(filtered)
    return filtered


def file_matches(fname, ids, acronyms):

    parsed = parse.parse("parsing-format", os.path.basename(fname))
    return parsed["id"] in ids and parsed["acronym"] in acronyms


def copy_files(filtered_files, output_folder):

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    pass


def main():

    options = get_options()
    # all_files = get_filelist(options.input)
    # ids = read_csv(options.ids)
    # acronyms = read_csv(options.acronyms)
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
