#Nmap: A network exploration tool and security scanner that can be used to map out a network and identify open ports and services.

import nmap

# Initialize nmap scanner
nm = nmap.PortScanner()

# Scan a host
nm.scan('host', '1-1024')

# Print the open ports
print(nm.all_tcp())
