import socket
import time
import hashlib
#Known information
host = "saturn.picoctf.net"
ip = "13.59.203.175"
port = 55823
newline = b"\x0a"
count = 0


#used to get the requests containing the quoted string
def get_server_message(s):
  data = s.recv(1024)
  return data.decode('utf-8')

#Used to send the hash back to the server
def send_hash(message, s: socket):
  message = bytes(message.encode('utf-8')) + newline
  s.send(message)
  return True

#used to has the quoted string
def get_hash(data):
  hash = hashlib.md5(data.encode('utf-8')).hexdigest()
  return hash


# Used to strip the quoted string.
def grab_string(message):
  string = message.split("'")[1].split("'")[0]
  return string


# Used for recieving the acknol
def ack():
  s.recv(0)
  return True


## Start of script
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))

    while count < 3: # Server needs you to complete 3 hashes
      message = get_server_message(s) # gets the server message containing the quited string.
      string = grab_string(message) # Gets the quoted string sent from the server.
      hash = get_hash(string) # Gets the hash of the quoted string."
      print(f"Server Requested MD5 of {string} sending {hash}")
      send_hash(hash, s) # Sends the hash of the quoted string to the server.
      ack() # Gets the acknowledgement that is sent to us from the server. note: its a packet sent with 0 bytes
      get_server_message(s) # Gets the echo message of what we sent to the server.
      count += 1 # Adds one to the count as we know that the server needs you to complete 3 hashes
    pico_ctf_key = get_server_message(s).split('\n')[1]# gets the pico ctf and strips the correct message :)
    print(f"Pico Flag: {pico_ctf_key}")
    input()
