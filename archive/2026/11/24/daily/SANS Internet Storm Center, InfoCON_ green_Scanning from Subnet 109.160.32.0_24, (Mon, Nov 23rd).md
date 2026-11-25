---
title: Scanning from Subnet 109.160.32.0/24, (Mon, Nov 23rd)
url: https://isc.sans.edu/diary/rss/33550
source: SANS Internet Storm Center, InfoCON: green
date: 2026-11-24
fetch_date: 2026-11-25T10:48:08.069912
---

# Scanning from Subnet 109.160.32.0/24, (Mon, Nov 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33534)

Click HERE to learn more about classes Guy is teaching for SANS

# [Scanning from Subnet 109.160.32.0/24](/forums/diary/Scanning%2Bfrom%2BSubnet%2B10916032024/33550/)

**Published**: 2026-11-23. **Last Updated**: 2026-11-24 02:32:00 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Scanning%2Bfrom%2BSubnet%2B10916032024/33550/#comments)

This subnet is assigned to a web hosting and virtual private server (VPS) provider BANATSYNC SRL with AS198364, located in Timisoara, Romania. This graph shows the DShield sensor activity over the past 90 days for this subnet and it is still ongoing as of this writing.

![](https://isc.sans.edu/diaryimages/images/90_days_activity.png)

Using the [ES|QL](https://www.elastic.co/docs/reference/query-languages/esql) query listed below, starting the query from the 1 September 2026, 159 IPs from this block scanned at least once to multiple times my DShield sensors against mostly the SSH service and when found, attempted and sometimes successfully login the sensor. This analysis from this subnet started on the 5 September 2026 and capture regularly by 2 separate DShield sensors.

A review of both the firewall and cowrie logs, all IPs involved attempted to login into the SSH service with almost all (152 out 159) of them succeeding to login into the sensors using with the standard usernames (root, ubuntu, admin, etc.) using a single command (uname -s -v -n -r -m) followed by a immediate disconnection. One sensor received 127 unique IPs while the other received 134 unique IPs.

The firewall logs show some interesting characteristics with a time-to-live mostly between 45 to 52 with some exception that also include ranges between 232 to 243. In order to understand the discrepancies, I reviewed the packet capture from each sensor and found some packets where **69 IPs** stared with a static IPID of 54321 and every one of them had a TTL that range between 232 to 243. All the inbound backets behaved the same way, SYN, SYN-ACK, RST targeting various ports including TCP/2323, TCP/22 and TCP/2222 where the actors/bots sometimes after multiple attemps, successfully login.

![](https://isc.sans.edu/diaryimages/images/ip_id_54321.png)

Using the logs from the DShield SIEM and selecting only the traffic with the IPID 54321 and reviewing the Vega-Lite graph, it is easy to see the activity was consistent with the previously identified **69 IPs** that each time each IP would come live, the first packet was always starting with high TTL (230+) and the remainder packets were all using normal TTL related to a moderl [Linux](https://jumpcloud.com/it-index/what-is-time-to-live-ttl) system. In order to inspect why this would be happening, using packet capture by the sensors based on matching high TTL for one specific IP address (109.160.32.146) and what appeared was interesting. Using [tshark](https://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html) to replay the initial packet for 13 Nov 2026 started with a TTL of 239 and when that traffic responded with a reset (0x0004), the TTL was now 50. Any traffic that followed the first SYN packets all had TTL of 50 (picture below).

![](https://isc.sans.edu/diaryimages/images/Packet_ttl_IP109_160_32_146.png)

This is a sample of 4 IPs (DSL query below) out of the 69 that shows the first packet starting with a TTL 230+ followed by normal TTL after the activity continue. Reviewing  the reports from VirusTotal of those 4 IPs [[7](https://www.virustotal.com/gui/ip-address/109.160.32.88/community)][[8](https://www.virustotal.com/gui/ip-address/109.160.32.141/community)][[9](https://www.virustotal.com/gui/ip-address/109.160.32.147/community)][[10](https://www.virustotal.com/gui/ip-address/109.160.32.150/community)] shows all the same characteristics with SSH brute-force if SSH is listening and running some commands before disconnecting.

![](https://isc.sans.edu/diaryimages/images/low_high_TTL.png)

**Shodan Open Ports**
This is a random list of IPs checked against [Shodan](https://www.shodan.io/) that list the same open ports. The two sample lists show these IPs have SSH available as the only service while other have nothing open. If the SSH service is listening, it is using 2 different version of Ubuntu 24.04 LTS and 26.04 LTS.

**Shodan Information about SSH TCP/22**

109.160.32.34  SSH-2.0-OpenSSH\_10.2p1 Ubuntu-2ubuntu3.2 (Ubuntu 26.04 LTS)
109.160.32.141 SSH-2.0-OpenSSH\_9.6p1 Ubuntu-3ubuntu13   (Ubuntu 24.04 LTS)
109.160.32.147 SSH-2.0-OpenSSH\_9.6p1 Ubuntu-3ubuntu13   (Ubuntu 24.04 LTS)
109.160.32.150 SSH-2.0-OpenSSH\_9.6p1 Ubuntu-3ubuntu13   (Ubuntu 24.04 LTS)
109.160.32.200 SSH-2.0-OpenSSH\_10.2p1 Ubuntu-2ubuntu3.2 (Ubuntu 26.04 LTS)

**Shodan No Open Port for this IP sample**

109.160.32.12
109.160.32.66
109.160.32.80
109.160.32.88

**Kibana Traffic Analysis with DSL and ES|QL**

**DSL Query IP Range**

{
  "range": {
    "related.ip": {
      "gte": "109.160.32.0",
      "lte": "109.160.32.255"
    }
  }
}

**DSL Query for IP with a TTL Greater than 230**

{
  "range": {
    "network.ttl": {
      "gte": "230"
    }
  }
}

**DSL Query IP with Low & High TTL**

{
  "terms": {
    "related.ip": [
      "109.160.32.88",
      "109.160.32.141",
      "109.160.32.147",
      "109.160.32.150"
    ]
  }
}

**ES|QL Query**

FROM cowrie\*
| WHERE event.reference == "no match"
| WHERE CIDR\_MATCH(related.ip, "109.160.32.0/24")
| STATS  BY related.ip

FROM cowrie\*
| WHERE event.reference == "no match"
| WHERE CIDR\_MATCH(related.ip, "109.160.32.0/24")
| WHERE network.ttl >= 230
| STATS  BY network.ttl

**TShark Output**

This is the command used to verify the activity between low and high TTL:

tshark.exe -nnr tcp2323\_54321\_random.pcap -T fields -e frame.time -e ip.src -e ip.dst -e ip.ttl -e tcp.flags

[1] https://scamalytics.com
[2] https://arxiv.org/html/2307.08490v1
[3] https://github.com/zmap/zmap
[4] https://github.com/zmap/zmap/blob/main/src/probe\_modules/packet.c
[5] https://isc.sans.edu/tools/honeypot/
[6] https://github.com/bruneaug/DShield-SIEM/tree/main
[7] https://www.virustotal.com/gui/ip-address/109.160.32.88
[8] https://www.virustotal.com/gui/ip-address/109.160.32.141
[9] https://www.virustotal.com/gui/ip-address/109.160.32.147
[10] https://www.virustotal.com/gui/ip-address/109.160.32.150

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [VPS](/tag.html?tag=VPS) [AS198364](/tag.html?tag=AS198364) [DShield SIEM](/tag.html?tag=DShield SIEM) [TTL](/tag.html?tag=TTL) [DShield sensor](/tag.html?tag=DShield sensor) [Analysis](/tag.html?tag=Analysis)

[0 comment(s)](/diary/Scanning%2Bfrom%2BSubnet%2B10916032024/33550/#comments)

Click HERE to learn more about classes Guy is teaching for SANS

* [previous](/diary/33534)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking ...