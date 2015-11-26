#!/usr/bin/python

import subprocess

#print subprocess.call(['./apiCVE.py', 'CVE-2015-1111'])

import web

urls = (
    '/','get_index',
    '/(.*)', 'get_CVE',
)

app = web.application(urls, globals())

class get_CVE:
    def GET(self, cve):
	print "log: "+cve
	p = subprocess.Popen(['./apiCVE.py', cve], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, err = p.communicate()
	return output

class get_index:
    def GET(self):
	message = "<H1>CVE API</H1> http://ip/CVE-YYYY-xxxx to get JSON CVE information"
        return message

if __name__ == "__main__":
    app.run()
