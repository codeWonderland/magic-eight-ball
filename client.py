from _socket import socket

import sys

"""
>>> data = 'abcdefg'
>>> [delim for delim in ('a', 'e') if delim in data]
['a', 'e']
"""

class EightBallClient:
    def __init__(self, hostname, port):
        # getaddrinfo functionality replicated from https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter04/www_ping.py
        try:
            info_list = socket.getaddrinfo(hostname, port, flags=socket.AI_ADDRCONFIG | socket.AI_V4MAPPED)
        except socket.gaierror as e:
            print('Failure in getaddrinfo: ', e.args[1])
            sys.exit(1)

        info = info_list[0]
        socket_args = info[0:3]
        address = info[4]
        self.sock = socket.socket(*socket_args)
        try:
            self.sock.connect(address)
        except socket.error as e:
            print('Network failure: ', e.args[1])
            sys.exit(1)
        else:
            print('Successfully connected to host ', info[3], ' is listening')
            # Client code here

if __name__ == "__main__":
    print("hello world")