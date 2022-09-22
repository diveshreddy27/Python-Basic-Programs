def prime(n):
    if(n<2):
        return False
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
        return True
if __name__ == "__main__":
    n=int(input())
    print("It is prime") if(prime(n)) else print("not prime")