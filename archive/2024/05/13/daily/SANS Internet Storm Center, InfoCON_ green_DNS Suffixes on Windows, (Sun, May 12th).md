---
title: DNS Suffixes on Windows, (Sun, May 12th)
url: https://isc.sans.edu/diary/rss/30912
source: SANS Internet Storm Center, InfoCON: green
date: 2024-05-13
fetch_date: 2025-10-06T17:15:43.551357
---

# DNS Suffixes on Windows, (Sun, May 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30908)
* [next](/diary/30916)

# [DNS Suffixes on Windows](/forums/diary/DNS%2BSuffixes%2Bon%2BWindows/30912/)

**Published**: 2024-05-12. **Last Updated**: 2024-05-12 13:02:10 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/DNS%2BSuffixes%2Bon%2BWindows/30912/#comments)

I was asked if I could provide mote details on the following sentence from my diary entry "[nslookup's Debug Options](https://isc.sans.edu/diary/nslookups%2BDebug%2BOptions/30894)":

*(notice that in my nslookup query, I terminated the FQDN with a dot: "example.com.", I do that to prevent Windows from adding suffixes)*

A DNS suffix is a configuration of the Windows DNS client (locally, via DHCP, ...) to have it append suffixes when doing domain lookups.

For example, if a DNS suffix local is configured, then Windows' DNS client will not only do a DNS lookup for example.com, but also for example.com.local.

As an example, let me configure mylocalnetwork as a suffix on a Windows machine:

![](https://isc.sans.edu/diaryimages/images/20240512-133158.png)

![](https://isc.sans.edu/diaryimages/images/20240512-133227.png)

![](https://isc.sans.edu/diaryimages/images/20240512-133311.png)

![](https://isc.sans.edu/diaryimages/images/20240512-133354.png)

With DNS suffix mylocalnetwork configured, nslookup will use this suffix. For example, when I perform a lookup for "example.com", nslookup will also do a lookup for "example.com.mylocalnetwork".

I can show this with [nslookup's debug option](https://isc.sans.edu/diary/nslookups%2BDebug%2BOptions/30894) d2:

![](https://isc.sans.edu/diaryimages/images/20240512-134548.png)

![](https://isc.sans.edu/diaryimages/images/20240512-134614.png)

![](https://isc.sans.edu/diaryimages/images/20240512-134734.png)

![](https://isc.sans.edu/diaryimages/images/20240512-134819.png)

![](https://isc.sans.edu/diaryimages/images/20240512-134916.png)

You can see in these screenshots DNS type A and AAAA resolutions for example.com.mylocalnetwork and example.com.

One of the ideas behind DNS suffixes, is to reduce typing. If you have a NAS, for example, named mynas, you can just access it with https://mynas/login. No need to type the fully qualified domain name (FQDN) https://mynas.mylocalnetwork/login.

Notice that the suffix also applies for AAAA queries, while in the screenshots above I only configured it for IPv4. That's because the DNS suffix setting applies both to IPv4 and IPv6:

![](https://isc.sans.edu/diaryimages/images/20240512-135003.png)

Before I show the results with "example.com." (notice the dot character at the end), let me show how I can summarize the lookups by grepping for "example" (findstr):

![](https://isc.sans.edu/diaryimages/images/20240512-135246.png)

If I terminate my DNS query with a dot character (.), suffixes will not be appended:

![](https://isc.sans.edu/diaryimages/images/20240512-135316.png)

Notice that there are no resolutions for mylocalnetwork in this last example. That's because the trailing dot instructs Windows' DNS client to start resolving from the [DNS root zone](https://en.wikipedia.org/wiki/DNS_root_zone).

A domain name consists of domain labels separated by dots:

![](https://isc.sans.edu/diaryimages/images/20240512-144444.png)

If you are adding a trailing dot, you are actually adding an empty domain label:

![](https://isc.sans.edu/diaryimages/images/20240512-144752.png)

The empty label represents the [DNS root zone](https://en.wikipedia.org/wiki/DNS_root_zone), and no suffixes are appended to the DNS root zone, as it is the top-level (root) DNS zone.

A small tip if you want to restrict nslookup's resolutions to A records, for example. There is an option for that.

If you use nslookup's help option /?, you will see that you can provide options, but the actual options are not listed:

![](https://isc.sans.edu/diaryimages/images/20240512-140534.png)

To see the available options, start nslookup, and then type "?" at its prompt, like this:

![](https://isc.sans.edu/diaryimages/images/20240512-140611.png)

Now you can see that option "type" allows you to specify which type of records to query. Here is an example for A records:

![](https://isc.sans.edu/diaryimages/images/20240512-140651.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/DNS%2BSuffixes%2Bon%2BWindows/30912/#comments)

* [previous](/diary/30908)
* [next](/diary/30916)

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