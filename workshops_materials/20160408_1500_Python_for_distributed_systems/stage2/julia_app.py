from flask import Flask, request

application = Flask(__name__)

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


@application.route('/')
def root():
    return 'Request: {}, {}, {}, {}, {}'.format(*parse_request())


if __name__ == '__main__':
    application.debug = True
    application.run()
