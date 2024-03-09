#!/usr/bin/python

import sys
import os
import socket

def print_header():
    header = """
    **********************************************************
    \tCSIS 3560 -002 Assignmnet 3
    \tPart 1: Banner Grabber 
    \tJi (300353446)
    **********************************************************
    """
    print(header)
   


def socket_connect(host, port):
    s = socket.socket()

    try:
        s.connect((host, int(port)))  # Ensure port is cast to an integer
        answer = s.recv(1024)
        s.settimeout(None)
        return answer
    except (socket.error) as e:
        return f"{e}"
    finally:
        s.close()



def banner_grabber():

    for host in servers:
         print(f"Server {host} scanning result: ")
         for port in ports:
                
                try:
                    port = int(port)
                    # Perform banner grabbing
                    answer = socket_connect(host, port)
                    # Display the results
                    print(f"\tPort {port} : {answer}")
                except ValueError:
                    print(f"Invalid port: {port}. Skipping.")
         print("----------------------------------------------")
         print()
            
if len(sys.argv) > 1: 
    host = sys.argv[1]

else:
    cmd ='hostname'
    host = os.popen(cmd).read().strip()

    #server_list_path = 'conf/servers.conf'
    servers = os.popen(f'cat conf/servers.conf').read().strip().split('\n')[:3]

    port_list_path = 'conf/ports.conf'
    ports = os.popen(f'cat {port_list_path}').read().strip().split(';')

print_header()
banner_grabber()
