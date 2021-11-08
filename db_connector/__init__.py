
import os

def test_func():
    print('Works!')
    this_dir, this_filename = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "creds", "server_ip.txt")
    print(open(DATA_PATH).read())

