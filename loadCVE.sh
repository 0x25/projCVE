#!/bin/bash

# edit and add this file in /etc/cron.daily
# chmod +x


# path to cve download bash script
path="/opt/projCVE/cveDbDownload.sh"
currentYear=$(date +'%Y')

$path -y $currentYear # add logfile if need

