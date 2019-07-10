import paramiko
from scp import SCPClient
import re
import os
from logger import *


# class for connection. Has IP, user id and pass

class Connection:
    ip_address = "x.x.x.x"
    user = ""
    passkey = ""
    mapper_path = ""
    ssh_port = 22
    client = paramiko.SSHClient()

    def __init__(self, ip_address, user, passkey):
        self.ip_address = ip_address
        self.user = user
        self.passkey = passkey

    def create_sshclient(self):
        # client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ip_address, self.ssh_port, self.user, self.passkey)
        # return client

    def check_ping(self):
        response = os.system("ping -c 1 " + self.ip_address)
        return response

    def check_for_valid_ip(self, ip_address):
        if re.match('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',ip_address):
            info_logger.write_info('i', '{} is in correct format \n'.format(ip_address))
        else:
            error_logger.write_info('e', 'Format of {} is incorrect, please verify\n'.format(ip_address))

    # ssh = create_sshclient(server, port, user, password)
    # scp = SCPClient(ssh.get_transport())
