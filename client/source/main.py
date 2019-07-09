from constants import *

# import initializer

from initializer import *

from logger import *

# Read config file and initialize global constants

# initialize logger file

info_logger = Logger('i')

error_logger = Logger('e')

# filling up the logs

info_logger.write_info('i', "Hello")

error_logger.write_error('e', "Error")

info_logger.write_info('i', " Rewriting something without opening Hello")
error_logger.write_error('e', " Rewriting something without opening Error")


# closing the logs at the last after all write operations has been done

info_logger.file_fp.close()
error_logger.file_fp.close()

print ("\n Finished !! \n")

# open log file

# logfile_pointer = open(log_fullpath, 'w')


# initialize_config_file()

# value = config_data['number_of_connections']

# initialize_connections()

# initialize_connections

# for i in range(1, value):
