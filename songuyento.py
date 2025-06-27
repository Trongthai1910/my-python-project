n=int(input("Nhập số n và đi em: "))
if n==1 or n==0:
	prin("Tổng S = 0")
else:
	s=0
	for i in range(2,n+1):
		t=0
		for j in range(1,i+1):
			if i%j==0:
				t+=1
		if t==2:
			s+=i
print("Tổng S = "+str(s))