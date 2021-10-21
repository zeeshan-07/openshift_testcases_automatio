import paramiko
import requests
import json
import yaml
from yaml.loader import SafeLoader
import os
import sys

def main(arg):
    print("openshift automation")
    # reading & then conversion of json file into python dictionary
    yaml_file = "var_info.yaml"
    if os.path.exists(yaml_file):
        try:
            with open("var_info.yaml", 'r') as stream:
                data_loaded = yaml.safe_load(stream)
        except:
            print("Failed to load yaml_File")
    else:
        print("\nFile not found!!! Exception Occurred \n")

#Read node.yaml file as a Ansible user
    host = (data_loaded["host"])
    port = (data_loaded["port"])
    username = (data_loaded["username"])
    password = (data_loaded["password"])
    node_yaml_dir = (data_loaded["node_yaml_dir"])

    print ("The script has the name %s" % (arg))


    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

    if os.path.exists(node_yaml_dir):
        try:
            with open(node_yaml_file, 'r') as stream:
                nodes_data_loaded = yaml.safe_load(stream)
        except:
            print("Failed to load yaml_File")
    else:
        print("\nFile not found!!! Exception Occurred \n")


#get Csah public ip and openshift user
    print(nodes_data_loaded["bootstrap_kvm"])
 #   print ("The script has the name %s" % (arg))


main(sys.argv[1])
