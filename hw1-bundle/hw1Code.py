import snap
import numpy as np
from numpy import dot
from numpy.linalg import norm

cos_sim = lambda a,b : dot(a, b)/(norm(a)*norm(b))

def createV(args):
    v = snap.TIntV()
    for i in args:
        v.Add(i)
    return v

def getFeatureV(G,n):
    deg = n.GetDeg()
    egonetNodes = [n.GetNbrNId(i) for i in range(deg) if n.GetNbrNId(i) != n.GetId()] + [n.GetId()]
    egonetNodes = createV(egonetNodes)
    egonetEdges = snap.GetEdgesInOut(G, egonetNodes)
    
    return [deg, egonetEdges[0] - deg, egonetEdges[1]]

if __name__ == "__main__":
    
    #2.1
    
    targetNode = G.GetNI(9)
    mainFeatV = getFeatureV(G, targetNode)
    print(mainFeatV)
    similarityV = []
    for n in G.Nodes():
        featV = getFeatureV(G, n)
        if featV[0] == 0:
            continue
        similarityV.append((cos_sim(featV, mainFeatV), n.GetId()))
    similarityV = sorted(similarityV, key = lambda x: x[0], reverse=True)
    print(similarityV[1:6])
    
    #2.2
    
    featureSet = {}
    for n in G.Nodes():
        featV = getFeatureV(G, n)    
        featureSet[n.GetId()] = featV

    for K in range(2):
        featureExtend = {}
        for n in G.Nodes():
            if n.GetDeg() == 0:
                featureExtend[n.GetId()] = [0]*len(featureSet[n.GetId()])*2
                continue
            neighbours = [n.GetNbrNId(i) for i in range(n.GetDeg()) if n.GetNbrNId(i) != n.GetId()]
            nbrSum = np.sum([featureSet[nid] for nid in neighbours], axis = 0)
            nbrMean = nbrSum / len(neighbours)
            featureExtend[n.GetId()] = np.concatenate((nbrMean,nbrSum))
        for n in G.Nodes():
            featureSet[n.GetId()].extend(featureExtend[n.GetId()])
            featureSet[n.GetId()] = [i for i in map(float, featureSet[n.GetId()])]
            
    mainFeatV = featureSet[9]
    print(mainFeatV)
    similarityV = []
    for n in G.Nodes():
        featV = featureSet[n.GetId()]
        if featV[0] == 0:
            continue
        similarityV.append((cos_sim(featV, mainFeatV), n.GetId()))
    similarityV = sorted(similarityV, key = lambda x: x[0], reverse=True)
    print(similarityV[1:6])
    
 
    