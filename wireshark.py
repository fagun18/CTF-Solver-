#Wireshark: A network protocol analyzer that can be used to capture and analyze network traffic.


import subprocess

# Start a capture on interface eth0
subprocess.run(["wireshark", "-i", "eth0"])
