import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

from sklearn import manifold, datasets
from scipy.spatial.distance import cdist



n=2               #power of number of samples
m=3               #number of molecules

# coordi_internal=np.loadtxt('coordi_3_internal.txt')
coordi=np.loadtxt('coordi_3_10^5.txt')

co = coordi[0:3*10**4]
del coordi
co=co.reshape(10**4,9)
points=5000
for j in range(4,30):
    
    LEoutput = manifold.SpectralEmbedding(n_components=3,n_neighbors=j).fit_transform(co)
    print("standrdok")
    standard=cdist(LEoutput, LEoutput, 'euclidean')
    standard=standard[0:100,0:100]
    divergence=[]
    F_lis_1_15 = []
    F_lis_2_25 = []
    F_lis_16_39 = []
    F_lis_51_92 = []
    F_lis_61_86 = []
    
    for i in range(490):
        coordinate = co[0:10 ** n+i*10]
        LEoutput = manifold.SpectralEmbedding(n_components=3, n_neighbors=j).fit_transform(coordinate)
        F = cdist(LEoutput, LEoutput, 'euclidean')
        F_lis_1_15.append(F[1][15])
        F_lis_2_25.append(F[2][25])
        F_lis_16_39.append(F[16][39])
        F_lis_51_92.append(F[51][92])
        F_lis_61_86.append(F[61][86])
        F=F[0:100,0:100]
        di = np.sum(np.absolute(F - standard))
        divergence.append(di)
        if i == 10:
            print(10)
        if i == 200:
            print(200)
        if i == 500:
            print(500)
        if i == 800:
            print(800)
        if i == 900:
            print(900)
    
    print("finish part")
    
    fig = plt.figure()
    plt.scatter( list(range(100,points,10)),F_lis_1_15, s=1, alpha=0.5,figure = fig)
    plt.savefig("/home/sky8/structure/Cartisian_LE_1_15_neighbor%d.png" % j,dpi=600)

    fig = plt.figure()
    plt.scatter( list(range(100,points,10)),F_lis_2_25, s=1, alpha=0.5,figure = fig)
    plt.savefig("/home/sky8/structure/Cartisian_LE_2_25_neighbor%d.png" % j,dpi=600)

    fig = plt.figure()
    plt.scatter( list(range(100,points,10)),F_lis_16_39, s=1, alpha=0.5,figure = fig)
    plt.savefig("/home/sky8/structure/Cartisian_LE_16_39_neighbor%d.png" % j,dpi=600)

    fig = plt.figure()
    plt.scatter( list(range(100,points,10)),F_lis_51_92, s=1, alpha=0.5,figure = fig)
    plt.savefig("/home/sky8/structure/Cartisian_LE_51_92_neighbor%d.png" % j,dpi=600)

    fig = plt.figure()
    plt.scatter( list(range(100,points,10)),F_lis_61_86, s=1, alpha=0.5,figure = fig)
    plt.savefig("/home/sky8/structure/Cartisian_LE_61_86_neighbor%d.png" % j,dpi=600)

    fig = plt.figure()
    plt.savefig("/home/sky8/structure/Cartisian_LE_convergence_neighbor%d.png" % j,dpi=600)
    plt.scatter( list(range(100,points,10)),divergence, s=1, alpha=0.5,figure = fig)