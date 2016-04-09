import re
import urllib2
import sys
import os

def parse(file_in,file_out):
	print "Starting"

	page = open(file_in,"r")
	linkfile = open("temp","w")
	for line in page:
		links = re.findall(r'(http:(?:\\a)?(?:\\)*/(?:\\)*/uptobox.com(?:\\)*/[a-zA-Z0-9]+)',line)
		for link in links:
			linkfile.write(str(link)+"\n")

	page.close()
	linkfile.close()

	files = open("temp","r")
	mod_links = open(file_out,"w")
	mod_link = []

	for link in files:
		mod_link = ''.join([x for x in link if x != "\\"])
		mod_links.write(str(mod_link))
	files.close()
	mod_links.close()
	print "Links Captured"

def rem_dupl_link(file_in,file_out):
	print "Removing Duplicate Links"
	dest = open(file_out,"w")

	with open(file_in,"r") as source:
		dictn=set()
		for line in source:
			dictn.add(line)
		for urls in dictn:
			dest.write(urls)
	dest.close()
	print "Duplicates Links Removed"

def rem_dupl(file_in,file_out):
	print "Removing Duplicates"
	dest = open(file_out,"w")

	with open(file_in,"r") as source:
		dictn={}
		for line in source:
			splitted = line.split()
			url = splitted[-1]
			file_name = ' '.join(splitted[:-2])
			dictn[url]=file_name
		for urls in dictn.keys():
			dest.write("{0:110}--- {1}\n".format(dictn[urls],urls))
	dest.close()
	print "Duplicates Removed"

def append(file_orig,file_append):
	print "Copying"
	final = open(file_append,"a")
	final_file = open(file_orig,"r")
	for line in final_file:
		final.write(line)
	final.close()
	final_file.close()
	print "Copying Done"

def get_title(file_in,file_out):
	print "Capturing Titles"
	links = open(file_in,"r")
	final_file = open(file_out,"w")
	new_file = open("new","w")
	for link in links:
		flag_error = False
		flag_title = True
		try:
			req = urllib2.Request(link, headers={'User-Agent' : "Magic Browser"}) 
			source = urllib2.urlopen(req)
		except:
			print "Error in opening - "+link
			flag_error = True
			sys.exit()
			pass
		else:
			for line in source:
				pattern = '(?<=<title>)(.*?)(?=</title>)'
				temp_str = re.search(pattern.decode('utf-8'),line.decode('utf-8'))
				error = re.search('The file expired'.decode('utf-8'),line.decode('utf-8'))
				if flag_title and temp_str:
					title = temp_str
					flag_title = False
				if error:
					flag_error = True
					break
		if flag_error:
			continue
		splitted = title.group(0).split()
		name = ' '.join(splitted[1:])+" ---"
		try:
			final_file.write("{0:110}--- {1}".format(name.encode('utf-8'),link))
			new_file.write("{0:110}--- {1}".format(name.encode('utf-8'),link))
		except:
			print name.encode('utf-8')
			print link
			pass
	links.close()
	new_file.close()
	final_file.close()
	print "Titles Captured"

def del_temp(**file_in):
	print "Deleting temp files"
	for temp_file in file_in:
		os.system("rm "+temp_file)
	print "Cleaning Done"

def sort(file_in,file_out):
	print "Sorting"
	document = []
	end_file = open(file_out,"w")
	with open(file_in,"r") as file:
		for line in file:
			document.append(line)
		document.sort()
		for entry in document:
			end_file.write(entry)
	end_file.close()
	print "Sorting Done"

def check_expiry(file_in,file_expire,file_live):
	dest = open(file_live,"w")
	expired = open(file_expire,"a")

	with open(file_in,"r") as source:
		for line in source:
			flag = False
			splitted = line.split()
			url = splitted[-1]
			try:
				req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
				src = urllib2.urlopen(req)
			except:
				print "Error in opening - "+line
				pass
			else:
				for ln in src:
					title = re.search('The file expired',ln)
					if title:
						flag = True
						break
				if flag:
					expired.write(line)
				else:
					dest.write(line)
	dest.close()
	expired.close()

if __name__=="__main__":
	parse("torrent to direct link.html","down_links")
	rem_dupl_link("down_links","links")
	get_title("links","new_entry")
	confirm = str(raw_input("Do you want to check for expired links?"))
	if confirm in ["Yes","yes","y","Y","Yup","yup"]:
		check_expiry("Torrent.txt","Expired.Txt","prev_entry")
		append("prev_entry","new_entry")
	else:
		append("Torrent.txt","new_entry")
	rem_dupl("new_entry","final")
	rem_dupl("new","rem_new")
	sort("final","Torrent.txt")
	sort("rem_new","New.txt")
	del_temp("links","down_links","new_entry","final","new","rem_new")
