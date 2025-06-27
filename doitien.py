print('1: Đổi từ VND sang USD')
print('2: Đổi từ USD sang VND')
print('Tỷ giá ngày 27/10/2022')
print("Bấm 'huy' để kết thúc")
i = input('Chọn: ')
while i != 'huy':
	m = int(i)
	if m == 1:
		VND = int(input('Nhập VND: '))
		USD = VND / 24.835
		print(str(VND) + 'VND = '+str(USD)+ 'USD')
	if m == 2:
		USD = int(input('Nhập USD: '))
		VND = USD * 24.835
		print(str(USD) + 'USD = '+str(VND)+ 'VND')
	else:
		print('Ko hợp lệ')
