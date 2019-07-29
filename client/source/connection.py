import re
import paramiko
from logger import *
import sys
from sys import platform
from scp import SCPClient

class Location:
    source = ""
    destination = ""
    source_exist = False

    def __init__(self, src, dest):
        self.source = src
        self.destination = dest


# class for connection. Has IP, user id and pass

class Connection:
    ip_address = "x.x.x.x"
    user = ""
    passkey = ""
    mapper_path = ""
    ssh_port = 22
    client = paramiko.SSHClient()
    is_up = False
    scp_established = False
    src_dest = []
    scp_connection = None

    def __init__(self, ip_address, user, passkey):
        self.ip_address = ip_address
        self.user = user
        self.passkey = passkey

    def create_sshclient(self):
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ip_address, self.ssh_port, self.user, self.passkey)

    def check_ping(self):
        if platform == 'linux' or platform == 'linux2':
            response = os.system("ping -c 1 " + self.ip_address)
        elif platform == 'win32':
            response = os.system("ping -n 1 " + self.ip_address)
        else:
            response = 'not supported for the os u are currently using'
        return response

    def check_for_valid_ip(self):
        if re.match('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                    self.ip_address):
            constant.info_logger.write_info('i', '{} is in correct format'.format(self.ip_address))
            self.is_up = True
        else:
            constant.error_logger.write_info('e', 'Format of {} is incorrect, please verify'.format(self.ip_address))
            self.is_up = False

    # def print_connection_info(self):

    def create_scp_connection(self, ip_address, user_name, password):

        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(ip_address, self.ssh_port, user_name, password)
            # scp = SCPClient(client.get_transport())
            # scp.put("C:\\Users\\vhowdhur\\Desktop\\hi", "/home/vibaswan/Desktop/", recursive=True)
            self.scp_established = True
            self.scp_connection = client
            return client
        except:
            constant.error_logger.write_info('e', 'Could not establish scp connection with client {}'
                                             .format(self.ip_address))
            # sys.exit()
            return None
        # ssh = create_sshclient(server, port, user, password)
        # scp = SCPClient(ssh.get_transport())

    def transfer_data_to_client(self, src_dest_obj, client):
        scp = SCPClient(client.get_transport())
        for src_dst in src_dest_obj:
            if src_dst.source_exist:
                scp.put(str(src_dst.source), str(src_dst.destination), recursive=True)
            else:
                constant.error_logger.write_info('e', 'the source file {} does not exist so data transfer failed'
                                                 .format(self.ip_address))
        print('aaa')
