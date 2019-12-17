low = 178416
high = 676461

#passwords = []
passwords = 0

def check_doubles(number):
	text = str(number)
	for i in range(0, len(text)-1):
		if(text[i] == text[i+1]):
			if ((i > 0 and text[i] != text[i-1]) or i==0):
				if ((i+2 <= len(text)-1 and text[i] != text[i+2]) or i+2 >len(text)-1):
					return True
	return False

def check_ascend(number):
	text = str(number)
	for i in range(0, len(text)-1):
		if(int(text[i]) > int(text[i+1])):
			return False
	return True

for num in range(low, high+1):
	if(check_doubles(num) and check_ascend(num)):
		passwords += 1


print(passwords)