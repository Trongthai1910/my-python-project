x=int(input('Bro muốn biết số hạng thứ bnh trong dãy số fibonacci? '))
if int(x)==1 or int(x)==2:
	f=1
if int(x)>=3:
	f=1
	a=1
	for i in range(1,x-1):
		f=f+a
		a=f-a
else: 
	print("Vui lòng chọn các số tự nhiên 1 2 3 ...")
print("Số thứ "+str(x)+" trong dãy fibonacci là: "+str(f))