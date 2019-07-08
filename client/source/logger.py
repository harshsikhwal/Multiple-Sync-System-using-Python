import os

from constants import *

from datetime import datetime


class Logger:
    # Read config file and initialize global constants

    log_file = ""
    # file_descriptor = open()

    def __init__(self, file_type):

        global error_log
        global info_log
        # global file_descriptor
        global log_path
        global log_file

        if file_type == 'e':
            error_log = "scp_error." + str(os.getpid()) + ".log"
            log_file = error_log

        elif file_type == 'i':
            info_log = "scp." + str(os.getpid()) + ".log"
            log_file = info_log

        if not os.path.exists(log_path):
            os.makedirs(log_path)



    # Why a different function: Because we can give the date as well

    def write_info(self, file_type, data):

        if file_type == 'i':
            log_type = "Info, "
        elif file_type == 'e':
            log_type = "Error, "
        elif file_type == 'w':
            log_type = "Warn, "
        elif file_type == 'd':
            log_type = "Debug, "
        else:
            return

        file_descriptor = open(log_path + log_file, "a")
        file_descriptor.write(log_type + datetime.now().strftime(' %d/%m/%Y %H:%M:%S ') + data + "\n")
        file_descriptor.close()

    def write_error(self, file_type, data):

        if file_type == 'e':
            log_type = "Error, "

        elif file_type == 'w':
            log_type = "Warn, "

        else:
            return

        file_descriptor = open(log_path + log_file, "a")
        file_descriptor.write(log_type + datetime.now().strftime(" %d/%m/%Y %H:%M:%S ") + data + "\n")
        file_descriptor.close()
