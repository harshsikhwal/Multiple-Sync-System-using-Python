from constants import *

from initializer import *

from logger import *

from connection import *


def main():
    # filling up the logs

    # IF NOTHING IS PRESENT THEN CREATE FOLDERS, FILES AND SO ON

    # Read the connections from connection_info.ini and initialize the connection objects

    initialize_config_file()

    constant.info_logger = Logger('i')

    constant.error_logger = Logger('e')

    constant.info_logger.write_info('i', "Main Start!")

    constant.error_logger.write_info('i', "Main Start!")

    constant.info_logger.write_info('i', "Initializing Connections\tStart")

    initialize_connections()

    constant.info_logger.write_info('i', "Initializing Connections\tEnd")

    # After initialization, read the particular file where destination and source is present and map it accordingly

    constant.info_logger.write_info('i', "Source and Destination locations\tStart")

    initialize_src_dest()

    # creating scp connections for the different connections

    initialize_scp_connection()

    # transferring the information to the respective clients

    transfer_data()

    # closing the logs at the last after all write operations has been done

    constant.info_logger.write_info('i', "Main End!")
    constant.error_logger.write_info('i', "Main End!")
    constant.info_logger.file_fp.close()
    constant.error_logger.file_fp.close()

    # print("\n Finished !! \n")


if __name__ == "__main__":
    main()
