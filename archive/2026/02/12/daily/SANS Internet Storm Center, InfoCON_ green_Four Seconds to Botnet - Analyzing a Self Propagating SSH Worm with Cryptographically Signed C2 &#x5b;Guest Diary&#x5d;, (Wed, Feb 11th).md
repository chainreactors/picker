---
title: Four Seconds to Botnet - Analyzing a Self Propagating SSH Worm with Cryptographically Signed C2 &#x5b;Guest Diary&#x5d;, (Wed, Feb 11th)
url: https://isc.sans.edu/diary/rss/32708
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-12
fetch_date: 2026-02-13T04:18:46.093001
---

# Four Seconds to Botnet - Analyzing a Self Propagating SSH Worm with Cryptographically Signed C2 &#x5b;Guest Diary&#x5d;, (Wed, Feb 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Russ McRee](/handler_list.html#russ-mcree "Russ McRee")

Threat Level: [green](/infocon.html)

* [previous](/diary/32706)
* [next](/diary/32712)

# [Four Seconds to Botnet - Analyzing a Self Propagating SSH Worm with Cryptographically Signed C2 [Guest Diary]](/forums/diary/Four%2BSeconds%2Bto%2BBotnet%2BAnalyzing%2Ba%2BSelf%2BPropagating%2BSSH%2BWorm%2Bwith%2BCryptographically%2BSigned%2BC2%2BGuest%2BDiary/32708/)

**Published**: 2026-02-11. **Last Updated**: 2026-02-12 01:56:24 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Four%2BSeconds%2Bto%2BBotnet%2BAnalyzing%2Ba%2BSelf%2BPropagating%2BSSH%2BWorm%2Bwith%2BCryptographically%2BSigned%2BC2%2BGuest%2BDiary/32708/#comments)

[This is a Guest Diary by Johnathan Husch, an ISC intern as part of the SANS.edu [BACS](http://https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

Weak SSH passwords remain one of the most consistently exploited attack surfaces on the Internet. Even today, botnet operators continue to deploy credential stuffing malware that is capable of performing a full compromise of Linux systems in seconds.

During this internship, my DShield sensor captured a complete attack sequence involving a self-spreading SSH worm that combines:

- Credential brute forcing
- Multi-stage malware execution
- Persistent backdoor creation
- IRC-based command and control
- Digitally signed command verification
- Automated lateral movement using Zmap and sshpass

**Timeline of the Compromise**
08:24:13   Attacker connects [(83.135.10.12](https://otx.alienvault.com/indicator/ip/83.135.10.12))
08:24:14   Brute-force success (pi / raspberryraspberry993311)
08:24:15   Malware uploaded via SCP (4.7 KB bash script)
08:24:16   Malware executed and persistence established
08:24:17   Attacker disconnects; worm begins C2 check-in and scanning

![](https://isc.sans.edu/diaryimages/images/Johnathan%20Husch_Picture1.png)
Figure 1: Network diagram of observed attack

**Authentication Activity**

The attack originated from 83.135.10.12, which traces back to Versatel Deutschland, an ISP in Germany [1].
The threat actor connected using the following SSH client:
SSH-2.0-OpenSSH\_8.4p1 Raspbian-5+b1
HASSH: ae8bd7dd09970555aa4c6ed22adbbf56
The 'raspbian' strongly suggests that the attack is coming from an already compromised Raspberry Pi.

**Post Compromise Behavior**

Once the threat actor was authenticated, they immediately uploaded a small malicious bash script and executed it.
Below is the attackers post exploitation sequence:

![](https://isc.sans.edu/diaryimages/images/Johnathan%20Husch_Picture2.png)

The uploaded and executed script was a 4.7KB bash script captured by the DShield sensor. The script performs a full botnet lifecycle. The first action the script takes is establishing persistence by performing the following:

![](https://isc.sans.edu/diaryimages/images/Johnathan%20Husch_Picture3.png)

The threat actor then kills the processes for any competitors malware and alters the hosts file to add a known C2 server [2] as the loopback address

![](https://isc.sans.edu/diaryimages/images/Johnathan%20Husch_Picture4.png)

**C2 Established**

Interestingly, an embedded RSA key was active and was used to verify commands from the C2 operator. The script then joins 6 IRC networks and connects to one IRC channel: #biret

![](https://isc.sans.edu/diaryimages/images/Johnathan%20Husch_Picture5.png)

Once connected, the C2 server finishes enrollment by opening a TCP connection, registering the nickname of the device and completes registration. From here, the C2 performs life checks of the device by quite literally playing ping pong with itself. If the C2 server sends down "PING", then the compromised device must send back "PONG".

**Lateral Movement and Worm Propagation**

Once the C2 server confirms connectivity to the compromised device, we see the tools zmap and sshpass get installed. The device then conducts a zmap scan on 100,000 random IP addresses looking for a device with port 22 (SSH) open. For each vulnerable device, the worm attempts two sets of credentials:

- pi / raspberry
- pi / raspberryraspberry993311

Upon successful authentication, the whole process begins again.
While a cryptominer was not installed during this attack chain, the C2 server would most likely send down a command to install one based on the script killing processes for competing botnets and miners.

**Why Does This Attack Matter**

This attack in particular teaches defenders a few lessons:

Weak passwords can result in compromised systems. The attack was successful as a result of enabled default credentials; a lack of key based authentication and brute force protection being configured.
IoT Devices are ideal botnet targets. These devices are frequently left exposed to the internet with the default credentials still active.
Worms like this can spread both quickly and quietly. This entire attack chain took under 4 seconds and began scanning for other vulnerable devices immediately after.

**How To Combat These Attacks**

To prevent similar compromises, organizations could:

- Disable password authentication and use SSH keys only
- Remove the default pi user on raspberry pi devices
- Enable and configure fail2ban
- Implement network segmentation on IoT devices

**Conclusion**

This incident demonstrates how a raspberry pi device with no security configurations can be converted into a fully weaponized botnet zombie. It serves as a reminder that security hardening is essential, even for small Linux devices and hobbyist systems.

[1] https://otx.alienvault.com/indicator/ip/83.135.10.12
[2] https://otx.alienvault.com/indicator/hostname/bins.deutschland-zahlung.eu
[3] https://www.sans.edu/cyber-security-programs/bachelors-degree/

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [BACS](/tag.html?tag=BACS) [Botnet](/tag.html?tag=Botnet) [C2](/tag.html?tag=C2) [DShield](/tag.html?tag=DShield) [Investigation](/tag.html?tag=Investigation) [SSH Worm](/tag.html?tag=SSH Worm)

[0 comment(s)](/diary/Four%2BSeconds%2Bto%2BBotnet%2BAnalyzing%2Ba%2BSelf%2BPropagating%2BSSH%2BWorm%2Bwith%2BCryptographically%2BSigned%2BC2%2BGuest%2BDiary/32708/#comments)

* [previous](/diary/32706)
* [next](/diary/32712)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons...