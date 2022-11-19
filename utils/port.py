import socket
import random
from ssh.main import hostname

# Cridentials
hostname = "ubuntu"

# Create randome 4 digit port
def createPort():
    # Create a random number
    port = random.randint(1000, 9999)

    # Check if the port is available
    if checkPort(port):
        createPort()
    else:
        return port


# Check if the server is up
def checkPort(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((hostname, int(port)))
        s.shutdown(2)
        return True
    except:
        return False