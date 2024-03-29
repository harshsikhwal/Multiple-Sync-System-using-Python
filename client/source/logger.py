import os
from datetime import datetime

from constants import *


class Logger:
    # Read config file and initialize global constants

    def __int__(self):
        return

    def __init__(self, file_type):
        # global file_descriptor

        self.log_file = ""
        self.file_fp = None

        if file_type == 'e':
            self.log_file = "scp_error." + str(os.getpid()) + ".log"

        elif file_type == 'i':
            self.log_file = "scp." + str(os.getpid()) + ".log"

        if not os.path.exists(constant.log_path):
            os.makedirs(constant.log_path)

        self.file_fp = open(constant.log_path + self.log_file, "a")

    # Why a different function: Because we can give the date as well

    def write_info(self, file_type, data):

        if file_type == 'i':
            log_type = "Info,\t"
        elif file_type == 'e':
            log_type = "Error,\t"
        elif file_type == 'w':
            log_type = "Warn,\t"
        elif file_type == 'd':
            log_type = "Debug,\t"
        else:
            return

        self.file_fp.write(log_type + datetime.now().strftime("\t%d/%m/%Y %H:%M:%S\t") + data + "\n")

    def write_error(self, file_type, data):

        if file_type == 'e':
            log_type = "Error,\t"

        elif file_type == 'w':
            log_type = "Warn,\t"

        elif file_type == 'i':
            log_type = ""

        else:
            return

        self.file_fp.write(log_type + datetime.now().strftime("\t%d/%m/%Y %H:%M:%S\t") + data + "\n")
