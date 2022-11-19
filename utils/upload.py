import os

from ssh.main import sftp, close_session

# Upload the directory
def sftp_upload(localpath, remotepath):
    try:
        # Create a directory on the server
        sftp.mkdir(remotepath)

        # Upload the directory
        for x in os.listdir(localpath):
            if os.path.isfile(os.path.join(localpath, x)):
                # Upload the file
                sftp.put(os.path.join(localpath, x), f"{remotepath}/{x}")
                print(f"Uploaded: {x}")
            else:
                # Upload the directory
                loopFiles(os.path.join(localpath, x), f"{remotepath}/{x}")

    except Exception as e:
        # Print the error
        print(f"Error uploading the directory: {e}")

        # Close the session
        close_session()

        # Exit the program
        exit()

# Upload a loop for the directory
def loopFiles(localpath, remotepath):
    # Create a directory on the server
    sftp.mkdir(remotepath)

    for x in os.listdir(localpath):
        if os.path.isfile(os.path.join(localpath, x)):
            sftp.put(os.path.join(localpath, x), f"{remotepath}/{x}")
            print(f"Uploaded: {x}")
        else:
            # Upload the directory
            loopFiles(os.path.join(localpath, x), f"{remotepath}/{x}")


# Upload config file
def sftp_upload_config(localpath, remotepath):
    try:
        # Upload the file
        sftp.put(localpath, remotepath)
        print(f"Uploaded {localpath}")

    except Exception as e:
        # Print the error
        print(f"Error uploading the file: {e}")

        # Delete the file from the local directory
        os.remove(localpath)

        # Close the session
        close_session()

        # Exit the program
        exit()