#Binwalk: A tool for analyzing and extracting firmware images.

import subprocess

# Analyze a firmware image
subprocess.run(["binwalk", "image.bin"])

# Extract files from a firmware image
subprocess.run(["binwalk", "-e", "image.bin"])
