import paramiko 
hostname='127.0.0.1'
port=22
username='user'
pkey_file='/home/niaa/.ssh/id_rsa'

if __name__ == "__main__":
	key = paramiko.RSAKey.from_private_key_file(pkey_file)
	s = paramiko.SSHClient()
	s.load_system_host_keys()
	s.connect(hostname,port,pkey=key)
	stdin, stdout, stderr=s.exec_command('ifconfig')
	print stdout.read()
	s.close()
