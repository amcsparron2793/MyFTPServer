from os.path import join, isdir
from typing import Type

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# basic authorizer
authorizer = DummyAuthorizer()
handler = FTPHandler
handler.authorizer = authorizer


def AddDummyUsers(auth: FTPHandler.authorizer, home_dir_root: str = '../../Misc_Project_Files/home_test'):
    # perm is permissions, user has basically everything?
    # anon has the basics?
    auth.add_user(username="user", password="12345",
                  homedir=join(home_dir_root, "test").replace('\\','/'), perm="elradfmwMT")
    auth.add_anonymous(homedir=join(home_dir_root, "nobody").replace('\\','/'))
    auth.add_user(username="gis", password=input("Set GIS Pass: "),
                  homedir="/Apache24/DocsToServe", perm="elradfmwMT")


def CreateServerInstance(server_handler: Type[FTPHandler], server_ip: str = "10.56.211.116", server_port: int = 21):
    # server_ip and server_port are a tuple
    s = FTPServer((server_ip, server_port), server_handler)
    return s


if __name__ == '__main__':
    AddDummyUsers(authorizer)
    server = CreateServerInstance(handler)
    server.serve_forever()
