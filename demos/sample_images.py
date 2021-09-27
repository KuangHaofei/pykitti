import numpy as np
from pykitti import omnicam
import matplotlib.pyplot as plt

start = 2300
end = 3500
step = 10

if __name__ == '__main__':
    basedir = '/media/ipb-hk/IPB_Backup/datasets/omnicam'

    # Specify the dataset to load
    date = '2013_05_14'
    drive = '0008'

    dataset = omnicam.raw(basedir, date, drive, frames=range(start, end, step))
    first_rgb = dataset.get_rgb(0)
    print(first_rgb)

    plt.imshow(first_rgb[0])
    plt.show()

