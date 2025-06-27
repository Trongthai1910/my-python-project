x=input("Nhap 3: ")
while x=="3":
	a=input("Nhap hang 1: ")
	aa=a.split(" ")
	b=input("Nhap hang 2: ")
	bb=b.split(" ")
	c=input("Nhap hang 3: ")
	cc=c.split(" ")
	for i in range(0,3):
		aa[i]=int(aa[i])
		bb[i]=int(bb[i])
		cc[i]=int(cc[i])
	det=aa[0]*bb[1]*cc[2]+aa[1]*bb[2]*cc[0]+aa[2]*bb[0]*cc[1]-aa[2]*bb[1]*cc[0]-aa[1]*bb[0]*cc[2]-aa[0]*bb[2]*cc[1]
	print("Det(A)= "+str(det))
	x=input("Nhap 3: ")