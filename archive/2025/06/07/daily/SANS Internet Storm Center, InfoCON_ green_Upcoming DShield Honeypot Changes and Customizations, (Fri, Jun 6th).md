---
title: Upcoming DShield Honeypot Changes and Customizations, (Fri, Jun 6th)
url: https://isc.sans.edu/diary/rss/32016
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-07
fetch_date: 2025-10-06T22:57:23.568580
---

# Upcoming DShield Honeypot Changes and Customizations, (Fri, Jun 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32014)
* [next](/diary/32020)

# [Upcoming DShield Honeypot Changes and Customizations](/forums/diary/Upcoming%2BDShield%2BHoneypot%2BChanges%2Band%2BCustomizations/32016/)

**Published**: 2025-06-06. **Last Updated**: 2025-06-06 00:35:23 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[0 comment(s)](/diary/Upcoming%2BDShield%2BHoneypot%2BChanges%2Band%2BCustomizations/32016/#comments)

There are some upcoming DShield honeypot [1] changes that introduce some opportunities for additional customization and data analysis. For most users, no additional actions are needed. A couple of those changes:

* **`dshield.ini`** file move from **`/etc/`** to **`/srv/dshield/etc/`** - A symbolic link will exist for the previous file location for backward compatibility. If you have automation to update anything in **`/etc/dshield.ini`**, you may need to update your scripts. Some tools can recreate the file in the previous location, breaking the link to the new location.
* New web honeypot with new options (thanks, Mark Baggett!) - By default, no local logs are generated, which is helpful to save space, but means some customizations may be required if you want to maintain local logs.

## Local Logging

For my own honeypots, I like to maintain local logs. This can be helpful for larger volumes of data or there is a need to analyze the data over time using your own tools. Downloading the information from your ISC portal account is useful, but may not include all data fields. In addition, some daily volumes make it very difficult, if not impossible, to download directly using the options given from the portal. Recently, one of my honeypots had a local web honeypot log of almost 60GB, which was only for one day. This was due to an increase in activity on 5/19/2025, including some URLs noted by Guy a few weeks prior [2].

**![](https://isc.sans.edu/diaryimages/images/2025-06-06_figure1.PNG)
Figure 1: Web honeypot logs showing large volumes of traffic from [193.29.13.44](/ipinfo.html?ip=193.29.13.44) and many other hosts on 5/19/2025.**

**![](https://isc.sans.edu/diaryimages/images/2025-06-06_figure2v2.PNG)
Figure 2: Volume of data storage for multiple honeypots, showing some large web honeypot logs.**

## New Web Honeypot [3]

The new web honeypot allows for much more customization for the honeypot itself, which opens up a lot of opportunities to gather data. One of the items that I'm most excited about is that **`POST`** data will now be collected within the log files.

Getting POST data from new web honeypot log:

```

# read all files in /logs starting with "webhoneypot"
# cat /logs/webhoneypot*

# filter for any data containing the string POST
# grep POST

# find data with the following URL path: "/cgi-bin/../../../../../../../../../../bin/sh"
# jq 'select(.url=="/cgi-bin/../../../../../../../../../../bin/sh")'

# get the POST .data field, sort it, count unique values and sort by the count
# jq .data | sort | uniq -c | sort -n
#

cat /logs/webhoneypot* | grep POST | jq 'select(.url=="/cgi-bin/../../../../../../../../../../bin/sh")' \
| jq .data | sort | uniq -c | sort -n
```

**![](https://isc.sans.edu/diaryimages/images/2025-06-06_figure3.PNG)
Figure 3: Gathering POST data from new local web honeypot logs.**

For the old web honeypot logs, no data is available in the local logs, but it can be retrieved in many ways if you have PCAPs. One method is tshark [4].

```

# read all PCAP files in the /dumps directory
# for file in /dumps/*.pcap

# for each file, read it with tshark
# do echo "$file";tshark -n -r "$file"

# filter for POST requests
# -Y "http.request.method == \"POST\""

# select URI and data fields
# -T fields -e http.request.uri -e data.data

# only show results with "cgi-bin"
# grep "cgi-bin";done

# look for any POST data in files where the URL contains "cgi-bin"
#  cat /logs/webhoneypot* | grep POST | jq 'select(.url | contains("cgi-bin"))' | \
#  jq .data | sort | uniq -c | sort -n

for file in /dumps/*.pcap;do echo "$file";tshark -n -r "$file" -Y "http.request.method == \"POST\"" \
-T fields -e http.request.uri -e data.data | grep "cgi-bin";done
```

![](https://isc.sans.edu/diaryimages/images/2025-06-06_figure4.PNG)
**Figure 4: POST data exists, but a PCAP is needed. The data does not appear in local JSON logs.**

## Modifications After Honeypot Upgrade

In a previous diary, I went through my steps to customize my honeypot [5] and many of these changes are to try and maintain the same kind of local log data storage.

| Function of Change | File / Folder | Change Made |
| --- | --- | --- |
| Add filebeat path to look for log file in new location for forwarding to DShield-SIEM [6] | `/etc/filebeat/filebeat.yml` | Added to paths:    `- /srv/log/webhoneypot*.json` |
| Update firewall rules for remote access | `/etc/network/iptables` | Ran script for automatic update [7] |
| Add web honeypot local logging | `/srv/dshield/etc/dsield.ini` | Added to **`[plugin:tcp:http]`** stanza:    `enable_local_logs=true` |
| Add web honeypot local logging location | `/srv/dshield/etc/dsield.ini` | Added to **`[plugin:tcp:http]`** stanza:    `local_logs_file=/srv/log/webhoneypot-srvconfig.json` |
| Fix dshield.ini permissions due to the use of 'sed -i' inplace editing [8] | `/srv/dshield/etc/dshield.ini` | `sudo chgrp webhpot /srv/dshield/etc/dshield.ini` |
| Update group ownership of folder so 'webhpot' user can save logs to location | `/srv/log` | `sudo chgrp webhpot /srv/log` |

To help automate this a bit, I created a bash script:

```

# specify file name to modify
file="/etc/network/iptables"

# specify domain of home domain name
domain="isc.sans.edu"

# delete any rule specifying destination port 12222
sudo sed -i "/\b\(dport 12222\)\b/d" $file

# specify ip addresses to allow for admin access
# space delimited
custom_ips=""
private_ips="172.16.0.0/12 192.168.0.0/16 10.0.0.0/8"

# get primary interface to the internet
interface=$(ip route get 1.1.1.1 | grep -Po '(?<=dev\s)\w+' | cut -f1 -d ' ')

# get remote IP address of my home domain
# only use first result
remoteip=$(host $domain | grep "has address" | cut -d " " -f 4 | head -1)

# add rule after line 'START: allow access to admin ports for remote IPs'
# double quotes used to expand variables while preserving whitespace
sudo sed -i "/START: allow access to admin ports for local IPs/a -A INPUT -i $interface -s $remoteip -p tcp --dport 12222 -j ACCEPT" $file

# add any other ip addresses you may want
# add rule after line 'START: allow access to admin ports for custom IPs'
# double quotes used to expand variables while preserving whitespace
for item in $custom_ips; do
  sudo sed -i "/START: allow access to admin ports for local IPs/a -A INPUT -i $interface -s $item -p tcp --dport 12222 -j ACCEPT" $file
done

# add any other ip addresses you may want
# add rule after line 'START: allow access to admin ports for private IPs'
# double quotes used to expand variables while preserving whitespace
for item in $private_ips; do
  sudo sed -i "/START: allow access to admin ports for local IPs/a -A INPUT -i $interface -s $item -p tcp --dport 12222 -j ACCEPT" $file
done

# add extra logging location for longer retention of iptables logs
sed -i '/localcopy\=/d' /srv/dshield/etc/dshield.ini
sed -i '/\[plugin:tcp:http\]/i localcopy=/logs/dshield_firewall_.log' /srv/dshield/etc/dshield.ini

# update new dshield.ini to enable local web-honeypot logging
sed -i '/enable_local_logs\=/d' /srv/dshield/etc/dshield.ini
sed -i '/\[plugin\:tcp\:http\]/a enable_local_logs\=true' /srv/dshield/etc/dshield.ini
sed -i '/local_logs_file\=/d' /srv/dshield/etc/dshield.ini
sed -i '/\[plugin\:tcp\:http\]/a local_logs_file\=\/srv\/log\/webhoneypot-srvconfig.json' /srv/dshield/etc/dshield.ini
...