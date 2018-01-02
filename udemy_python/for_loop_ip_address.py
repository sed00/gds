# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
#    127.0.0.1
#    .192.168.0.1
#    10.0.123456.255
#    172.16
#    255
#
# So your program should work even with invalid IP Addresses. We're just interested in the
# number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test:
#    .123.45.678.91
#    123.4567.8.9.
#    123.156.289.10123456
#    10.10t.10.10
#    12.9.34.6.12.90
#    '' - that is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.
def ip_address_segment_print (ipAddress):
	print("IP Address: {}".format(ipAddress))
	segment = 0
	length = 0
	char = ''
	for char in ipAddress:
		if (char == '.'):
			segment+=1
			print("segment {} contains {} characters".format(segment,length))
			length=0
		else:
			length+=1
	else:
		if (char != '.'):
			print("segment {} contains {} characters".format(segment+1,length))
	print('')
	return;

ip_address_segment_print(".123.45.678.91")
ip_address_segment_print("123.4567.8.9.")
ip_address_segment_print("123.156.289.10123456")
ip_address_segment_print("10.10t.10.10")
ip_address_segment_print("12.9.34.6.12.90")
ip_address_segment_print("")









