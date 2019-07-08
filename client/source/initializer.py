# Initializes values to constants that will be used globally
# Also creates basic configuration

from constants import *
from utils import *
from connection import *


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
    file = open("../config/connection_info.ini", "r")
    for line in file:
        if line[0] == '#' or line[0] == ' ' or line[0] == '' or line[0] == '\n' or line[0] == '\r':
            continue
        # add a check for ip address

        user_tuple = (line[line.find(';') + 1: line.find(',')], line[line.find(','):line.find('\n')])

        print(user_tuple)

        connection_data[line[0:line.find(';')]] = user_tuple

        print(connection_data)

        connectionObj = Connection(line[0:line.find(';')], line[line.find(';') + 1:line.find(',')],
                                   line[line.find(','):line.find('\n')])
        # if connectionObj.check_ping() == 0:
        # print host is up
        # else:
        # print host is down
        
        connectionList.append(connectionObj)
