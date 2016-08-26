import re
import os
import sys
import urllib.parse
import urllib.request


def getSequenceDiagram( text, outputFile, style = 'default' ):
	request = {}
	request["message"] = text
	request["style"] = style
	request["apiVersion"] = "1"

	data = urllib.parse.urlencode(request)

	f = urllib.request.urlopen("http://www.websequencediagrams.com/",data.encode()) 
	line = f.readline().decode()
	f.close()


	print(line)

	expr = re.compile("(\?(img|pdf|png|svg)=[a-zA-Z0-9]+)")
	m = expr.search(line)

	if m == None:
		print('Invalid response from server.')
		return False

	urllib.request.urlretrieve("http://www.websequencediagrams.com/" + m.group(0),
			outputFile )
	return True

	

def convert(f,style= 'default' ):
	with open(f) as file: 
		getSequenceDiagram( file.read(), f+'.png', style ) 

if __name__ == '__main__':
	input=sys.argv[1]
	style=sys.argv[2]
	if os.path.isdir(input):
		files = [f for f in os.listdir(input) if f.endswith('.seq')]
		print(files)
		for f in files:
			convert(os.path.join(input,f),style)
	elif os.path.exists(input):
		convert(input,style)
	else:
		print('file doesnt exist')
      
                