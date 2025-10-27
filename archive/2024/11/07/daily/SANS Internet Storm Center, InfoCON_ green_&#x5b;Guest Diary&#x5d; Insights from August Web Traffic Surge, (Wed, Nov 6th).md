---
title: &#x5b;Guest Diary&#x5d; Insights from August Web Traffic Surge, (Wed, Nov 6th)
url: https://isc.sans.edu/diary/rss/31408
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-07
fetch_date: 2025-10-06T19:26:58.546027
---

# &#x5b;Guest Diary&#x5d; Insights from August Web Traffic Surge, (Wed, Nov 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31406)
* [next](/diary/31414)

# [[Guest Diary] Insights from August Web Traffic Surge](/forums/diary/Guest%2BDiary%2BInsights%2Bfrom%2BAugust%2BWeb%2BTraffic%2BSurge/31408/)

**Published**: 2024-11-06. **Last Updated**: 2024-11-06 04:32:30 UTC
**by** [Trevor Coleman, SANS.edu BACS Student](/handler_list.html#trevor-coleman,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/Guest%2BDiary%2BInsights%2Bfrom%2BAugust%2BWeb%2BTraffic%2BSurge/31408/#comments)

[This is a Guest Diary by Trevor Coleman, an ISC intern as part of the SANS.edu Bachelor's Degree in Applied Cybersecurity (BACS) program [1].

**![](https://isc.sans.edu/diaryimages/images/2024-11-02_figure1.png)
Figure 1: ISC Web Honeypot Log Overview Chart [2]**

The month of August brought with it a notable surge in web traffic log activities, catching my attention. As I delved into investigating the underlying causes of this spike, I uncovered some concerning findings that shed light on the potential risks organizations face in today's digital landscape.

The web honeypot log traffic, as parsed in the DShield-SIEM dashboard [3], served as a visual representation of the significant increase in activity. With over 62,000,000 activity logs originating from a single IP source, it was evident that something was amiss, comparatively to the second most source at 757,000.  The most observed activity was directed towards destination ports 5555, 7547, and 9000, indicating a targeted effort to exploit vulnerabilities in web applications.  Ports 5555 and 9000 are commonly used in malware attacks for known vulnerabilities on webservers.

**![](https://isc.sans.edu/diaryimages/images/2024-11-02_figure2.png)
Figure 2: DShield-SIEM Traffic Analytics for IP %%ip: 23.95.107.6%%.**

**![](https://isc.sans.edu/diaryimages/images/2024-11-02_figure3.PNG)
Figure 3: Five IP addresses with highest traffic volume in August.**

Analysis of the HTTP requests to the web honeypot revealed that the attacker exploited various known vulnerabilities. Out of the total requests, 57,243,299 (92%) were **GET** requests, 4,960,056 (8%) were **POST** requests, while there were significantly fewer **PUT** (18,466) and **DELETE** (4,150) requests. Figure 5 shows the top 5 http request methods and corresponding logs and count of each attempt. Note only 2 different **PATCH** request types were present.

**![](https://isc.sans.edu/diaryimages/images/2024-11-02_figure4_v4.PNG)
Figure 4: Top HTTP Request Methods and Logs for IP [23.95.107.6](/ipinfo.html?ip=23.95.107.6).**

These included path traversal, Nuclei exploits, open redirect in Bitrix site manager, SQL injection, and PHP/WordPress attacks. The frequency and nature of these attacks pointed towards a well-orchestrated campaign aimed at compromising systems and gaining unauthorized access to sensitive information [4][5][6].

The attacker's use of scanning capabilities to identify known exploits and CVEs, as well as the observation of Mitre ATT&CK techniques and tactics [7], highlighted the sophistication of the threat actors behind these malicious activities. The ultimate goal of this attack was clear - to exploit vulnerabilities in web applications and compromise target systems for nefarious purposes.

In order to protect systems from such attacks, it is imperative for organizations to implement a multi-layered defense strategy. This includes the following measures:

* Deploy a web application firewall to monitor and filter incoming and outgoing traffic.
* Ensure continuous application patching to address known vulnerabilities and mitigate risks.
* Conduct frequent web application vulnerability scans to identify and remediate CVEs.
* Perform annual web penetration tests to proactively identify weaknesses and shore up defenses.
* Monitor **GET** and **POST** request traffic exposed to the internet to detect and respond to suspicious activities.
* Close unnecessary ports and services to minimize the attack surface and reduce potential entry points for threat actors.

Furthermore, it is important to keep a watchful eye on IP addresses associated with malicious activities and take appropriate action to mitigate risks. In this case, the IP address 23.95.107.6, leased by RackNerd LLC, has been flagged for abuse due to web application attacks [8][9]. RackNerd, which provides Infrastructure-as-a-Service (IaaS), including VPS and dedicated servers with headquarters in Los Angeles, California.

Ports 22, 5222, and 5269 were found to be open on this device [10]. Ports 5222 and 5269 are commonly used for Extensible Messaging and Presence Protocol (XMPP) for chat clients such as Jabber, Google Talk and WhatsApp to name a few [11][12].  This situation further highlighting the need for heightened vigilance and remediation efforts.

In conclusion, the recent surge in web traffic log activities serves as a stark reminder of the evolving cybersecurity threat landscape and the importance of proactive defense measures. By staying informed, conducting regular vulnerability assessments, and implementing robust security protocols, organizations can strengthen their resilience against cyber threats and safeguard their digital assets from malicious actors.

[1] <https://www.sans.edu/cyber-security-programs/bachelors-degree/>
[2] <https://isc.sans.edu/myweblogs/>
[3] <https://github.com/bruneaug/DShield-SIEM/blob/main/README.md>
[4] <https://www.cve.org/CVERecord?id=CVE-2024-1561>
[5] <https://nvd.nist.gov/vuln/detail/CVE-2024-27920>
[6] <https://www.cvedetails.com/cve/CVE-2008-2052/>
[7] <https://attack.mitre.org/tactics/TA0043/>
[8] <https://www.virustotal.com/gui/ip-address/23.95.107.6/detection>
[9] <https://www.abuseipdb.com/check/23.95.107.6>
[10] <https://www.shodan.io/host/23.95.107.6>
[11] <https://www.speedguide.net/port.php?port=5222>
[12] <https://www.speedguide.net/port.php?port=5269>

Keywords: [wordpress](/tag.html?tag=wordpress) [web](/tag.html?tag=web) [php](/tag.html?tag=php) [methods](/tag.html?tag=methods) [honeypot](/tag.html?tag=honeypot) [dshield](/tag.html?tag=dshield) [bitrix](/tag.html?tag=bitrix)

[0 comment(s)](/diary/Guest%2BDiary%2BInsights%2Bfrom%2BAugust%2BWeb%2BTraffic%2BSurge/31408/#comments)

* [previous](/diary/31406)
* [next](/diary/31414)

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
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](...