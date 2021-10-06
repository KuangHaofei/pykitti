import os
import numpy as np
from pykitti import omnicam
import matplotlib.pyplot as plt

start = 5400
end = 6201
step = 1

if __name__ == '__main__':
    basedir = '/home/ipb-hk/Desktop/data/omnicam'
    outdir = '/home/ipb-hk/Desktop/omni-sinusoid/unit-test/seq-1/images'

    # Specify the dataset to load
    date = '2013_05_14'
    drive = '0008'

    dataset = omnicam.raw(basedir, date, drive, frames=range(start, end, step))
    first_rgb = dataset.get_rgb(0)

    # save images
    for i in range(start, end, step):
        idx = i - start
        des = os.path.join(outdir, '{}.png'.format(idx))
        img = dataset.get_rgb(idx)
        img[0].save(des)
