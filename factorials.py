def fact(num):
    result=1
    for i in range(num,0,-1):
        result= result*i
    print(result)
fact(16)