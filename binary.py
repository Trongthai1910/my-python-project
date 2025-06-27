# x = [4,65,12 ,64,25 ,54,76,24,33]
x = [2,1,4,3] #1 2 3 4
x.sort()
# x.remove(x[0])
x.remove(x[1])
print(x)

#001

s = 3

l = len(x) #l=4

k = ""
# while(l != 1):
#   if (l%2==0): 
#     l = int(l/2) #l=2
#     if(x[l - 1] >= s): #x[l-1] = x[1] = 2 < 3
#       k += "0"
#       for i in range(l,l*2): #range(2, 2*2) = range(2,4)
#         x.remove(x[i]) #remove x[2] x[3] ==> x = [1,2]
#     else:
#       k += "1" #ok
#       for i in range(l): #range(0,2) ==> x[0] x[1]
#         x.remove(x[i]) #remove x[0] x[1] ==> x = [3,4]
#       print(x)
#x = 3 4
# while(l != 1):
#   if (l%2==0): 
#     l = int(l/2) #l=1
#     if(x[l-1] >= s): #x[l-1] = x[0] = 3 = 3
#       k += "0" #ok
#       for i in range(l,l*2): #range(1, 1*2) = range(1,2)
#         x.remove(x[i]) #remove x[1] ==> x = [3]
#     else:
#       k += "1" 
#       for i in range(l): #range(0,1) ==> x[0]
#         x.remove(x[i]) #remove x[0] ==> x = [4]
print(k)

      
    
