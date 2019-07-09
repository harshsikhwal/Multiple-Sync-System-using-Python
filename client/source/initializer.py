# Initializes values to constants that will be used globally
# Also creates basic configuration

from constants import *
from utils import *
from connection import *
import sys
from logger import *


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
        file = open("../config/connection_info.ini", "r")
        for line in file:
            if line[0] == '#' or line[0] == ' ' or line[0] == '' or line[0] == '\n' or line[0] == '\r':
                continue

            info_logger.write_info('i', "Initializing connection with IP address\t" + line[0:line.find(';')])
            connection_obj = Connection(line[0:line.find(';')],
                                        line[line.find(';') + 1:line.find(';')],
                                        line[line.find(','):line.find('\n')])

            if connection_obj.check_ping() == 0:

                info_logger.write_info('i', "Host " + line[0:line.find(';')] + " is reachable!!")
            else:
                info_logger.write_info('w', "Host " + line[0:line.find(';')] + " is unreachable!")
                error_logger.write_info('w', "Host " + line[0:line.find(';')] + " is unreachable!")


            connectionList.append(connection_obj)
