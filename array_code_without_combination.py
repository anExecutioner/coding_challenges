def array_pairs(x):
    z=[]
    
    count=0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            a=int(x[i])+int(x[j])
            if a%5==0:
                if a%2==0:
                    count+=1
                t=(x[i],x[j])
                z.append(t)
    print("pairs divisible by 5 : {}".format(z))
    print("number of even pairs in given array divisble by 5 : {}".format(count))
    
if __name__ == "__main__":
    x= input("enter elements of your array : ").split()
    array_pairs(x)