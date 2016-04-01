from flask import Flask, request, make_response
import julia_set
from PIL import Image
from matplotlib import cm
from itertools import product
import numpy as np
import time
import io

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


def gen_image(w, h, cre, cim, cmap):
    start = time.perf_counter()
    m = julia_set.julia_set(w, h, cre + cim*1j)
    end = time.perf_counter()-start
    print('Made a {} x {} image in {} s'.format(w, h, end))

    image_data = np.empty((h,w,3), dtype=np.uint8)
    colors = 255*np.array(getattr(cm,cmap).colors)
    for j, i in product(range(h), range(w)):
        image_data[j, i, :] = colors[m[j,i]]

    image = Image.fromarray(image_data, mode='RGB')

    stream = io.BytesIO()
    image.save(stream, format='png')
    stream.seek(io.SEEK_SET)
    return stream.read()

@application.route('/')
def root():
    image = gen_image(*parse_request())
    resp = make_response(image)
    resp.headers['Content-Type'] = 'image/png'

    return resp


if __name__ == '__main__':
    application.debug = True
    application.run()
