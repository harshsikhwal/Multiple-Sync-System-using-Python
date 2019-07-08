import paramiko
from scp import SCPClient

# class for connection. Has IP, user id and pass

#
# class Connection:
#    ip_address = "x.x.x.x"
#    user = ""
#    passkey = ""
#    mapper_path = ""
#    ssh_port = "22"
#    client = paramiko.SSHClient()

#   def __init__(self, ip_address, user, passkey):
#       self.ip_address = ip_address
#       self.user = user
#       self.passkey = passkey


# def create_sshclient():

#    return client

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:

    client.connect("10.39.39.64", "22", "astro", "pip")

    ssh = client

    scp = SCPClient(ssh.get_transport())

    # ssh = create_sshclient(server, port, user, password)

    # put(self, files, remote_path=b'.', recursive=False, preserve_times=False)

    scp.put("/home/astro/Desktop/scp_project", "/home/astro/Desktop/", recursive=True)

    # def get(self, remote_path, local_path='', recursive=False, preserve_times=False):

    # scp.get("/home/astro/Desktop/py", "/home/astro/Desktop/py", recursive=True)

except:

    print("Invalid ")
