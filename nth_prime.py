def nth_prime(n):
    primeList=[2]
    d=1
    x=3
    while (d<n):
        tracker=0
        for item in primeList:
            if x%item==0:
                tracker=1
                break
            else:
                continue
        if tracker==0:
            primeList.append(x)
            d=d+1
            x=x+2
        else:
            x=x+2
    return (primeList[n-1])
    
if __name__ == "__main__":
    while True:
        n = int(input('> '))
        print(nth_prime(n))
    
    
