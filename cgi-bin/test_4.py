#!/usr/bin/python2.7

import paramiko
import cgi, cgitb

form = cgi.FieldStorage()  
site_command = form.getvalue('command')
def sshclient_execmd(hostname, port, username, password, execmd):  
    paramiko.util.log_to_file("paramiko.log")  
      
    s = paramiko.SSHClient()  
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
      
    s.connect(hostname=hostname, port=port, username=username, password=password)  
    stdin, stdout, stderr = s.exec_command (execmd)  
#   stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
      
#    print stdout.read()  
    stdlines = stdout.readlines()
    for x in stdlines:
#        print("<center>" + x + "</center>")
        print(x)
        print("<br />")

    s.close()  
      

def main():  
      
    hostname = '172.30.32.106'  
    port = 22  
    username = 'root'  
    password = 'cw123'  
    execmd = site_command  

    sshclient_execmd(hostname, port, username, password, execmd) 


print("Content-type: text/html")
print
print("<html>")
print("<body>")
main()
#print("<center>Hello, Linux.com!</center>")
#print("<center>Hello, Linux.com!</center>")
#print("<center>Hello, Linux.com!</center>")
print("</body>")
print("</html>")
