#John the Ripper: A password cracking tool that can be used to crack hashed passwords.

import subprocess

# Use John the Ripper to crack a hash
subprocess.run(["john", "--wordlist=/usr/share/wordlists/rockyou.txt", "hashes.txt"])
