---
title: Nation-State Attack or Compromised Government&#x3f; &#x5b;Guest Diary&#x5d;, (Thu, Dec 4th)
url: https://isc.sans.edu/diary/rss/32536
source: SANS Internet Storm Center, InfoCON: green
date: 2025-12-04
fetch_date: 2025-12-05T03:18:39.457104
---

# Nation-State Attack or Compromised Government&#x3f; &#x5b;Guest Diary&#x5d;, (Thu, Dec 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32532)

# [Nation-State Attack or Compromised Government? [Guest Diary]](/forums/diary/NationState%2BAttack%2Bor%2BCompromised%2BGovernment%2BGuest%2BDiary/32536/)

**Published**: 2025-12-04. **Last Updated**: 2025-12-04 02:34:40 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/NationState%2BAttack%2Bor%2BCompromised%2BGovernment%2BGuest%2BDiary/32536/#comments)

[This is a Guest Diary by Jackie Nguyen, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

The ISC internship didn't just teach me about security, it changed how I thought about threats entirely. There's something intriguing about watching live attacks materialize on your DShield Honeypot, knowing that somewhere across the world, an attacker just made a move. And the feedback loop of writing detailed attack observations, then having experienced analysts critique and refine your analysis? That's where real learning happens. One attack observation in particular stands out as a perfect example of what makes this internship so powerful. Let me show you what I discovered!

**The Beginning…**

On November 10, 2025, my honeypot captured very interesting activity that really demonstrates how evolved modern threat actors are getting. What initially appeared to be a simple, but successful SSH brute force attempt quickly revealed itself as something far more concerning, a deployment of an advanced trojan designed for long-term persistence and evasion.

**What happened?**

Suspicious activity was detected when the IP address 103[.]148[.]195[.]161 successfully SSH’d into my honeypot using the credentials username “root” and password “linux”. The bad actor maintained access to the honeypot for 1 minute and 45 seconds but ultimately ran no commands. Instead, the attacker uploaded a single file, a trojan binary named “sshd” designed to evade security detections by pretending to be the OpenSSH daemon. It was an Executable and Linkable Format (ELF) binary (7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d) that was classified as malicious by VirusTotal and Hybrid-Analysis.

We won’t be able to see what the Trojan did on my honeypot at this time, however, I found the hash on Hybrid-Analysis and got a good idea of what the trojan does.

![](https://isc.sans.edu/diaryimages/images/Jackie_Nguyen_pic1.png)

A screenshot of the cowrie output using Jesse La Grew’s cowrieprocessor [[4](http://https://github.com/jslagrew/cowrieprocessor)]

**Trojan File Analysis**

![](https://isc.sans.edu/diaryimages/images/Jackie_Nguyen_pic2.png)

**MITRE ATT&CK MAPPING**

•    T1078 - Valid Accounts
•    T1110.001 - Brute Force
•    T1204.002 - User Execution
•    T1036.005 - Masquerading
•    T1554 - Compromise Client Software Binary
•    T1548.001 - Abuse Elevation Control Mechanism
•    T1027 - Obfuscated Files or Information
•    T1497 - Virtualization/Sandbox Evasion
•    T1480 - Execution Guardrails
•    T1003.008 - OS Credential Dumping

**Prevent Similar Attacks**

1.    Disable Password Authentication and utilize SSH keys instead
2.    IP Allowlisting
3.    IDS/IPS/EDR
4.    Threat Hunting
5.    MFA

**What does this show?**

This really shows how much effort sophisticated attackers would put in for long-term persistence and advanced evasion. Attacks from a government IP address doesn’t always mean it’s the government; it more than likely would mean that they were compromised. If you think about it logically, why would a nation-state threat actor use their actual government IP address to execute attacks?

**Importance?**

It’s important when working on a high performing security team to not attribute attacks to the wrong threat actor. Politically, this may cause problems, especially if the company you’re working for has a large media presence. Problems including wrongful retaliation and political tension could arise from making this mistake.

This attack also shows how threat actors use legitimate processes to blend in with normal ones. We must remember that the goal of this attacker is most likely long-term so they will do everything they can to evade your defenses.

**Actionable Intelligence for Defenders**

Threat hunting is a critical part of any security program and having concrete Indicators of Compromise (IOCs) like file hashes, malicious IP addresses, and more would give teams actionable intelligence to use immediately. This observation also helps defenders understand what to look for. Brief sessions without commands can be just as dangerous as those with suspicious activity.

**Key Takeaways**

This attack really shows how threat actors are getting more sophisticated. By uploading a legitimate looking trojan instead of running commands, the attacker could have avoided the typical red flags most monitoring tools look for. The use of a government IP address also teaches us an important lesson not to immediately jump to conclusions solely based on IP block owner since it might have been compromised. For analysts out there, what seems to be a quiet session can sometimes be the most dangerous.

[1] https://www.virustotal.com/gui/file/7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d/detection
[2 ]https://www.abuseipdb.com/whois/103.148.195.161
[3] https://hybridanalysis.com/sample/7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d/6542c8b6abeb51c5ee0bbf2a
[4] https://github.com/jslagrew/cowrieprocessor
[5] https://www.sans.edu/cyber-security-programs/bachelors-degree/

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [BACS](/tag.html?tag=BACS) [DShield](/tag.html?tag=DShield) [Investigation](/tag.html?tag=Investigation)

[0 comment(s)](/diary/NationState%2BAttack%2Bor%2BCompromised%2BGovernment%2BGuest%2BDiary/32536/#comments)

* [previous](/diary/32532)

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

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)