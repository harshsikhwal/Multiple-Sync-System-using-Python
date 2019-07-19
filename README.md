# Multiple Host Sync using Python 

This codebase can be used to sync multiple files across various systems. This uses SCP to transfer files, therefore the receiving system should have SSH and SCP service enabled.

The code contains the following:
* main.py        : The main started thread
* initializer.py : This contains various modules which are used to initialize various data segments, like basic configuration, connection parameters and source and destination folders.
* logger.py      : A class structure defined which is used to create 'Info' and 'Error' logs
* connection.py  : This contains the connection class, which does network based operations.
* constants.py   : This contains a static class, having constants that are used by multiple modules

## Logs

Logs are divided into two types:

* Info logs : They contain all the types of logs, like info, error, warn and debug
* Error logs: These logs report errors and various warnings that may arise


# Configuration Files

3 files are used for parameters:
* config.ini
* connection_info.json
* [ip].json

## config.ini ##

This file contains the basic configuration parameters, like number of connection, logger path, connection info path and so on.
Initially the main program reads this ini file, sets the various global parameters and starts the initialization process.
The user is free to change the parameter value as per his needs for example log file path, otherwise it stays to default.
<br /><b>Note:- If config file is missing, the program will exit</b>

## connection_info.json

This file contains the connection info, basically the ip_address, username and password, in JSON format:
<br />[<br />
&nbsp;&nbsp;&nbsp;&nbsp;{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"ip_address" : "x.x.x.x",<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"user" : "username1",<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"passkey"  : "passcode1"<br />
&nbsp;&nbsp;&nbsp;&nbsp;},<br />
&nbsp;&nbsp;&nbsp;&nbsp;{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"ip_address" : "y.y.y.y",<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"user" : "username2",<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"passkey"  : "passcode2"<br />
&nbsp;&nbsp;&nbsp;&nbsp;}<br />
] <br />

So to add values, the user can directly add the value for keys('ip_address','user','passkey') and the corresponding format within { }

## [ip].json

This file is a mapper file, that maps the ip address with the source and destination address. The name of the file corresponds to the ip address with which we are mapping the stored source and destination address. For example, to map a particular source and destination address for ip address 127.34.45.22, we name the file as 127.34.45.22.json<br />
The file contains the source and destination in json format:
<br />[<br />
&nbsp;&nbsp;&nbsp;&nbsp;{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"src"      : "source folder/file path1",<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"dest"      : "source folder/file path1",<br />
&nbsp;&nbsp;&nbsp;&nbsp;},<br />
&nbsp;&nbsp;&nbsp;&nbsp;{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"src"      : "source folder/file path2",<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"dest"      : "source folder/file path2",<br />
&nbsp;&nbsp;&nbsp;&nbsp;}<br />
] <br />

So to add values, the user can directly add the value for keys('src','dest') and the corresponding format within { }
