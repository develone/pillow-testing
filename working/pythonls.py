import subprocess

# Example: List files in the current directory (Unix/macOS 'ls -l', Windows 'dir /w')
# For cross-platform compatibility, use commands that work on both or check OS
try:
    subprocess.run(["ls", "-l"], check=True)
except FileNotFoundError:
    subprocess.run(["cmd", "/c", "dir", "/w"], check=True)
