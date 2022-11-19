import paramiko

# Credentials for the server
port = "22"
hostname = "ubuntu"
username = "drg"
password = "Dragomirescu22"

# Connect to the server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = hostname, username = username, password = password, port = port)

# Open a session
sftp = ssh.open_sftp()

def close_session():
    # Close the session
    sftp.close()
    ssh.close()