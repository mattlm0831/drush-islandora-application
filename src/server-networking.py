import paramiko



class ssh_connection:

    def __init__(self, server, user, password):
        self.ssh = paramiko.SSHClient()
        self.ssh.connect(server = server, user = user, password = password)
    
    def ls(self):
        return self.ssh.exec_command('ls')