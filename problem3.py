def chk_num(line):
	count = 0
	for letter in line:
		if letter.isdigit():
			count += 1
	if count >= 4:
		return True 

def chk_lowcase(line):
	count = 0
	#i = 0
	for letter in line:
		if letter.islower():
			count += 1
	if count >= 2:
		return True 

def chk_upcase(line):
	count = 0
	#i = 0
	for letter in line:
		if letter.isupper():
			count += 1
	if count >= 4:
		return True

# if has at least 4 numbers
# if has at least 2 lowercase letters
# if has at least 4 uppercase
def valid_pwd():
	f = open('gistfile.txt', 'r')
	
	count = 0

	while True:
		line = f.readline()	
		if chk_lowcase(line) and chk_upcase(line) and chk_lowcase(line):
			count += 1

		if len(line) == 0:
			break

	print count