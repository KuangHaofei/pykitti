import numpy as np
from pykitti import omnicam

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    basedir = '/home/ipb-hk/Desktop/data/omnicam'

    # Specify the dataset to load
    date = '2013_05_14'
    drive = '0008'

    dataset = omnicam.raw(basedir, date, drive, frames=range(0, 20, 5))

    # Grab some data
    second_pose = dataset.oxts[1].T_w_imu
    first_rgb = dataset.get_rgb(0)
    first_cam2 = dataset.get_cam2(0)
    third_velo = dataset.get_velo(2)

    # Display some of the data
    np.set_printoptions(precision=4, suppress=True)
    print('\nDrive: ' + str(dataset.drive))
    print('\nFrame range: ' + str(dataset.frames))

    print('\nFirst timestamp: ' + str(dataset.timestamps[0]))
    print('\nSecond IMU pose:\n' + str(second_pose))

    f, ax = plt.subplots(1, 2, figsize=(15, 5))

    ax[0].imshow(first_cam2)
    ax[0].set_title('Left RGB Image (cam2)')

    ax[1].imshow(first_rgb[1])
    ax[1].set_title('Right RGB Image (cam3)')

    f2 = plt.figure()
    ax2 = f2.add_subplot(111, projection='3d')
    # Plot every 100th point so things don't get too bogged down
    velo_range = range(0, third_velo.shape[0], 100)
    ax2.scatter(third_velo[velo_range, 0],
                third_velo[velo_range, 1],
                third_velo[velo_range, 2],
                c=third_velo[velo_range, 3],
                cmap='gray')
    ax2.set_title('Third Velodyne scan (subsampled)')

    plt.show()
