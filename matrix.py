def matrix(m,n):
    lsmatrix=[]
    for i in range(m):
        ls=[]
        lsmatrix.append(ls)
        for j in range(n):
            mat=i*j
            ls.append(mat)


    return lsmatrix



sor=int(input("Sor:"))
oszlop=int(input("Oszlop:"))
print(matrix(sor,oszlop))