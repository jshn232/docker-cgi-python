#!/usr/bin/python2.7

import paramiko
import cgi, cgitb

form = cgi.FieldStorage()  

def sshclient_execmd(hostname, port, username, password, execmd):  
    paramiko.util.log_to_file("paramiko.log")  
      
    s = paramiko.SSHClient()  
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
      
    s.connect(hostname=hostname, port=port, username=username, password=password)  
    stdin, stdout, stderr = s.exec_command (execmd)  
#   stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
      
#    print stdout.read()  
    print("<center>" + stdout.read() + "</center>")

    s.close()  
      

def main():  
      
    hostname = '172.30.32.106'  
    port = 22  
    username = 'root'  
    password = 'cw123'  
    execmd = "docker images"  

    sshclient_execmd(hostname, port, username, password, execmd) 


print("Content-type: text/html")
print
print("<html>")
main()
#print("<center>Hello, Linux.com!</center>")
#print("<center>Hello, Linux.com!</center>")
#print("<center>Hello, Linux.com!</center>")
print("</html>")
