from itertools import combinations
def array_pairs(x):
    z=[]
    l=list(combinations(x,2))
    for i in l:
        if (int(i[0])+int(i[1])) % 5 == 0:
            z.append(i)
            
    return z
    
if __name__ == "__main__":
    x= input().split()
    print(array_pairs(x))