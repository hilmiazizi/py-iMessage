from py_imessage import imessage
import os
import sys


###
message = "Your message go here"
###

os.system('clear')
def doDelete(phone):
	payload = "sed -i '' '/"+phone+"/d' ./"+sys.argv[1]
	os.system(payload)

def doSend(phone):
	global counter
	global num_lines
	global message
	counter = counter+1
	if not imessage.check_compatibility(phone):
		print("["+str(counter)+"|"+str(num_lines)+"] Failed  => "+phone+" | Not an iPhone")
		doDelete(phone)
		return None
	try:
		guid = imessage.send(phone, message)
	except Exception as e:
		doDelete(phone)
		if 'unable to open database file' in str(e):
			print("["+str(counter)+"|"+str(num_lines)+"] Success => "+phone)
		else:
			return None

counter = 0
num_lines = sum(1 for line in open(sys.argv[1]))
for line in open(sys.argv[1]):
	if '+' in line:
		print(phone+' => Wrong format!')
		pass
	else:
		doSend(line.rstrip())
