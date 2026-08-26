---
title: Obfuscating IP Addresses as Hostnames, (Tue, Aug 25th)
url: https://isc.sans.edu/diary/rss/33280
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-25
fetch_date: 2026-08-26T03:06:53.924056
---

# Obfuscating IP Addresses as Hostnames, (Tue, Aug 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Rob VandenBrink](/handler_list.html#rob-vandenbrink "Rob VandenBrink")

Threat Level: [green](/infocon.html)

* [previous](/diary/33274)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Obfuscating IP Addresses as Hostnames](/forums/diary/Obfuscating%2BIP%2BAddresses%2Bas%2BHostnames/33280/)

**Published**: 2026-08-25. **Last Updated**: 2026-08-25 15:03:33 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Obfuscating%2BIP%2BAddresses%2Bas%2BHostnames/33280/#comments)

It is pretty obvious that hostnames can replace IP addresses. Pretty much any software accepting an IP address will also accept a hostname as an argument. Last week, I wrote about [scans for the cloud metadata service](https://isc.sans.edu/diary/Simple%2BScans%2Bfor%2BCloud%2BMetadata%2BService/33260/) listening at 169.254.169.254. These scans attempted to exploit Server Side Request Forgery (SSRF) vulnerability. One way to prevent these types of exploits is to filter requests that contain the string "169.254.169.254" or to add this IP to a blocklist of URLs that should not be accessed.

But as is almost always the case, blocklists are not the solution you are looking for.

In response to last week's diary, Sean wrote that they saw attackers use hostnames instead of IP addresses. In particular:

* 169.254.169.254.nip.io
* 169-254-169-254.sslip.io
* test.169.254.169.254.nip.io (or other prefixes instead of test)
* make-1.1.1.1-rebind-169.254.169.254-rr.1u.ms

The last one, as Sean pointed out, is likely linked to the [1u.ms tool](https://github.com/neex/1u.ms). This tool allows attackers to define hostnames "on the fly". It offers numerous options. For example, you can configure the IP address to change after a certain number of lookups or after a certain time. IP addresses can use various encoding/obfuscating formats. The tool can also be configured with a custom domain, but 1u.ms is ready to go.

1u.ms maintains public logs for all requests sent to it, so you can check if it was used against one of your systems. The last 100 requests can be found at http://1u.ms/last and the

Similar hostnames can likely be configured with many dynamic hosting services. If you do retain DNS logs (you should!!), Check whether any resolution resulted in IPs such as 169.254.169.254.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [metadata 169254169254](/tag.html?tag=metadata 169254169254)

[0 comment(s)](/diary/Obfuscating%2BIP%2BAddresses%2Bas%2BHostnames/33280/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33274)

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