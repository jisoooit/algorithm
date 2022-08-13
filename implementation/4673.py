arr=[True]*10000

for i in range(10000):
  n=[int(j) for j in str(i)]
  if sum(n)+i<10000:
    arr[sum(n)+i]=False

for i in range(10000):
  if arr[i]==True:
    print(i)
