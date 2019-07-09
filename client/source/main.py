from constants import *

# import initializer

from initializer import *

from logger import *

# filling up the logs



info_logger.write_info('w', "Start!")

error_logger.write_info('w', "Start!")


initialize_connections()

# closing the logs at the last after all write operations has been done

info_logger.write_info('w', "End!")

error_logger.write_info('w', "End!")

info_logger.file_fp.close()
error_logger.file_fp.close()

print ("\n Finished !! \n")

