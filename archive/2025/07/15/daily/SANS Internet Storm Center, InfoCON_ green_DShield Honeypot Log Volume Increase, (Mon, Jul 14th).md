---
title: DShield Honeypot Log Volume Increase, (Mon, Jul 14th)
url: https://isc.sans.edu/diary/rss/32100
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-15
fetch_date: 2025-10-06T23:51:17.537821
---

# DShield Honeypot Log Volume Increase, (Mon, Jul 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32094)
* [next](/diary/32102)

# [DShield Honeypot Log Volume Increase](/forums/diary/DShield%2BHoneypot%2BLog%2BVolume%2BIncrease/32100/)

**Published**: 2025-07-14. **Last Updated**: 2025-07-14 18:58:30 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[0 comment(s)](/diary/DShield%2BHoneypot%2BLog%2BVolume%2BIncrease/32100/#comments)

The volume of honeypot logs changes over time. Very rarely are honeypot logs quiet, meaning that there are no internet scans or malicious activity generating logs. Honeypots can see large increases in activity [1], but this has tended to be the exception, rather than the rule. Within the last few months, however, there has been a dramatic increase in honeypot log volumes and how often these high volumes are seen. This has not just been from my residential honeypot, which has historically seen higher log volumes, but from all of the honeypots that I run and archive logs from frequently.

**![](https://isc.sans.edu/diaryimages/images/2025-07-14_figure1.png)
Figure 1: Log volumes for multiple honeypots over the last 13-14 months. Recent activity has drowned out earlier traffic volumes, making them appear nonexistent.**

To help demonstrate that other logs do exist, the high volume contributors were filtered out. Any source network (/24 in size) that contributed more than 1,000,000 logs in a day was removed.

**![](https://isc.sans.edu/diaryimages/images/2025-07-14_figure2.png)
Figure 2: Log volumes over time when filtering out sources that have contributed more than 1,000,000 logs in a day.**

The source of the log volume has been from the web honeypot logs.

**![](https://isc.sans.edu/diaryimages/images/2025-07-14_figure3.png)
Figure 3: Web honeypot log volumes have been the highest contributor for these outliers.**

More activity can be seen earlier in the year when large volume contributors are taken out. Even though this allows us to see more data prior to April of 2025, there is still an obvious increase in the last few months.

**![](https://isc.sans.edu/diaryimages/images/2025-07-14_figure4.png)
Figure 4: Web honeypot logs for the last 13-14 months, factoring out sources that have contributed more than 1,000,000 logs in a single day.**

Previous high volume periods are also unable to be seen easily due to the recent higher log volume.

**![](https://isc.sans.edu/diaryimages/images/2025-07-14_figure5.png)
Figure 5: Previous days considered to be anomalous in terms of high-volume traffic barely register in comparison to recent web honeypot logs.**

It has not been uncommon to see web honeypot files greater than 1 GB for a day of activity in the last couple of months. In the last few weeks, multiple honeypots have generated logs over 20 GB for one day of activity and for multiple days. In one day, a honeypot generated nearly 58 GB of web honeypot logs, which beat a previous "record" of ~35 GB.

**![](https://isc.sans.edu/diaryimages/images/2025-07-14_figure6.png)
Figure 6: The volumes are increasing, but are also happening more often, demonstrated by a significant rise in the average size of locally stored web honeypot logs.**

So where are these logs coming from and what are they looking for? Since many source IP addresses were seen coming from overlapping subnets, the data was summarized by subnet. The data highlights that some subnets are focused on a small number of unique URL paths.

| Subnet | Web Honeypot Hits | Unique IP Count | Unique URL Path Count | Top IP | Top URL Path |
| --- | --- | --- | --- | --- | --- |
| 45.146.130.0/24 | 20078392935 | 6 | 55 | [45.146.130.107](/ipinfo.html?ip=45.146.130.107) | / |
| 179.60.146.0/24 | 15730010424 | 2 | 2 | [179.60.146.100](/ipinfo.html?ip=179.60.146.100) | /\_\_api\_\_/v1/config/domains [2] |
| 185.93.89.0/24 | 4976900543 | 6 | 134 | [185.93.89.185](/ipinfo.html?ip=185.93.89.185) | / |
| 204.152.199.0/24 | 4421115971 | 9 | 2 | [204.152.199.8](/ipinfo.html?ip=204.152.199.8) | / |
| 72.11.141.0/24 | 4241370914 | 13 | 2 | [72.11.141.14](/ipinfo.html?ip=72.11.141.14) | / |
| 96.47.225.0/24 | 3636730956 | 9 | 2 | [96.47.225.5](/ipinfo.html?ip=96.47.225.5) | / |
| 185.193.88.0/24 | 3610407610 | 4 | 4 | [185.193.88.178](/ipinfo.html?ip=185.193.88.178) | /\_\_api\_\_/v1/config/domains |
| 155.94.185.0/24 | 3165292268 | 9 | 2 | [155.94.185.3](/ipinfo.html?ip=155.94.185.3) | / |
| 149.56.205.0/24 | 2718351438 | 1 | 3 | [149.56.205.13](/ipinfo.html?ip=149.56.205.13) | / |
| 193.111.208.0/24 | 2517999488 | 1 | 3 | [193.111.208.87](/ipinfo.html?ip=193.111.208.87) | / |
| 193.29.13.0/24 | 2248677302 | 1 | 2 | [193.29.13.44](/ipinfo.html?ip=193.29.13.44) | / |
| 92.63.196.0/24 | 2204582018 | 5 | 4 | [92.63.196.179](/ipinfo.html?ip=92.63.196.179) | /\_\_api\_\_/v1/config/domains |
| 80.82.65.0/24 | 927668585 | 3 | 3 | [80.82.65.127](/ipinfo.html?ip=80.82.65.127) | / |
| 151.243.93.0/24 | 560421646 | 1 | 3 | [151.243.93.62](/ipinfo.html?ip=151.243.93.62) | / |
| 79.141.162.0/24 | 527387481 | 1 | 3 | [79.141.162.39](/ipinfo.html?ip=79.141.162.39) | / |
| 83.229.17.0/24 | 463243368 | 2 | 4 | [83.229.17.112](/ipinfo.html?ip=83.229.17.112) | / |
| 91.199.163.0/24 | 447956151 | 1 | 2 | [91.199.163.102](/ipinfo.html?ip=91.199.163.102) | /\_\_api\_\_/v1/config/domains |
| 141.98.80.0/24 | 174475074 | 22 | 3 | [141.98.80.136](/ipinfo.html?ip=141.98.80.136) |  |
| 46.161.27.0/24 | 76298489 | 9 | 3 | [46.161.27.97](/ipinfo.html?ip=46.161.27.97) | / |
| 80.243.171.0/24 | 68840696 | 1 | 18152 | [80.243.171.172](/ipinfo.html?ip=80.243.171.172) | / |
| 171.22.28.0/24 | 60795298 | 2 | 2 | [171.22.28.30](/ipinfo.html?ip=171.22.28.30) | / |
| 45.227.255.0/24 | 39617032 | 7 | 4 | [45.227.255.90](/ipinfo.html?ip=45.227.255.90) |  |
| 184.105.247.0/24 | 33156996 | 46 | 7 | [184.105.247.252](/ipinfo.html?ip=184.105.247.252) | / |
| 213.209.150.0/24 | 23439064 | 2 | 2 | [213.209.150.239](/ipinfo.html?ip=213.209.150.239) | / |
| 204.76.203.0/24 | 17219727 | 15 | 1127 | [204.76.203.206](/ipinfo.html?ip=204.76.203.206) | / |
| 198.7.119.0/24 | 14768235 | 2 | 5437 | [198.7.119.14](/ipinfo.html?ip=198.7.119.14) | /index.php |
| 77.90.153.0/24 | 13968760 | 2 | 144 | [77.90.153.248](/ipinfo.html?ip=77.90.153.248) | / |
| 185.218.84.0/24 | 12687799 | 13 | 4 | [185.218.84.178](/ipinfo.html?ip=185.218.84.178) | / |
| 65.49.20.0/24 | 11897736 | 61 | 6 | [65.49.20.68](/ipinfo.html?ip=65.49.20.68) | / |
| 74.82.47.0/24 | 9974952 | 61 | 6 | [74.82.47.3](/ipinfo.html?ip=74.82.47.3) | / |
| 184.105.139.0/24 | 8966536 | 60 | 7 | [184.105.139.67](/ipinfo.html?ip=184.105.139.67) | / |
| 111.170.18.0/24 | 8271554 | 1 | 1 | [111.170.18.49](/ipinfo.html?ip=111.170.18.49) | api.ipapi.is:443 |
| 185.91.127.0/24 | 7976326 | 10 | 27 | [185.91.127.66](/ipinfo.html?ip=185.91.127.66) | myip.wtf:443 |
| 216.218.206.0/24 | 6055214 | 61 | 6 | [216.218.206.66](/ipinfo.html?ip=216.218.206.66) | / |
| 98.82.141.0/24 | 4647608 | 1 | 6724 | [98.82.141.184](/ipinfo.html?ip=98.82.141.184) |  |
| 51.222.26.0/24 | 4598477 | 2 | 7029 | [51.222.26.42](/ipinfo.html?ip=51.222.26.42) |  |
| 23.234.91.0/24 | 4454070 | 1 | 1 | [23.234.91.166](/ipinfo.html?ip=23.234.91.166) | / |
| 5.183.209.0/24 | 3993952 | 1 | 6 | [5.183.209.244](/ipinfo.html?ip=5.183.209.244) | / |
| 37.19.221.0/24 | 3922037 | 4 | 1 | [37.19.221.152](/ipinfo.html?ip=37.19.221.152) | / |
| 149.50.103.0/24 | 3764760 | 1 | 1 | [149.50.103.48](/ipinfo.html?ip=149.50.103.48) | / |
| 154.81.156.0/24 | 3665899 | 10 | 10 | [154.81.156.7](/ipinfo.html?ip=154.81.156.7) | / |
| 207.167.67.0/24 | 3593126 | 7 | 6 | [207.167.67.206](/ipinfo.html?ip=207.167.67.206) |  |
| 64.62.197.0/24 | 3456463 | 240 | 8 | [64.62.197.92](/ipinfo.html?ip=64.62.197.92) | / |
| 207.180.204.0/24 | 3291942 | 1 | 6911 | [207.180.204.178](/ipinfo.html?ip=207.180.2...