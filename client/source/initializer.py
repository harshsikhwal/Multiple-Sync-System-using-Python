# Initializes values to constants that will be used globally
# Also creates basic configuration

from constants import *
import configparser
import threading
from connection import *
import sys
from logger import *
import json


def initialize_config_file():

    if not os.path.exists("../config/config.ini"):
        print("Config file does not exist")
        sys.exit(-1)

    config = configparser.ConfigParser(allow_no_value=True)
    config.read("../config/config.ini")

    constant.number_of_connections = config['DEFAULT']['number_of_connections']
    constant.log_path = config['DEFAULT']['log_path']
    constant.address_mapper_path = config['DEFAULT']['address_mapper_path']
    constant.connection_info_path = config['DEFAULT']['connection_info_path']

    
def initialize_connections():

    if not os.path.exists(constant.connection_info_path):
        constant.info_logger.write_info('e', "Connection info file is absent!\nAborting")
        constant.error_logger.write_info('e', "Connection info file is absent!\nAborting")
        sys.exit()

    else:
        with open(constant.connection_info_path, "r") as file1:
            connection_file = json.load(file1)

        for obj in connection_file:
            connection_obj = Connection(obj['ip_address'], obj['user'], obj['passkey'])

            connection_obj.check_for_valid_ip()

            if connection_obj.check_ping() == 0:
                constant.info_logger.write_info('i', "Host {} is reachable!!".format(obj['ip_address']))
                connection_obj.is_up = True

            else:
                connection_obj.is_up = False
                constant.info_logger.write_info('w', "Host {} is unreachable!".format(obj['ip_address']))
                constant.error_logger.write_info('w', "Host {} is unreachable!".format(obj['ip_address']))
            constant.connection_list.append(connection_obj)


def reader_thread_task(connection_ob, i):
    i = str(i)
    constant.info_logger.write_info('w', "Starting Thread {}".format(i))
    if not os.path.exists("../config/path_mapper/{}".format(connection_ob.ip_address) + ".json"):
        constant.info_logger.write_info('e', "Path Mapper file is absent!\nAborting Thread " + i)
        constant.error_logger.write_info('e', "Path Mapper file is absent!\nAborting Thread " + i)
        return
    else:
        constant.info_logger.write_info('i', "[Thread " + i + "]Path Mapper file is present!\tReading data")
        with open("../config/path_mapper/{}".format(connection_ob.ip_address) + ".json", "r") as file:
            path_mapper_file = json.load(file)
        # Handle exception here
        for obj in path_mapper_file:
            loc = Location(obj['src'], obj['dest'])
            if not os.path.exists(obj['src']):
                constant.info_logger.write_info('w', "[Thread " + i + "]Source Path {} "
                                                                      "does not exist!".format(obj['src']))
                constant.error_logger.write_info('w', "[Thread " + i + "]Source Path {} "
                                                                       "does not exist!".format(obj['src']))
                loc.source_exist = False
            else:
                constant.info_logger.write_info('i', "[Thread " + i + "]Source Path {} exist!".format(obj['src']))
                loc.source_exist = True
            connection_ob.src_dest.append(loc)
    constant.info_logger.write_info('w', "Ending Thread {}".format(i))


def initialize_src_dest():
    Thread_List = []
    for i in range(0, len(constant.connection_list)):
        t = threading.Thread(target=reader_thread_task, args=(constant.connection_list[i], i), name=i)
        t.setDaemon(True)
        Thread_List.append(t)
        # t.start()
        # t.join()

    for t in Thread_List:
        t.start()

    for t in Thread_List:
        t.join()


def scp_thread_task(connection_ob, i):

    constant.info_logger.write_info('w', "Starting Thread {}".format(str(i)))
    constant.info_logger.write_info('w', "Initialising scp connection of client {}"
                                    .format(str(connection_ob.ip_address)))

    # calling function to initialize scp connection from connections.py
    scp_connection = connection_ob.create_scp_connection(str(connection_ob.ip_address), str(connection_ob.user),
                                        str(connection_ob.passkey))
    constant.scp_connections_list.append(scp_connection)
    constant.info_logger.write_info('w', "Initialising scp connection of client {} is successful"
                                    .format(str(connection_ob.ip_address)))
    constant.info_logger.write_info('w', "Ending Thread {}".format(str(i)))


def initialize_scp_connection():

    scp_connection_list = []
    for i in range(0, len(constant.connection_list)):
        t = threading.Thread(target=scp_thread_task, args=(constant.connection_list[i], i), name=i)
        t.setDaemon(True)
        scp_connection_list.append(t)

    for t in scp_connection_list:
        t.start()

    for t in scp_connection_list:
        t.join()
