#!/usr/bin/python
# -*- encoding: utf-8 -*-
def Download_Meta(urlfromdl):
	from meta_parser import MetaParser
	inputurl = str(urlfromdl)
	schema = {
		'five_hundred_pixels:author': 'five_hundred_pixels:author',
		'five_hundred_pixels:category': 'five_hundred_pixels:category',
		'five_hundred_pixels:highest_rating': 'five_hundred_pixels:highest_rating',
		'five_hundred_pixels:uploaded': 'five_hundred_pixels:uploaded',
		'five_hundred_pixels:tags': 'five_hundred_pixels:tags',
		'og:title': 'og:title',
		'og:description': 'og:description',
		'og:image': 'og:image',
		'og:image:width': 'og:image:width',
		'og:image:height': 'og:image:height',
		'og:type': 'og:type',
		'og:url': 'og:url',
		'al:ios:app_name': 'al:ios:app_name',
		'al:android:app_name': 'al:android:app_name',
		'al:ios:url': 'al:ios:url',
		'al:android:url': 'al:android:url',
		'al:ios:app_store_id': 'al:ios:app_store_id',
		'al:android:package': 'al:android:package',
		'twitter:card': 'twitter:card',
		'twitter:site': 'twitter:site',
		'twitter:title': 'twitter:title',
		'twitter:image:src': 'twitter:image:src',
		'twitter:image:width': 'twitter:image:width',
		'twitter:image:height': 'twitter:image:height',
		'twitter:domain': 'twitter:domain',
		'twitter:app:name:iphone': 'twitter:app:name:iphone',
		'twitter:app:name:ipad': 'twitter:app:name:ipad',
		'twitter:app:name:googleplay': 'twitter:app:name:googleplay',
		'twitter:app:url:iphone': 'twitter:app:url:iphone',
		'twitter:app:url:ipad': 'twitter:app:url:ipad',
		'twitter:app:url:googleplay': 'twitter:app:url:googleplay',
		'twitter:app:id:iphone': 'twitter:app:id:iphone',
		'twitter:app:id:ipad': 'twitter:app:id:ipad',
		'twitter:app:id:googleplay': 'twitter:app:id:googleplay'
	}
	urls = [inputurl]
	data = []

	for url in urls:
		result = MetaParser(url, schema).result
		data.append(result)
	finaldata = str(data)
	open('500pxID_' + str(inputurl.split('/')[-2]) + '_metadata.txt', 'wb').write(finaldata)
