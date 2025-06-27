n=float(input("Nhập số điện: "))
s=0
for i in range(1,4):
	t=n-i*100
	if t>0:
		s=s+100*(750+(i-1)*500)
	else:
		s=s+(100+t)*(750+(i-1)*500)
		break
if t>0:
	s=s+t*3000
print("Số tiền phải trả là: "+str(s))
