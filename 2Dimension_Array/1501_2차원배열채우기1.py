import sys

n = int(sys.stdin.readline())
array_items = pow(n, 2)

dimen =[['0' for j in range(n)] for i in range(n)]

array_num = 1
for j in range(n):
    for k in range(n):
        dimen[j][k] = '%d' %array_num
        array_num += 1


for k in range(n):
    print(" ".join(dimen[k]))

'''
    가장 기초적인 2차원 배열에 대해 생각해보고
    배열을 채워넣을 경우 순서가 어떻게 발생되는지
    확인하는 문제
'''