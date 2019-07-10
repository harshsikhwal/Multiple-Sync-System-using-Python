# Initializes values to constants that will be used globally
# Also creates basic configuration

from constants import *
from utils import *
from connection import *
import sys
from logger import *
import re


def initialize_config_file():
    file = open("../config/config.ini", "r")
    for line in file:
        if line[0] == '#' or line[0] == ' ' or line[0] == '' or line[0] == '\n' or line[0] == '\r':
            continue
        config_data[line[0:line.find('=')]] = line[line.find('=') + 1:]

        # print("key = " + key)
        # print("value = " + line[line.find('=') + 1: ])
        print(line)


def initialize_connections():

    if not os.path.exists("../config/connection_info.ini"):
        info_logger.write_info('e', "Connection info file is absent!\nAborting")
        error_logger.write_info('e', "Connection info file is absent!\nAborting")
        sys.exit()

    else:
        connection_file = open("../config/connection_info.ini", "r")
        for line in connection_file:
            if line[0] == '#' or line[0] == ' ' or line[0] == '' or line[0] == '\n' or line[0] == '\r':
                continue

            if re.match('(\d+|\.)+;\w+;\w+', line):
                line = line.split(';')
                info_logger.write_info('i', 'Format of {} is correct proceeding forward \n'.format(line))
                info_logger.write_info('i', "Initializing connection with IP address\t" + line[0])
                if '\n' in line[2]:
                    re.sub('\n', '', line[2])
                connection_obj = Connection(line[0], line[1], line[2])

                connection_obj.check_for_valid_ip(line[0])

                if connection_obj.check_ping() == 0:

                    info_logger.write_info('i', "Host {} is reachable!!".format(line[0]))
                else:
                    info_logger.write_info('w', "Host {} is unreachable!".format(line[0]))
                    error_logger.write_info('w', "Host {} is unreachable!".format(line[0]))

                connectionList.append(connection_obj)
            else:
                info_logger.write_info('e', "Format of {} is incorrect should be format ip;username;password\nAborting"
                                       .format(line))
                error_logger.write_info('e', "Connection info file is absent!\nAborting")
                sys.exit()
