---
title: nslookup's Debug Options, (Sun, May 5th)
url: https://isc.sans.edu/diary/rss/30894
source: SANS Internet Storm Center, InfoCON: green
date: 2024-05-06
fetch_date: 2025-10-06T17:15:53.466632
---

# nslookup's Debug Options, (Sun, May 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30890)
* [next](/diary/30898)

# [nslookup's Debug Options](/forums/diary/nslookups%2BDebug%2BOptions/30894/)

**Published**: 2024-05-05. **Last Updated**: 2024-05-05 07:24:11 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[1 comment(s)](/diary/nslookups%2BDebug%2BOptions/30894/#comments)

A friend was having unexpected results with DNS queries on a Windows machine. I told him to use nslookup's debug options.

When you execute a simple DNS query like "nslookup example.com. 8.8.8.8", you get an answer like this (notice that in my nslookup query, I terminated the FQDN with a dot: "example.com.", I do that to prevent Windows from adding suffixes):

![](https://isc.sans.edu/diaryimages/images/20240505-081850.png)

You see the result of a reverse DNS lookup (8.8.8.8 is dns.google) and you get 2 IP addresses for example.com in your answer: an IPv6 address and an IPv4 address.

If my friend would have been able to run packet capture on the machine, he would have seen 3 DNS queries and answers:

![](https://isc.sans.edu/diaryimages/images/20240505-085618.png)

A PTR query to do a reverse DNS lookup for 8.8.8.8, an A query to lookup IPv4 addresses for example.com, and an AAAA query to lookup IPv6 addresses for example.com.

One can use nslookup's debug options to obtain equivalent information, without doing a packet capture.

Debug option -d displays extra information for each DNS response packet:

![](https://isc.sans.edu/diaryimages/images/20240505-082057.png)

Here is nslookup's parsed DNS response packet for the PTR query:

![](https://isc.sans.edu/diaryimages/images/20240505-082120.png)

Here is Wireshark's dissection of this packet:

![](https://isc.sans.edu/diaryimages/images/20240505-090417.png)

You can see that the debug output contains the same packet information as Wireshark's, but presented in another form.

The same applies for the A query:

![](https://isc.sans.edu/diaryimages/images/20240505-082232.png)

![](https://isc.sans.edu/diaryimages/images/20240505-091124.png)

And the AAAA query:

![](https://isc.sans.edu/diaryimages/images/20240505-082320.png)

![](https://isc.sans.edu/diaryimages/images/20240505-091411.png)

If you also want to see the DNS query packets, you can use debug option -d2:

![](https://isc.sans.edu/diaryimages/images/20240505-083426.png)

Besides the parsed DNS query, you now also see the length in bytes of each DNS packet (the UDP payload).

![](https://isc.sans.edu/diaryimages/images/20240505-091839.png)

Here is the A query:

![](https://isc.sans.edu/diaryimages/images/20240505-083507.png)

![](https://isc.sans.edu/diaryimages/images/20240505-091953.png)

And here is the AAAA query:

![](https://isc.sans.edu/diaryimages/images/20240505-083534.png)

![](https://isc.sans.edu/diaryimages/images/20240505-092011.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[1 comment(s)](/diary/nslookups%2BDebug%2BOptions/30894/#comments)

* [previous](/diary/30890)
* [next](/diary/30898)

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