#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 26/11/2015

# DOC
#https://github.com/jkordish/Python/blob/master/nvdcve-xml-parser-new.py
#http://infohost.nmt.edu/~shipman/soft/pylxml/web/Element-find.html

# INSTALL
#apt-get install libxml2 python-lxml

from lxml import etree, objectify
import sys
import json
import re

# namespaces definition
nsd = {'vuln':'http://scap.nist.gov/schema/vulnerability/0.4',
       'cvss':'http://scap.nist.gov/schema/cvss-v2/0.2',
       'scap-core':'http://scap.nist.gov/schema/scap-core/0.1',
       'xsi':'http://www.w3.org/2001/XMLSchema-instance',
       'patch':'http://scap.nist.gov/schema/patch/0.1',
       'cpe-lang':'http://cpe.mitre.org/language/2.0',
      }
# element recovered in xml
xmlVuln = {'summary': 'vuln:summary',
            'published-datetime': 'vuln:published-datetime',
	    'last-modified-datetime': 'vuln:last-modified-datetime',
           }

# script need one arg  
if len(sys.argv) != 2:
	print('fail nb arg')
	print('python apiCVE.py CVE-YYYY-xxxx')
	exit()
cveName = sys.argv[1].upper()

if re.match('CVE-[0-9]{4}-[0-9]{4}',cveName) is None:
	print '{"error": "fail format arg, format like CVE-YYYY-xxxx Y and x is int"}'
	exit()

search = sys.argv[1].split("-") #split input CVE-2015-8320
date = search[1]
file="nvdcve-2.0-"+date+".xml" # xml db name

try:
	tree = etree.parse("db/"+file) # load xml db
except:
	print '{"error": "file doesn\'t exist"}'
	exit()

root = tree.getroot()

# search in xml
data = {} # result
cvss = {}
product = []
for entry in root:
	id = entry.get('id') # get CVE id
	if id == "-".join(search):
		data['id'] = id	
		# extract vuln information
		for name,value in xmlVuln.iteritems():
			data[name] = entry.find(value,namespaces=nsd).text
		
		# extract cvss information
		for cvssObj in entry.find('vuln:cvss/cvss:base_metrics',namespaces=nsd).iterchildren():
			name = cvssObj.tag.split('}')[1] # split namespace and name !
			cvss[name] = cvssObj.text

		# extract product information
                for productObj in entry.find('vuln:vulnerable-software-list',namespaces=nsd).iterchildren():
                        product.append(productObj.text)
	
		break # exit if

if data:
        data['cvss'] = cvss
        data['product'] = product
else:
        data['result']= ' no result'

print json.dumps(data)

