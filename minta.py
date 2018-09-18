def sajat(k):
    m="* "
    for i in range(k):
        print(m*i)
    for j in range(k-2,0,-1):
        print(j*m)

sajat(6)
print("_____________________________________________________")

def haromszog(t):
    for i in range(t):
        print(''*(t-i-1)+'* '*(i+1))
    for j in range(t-1,0,-1):
        print(''*(t-j)+'* '*(j))



haromszog(5)