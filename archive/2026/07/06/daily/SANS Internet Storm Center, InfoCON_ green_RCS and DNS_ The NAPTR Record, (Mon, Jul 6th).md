---
title: RCS and DNS: The NAPTR Record, (Mon, Jul 6th)
url: https://isc.sans.edu/diary/rss/33124
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-06
fetch_date: 2026-07-07T06:05:08.992919
---

# RCS and DNS: The NAPTR Record, (Mon, Jul 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33118)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [RCS and DNS: The NAPTR Record](/forums/diary/RCS%2Band%2BDNS%2BThe%2BNAPTR%2BRecord/33124/)

**Published**: 2026-07-06. **Last Updated**: 2026-07-06 13:35:58 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/RCS%2Band%2BDNS%2BThe%2BNAPTR%2BRecord/33124/#comments)

Over the last year, with recent updates to iOS and Android, RCS (Rich Communication Services) has become an increasingly used protocol [1]. RCS is supposed to eventually replace SMS, and in addition to richer formatting, provides added (but optional) security. RCS messages may be end-to-end encrypted and digitally signed. Unlike SMS, which was "bolted on" to existing voice-focused phone standards. The SMS standard was based on old-fashioned pagers and allowed for limited clear-text communications. RCS is built from the ground up around modern IP-based network infrastructure and behaves more like IP chat services (think iMessage, WhatsApp...). RCS defines the message format, while protocols like SIP are used to establish connections and transport messages.

"Do as you say", I do from time to time take a look at odd DNS traffic on my network. An activity I recommend when teaching SEC503. Recently, I noticed more "NAPTR" queries, a record type I had not seen before. The record type is defined in RFC 2915 [2], which was ratified in 2000. It is not a new record. But so far, at least in my network, it has not really shown up before.

The description of the record sounds rather ominous:

> "a Resource Record that included a regular expression that would be used by a client program to rewrite a string into a domain name."

Wow. Regular expressions to rewrite resource records? What could possibly go wrong? However, right now, I just want to talk about how it "goes right" and how these records are currently being used for RCS.

Below is the relevant part of the t-shark decode of a record typical for what I have seen in my network:

>     Queries
>         fp-us-verizon.rcs.telephony.goog: type NAPTR, class IN
>             Name: fp-us-verizon.rcs.telephony.goog
>             [Name Length: 32]
>             [Label Count: 4]
>             Type: NAPTR (35) (Naming Authority Pointer)
>             Class: IN (0x0001)
>     Answers
>         fp-us-verizon.rcs.telephony.goog: type NAPTR, class IN, order 100, preference 100, flags s
>             Name: fp-us-verizon.rcs.telephony.goog
>             Type: NAPTR (35) (Naming Authority Pointer)
>             Class: IN (0x0001)
>             Time to live: 295 (4 minutes, 55 seconds)
>             Data length: 61
>             Order: 100
>             Preference: 100
>             Flags Length: 1
>             Flags: s
>             Service Length: 8
>             Service: SIPS+D2T
>             Regex Length: 0
>             Regex:
>             [Replacement Length: 43]
>             Replacement: \_sips.\_tcp.fp-us-verizon.rcs.telephony.goog

This was the only applicable NAPTR record, so order and preference do not matter in this case. The "S" flag indicates that the next lookup should be a SRV record. And indeed, we do have a SRV query (see below). Only a "U" flag would result in a URI.

Remember that this record is about URIs, not IP addresses? The "Service" field indicates what service we may find at the to-be-determined URI. In this case, it is SIPS+D2T. SIPS+D2T is a transport protocol defined in the SIP standard (RFC 3263). SIPS+D2T stands for "Secure SIP Direct to TCP". So we will be using SIP over TLS with TCP as the transport protocol. The SIP standard specifically calls for NAPTR records to find SIP servers. The reason for the NAPTR record is to allow URIs to be returned, not just IP addresses/hostnames (as an SRV record would).

Lucky for us (and the DNS server), the regular expression is empty. And this appears to be normal for this use case. Instead, we just get a "SRV" record to request:

> `Queries
>         _sips._tcp.fp-us-verizon.rcs.telephony.goog: type SRV, class IN
>             Name: _sips._tcp.fp-us-verizon.rcs.telephony.goog
>             [Name Length: 43]
>             [Label Count: 6]
>             Type: SRV (33) (Server Selection)
>             Class: IN (0x0001)
>     Answers
>         _sips._tcp.fp-us-verizon.rcs.telephony.goog: type SRV, class IN, priority 20, weight 0, port 5223, target fp-us-verizon.rcs.telephony.goog
>             Service: _sips
>             Protocol: _tcp
>             Name: fp-us-verizon.rcs.telephony.goog
>             Type: SRV (33) (Server Selection)
>             Class: IN (0x0001)
>             Time to live: 300 (5 minutes)
>             Data length: 40
>             Priority: 20
>             Weight: 0
>             Port: 5223
>             Target: fp-us-verizon.rcs.telephony.goog
>         _sips._tcp.fp-us-verizon.rcs.telephony.goog: type SRV, class IN, priority 30, weight 0, port 443, target fp-us-verizon.rcs.telephony.goog
>             Service: _sips
>             Protocol: _tcp
>             Name: fp-us-verizon.rcs.telephony.goog
>             Type: SRV (33) (Server Selection)
>             Class: IN (0x0001)
>             Time to live: 300 (5 minutes)
>             Data length: 40
>             Priority: 30
>             Weight: 0
>             Port: 443
>             Target: fp-us-verizon.rcs.telephony.goog`???????

And yes, in the end, there is a "normal" A and AAAA lookup for fp-us-verizon.rcs.telephony.goog.

So far, NAPTR records do not appear to be used to their full potential. I am sure that the use of regular expressions will be of interest to bug hunters and penetration testers.

[1] https://support.google.com/messages/answer/13508703?hl=en
[2] https://www.ietf.org/rfc/rfc2915.txt

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [dns](/tag.html?tag=dns) [naptr](/tag.html?tag=naptr) [rcs](/tag.html?tag=rcs) [sip](/tag.html?tag=sip) [sms](/tag.html?tag=sms)

[0 comment(s)](/diary/RCS%2Band%2BDNS%2BThe%2BNAPTR%2BRecord/33124/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33118)

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
Developers: We have an [API](/api/) for you!   [![Creative Commons Lic...