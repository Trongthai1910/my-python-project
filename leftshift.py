bit = input("Nhap bit: ")
n = int(input("Dịch trái mấy bit đây em: "))

def ls(bit,n):
	bit = list(bit)
	tmp = []
	for i in range(0,2):
		tmp.append(bit[i])
	for i in range(0,len(bit)-2):
		bit[i] = bit[i+n]
	j=0
	for i in range(len(bit)-2, len(bit)):
		bit[i] = tmp[j]
		j += 1
	return ''.join(bit)

