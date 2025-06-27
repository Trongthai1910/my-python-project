n = input("Nhap ma nhi phan: ")
so = 0;
while len(n)%8!=0:
	print("Ma nhi phan khong hop le: ")
	n = input("Nhap ma nhi phan: ")
n = list(n)
for i in range(0,len(n)):
	n[i] = int(n[i])
mu = 7
for i in range(0,len(n)):
	so+=n[i] * 2**mu
	mu-=1
match so:
	case 95:
		print(0)
	case 5:
		print(1)
	case 118:
		print(2)
	case 117:
		print(3)
	case 45:
		print(4)
	case 121:
		print(5)
	case 123:
		print(6)
	case 69:
		print(7)
	case 127:
		print(8)
	case 125:
		print(9)
	case _:
		print("...")