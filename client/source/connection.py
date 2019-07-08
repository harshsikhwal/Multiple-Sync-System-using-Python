import paramiko
from scp import SCPClient
import os


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

    # ssh = create_sshclient(server, port, user, password)
    # scp = SCPClient(ssh.get_transport())
