Banner grabbing is like reading a welcome sign when connecting to a computer. It tells us what services, like a website or server, are running and their versions. Port analysis is like checking which entry points, or ports, are open on a computer. This helps us understand and secure the network by identifying potential vulnerabilities.

List of ports I will scan: 22, 80, 431, 443, 3306.


List of servers I will scan: localhost (Kali), Linux Mint, Host machine.


I created a ‘conf’ directory and stored these two configuration files.

Then, open a vi editor or Visual Studio Code to create a Python script.

!/usr/bin/python

This line is known as a shebang and is used to specify the interpreter for the script.

import sys
import os
import socket

The script imports necessary modules: sys for system-related functionality, os for interacting with the operating system, and socket for creating and interacting with network sockets.


This function creates a socket, attempts to connect to a specified host and port, receives a response (up to 1024 bytes), and then returns the response. If an error occurs during the connection attempt, it returns an error message.


This function iterates through a list of servers and associated ports, calls socket_connect to get information about the service running on each port, and prints the result.


If a command-line argument is provided, it uses that as the target host. Otherwise, it uses the result of the hostname command.

It reads server configurations from a file (conf/servers.conf) and limits the number of servers to three. It also reads port configurations from a file (conf/ports.conf) using a semicolon (;) as the delimiter.

If you run the Python script, the output will resemble the following.


With this banner grabber, I can gather valuable information about the services and versions running on a target system.

Localhost (127.0.0.1):
Port 22 (SSH): Running OpenSSH version 9.6p1 on a Debian system.
Port 80 (HTTP): No banner information retrieved (empty response).
Port 431: Connection refused (no service running on this port).
Port 443: Connection refused (no service running on this port).
Port 3306 (MySQL/MariaDB): Running MariaDB version 5.5.5-10.11.5, and it mentions that the host ‘localhost’ is allowed to connect using the mysql_native_password authentication method.
Mint-3560 (10.35.62.9):
Port 22 (SSH): Running OpenSSH version 8.9p1 on an Ubuntu system.
Port 80 (HTTP): No banner information retrieved (empty response).
Port 431: Connection refused (no service running on this port).
Port 443: Connection refused (no service running on this port).
Port 3306 (MySQL/MariaDB): It mentions that the host ‘10.35.62.4’ is not allowed to connect to this MySQL server. This indicates a security restriction on the MySQL server.
ServerHost (192.168.38.1):
Port 22 (SSH): Connection refused (no SSH service running on this port).
Port 80 (HTTP): No banner information retrieved (empty response).
Port 431: Connection refused (no service running on this port).
Port 443 (HTTPS): Empty response (no service running on this port).
Port 3306 (MySQL/MariaDB): It mentions that the host ‘DESKTOP-JTUBM0T’ is not allowed to connect to this MariaDB server. Similar to Mint-3560, this indicates a security restriction on the MariaDB server.
In summary, the banner grabbing results provide information about the versions and configurations of SSH, MySQL/MariaDB services, and indicate connection restrictions on the MySQL/MariaDB servers for specific hosts. This information can be valuable for understanding the security posture of the servers and potential areas of interest for further investigation or testing

