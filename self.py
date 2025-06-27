from random import randint
print('''
	1. Nofap
	2. No porn
	3. Fap without porn
''')
chan = 0
le = 0
option = 0
option = input("Choose: ")
while option != "1" and option != "2" and option != "3":
	option = input("Choose: ")
for i in range(0,7):
	test = randint(1,100)
	print(str(test)+ "  ")
	if test % 2 == 0:
		chan = chan+1
	else:
		le = le + 1
if chan>le:
	if option == "1":
		print("You are not allowed to fap but watch porn")
	if option == "2":
		print("You are not allowed to watch porn")
	if option == "3":
		print("You are allowed to fap but not porn")
else:
	if option == "1":
		print("You are allowed to fap and watch porn")
	if option == "2":
		print("You are allowed to watch porn and fap")
	if option == "3":
		print("You are allowed to do anything")