def mod_array(A,B):
    result=0
    for digit in A:
        result=(result*10+digit)%B
    return result
A=list(map(int,input().split()))
B=int(input())
result=mod_array(A,B)
print(result)

