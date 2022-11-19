import os

# Variables for the config file
# LOCAL_SERVER_PORT REMOTE_ROOT_PATH

def create_config(name, serverPort):
    try: 
        #input file
        fin = open("config/default", "rt")

        #output file to write the result to
        fout = open(f"config/{name}", "wt")

        #for each line in the input file
        for line in fin:
            #read replace the string and write to output file
            fout.write(line.replace('LOCAL_SERVER_PORT', str(serverPort)).replace('REMOTE_ROOT_PATH', f"/var/www/{name}"))

        #close input and output files
        fin.close()
        fout.close()
    
    except Exception as e:
        # Print the error
        print(f"Error creating the config file: {e}")

        # Delete the file from the local directory
        delete_config(name)

        # Exit the program
        exit()


def delete_config(name):
    # Delete the file from the local directory
    os.remove(f"config/{name}")