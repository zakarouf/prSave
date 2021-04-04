#!/usr/bin/env python3
import argparse
import os
from datetime import datetime
from datetime import timedelta
from subprocess import Popen
import sys

SELF_CONFIG_FILE_NAME = "prSave.conf"

ARCHIVE_CONFIG_FILE_NAME = "prSave.archive.conf"
ARCHIVE_LOG_FILE_NAME = "prSave.log.txt"



ARCHIVE_SYNTX__ARFOLDER = "ar"
ARCHIVE_SYNTX__START = "---"

def run(commands):
    Popen(commands).wait()


def create_new():
    try:
        fp = open(ARCHIVE_CONFIG_FILE_NAME, "r")
        confirm = input("An Archive Instance Already Exist <Overwrite> (Y)es|(N)o|(E)dit: ")
        if confirm.lower() == 'y':
            pass
        fp.close()

    except FileNotFoundError:
        pass

    fp = open(ARCHIVE_CONFIG_FILE_NAME, "w")
    fp.write(ARCHIVE_SYNTX__START)

    _tmp = input("Set Archive Folder (absolute path): ")
    if _tmp[-1] != '/':
        _tmp += '/'
    _tmp += "\n"
    fp.write(ARCHIVE_SYNTX__ARFOLDER + " !" + _tmp)

    fp.close()

    print("DONE!")


ARCHIVE_data__ar = ""

def do_archive(set_arfolder, set_ifdisable_log):
    global ARCHIVE_data__ar

    data = []
    try:
        fp = open(ARCHIVE_CONFIG_FILE_NAME, "r")

        data = fp.readlines()

        fp.close()
    except FileNotFoundError:
        print("No prSave Instance has been Initiated yet use '--new' to first")
        return

    st = 0

    for i in data:
        if i == ARCHIVE_SYNTX__START:
            break
        st += 1

    leng = len(data)
    for i in range(st-1, leng):

        if data[i][:2] == ARCHIVE_SYNTX__ARFOLDER:
            count = 0
            for ch in data[i]:
                if ch == '!':
                    ARCHIVE_data__ar = data[i][count+1:]
                    break
                count += 1

        


    if ARCHIVE_data__ar == "":
        print("Couldn't find Archive Folder Name in Config")
        print(data)

    outFile = input("Version: ")
    outFile += ".tar"
    run(["tar", "-cf", outFile, ] + os.listdir())
    run(["mv", outFile, ARCHIVE_data__ar])

    print("Project Archived\nAt: ", ARCHIVE_data__ar+outFile)

    if set_ifdisable_log == True:
        return

    logfile = open(ARCHIVE_data__ar + ARCHIVE_LOG_FILE_NAME, "a")
    curDT = datetime.now().strftime("[%Y-%m-%d||%H:%M:%S]")
    logfile.write(curDT + outFile)
    logfile.close()
        

def main(def_args=sys.argv[1:]):
    args = arguments_parse(def_args)

    if args.new:
        create_new()
        return

    do_archive(args.archive_in, args.archive_log)



def arguments_parse(argsval):
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--new',
                        required=False, action='store_true', default=False,
                        help="""Create A new archiver in Current Directory""")

    parser.add_argument('-a', '--archive_in',
                        required=False, default="", type=str,
                        help="""Custom Archive Folder (One Time)""")

    parser.add_argument('-c', '--archive_perm',
                        required=False, default="", type=str,
                        help="""Change Archive Folder""")

    parser.add_argument('-l', '--archive_log',
                        required=False, action='store_true',default=True,
                        help="""Disable Archive Log (One Time)""")

    parser.add_argument('-p', '--archive_log_perm',
                        required=False, action='store_true',default=True,
                        help="""Disable Archive Log (Permanent)""")

    parser.add_argument('-s', '--show_arpath',
                        required=False, default="", type=str,
                        help="""Show Archive Folder""")

    return parser.parse_args(argsval)


if __name__ == "__main__":
    main()