import time
from utils.port import createPort
from utils.upload import sftp_upload, sftp_upload_config
from utils.config import create_config, delete_config
from ssh.main import close_session, ssh, password

# Hi message
print("Hi,")

# User input
localpath = input("Drop your directory path here: ")
name = input("Project name: ")

# Paths
remoteWebPath = f"/var/www/{name}"
remoteConfigAvailable = f"/etc/nginx/sites-available/{name}"
remoteConfigEnabled = f"/etc/nginx/sites-enabled/{name}"

# Create new port for de webserver
serverPort = createPort()

# Upload the directory
sftp_upload(localpath.replace('"', ''), remoteWebPath)

# Create config file
create_config(name, serverPort)

# Upload the config file
sftp_upload_config(f"config/{name}", remoteConfigAvailable)
sftp_upload_config(f"config/{name}", remoteConfigEnabled)

delete_config(name)

# Confirm message
print(f"Your {name} project port is: {str(serverPort)}")

# Ask user id want to restart nginx server
restart = input("Do you want to restart nginx server? (y/n): ")
if restart == "y":
    # Restart nginx server
    (stdin, stdout, stderr) = ssh.exec_command("sudo -S service nginx restart")
    stdin.write(password + "\n")
    stdin.flush()

    # Response
    print("Nginx server restarted.")
else:
    # Response
    print("Nginx server not restarted.")

# Close the session
close_session()

# Goodbye message
print("Goodbye!")

# Delay for 60 seconds == 1 minute
time.sleep(60)

# netstat -an | grep :1552 | grep -v TIME_WAIT | wc -l