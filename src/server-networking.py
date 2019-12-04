from fabric import Connection

valid_arguments = ['namespace', 'collection', 'is_member_of','content_model','without_cmodel','with_dsid','without_dsid','solr_query']

class ssh:

    def __init__(self, user, host, password):
        self.ssh = Connection(host= user + '@' + host, connect_kwargs={"password": password})
        
    def __del__(self):
        self.ssh.close()
    
    def query(self, **kwargs):
        with self.ssh.cd("/var/www/drupal7/"):
            if len(kwargs) < 1:
                return
            for k,v in kwargs.items():
                if k.lower() not in valid_arguments:
                    raise(ValueError)
            arguments = ' '.join(['--' + str(k) + '=' + str(v) for k,v in kwargs.items()])
            
            cmd = 'sudo drush islandora_datastream_crud_fetch_pids ' + arguments + ' --pid_file=/var/www/drupal7/tmp/pids.txt'
            self.ssh.run(cmd)
            self.ssh.get("/var/www/drupal7/tmp/pids.txt", 'pids.txt')
            
            