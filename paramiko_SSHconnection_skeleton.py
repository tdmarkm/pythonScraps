import paramiko as pk

hostn="" #ip address or hostname
unix_connection=pk.SSHClient()
unix_connection.set_missing_host_key_policy(pk.AutoAddPolicy()) #important and always comes before connect method
unix_connection.connect(hostname=hostn,username="root",password="root")

#tri-quotes will allow sequences of unix commands

stdin,stdout,stderr=unix_connection.exec_command ("""
pwd
""")


while not stderr.channel.exit_status_ready():
    print('Please wait...')
    unix_connectionOut=stdout.read().decode('ascii').rstrip()
    print(unix_connectionOut)

unix_connection.close()
