print "euler"
vertex=PickVertex()
T = []
HatT = []
while not done:
    while e:
        HatT.Append(e)
        vertex=OtherEnd(e, vertex)
        e=NextEdge(vertex)
    T.SpliceIntoCurrentPosition(HatT)

    vertex=T.CurrentVertex()

    while True:
        e=NextEdge(vertex)
        if not e:
            T.IncPosition()
            if T.PositionAtEnd():
                done=True
                break
            vertex = T.CurrentVertex()
        else:
            break