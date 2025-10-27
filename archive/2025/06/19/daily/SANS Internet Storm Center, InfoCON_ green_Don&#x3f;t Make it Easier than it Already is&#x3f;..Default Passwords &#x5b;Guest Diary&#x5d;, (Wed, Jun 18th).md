---
title: Don&#x3f;t Make it Easier than it Already is&#x3f;..Default Passwords &#x5b;Guest Diary&#x5d;, (Wed, Jun 18th)
url: https://isc.sans.edu/diary/rss/32054
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-19
fetch_date: 2025-10-06T22:56:59.585689
---

# Don&#x3f;t Make it Easier than it Already is&#x3f;..Default Passwords &#x5b;Guest Diary&#x5d;, (Wed, Jun 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32052)
* [next](/diary/32058)

# [Don?t Make it Easier than it Already is?..Default Passwords [Guest Diary]](/forums/diary/Dont%2BMake%2Bit%2BEasier%2Bthan%2Bit%2BAlready%2BisDefault%2BPasswords%2BGuest%2BDiary/32054/)

**Published**: 2025-06-18. **Last Updated**: 2025-06-18 00:53:35 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Dont%2BMake%2Bit%2BEasier%2Bthan%2Bit%2BAlready%2BisDefault%2BPasswords%2BGuest%2BDiary/32054/#comments)

[This is a Guest Diary by Matthew Paul, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

Over the past few months, I’ve been working under a SANS Internet Storm Center (ISC) Sr. Handler as part of the SANS Degree Program ISC Internship.  The first objective of the internship is setting up a forward-facing honeypot on your network to review and report on log activity.

For this internship I wanted to focus more on packet vs log analysis. For my setup, I did a bare-metal install of the network analysis tool Malcolm to use as an NSM/IDS.  I setup a 5-port managed switch and configured a monitor port for the honeypot with the mirror sending packets to my Malcolm sensor. This setup allowed me to collect and analyze all traffic going to and from my honeypot.

Malcolm is a network capture and analysis tool smartly comprised of various open-source tools; Arkime, OpenSearch, Logstash, Filebeat, OpenSearch Dashboards, Zeek, Suricata, Yara, Capa, ClamAV, CyberChef, jQuery File Upload, NetBox, PostgresSQL, Redis, Keycloak, OpenResty, nginx-auth-ldap, Fluent Bit, Mark Baggett’s (SANS Instructor) freq.py, Florian Roth’s Signature-Base Yara Rules, Bart Blaze’s Yara Rules, RerversingLabs’ Yara Rules and multiple Zeek Packages.[[1](https://malcolm.fyi/docs/components.html)]

![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture1.png)
\*Graphic Sourced from https://malcolm.fyi/docs/components.html

Malcolm was created by Idaho National Labs as part of a CISA contract to assist with protecting critical infrastructure, most notably it incorporates ICS protocol parsers not commonly seen with other tools, albeit their inclusion is growing.

There is an additional tool that can be used with Malcolm, Hedgehog Linux. Deployment of a Hedgehog sensor seemed overkill for my use case, but it’s an option nonetheless.   Hedgehog Linux can be installed on a separate appliance as a PCAP ingestion sensor freeing up Malcolm resources for analysis.  The Hedgehog sensor monitors network interfaces, captures traffic and generates PCAPs, detects file transfers in network traffic and extracts/scans the files for threats, generates and forward Zeek logs, Arkime sessions, and other information to Malcolm [[2](https://malcolm.fyi/docs/hedgehog.html)].  It’s important to note you do not need the Hedgehog Linux sensor for Malcolm to work.  During the Malcolm install there is an option to have Malcolm ingest packets or use a Hedgehog Linux sensor.

![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture2.png)
\*Graphic Sourced from https://malcolm.fyi/docs/hedgehog.html

Malcolm can be installed via an ISO or ran in a Docker/Kubernetes container.  I opted for the bare-metal option as I had a spare Intel NUC computer that fit my needs, and having a dedicated compact capture sensor seemed like a good idea.  The Malcolm ISO is quite large, anywhere from 4 – 6 GBs requiring the ISO to be downloaded in chunks from GitHub. There is an included script (release\_cleaver.ps1) to stitch everything together.  Once downloaded and assembled, the ISO can be used to create a bootable drive using your favorite tool – Rufus, Balena Etcher…etc.

The install is straight forward and runs through multiple prompts for selecting a customized installation. The documentation is quite robust on the Malcolm page (https://malcolm.fyi/)  which mirrors their GitHub page. While previous installations resulted in some tweaks here and there, the most recent ISO worked as advertised post installation.

I am always surprised by the amount of people who are unaware of this tool.  The features and workflow made this internship so much easier than simply pulling and parsing honeypot logs.  Below is a common workflow that I used for one of the attacks I analyzed.

![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture3.jpg)

I found info for this particular attack in the Zeek Weird Logs.  Zeek Weird logs are generated by protocol anomalies [[3](http://Zeek Weird Logs: https://docs.zeek.org/en/master/logs/weird-and-notice.html)].  Weird.logs are often overlooked but can be advantageous to review, especially in my case where I only had traffic from one device.  There are other ways to filter for this example such as selecting Telenet from the Common Protocols List.  From here I filtered NUL\_in\_line to get the below. These logs indicate null bytes (\x00) are found in unexpected places.

![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture4.jpg)

From here I chose an IP originating from a country which I had a significant higher number of attacks – RUS.  Note:  Not captured on the previous dashboard image, but further down the screen was a world map with the IP activity level for each country. Selecting any identifying characteristic creates a dashboard filter.  Note the destination port number 23; Telnet.

![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture5.jpg)

Once I have an IP, date, and time I pivot over to Arkime.  From here I create a filter for the IP and input the appropriate date and time.  Arkime provides session data and the ability to download the pcap to open in Wireshark for a more thorough deep dive.  Note under the Data Source Zeek is displayed.  There are multiple data sources (Arkime, Suricata, Zeek…etc.) that can be separately displayed or displayed all at once.

![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture6.jpg)

Below Arkime is selected as the data source.  This view will provide the option to download the pcap which we will do next.

![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture7.jpg)

We’ll expand the session and select “Download PCAP.”

![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture8.jpg)

In Wireshark we see the below activity:

![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture9.jpg)

Since this is an unencrypted TCP session, we can right click and select follow stream to view the below output:

We see some root password guessing here with success using jvbzd, a default UNIX password SANS ISC advised against using this default password in 2016. [[4](https://isc.sans.edu/diary/21791)]

![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture10.jpg)
![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture11.jpg)
![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture12.jpg)

We see some recon attempts for mount points and attempts to reach out using wget. With this being a honeypot, the threat actor’s mobility was restricted and they eventually realized this and exited the box.

This is another strong reminder that only you can prevent easy exploitation by changing your default password. ![](https://isc.sans.edu/diaryimages/images/Matthew_Paul_Picture13.png)
Malcolm is a great tool and free to implement.

[1] https://malcolm.fyi/docs/components.html
[2] https://malcolm.fyi/docs/hedgehog.html
[3] Zeek Weird Logs: https://docs.zeek.org/en/master/logs/weird-and-notice.html
[4] https://isc.sans.edu/diary/21791
[5] https://www.sans.edu/cyber-security-programs/bachelors-degree/

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyB...