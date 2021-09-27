import numpy as np
from scipy.spatial.transform import Rotation
import matplotlib.pyplot as plt

start = 5400
# max: 12607
end = 6201
step = 10
label = True

if __name__ == '__main__':
    data = np.loadtxt("pose_gt.txt")

    x = data[:, 3]
    y = data[:, 7]
    z = data[:, 11]

    n = np.arange(x.shape[0])
    x = x[start:end+1:step]
    y = y[start:end+1:step]
    z = z[start:end+1:step]
    n = n[start:end+1:step]

    fig = plt.figure()
    line, = plt.plot(x, y)

    if label:
        for i, txt in enumerate(n):
            plt.annotate(txt, (x[i], y[i]))

    plt.show()

    np.savetxt("sub_pose.txt", data[start:end, :])

