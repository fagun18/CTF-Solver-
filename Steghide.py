#Steghide: A steganography tool that can be used to hide data within an image or audio file.

import subprocess

# Embed a file in an image
subprocess.run(["steghide", "embed", "-cf", "image.jpg", "-ef", "secret.txt"])

# Extract a file from an image
subprocess.run(["steghide", "extract", "-sf", "image.jpg"])
