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
			dummy = doc['position']
		except:
			# no position data for this record just skip it
			continue
		# '{"index":{"_index":"nhs","_type":"prescription", "_id":"' + s[2]+s[8].replace(' ','').replace('\n','').replace('\r','') + '"}}\n' + json.dumps(doc) + '\n'
		bulk_doc.append(doc)
		if ((doc_id % batch_size) == 0):
			try:
				print ('indexing docs, up to ' + str(doc_id))
				#print(bulk_doc)
				#es.index(index='nhs', doc_type='prescription', id=str(doc_id),
				#	body=doc)
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
		#print(bulk_doc)
		#es.index(index='nhs', doc_type='prescription', id=str(doc_id),
		#	body=doc)
		helpers.bulk(es, bulk_doc)
		bulk_doc = []
	except:
		print ('Failed to insert ' + bulk_doc)
		bulk_doc = []
