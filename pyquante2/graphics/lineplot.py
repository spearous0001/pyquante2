import numpy as np
import pylab as pl

def lineplot_orbs(points,orbs,bfs,doshow=False,
               title="Line plot of pyquante orbital"):
    bfmesh = bfs.mesh(points)
    for orb in orbs.T: # Transpose makes interations work
        pl.plot(orb_on_points_with_mesh(points,orb,bfmesh))
    pl.title(title)
    if doshow:
        pl.show()
    return

def orb_on_points(points,orb,bfs):
    f = np.zeros(len(points),'d')
    for c,bf in zip(orb,bfs):
        f = f + c*bf.mesh(points)
    return f

def orb_on_points_with_mesh(points,orb,bfmesh):
    return np.dot(bfmesh,orb)

def lineplot_bfs(points,bfs,doshow=False,
                 title="Line plot of pyquante bfs"):
    bfmesh = bfs.mesh(points)
    ng,nbf = bfmesh.shape
    for i in range(nbf):
        pl.plot(bfmesh[:,i])
    pl.title(title)
    if doshow:
        pl.show()
    return

def line(origin,destination,npts=50):
    """
    Create a 1d line from the 3-tuple origin to the 3-tuple destination
    Yet another solution from @unutbu at stackoverflow.
    http://stackoverflow.com/questions/17396164/numpythonic-way-to-make-3d-meshes-for-line-plotting
    """
    return np.column_stack((np.linspace(o,d,npts) for o,d in zip(origin,destination)))

def test_plot_bfs():
    from pyquante2 import basisset,h2
    bfs = basisset(h2,'sto3g')
    points = line((0,0,-5),(0,0,5))
    lineplot_bfs(points,bfs,True)
    return

def test_plot_orbs():
    from pyquante2 import basisset,h2
    bfs = basisset(h2,'sto3g')
    orbs = np.array([[1.0,1.0],
                     [1.0,-1.0]],'d')
    
    zvals = np.linspace(-5,5)
    points = line((0,0,-5),(0,0,5))
    lineplot_orbs(points,orbs,bfs,True)
    return

if __name__ == '__main__':
    test_plot_orbs()
    #test_plot_bfs()

        
