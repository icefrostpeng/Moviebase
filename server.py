# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:43:59 2021

@author: Elton
"""

import time
import socket              
  
# next create a socket object  

token=1
s = socket.socket()          
print ("Socket successfully created") 
  
# reserve a port on your computer in our  
# case it is 12345 but it can be anything  
port = 12345                
  
# Next bind to the port  
# we have not typed any ip in the ip field  
# instead we have inputted an empty string  
# this makes the server listen to requests  
# coming from other computers on the network  
s.bind(('', port))          
print ("socket binded to %s" %(port))  
  
# put the socket into listening mode  
s.listen(5)      
print ("socket is listening")             
  
# a forever loop until we interrupt it or  
# an error occurs
time.sleep(5)  
while True:  
  
# Establish connection with client.  
    c, addr = s.accept()

    if token:
        
        print ('Got connection from', addr, token ) 
        
        c.send(b'Thank you for connecting and the token was there')
        token=0
    else:
        print("sorry was already taken")
        c.send(b'Sorry token was taken')
    
    # send a thank you message to the client.  
      
  
# Close the connection with the client  
    c.close()  