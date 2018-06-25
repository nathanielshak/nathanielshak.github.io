import os

f = open("list.html", 'w')

message = """<html>
<h1>Find the learning map for your class below:</h1>
"""

for filename in os.listdir('.'):
	if os.path.isfile(filename):
		message += "<a href=\"" + filename + "\">" + filename + "</a>"

f.write(message)
f.close()