def nth_prime(n):
    count = 1
    x=n
    d =2
    while(d<n):
        if (x%d==0):
    	    dict[count] = d
    	    count = count+1
    	    x=x/d
        d = d+1
        
def main():
    n = int(input('> '))
    print(nth_prime(n))

if __name__ == "__main__":
    main()
