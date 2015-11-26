#!/bin/bash
# download CVE db full or last modified
# 25/11/2015
# chmod +x cveDbDownload.sh
# use unzip,


usage() { 
	echo "-a download all xml file from 2002 to now"
	echo "-y [yyyy] download the yyyy year database. yyyy is for example 2015"
	echo "Usage: ./$0 [-a | -y yyyy]" 1>&2; exit 1;
 }

dlAllDb(){
	start=2002
	currentYear=$(date +'%Y')
	for (( y=$start; y<=$currentYear; y++ ))
	do
		path="db"
		zipName="nvdcve-2.0-${y}.xml.zip"
		name="nvdcve-2.0-${y}.xml"
		url="http://static.nvd.nist.gov/feeds/xml/cve/${zipName}"
		mkdir db 2>/dev/null
		echo "	dl $name in $path ..."
		wget -q -O ${path}/${zipName} $url
		echo "unzip ..."
		unzip -qq -o ${path}/${zipName} -d ${path}/
		echo "rm zip ..."
		rm ${path}/${zipName}
	done
}

dlYearDb(){
	y=$1
   	path="db"
        zipName="nvdcve-2.0-${y}.xml.zip"
        name="nvdcve-2.0-${y}.xml"
        url="http://static.nvd.nist.gov/feeds/xml/cve/${zipName}"
        mkdir db 2>/dev/null
        echo "  dl $name in $path ..."
        wget -q -O ${path}/${zipName} $url
        echo "unzip ..."
        unzip -qq -o ${path}/${zipName} -d ${path}/
        echo "rm zip ..."
        rm ${path}/${zipName}
}

while getopts "ay:" o; do
    case "${o}" in
        a)
            	dlAllDb
           	;;
        y)
            	year=${OPTARG}
	    	dlYearDb "$year"
	   	;;
        *)
		usage
            	;;
    esac
done

if test $# -eq 0
then
     usage
fi
