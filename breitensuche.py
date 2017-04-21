# -*- coding: utf-8 -*-
""" Ein kleines Beispielprogramm """
import Knoten

def knoten_breiten(r):
    """Breitensuche"""
    pred = []
    component = []
    Q = []
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

if __name__ == '__main__':
    print("Et jeht loss!")
    knoten_anfang = Knoten.Knoten()
    knoten_eins = Knoten.Knoten()
    knoten_zwei = Knoten.Knoten()
    knoten_drei = Knoten.Knoten()
    knoten_vier = Knoten.Knoten()
    knoten_fuenf = Knoten.Knoten()


    knoten_eins.add_knoten_pred(knoten_zwei)
    knoten_eins.add_knoten_succ(knoten_drei)
    knoten_zwei.add_knoten_succ(knoten_eins)
    knoten_zwei.add_knoten_succ(knoten_fuenf)

    knoten_anfang.add_knoten_pred(knoten_eins)

    knoten_breiten(knoten_anfang)
    print("Und Ende")
