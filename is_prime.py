def is_prime(n):
    d=2
    while(d<n):
        if (n%d==0):
            return(False)
            break
        d = d+1
    if (d==n):
        return (True)

if __name__ == "__main__":
    while True:
        n = int(input('> '))
        print(is_prime(n))
