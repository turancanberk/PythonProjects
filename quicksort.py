def hizli(liste):
    if len(liste)<=1:
        return liste
    ornek=liste[0]
    a1,a2,a3=[],[],[]
    for i in liste:
        if i<ornek:
            a1.append(i)
        elif i==ornek:
            a2.append(i)
        else:
            a3.append(i)
    return hizli(a1)+a2+hizli(a3)