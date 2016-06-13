import paramiko
import sys
 
hostname='localhost'
port=22
username=' '
password=' '
pkey_file='/home/niaa/.ssh/id_rsa'

if __name__ == "__main__":
	k=paramiko.RSAKey.from_private_key_file(pkey_file)
	rmt = paramiko.SSHClient()
	rmt.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	rmt.load_system_host_keys()	
	rmt.connect('localhost', username=' ', password=' ')
	stdin.stdout.stderr=rmt.exec_command('ifconfig')
	print stdout.read()
	rmt.close()

