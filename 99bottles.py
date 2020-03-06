# Author: Rivindu Wijedoru (rivindu1289)
# 99 Bottles program

x = 99	#99 bottle count

while x >= 0: #print the lines of the song for each bottle
	msg1= ''
	msg2= ''
	if x > 2:
		msg1 = str(x) + ' bottles'
		msg2 = str(x-1) + ' bottles'
	#change bottles to bottle if there is only 1
	elif x == 2:
		msg1 = str(x) + ' bottles'
		msg2 = str(x-1) + ' bottle'
	elif x == 1:
		msg1 = str(x) + ' bottle'
		msg2 = 'no more bottles' #if there are no bottles left after 'take one down'

	if x > 0:
		print(msg1, 'of beer on the wall,', msg1, 'of beer.')
		print('Take one down and pass it around,', msg2, 'of beer on the wall.')
	#if there are 0 bottles, print last line of song
	else:
		print('No more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.')

	x-=1	#change count of bottles