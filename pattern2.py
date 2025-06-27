n = int(input("Nhập chiều rộng: "))
m = int(input("Nhập chiều dài: "))
for i in range(1,m+1):
  if (i==1 or i==m):
    print("*"*n)
  else:
    print("*"+" "*(n-2)+"*")