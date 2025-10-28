---
title: Bytes over DNS, (Mon, Oct 27th)
url: https://isc.sans.edu/diary/rss/32420
source: SANS Internet Storm Center, InfoCON: green
date: 2025-10-27
fetch_date: 2025-10-28T03:08:21.494199
---

# Bytes over DNS, (Mon, Oct 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/32416)
* [next](/diary/32422)

# [Bytes over DNS](/forums/diary/Bytes%2Bover%2BDNS/32420/)

**Published**: 2025-10-27. **Last Updated**: 2025-10-27 09:10:01 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Bytes%2Bover%2BDNS/32420/#comments)

I was intrigued when Johannes talked about malware that uses BASE64 over DNS to communicate. Take a DNS request like this: label1.label2.tld. Labels in a request like this can only be composed with letters (not case-sensitive), digits and a hyphen character (-). While BASE64 is encoded with letters (uppercase and lowercase), digits and special characters + and /. And also a special padding character: =.

So when sticking to the standards, it is not possible to use BASE64 in a label. What happens when we don't stick to the standards?

So I wanted to know what byte values I could transmit over DNS when using third-party DNS infrastructure over which I have no control, like my ISP, CloudFlare, Google, ...

Here is a schema:

![](https://isc.sans.edu/diaryimages/images/20251025-140518.png)

In red, you have the machines I have control over: my workstation on the left, where I do the DNS queries, and my server on the Internet on the right, where I have my DNS software running ([dnsresolver.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/dnsresolver.py)).

In blue are the servers of the DNS infrastructure I'm using, over which I have no control.

**In a first test**, I'm using the name resolution API of the OS.

![](https://isc.sans.edu/diaryimages/images/20251025-141201.png)

My queries look like this: bytes.41.A.mydomain.com. In this example, 41 is the hexadecimal value of the byte value I'm transmitting, and A is the ASCII representation of the byte value I'm transmitting. On the other end, I have my dnsresolver.py software running with a custom function, that checks the incoming request to see if the hexadecimal value still corresponds to the ASCII value. It logs the result in a log file, and replies with 127.0.0.1 if it matches, and with NXDOMAIN if it doesn't.

Then on my workstation, I do these queries for all byte values between 0x00 and 0xFF.

On Windows using CloudFlare (1.1.1.1), I can only reliably transmit letters (uppercase and lowercase), digits, a hyphen (-) and an underscore (\_).

On Windows using Google (8.8.8.8), I can only reliably digits, a hyphen (-) and an underscore (\_). Letters can not be reliably transmitted, because of an anti DNS-spoofing measure: Google will change the case of letters (for example, google.com becomes GoOgLe.com). You don't see that as an enduser, but my DNS software sees it.

So in theory, I could use BASE64 in a DNS C2 channel, provided CloudFlare is used and provided I replace + and / with - and \_. And provided I don't use a padding character.

On Ubuntu, I can transmit reliably all ASCII characters (0x00 - 0x7F), except 0x00 and 0x2E (.). That's for CloudFlare. Google is the same, except for letters.

So I could do even better than BASE64, since I have 126 byte values at my disposition.

All byte values between 0x80 and 0xFF fail, most of them because they get converted to punicode.

**Second test** is to use a DNS library in stead of the OS API (I use Python module [dnspython/dns.resolver](https://pypi.org/project/dnspython/)).

![](https://isc.sans.edu/diaryimages/images/20251025-142742.png)

On Windows and Ubuntu, I can transmit reliably all ASCII characters (0x00 - 0x7F), except 0x2E (.). That's for CloudFlare. Google is the same, except for letters.

The reason that the library cannot transmit a dot (.), so that's request bytes.2E...mydomain.com., is that in a DNS packet, a query is a encoded as a sequence of run-length encoded labels, and dots are not represented.

So mydomain.com. becomes:

![](https://isc.sans.edu/diaryimages/images/20251025-143343.png)

0x08 is the length of label mydomain, 0x03 is the length of label com, and 0x00 is the length of the root label (the . at the end of mydomain.com.).

All byte values between 0x80 and 0xFF fail, most of them because they get converted to PUNICODE.

**And as a third test**, I'm going to craft and transmit my own DNS packets, so that I have full control:

![](https://isc.sans.edu/diaryimages/images/20251025-143917.png)

On Windows and Ubuntu, I can transmit reliably all ASCII characters (0x00 - 0x7F), also 0x2E (.). That's for CloudFlare. Google is the same, except for the letters.

And I can reliably transmit all values between 0x80 and 0xFF, but my dnsresolver.py tool that uses the dnslib Python library, can not parse them. So I would need to find a DNS packet parser that handles this, or write my own. I verified that values between 0x80 and 0xFF arrive reliably, but doing a packet capture on my server.

**Conclusion**

All byte values (even 0x2E .) can be reliably transmitted over the CloudFlare DNS infrastructure, provided one crafts and parses their own DNS packets.

On Google, all values are accepted too, but the case of letters can change because of Google's anti-spoofing measure.

If you want to perform your own DNS tests, you can find more details on my blog post "[Bytes over DNS Tools](https://blog.didierstevens.com/2025/10/27/bytes-over-dns-tools/)".

Next on my todo list is to perform research to detect abnormal DNS traffic like this.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Bytes%2Bover%2BDNS/32420/#comments)

* [previous](/diary/32416)
* [next](/diary/32422)

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