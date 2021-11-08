import sshtunnel as ssh
import os


this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "creds", "server_ip.txt")
# print(open(DATA_PATH).read())

SSH_HOST = open(this_dir + '\\creds\\server_ip.txt', 'r').read()
SSH_PASS = open(this_dir + '\\creds\\pw.txt', 'r').read()
SSH_UNAME = open(this_dir + '\\creds\\user.txt', 'r').read()
DB_HOST = open(this_dir + '\\creds\\db_address.txt', 'r').read()
DB_WH_HOST = open(this_dir + '\\creds\\db_warehouse_address.txt', 'r').read()

def open_tunnel(
    SSH_HOST=SSH_HOST
    , SSH_PASS=SSH_PASS
    , SSH_UNAME=SSH_UNAME
    , DB_HOST=DB_HOST):

    tunnel = ssh.SSHTunnelForwarder(
        ('3.95.103.37', 22)
        , ssh_password=SSH_PASS
        , ssh_username=SSH_UNAME
        ,remote_bind_address=(DB_HOST, 3306))
    tunnel.start()
    return tunnel

def close_tunnel(tunnel):
    tunnel.close()
