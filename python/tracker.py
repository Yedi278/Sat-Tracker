import numpy as np

import matplotlib.pyplot as plt
plt.style.use('dark_background')
from TLE_ import*
from TLE_file import*

try:
    from sgp4.api import Satrec
    from sgp4.api import jday
except ImportError:
    print("Error: sgp4.api not found. Installing sgp4...") 

try:
    import requests
except ImportError as e:
    print("requests is not installed",e)


def plot_earth(ax):

    R = 6.371
    ax.set_xlim(-1.5e8,1.5e8)
    ax.set_ylim(-1.5e8,1.5e8)
    ax.set_zlim(-1.5e8,1.5e8)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = R * np.outer(np.cos(u), np.sin(v))
    y = R * np.outer(np.sin(u), np.sin(v))
    z = R * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='b', alpha=0.3)


def plt_sats(sats,ax):

    for i in sats:

        jd, fr = jday(i['time']['year'], i['time']['month'], i['time']['days'], i['time']['hours'], i['time']['minutes'], i['time']['seconds'])
        e, r, v = i['obj'].sgp4(jd,fr)

        c = np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)

        ax.scatter(*r,color='white', s=20)
        ax.text(*r, i['name'], fontsize=10, color='white')

if __name__ == '__main__':

    from mayavi import mlab

    TLE_objs = TLE_obj_from_file('TLE_database.txt')

    sats = []
    for i in TLE_objs:
        d = dict()
        d['obj'] = Satrec.twoline2rv(i.line1,i.line2)
        d['name'] = i.name
        d['time'] = i.time[1]
        sats.append(d)

    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111, projection='3d')

    R = 6000
    u, v = np.mgrid[0:2*np.pi:10j, 0:np.pi:10j]
    x = R*np.cos(u)*np.sin(v)
    y = R*np.sin(u)*np.sin(v)
    z = R*np.cos(v)

    ax.plot_wireframe(x, y, z, color="red")
    # ax.plot_surface(x, y, z, color="red", alpha=0.3)

    plt_sats(sats,ax)
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.show()