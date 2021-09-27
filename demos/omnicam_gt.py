import numpy as np
from pykitti import omnicam

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    basedir = '/media/ipb-hk/IPB_Backup/datasets/omnicam'

    # Specify the dataset to load
    date = '2013_05_14'
    drive = '0008'

    dataset = omnicam.raw(basedir, date, drive)

    # Grab some data
    poses = dataset.oxts

    origin_T = poses[0].T_w_imu
    groundtruth_poses = []
    for pose in poses:
        T = np.dot(np.linalg.inv(origin_T), pose.T_w_imu)
        # T = pose.T_w_imu
        groundtruth_poses.append(T[:3, :].flatten())

    groundtruth_poses = np.array(groundtruth_poses)

    np.savetxt("pose_gt.txt", groundtruth_poses)
