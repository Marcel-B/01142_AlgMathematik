import Knoten

knotenf = Knoten.Knoten()
hallo = Knoten.Knoten()
hallo.addKnoten(knotenf)

'''
pred[r] = r
component[r] = r
Q.Append(r)
while Q.IsNotEmpty():
    v = Q.Top()
    for w in Neighborhood(v):
        if pred[w]==None:
            pred[w] = v
            component[w] = component[v]
            Q.Append(w)
            '''