import re
import requests
import shutil
import os.path

img_dir = "pinterest_images"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)
f = open("source.har","r")
src = f.read()
urls = re.findall("\"url\": \"(.+?\.jpg)\"",src)
n=0
for u in urls:
	if re.search('\.com/\d+?x/',u):
		n+=1
		name = re.search("/([^/]+$)",u).group(1)
		if os.path.exists(img_dir+"/"+name):
			print n, "already exists" 
			continue

		v = re.sub('/[\dx]+?/','/originals/',u,count=1)
		print u, v
		image = ""
		try:
			image = requests.get(v,timeout=3.00,stream=True)
		except:
			print "1.", v, "not found" 	
			try:
				name = "low_"+name
				image = requests.get(u,timeout=3.00,stream=True)
			except:
				print "2.", u, "not found, skipping..."
				continue
		with open(img_dir+"/"+name, 'wb') as f:
			try:
				shutil.copyfileobj(image.raw,f)		
			except:
				print "failed at save", n, name 
				continue
		print "SUCESS", n, name
print "finished!  total:", n
