# -*- coding: utf-8 -*-
"""
@author: Salim Khazem
"""
import numpy as np

def Dijkstra(start,end,graph):
    '''
    Recherche le chemin en commencant par la fin et
    en allant de predec en predec
    '''
    def findOptimalPath(start,end,predec):
        optPath=[]
        s=end
        while s !=start:
           optPath.append(s) 
           s=predec[s]
        optPath.append(s)  
        optPath.reverse()
        return optPath
    
    def findmin(Q,distances):
        '''
        Dans cette partie on recherche des sommets les plus proches 
        on retourne une liste de sommets ayant une distance minimale
        '''
        dmin=float('inf')
        a=[]
        for d in Q:
            if distances[d] <= dmin and np.isfinite(distances[d]):
                dmin=distances[d]
                if dmin == distances[d]:
                    a.append(d)
                else:
                    a=[d]
        return a

    P=[]
    Q=[ x for x in graph]
    distances={}
    predec={}
    for q in Q:
        distances[q]=float('inf')
    distances[start]=0
        
    while len(Q) > 0:
        a=findmin(Q,distances)
        if len(a) == 0:
            return None,None       # pas de chemin !
        a=a[-1]         # on prend le dernier trouvé !
        P.append(a)
        Q.remove(a)
            
        if a==end:
            break
        for b in graph[a] :
            if b in Q:
                d= distances[a]+graph[a][b]
                if d < distances[b]:
                    distances[b]=d
                    predec[b]=a
                if b==end:
                    #return findOptimalPath(start,end,predec),distances,predec
                    return findOptimalPath(start,end,predec),distances
