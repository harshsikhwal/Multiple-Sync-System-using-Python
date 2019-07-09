# Multiple Host Sync using Python 

This codebase can be used to sync multiple files across various systems. This uses SCP to transfer files, therefore the receiving system should have SSH and SCP service enabled.

The code contains the following:
* main.py       : The main started thread
* logger.py     : A class structure defined which is used to create 'Info' and 'Error' logs
* connection.py : This contains the connection class, which does network based operations.

## Logs

Logs are divided into two types:

* Info logs : They contain all the types of logs, like info, error, warn and debug
* Error logs: These logs report errors and various warnings that may arise


