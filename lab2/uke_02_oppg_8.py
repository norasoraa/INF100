#oppgave 8a
def point_in_rectangle(x0, y0, x1, y1, x2, y2):
    venstre_side = min(x0, x1)
    høyre_side = max(x0, x1)
    topp = max(y0, y1)
    bunn = min(y0, y1)
    if venstre_side <= x2 <= høyre_side and bunn <= y2 <= topp:
        return True
    else:
        return False

print(point_in_rectangle(0,0,5,5,3,3))


print()

#oppgave 8b
def rectangles_overlap(x0, y0, x1, y1, x2, y2, x3, y3):
#1.rektangel
    venstre_side_1 = min(x0, x1)
    høyre_side__1 = max(x0, x1)
    topp_1 = max(y0, y1)
    bunn_1 = min(y0, y1)
#2.rektangel
    venstre_side_2 = min(x2, x3)
    høyre_side__2 = max(x2, x3)
    topp_2 = max(y2, y3)
    bunn_2 = min(y2, y3)

    if høyre_side__1 < venstre_side_2 or topp_1 < bunn_2 or høyre_side__2 < venstre_side_1 or topp_2 < bunn_1:
        return False
    else:
        return True

print(rectangles_overlap(0,0,5,5,2,2,6,6))


print()

#oppgave 8c
def circle_overlaps_rectangle(x0, y0, x1, y1, x2, y2, r2):
    venstre_side = min(x0, x1)
    høyre_side = max(x0, x1)
    topp = max(y0, y1)
    bunn = min(y0,y1)
    utvidet_høyre = høyre_side + r2
    utvidet_venstre = venstre_side - r2
    utvidet_opp = topp + r2
    utvidet_ned = bunn - r2
    if venstre_side <= x2 <= høyre_side and bunn <= y2 <= topp:
        return True
    elif utvidet_høyre < x2  or x2 < utvidet_venstre or utvidet_opp < y2 or y2 < utvidet_ned:
        return False
    elif venstre_side <= x2 <= høyre_side or bunn <= y2 <= topp:
        return True
    elif (((abs(venstre_side - x2))**2 + (abs(topp - y2))**2)**0.5) < r2:
        return True
    elif (((abs(høyre_side - x2))**2 + (abs(topp - y2))**2)**0.5) < r2:
        return True
    elif (((abs(x2 - venstre_side))**2 + (abs(y2 - bunn))**2)**0.5) < r2:
        return True
    elif (((abs(x2 - høyre_side))**2 + (abs(y2 - bunn))**2)**0.5) < r2:
        return True
    else:
        return False

print(circle_overlaps_rectangle(0,5,5,0,8,3,2))