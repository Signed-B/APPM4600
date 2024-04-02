def eval_legendre(n, x):
    if n == 0:
        return [1]
    elif n == 1:
        return [1,x]
    else:
        p = [1,x]
        for i in range(1,n):
            p.append(((2*i+1)*x*p[i] - i*p[i-1])/(i+1))
        return p
