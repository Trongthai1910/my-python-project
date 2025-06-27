def swap(a, b, s):  #Hàm đổi vị trí string a, b trong string s
    s_list = list(s)  # Chuyển đổi chuỗi thành danh sách
    for i in range(len(s_list)):
        if s_list[i] == a:
            s_list[i] = b
        elif s_list[i] == b:
            s_list[i] = a
    return ''.join(s_list)  # Chuyển đổi danh sách thành chuỗi

def get2(s): #hàm sinh tổ hợp chập 2 của các ký tự trong chuỗi s
    th = []
    for i in range(0,len(s)-1):
        text = s[i]
        for j in range(i+1,len(s)):
            text += s[j]
            th.append(text)
            text = s[i]
    return th

def ktra_tontai(a,s): #Hàm kiểm tra xem phần tử a đã tồn tại trong array s hay chưa
    for i in range(len(s)):
        if (s[i]==a): return True
    return False

s = "abcd"
print(swap("a","c",s))
tohop2 = get2(s)
print(tohop2)
print(ktra_tontai("z",s))

hoanvi = []

hoanvi.append(s)
for i in range(0,len(tohop2)):
    hoanvi1 =  swap(tohop2[i][0],tohop2[i][1],s)
    if(ktra_tontai(hoanvi1,hoanvi)==False):
        hoanvi.append(hoanvi1)
    for j in range(0,len(tohop2)):
        if (j!=i): 
            hoanvi2 = swap(tohop2[j][0],tohop2[j][1],hoanvi1)
            if(ktra_tontai(hoanvi2,hoanvi)==False):
                hoanvi.append(hoanvi2)
print(hoanvi)
print(len(hoanvi))