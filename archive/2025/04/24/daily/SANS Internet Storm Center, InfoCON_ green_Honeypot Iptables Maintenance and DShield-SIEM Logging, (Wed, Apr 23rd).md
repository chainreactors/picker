---
title: Honeypot Iptables Maintenance and DShield-SIEM Logging, (Wed, Apr 23rd)
url: https://isc.sans.edu/diary/rss/31876
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-24
fetch_date: 2025-10-06T22:15:20.263412
---

# Honeypot Iptables Maintenance and DShield-SIEM Logging, (Wed, Apr 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31872)
* [next](/diary/31880)

# [Honeypot Iptables Maintenance and DShield-SIEM Logging](/forums/diary/Honeypot%2BIptables%2BMaintenance%2Band%2BDShieldSIEM%2BLogging/31876/)

**Published**: 2025-04-23. **Last Updated**: 2025-04-23 00:01:45 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[0 comment(s)](/diary/Honeypot%2BIptables%2BMaintenance%2Band%2BDShieldSIEM%2BLogging/31876/#comments)

In the last week I ran into some issues that I hadn't anticipated:

* Residential IP changed, some honeypots inacessible remotely
* Rebuilit DShield-SIEM [1], Zeek logs not displaying

## Be mindful of network interface labels

First, an IP address changing for a residential network is not uncommon. Some ISPs may regularly change IP addresses for homes and for most people using their connection for standard usage, it's not a problem. However, it can be challening when this IP address is used to grant special network access to resources. In my case, the local iptables firewall for my honeypots had a rule to allow access from specific IP addresses, including the public IP address for my home. Once the IP address changed, I no longer SSH access to my honeypot over port 12222 and someone else could try to connect if the had my previous IP address, even through they'd need my private SSH key. I thought that I had planned well, giving myself multiple networks I could access my honeypots from. It turns out that I made some mistakes when reusing iptables configurations from different honeypots.

**![](https://isc.sans.edu/diaryimages/images/2025-04-20_figure1.PNG)
Figure 1: Reusing iptables rules in '`/etc/network/iptables'` is problematic when interfaces are different between honeypots.**

The interface names were different for the primary network connection. The primary interface is often **`eth0`**, but this is not always the case. A couple of my honeypots had different interface names, which means that the rules I had created for remote access from other networks didn't function as expected.

Outside of statically assigning these in the `/etc/network/iptables` file, another way would be to leverage scripting to update this value on a regular basis, using interface data from the honeypot.

```

# script adds IP addresses that can connect to TCP 12222 for remote admin
# isc.sans.edu first resolved IP
# 172.16.0.0/12
# 192.168.0.0/16
# 10.0.0.0/8

# specify domain of home domain name
domain="isc.sans.edu"

# delete any rule specifying destination port 12222
sed -i "/\b\(dport 12222\)\b/d" /etc/network/iptables

# get primary interface to the internet
interface=$(ip route get 1.1.1.1 | grep -Po '(?<=dev\s)\w+' | cut -f1 -d ' ')

# get remote IP address of my home domain
# only use first result
remoteip=$(host $domain | grep "has address" | cut -d " " -f 4 | head -1)

# enter firewall rule in /etc/network/iptables
# add rule after line 'START: allow access to admin ports for local IPs'
# double quotes used to expand variables while preserving whitespace
sed -i "/START: allow access to admin ports for local IPs/a -A INPUT -i $interface \
-s $remoteip -p tcp --dport 12222 -j ACCEPT" /etc/network/iptables

# add any other ip addresses you may want
# enter firewall rule in /etc/network/iptables
# add rule after line 'START: allow access to admin ports for local IPs'
# double quotes used to expand variables while preserving whitespace
sed -i "/START: allow access to admin ports for local IPs/a -A INPUT -i $interface \
-s 172.16.0.0/12 -p tcp --dport 12222 -j ACCEPT" /etc/network/iptables

# add any other ip addresses you may want
# enter firewall rule in /etc/network/iptables
# add rule after line 'START: allow access to admin ports for local IPs'
# double quotes used to expand variables while preserving whitespace
sed -i "/START: allow access to admin ports for local IPs/a -A INPUT -i $interface \
-s 192.168.0.0/16 -p tcp --dport 12222 -j ACCEPT" /etc/network/iptables

# add any other ip addresses you may want
# enter firewall rule in /etc/network/iptables
# add rule after line 'START: allow access to admin ports for local IPs'
# double quotes used to expand variables while preserving whitespace
sed -i "/START: allow access to admin ports for local IPs/a -A INPUT -i $interface \
-s 10.0.0.0/8 -p tcp --dport 12222 -j ACCEPT" /etc/network/iptables
```

![](https://isc.sans.edu/diaryimages/images/2025-04-20_figure2.PNG)
**Figure 2: Scripted update of iptables rules for honeypot.**

This can get updated with variables to allow for some easier updating. In addition, some loops save some space and also allow for DNS names that may return multiple IP addresses.

```

# specify file name to modify
file="/etc/network/iptables"

# specify domain of home domain name
domain="isc.sans.edu"

# delete any rule specifying destination port 12222
sed -i "/\b\(dport 12222\)\b/d" $file

# specify ip addresses to allow for admin access
# space delimited
custom_ips="213.233.1.23 43.212.322.32 324.23.2.12"
private_ips="172.16.0.0/12 192.168.0.0/16 10.0.0.0/8"

# get primary interface to the internet
interface=$(ip route get 1.1.1.1 | grep -Po '(?<=dev\s)\w+' | cut -f1 -d ' ')

# get remote IP address(es) of my home domain
remoteips=$(host $domain | grep "has address" | cut -d " " -f 4)

# add rule after line 'START: allow access to admin ports for local IPs'
# double quotes used to expand variables while preserving whitespace
for item in $remoteips; do
  sed -i "/START: allow access to admin ports for local IPs/a -A INPUT -i $interface \
-s $item -p tcp --dport 12222 -j ACCEPT" $file
done

# add any other ip addresses you may want
# add rule after line 'START: allow access to admin ports for local IPs'
# double quotes used to expand variables while preserving whitespace
for item in $custom_ips; do
  sed -i "/START: allow access to admin ports for local IPs/a -A INPUT -i $interface \
-s $item -p tcp --dport 12222 -j ACCEPT" $file
done

# add any other ip addresses you may want
# add rule after line 'START: allow access to admin ports for local IPs'
# double quotes used to expand variables while preserving whitespace
for item in $private_ips; do
  sed -i "/START: allow access to admin ports for local IPs/a -A INPUT -i $interface \
-s $item -p tcp --dport 12222 -j ACCEPT" $file
done
```

**![](https://isc.sans.edu/diaryimages/images/2025-04-20_figure3_v2.PNG)
Figure 3: Firewall rules entered through new script.**

This works well for me since I'm using a Dynamic DNS service through AWS [2] on my pfsense [3] firewall. When my home IP address changes, an A record for my domain will get updated. That DNS entry will be used to retrieve my new IP address and the `/etc/network/iptables` files will get updated. It'll take about a day and I'll regain access to my honeypot. Why a day? The `/etc/network/iptables` file is only processed on boot and the honeypot automatically reboots once per day.

**![](https://isc.sans.edu/diaryimages/images/2025-04-20_figure3.PNG)
Figure 4: Example configuration from pfsense router for Dynamic DNS.**

Now, there's a workaround in place for my infrequent IP address changes. Now onto my Zeek logging issues.

## Filebeat versioning and Zeek log forwarding

After rebuilding my DShield-SIEM ELK instance at home, I noticed I wasn't receiving Zeek logs in my dashboards. While troubleshooting, I learned how to use some helpful troubleshooting tools within Elastic, particularly Dev Tools [4].

**![](https://isc.sans.edu/diaryimages/images/2025-04-20_figure4.PNG)
Figure 5: Dev Tools link highlighted in Management area of Elastic.**

Troubleshooting steps given in many guides reference commands that can be run against Elasticsearch APIs. This can be done using other tools like Curl, but the Console was much easier. I ended up going t...