# Paramiko Module:- for running remote shell commands or transferring files without login uses sshv2 protocol as base.
# This is the third party module in python thus required to be installed before use.


import paramiko
import os

passW = os.environ.get('PASS')    #export this by shell:- export PASS = Ayushi@099

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # For first time ssh to the server we need to trust that serverS
ssh.connect(hostname='10.132.128.96', username='ubuntu', password=passW)  #any one line out of this and below according to requirement
ssh.connect(hostname='10.132.128.96', username='ubuntu', key_filename="/home/ubuntu/private.pem")
stdin,stdout,stderr = ssh.exec_command("free -m")
print(stdout.readlines())
ssh.close()

ftp_client = ssh.open_sftp()
ftp_client.put("template","/tmp/template")
ftp_client.close()