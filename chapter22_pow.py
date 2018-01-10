def pow(x,y):
    if y == 1:
        return x
    else:
        return x * pow(x,y-1)

result = pow(3,3)
print(result)
