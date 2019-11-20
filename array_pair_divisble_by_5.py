from itertools import combinations
def array_pairs(x):
    z=[]
    count=0
    l=list(combinations(x,2))
    for i in l:
        a=int(i[0])+int(i[1])
        if a%5 == 0:
            if a%2==0:
                count+=1
            z.append(i)
        
    print(z)
    print(count)
    
if __name__ == "__main__":
    x= input().split()
    array_pairs(x)