def ChkPrime(iNo):
    for i in range(2,int(iNo/2)+1):
        if (iNo % i == 0):
            return False
            break;
    else:
        return True

