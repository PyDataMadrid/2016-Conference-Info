import zmq
import json

context = zmq.Context.instance()
socket = context.socket(zmq.REQ)
socket.bind("tcp://127.0.0.1:5555")

request = {"w": 4000,
           "h": 2000,
           "cre": -0.8,
           "cim":0.156,
           "cmap": "inferno"}

socket.send(json.dumps(request).encode('utf-8'))
m = socket.recv()

with open("something.png", "wb") as f:
    f.write(m)


            
            
  
