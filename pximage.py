#!/usr/bin/python
# -*- encoding: utf-8 -*-
def Download_Image(urlfromdl):
	import requests
	from meta_parser import MetaParser
	inputurl = str(urlfromdl)
	schema = {
		'og:image': 'og:image'
	}

	urls = [inputurl]
	data = []

	for url in urls:
		result = MetaParser(url, schema).result
		data.append(result)
	finaldata = str(data)
	out = finaldata[ finaldata.find(" ")+2 : finaldata.find("'}]") ]
	downloadurl = str(out)
	fname = '500pxID_' + str(inputurl.split('/')[-2]) + '_photo.jpg'
	photodownload = requests.get(downloadurl)
	open(fname , 'wb').write(photodownload.content)


	
