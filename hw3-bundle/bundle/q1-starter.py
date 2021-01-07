import snap
import numpy as np
import matplotlib.pyplot as plt

def load_graph(name):
    '''
    Helper function to load graphs.
    Use "epinions" for Epinions graph and "email" for Email graph.
    Check that the respective .txt files are in the same folder as this script;
    if not, change the paths below as required.
    '''
    if name == "epinions":
        G = snap.LoadEdgeList(snap.PNGraph, "soc-Epinions1.txt", 0, 1)
    elif name == 'email':
        G = snap.LoadEdgeList(snap.PNGraph, "email-EuAll.txt", 0, 1)   
    else: 
        raise ValueError("Invalid graph: please use 'email' or 'epinions'.")
    return G

def q1_1():
    '''
    You will have to run the inward and outward BFS trees for the 
    respective nodes and reason about whether they are in SCC, IN or OUT.
    You may find the SNAP function GetBfsTree() to be useful here.
    '''
    
    ##########################################################################
    #TODO: Run outward and inward BFS trees from node 2018, compare sizes 
    #and comment on where node 2018 lies.
    G = load_graph("email")
    #Your code here:
    outTree = snap.GetBfsTree(G, 2018, True, False)
    inTree = snap.GetBfsTree(G, 2018, False, True)
    print("out size 2018:", outTree.GetNodes())
    print("in size 2018:", inTree.GetNodes())
    
    
    ##########################################################################
    
    ##########################################################################
    #TODO: Run outward and inward BFS trees from node 224, compare sizes 
    #and comment on where node 224 lies.
    G = load_graph("epinions")
    #Your code here:
    outTree = snap.GetBfsTree(G, 224, True, False)
    inTree = snap.GetBfsTree(G, 224, False, True)
    print("out size 224: ", outTree.GetNodes())
    print("in size 224: ", inTree.GetNodes())
      
    
    ##########################################################################

    print ('2.1: Done!\n')

def get_reach(data):
    G = load_graph(data)
    sample = np.random.randint(G.GetNodes(), size=100)
    inReachArr, outReachArr = [], []
    for nid in sample:
        outReachArr.append(snap.GetBfsTree(G, int(nid), True, False).GetNodes())
        inReachArr.append(snap.GetBfsTree(G, int(nid), False, True).GetNodes())
    inReachArr = sorted(inReachArr)
    outReachArr = sorted(outReachArr)
    frac = np.array(range(1, 101)) / 100
    plt.plot(frac, inReachArr, label = "inward reach")
    plt.plot(frac, outReachArr, label = "outward reach")
    plt.xlabel('Fration of nodes')
    plt.ylabel('Node count')
    plt.title(data + ' graph')
    plt.legend()
    plt.show()

def q1_2():
    '''
    For each graph, get 100 random nodes and find the number of nodes in their
    inward and outward BFS trees starting from each node. Plot the cumulative
    number of nodes reached in the BFS runs, similar to the graph shown in 
    Broder et al. (see Figure in handout). You will need to have 4 figures,
    one each for the inward and outward BFS for each of email and epinions.
    
    Note: You may find the SNAP function GetRndNId() useful to get random
    node IDs (for initializing BFS).
    '''
    ##########################################################################
    #TODO: See above.
    #Your code here:
    
    get_reach("email")
    
    get_reach("epinions")
    
    ##########################################################################
    print('2.2: Done!\n')

def get_decomposition(data):
    G = load_graph(data)
    totalS = G.GetNodes()
    srcS = totalS*snap.GetMxSccSz(G)
    wccS = snap.GetMxWccSz(G)
    discS = totalS - totalS*wccS
    print(data, "graph")
    print("Total size:", totalS)
    print("Biggest SCC size:", srcS)
    print("Biggest WCC size:", totalS*wccS)
    print("DISCONNECTED size:", discS)
    
    
def q1_3():
    '''
    For each graph, determine the size of the following regions:
        DISCONNECTED
        IN
        OUT
        SCC
        TENDRILS + TUBES
        
    You can use SNAP functions GetMxWcc() and GetMxScc() to get the sizes of 
    the largest WCC and SCC on each graph. 
    '''
    ##########################################################################
    #TODO: See above.
    #Your code here:
    
    get_decomposition("email")
    print("")
    get_decomposition("epinions")
    
    ##########################################################################
    print('2.3: Done!\n')

def get_connection(data, sample_size=1000):
    G = load_graph(data)
    print(data, "graph")
    count = []
    for _ in range(sample_size):
        path = snap.GetShortPath(G, G.GetRndNId(), G.GetRndNId(), True)
        count.append(path!=-1)
    frac_connected = sum(count) / sample_size
    print(frac_connected)
    
def q1_4():
    '''
    For each graph, calculate the probability that a path exists between
    two nodes chosen uniformly from the overall graph.
    You can do this by choosing a large number of pairs of random nodes
    and calculating the fraction of these pairs which are connected.
    The following SNAP functions may be of help: GetRndNId(), GetShortPath()
    '''
    ##########################################################################
    #TODO: See above.
    #Your code here:
    
    get_connection("email")
    print("")
    get_connection("epinions")
    
    ##########################################################################
    print('2.4: Done!\n')
    
if __name__ == "__main__":
    q1_1()
    q1_2()
    q1_3()
    q1_4()
    print("Done with Question 2!\n")