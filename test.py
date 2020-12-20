



def append_to_begining_str(str, letter):
	str = str[::-1] + letter
	return str[::-1]

print(append_to_begining_str('ok boomer', 'o'))