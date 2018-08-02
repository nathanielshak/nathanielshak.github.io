import os

f = open("list.html", 'w')

message = """<html>
<h1>Find the learning map for your class below:</h1>
"""

for filename in os.listdir('.'):
	if os.path.isfile(filename) and filename.endswith(".html"):
		message += "<li><a href=\"" + filename + "\">" + filename + "</a></li>"

for foldername in os.listdir('.'):
	if os.path.isdir(foldername) and not foldername.endswith(".git"):
		message += "<h2>" + foldername + "</h2>"
		for filename in os.listdir("./" + foldername):
			message += "<li><a href=\"" + foldername + "/" + filename + "\">" + filename + "</a></li>"

message += "</html>"
f.write(message)
f.close()