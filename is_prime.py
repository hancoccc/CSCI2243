def is_prime(n):
    if (n<2):
        return(False)
    d=2
    while(d<n):
        if (n%d==0):
            return(False)
            break
        d = d+1
    if (d==n):
        return (True)
        
def main():
    n = int(input('> '))
    print(is_prime(n))

if __name__ == "__main__":
    main()
