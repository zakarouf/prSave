#!/usr/bin/env python3
import argparse
import os
from datetime import datetime
from datetime import timedelta
from subprocess import Popen
import sys

ARCHIVE_CONFIG_FILE_NAME = "prSave.archive.conf"
SELF_CONFIG_FILE_NAME = "prSave.conf"

def run(commands):
    Popen(commands).wait()

def arguments(argsval):
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