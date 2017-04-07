#!/usr/bin/env python

import sys
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(hosts=['localhost'])

if (len(sys.argv)<2):
	print ('usage ' + sys.argv[0] + ' <file>')
	exit()

batch_size = 100000

with open(sys.argv[1]) as f:
	doc_id=0;
	bulk_doc=[];
	for line in f:
		doc=eval(line);
		doc['_index']   = 'fit'
		doc['_type']    = 'wes'
		doc_id += 1
		try:
			dummy = doc['timestamp']
		except:
			# No timestamp, continue
			continue
		try:
			dummy = doc['position_lat']
			doc['position'] = {}
			# units are semicircles. Switch to degrees via
			# http://gis.stackexchange.com/questions/156887/conversion-between-semicircles-and-latitude-units
			doc['position']['lat'] = doc['position_lat'] * ( 180.0 / 2**31 )
			doc['position']['lon'] = doc['position_long'] * ( 180.0 / 2**31 )
			if (doc['position']['lon'] > 180.0):
				doc['position']['lon'] = doc['position']['lon'] - 360
			if (doc['position']['lat'] > 180.0):
				doc['position']['lat'] = doc['position']['lat'] - 360
		except:
			dummy = 1
		bulk_doc.append(doc)
		if ((doc_id % batch_size) == 0):
			try:
				print ('indexing docs, up to ' + str(doc_id))
				helpers.bulk(es, bulk_doc)
				bulk_doc = []
			except:
				print ('Failed to insert ' + bulk_doc)
				bulk_doc = []
				continue
# Write final odd batch
if (len(bulk_doc)>0):
	try:
		print ('indexing docs, up to ' + str(doc_id))
		helpers.bulk(es, bulk_doc)
		bulk_doc = []
	except:
		print ('Failed to insert ' + bulk_doc)
		bulk_doc = []
