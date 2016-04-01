from flask import Flask, request, make_response, redirect
from julia_set import julia_set
from PIL import Image
from matplotlib import cm
from itertools import product
from threading import Thread
from uuid import uuid4
import numpy as np
import shelve
import time
import io
import julia_fast
import zmq

zmq_context = zmq.Context.instance()
app = Flask(__name__)
store = shelve.open('example.dat')


def parse_request():
    w = request.args.get('w')
    if not w: w = 600
    else: w = int(w)
    h = request.args.get('h')
    if not h: h = 400
    else: h = int(h)
    cre = request.args.get('cre')
    if not cre: cre = -0.8
    else: cre = float(cre)
    cim = request.args.get('cim')
    if not cim: cim = .156
    else: cim = float(cim)
    cmap = request.args.get('cmap')
    if not cmap: cmap = 'inferno'

    return w, h, cre, cim, cmap


def gen_image(key, w, h, cre, cim, cmap):
    # This is well designed, but it is not responsive because
    # of the gil.
    start = time.perf_counter()
    m = julia_fast.julia_set(w, h, cre + cim*1j)
    end = time.perf_counter()-start
    
    image_data = np.empty((h,w,3), dtype=np.uint8)
    colors = 255*np.array(getattr(cm, cmap).colors)

    for j,i in product(range(h), range(w)):
        image_data[j,i,:] = colors[m[j,i]]

    image = Image.fromarray(image_data, mode='RGB')
    
    stream = io.BytesIO()
    image.save(stream, format='png')
    stream.seek(io.SEEK_SET)
    print('Made {} x {} image in {} seconds'.format(w, h, end))
    store[key] = stream.read()


def remote_image(key, w, h, cre, cim, cmap):
    start = time.perf_counter()
    req_socket = zmq_context.socket(zmq.REQ)
    req_socket.identity = str(uuid4()).encode('utf-8')
    req_socket.connect('tcp://127.0.0.1:5555')
    print('Trying to send message')
    message = {'key': key,
               'w': w,
               'h': h,
               'cre': cre,
               'cim': cim,
               'cmap': cmap}
    req_socket.send_json(message)
    store[key] = req_socket.recv()
    req_socket.close()
    

@app.route('/')
def root():
    key = str(uuid4())
    img_thread = Thread(target=remote_image, args=(key,*parse_request()))
    img_thread.daemon = True
    img_thread.start()

    return '<http><body>' + \
           '<a href="/image/{}">click here</a>'.format(key) + \
           '</body></http>'


@app.route('/image/<key>')
def image(key):
    image = store.get(key)
    if image:
        resp = make_response(image)
        resp.headers['Content-Type'] = 'image/png'
        del store[key]
        
    else:
        resp = '<href><body><a href="./{}">Not yet.</a></body></html>'.format(key)

    return resp


application = app


if __name__ == '__main__':
    app.debug = True
    app.run()

    
