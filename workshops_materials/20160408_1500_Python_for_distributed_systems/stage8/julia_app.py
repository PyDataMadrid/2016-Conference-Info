from flask import Flask, request, make_response
from threading import Thread
from uuid import uuid4
import shelve
import zmq

application = Flask(__name__)
store = shelve.open('example.dat')
context = zmq.Context.instance()

#API
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
    if not cim: cim = 0.156
    else: cim = float(cim)
    cmap = request.args.get('cmap')
    if not cmap: cmap = 'inferno'

    return w, h, cre, cim, cmap


def remote_image(key, w, h, cre, cim, cmap):
    socket = context.socket(zmq.REQ)
    socket.identity = str(uuid4()).encode('utf-8')
    socket.connect('tcp://127.0.0.1:5555')

    message = {'key': key,
               'w': w,
               'h': h,
               'cre': cre,
               'cim': cim,
               'cmap': cmap}
    socket.send_json(message)
    store[key] = socket.recv()
    socket.close()
    store.sync()
               

@application.route('/')
def root():
    key = str(uuid4())
    img_thread = Thread(target=remote_image, args=(key, *parse_request()))
    img_thread.daemon = True
    img_thread.start()

    return '<http><body>' +\
        '<a href="/image/{}">click here</a>'.format(key) +\
        '</body></http>'


@application.route('/image/<key>')
def image(key):
    store.sync()
    image = store.get(key)
    if image:
        resp = make_response(image)
        resp.headers['Content-Type'] = 'image/png'
        del store[key]
        store.sync()
    else:
        resp = '<html><body>' + \
               '<a href="./{}">not yet</a>'.format(key) + \
               '</body></html>'

    return resp


if __name__ == '__main__':
    application.debug = True
    application.run()
