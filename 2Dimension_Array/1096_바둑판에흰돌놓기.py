import sys

goboard = [['0' for j in range(20)] for i in range(20)]

baduk = int(sys.stdin.readline())

for _ in range(baduk):
    row, col = map(int, sys.stdin.readline().split())
    goboard[row-1][col-1] = '1'

for i in range(19):
    print(" ".join(goboard[i]))
    

'''
    파이썬으로는 답안 제출이 불가능한 문제였다. 출력에 이상이 없는걸 보아 맞을 듯
'''