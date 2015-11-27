projCVE

cveDbDownload.sh download CVE xml file

loadCVE.sh is to put in the /etc/cron.daily to update the xml 

apiCVE.py is the search script to xml file (response with JSON)

serverCVE.py is a web server between client and apiCVE.py


query example

curl http://10.1.101.41:8080/CVE-2015-1111
{"product": ["cpe:/o:apple:iphone_os:8.2"], "last-modified-datetime": "2015-09-30T14:12:59.597-04:00", "published-datetime": "2015-04-10T10:59:26.420-04:00", "id": "CVE-2015-1111", "summary": "Safari in Apple iOS before 8.3 does not delete Recently Closed Tabs data in response to a history-clearing action, which allows attackers to obtain sensitive information by reading a history file.", "cvss": {"availability-impact": "NONE", "access-vector": "NETWORK", "integrity-impact": "NONE", "access-complexity": "LOW", "generated-on-datetime": "2015-09-30T07:33:10.973-04:00", "source": "http://nvd.nist.gov", "authentication": "NONE", "score": "5.0", "confidentiality-impact": "PARTIAL"}}

