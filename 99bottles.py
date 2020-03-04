x = 99

while x >= 0:
	msg1= ''
	msg2= ''
	if x > 2:
		msg1 = str(x) + ' bottles'
		msg2 = str(x-1) + ' bottles'
	elif x == 2:
		msg1 = str(x) + ' bottles'
		msg2 = str(x-1) + ' bottle'
	elif x == 1:
		msg1 = str(x) + ' bottle'
		msg2 = 'no more bottles'

	if x > 0:
		print(msg1, 'of beer on the wall,', msg1, 'of beer.')
		print('Take one down and pass it around,', msg2, 'of beer on the wall.')
	else:
		print('No more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.')
	x-=1

