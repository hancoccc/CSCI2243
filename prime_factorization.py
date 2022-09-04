def prime_factorization(n):
    x = n
    d =2
    numList = []
    while(d<n):
        while (x%d==0):
            numList.append(d)
            x = x/d
        d = d+1
        if (len(numList) == 0):
            numList.append(n)
    return(numList)
        
def main():
    n = int(input('> '))
    print(prime_factorization(n))

if __name__ == "__main__":
    main()
