n = int(input())
m = 1000 - n
arr = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in arr :
    cnt += m//i
    m = m%i
print(cnt)
