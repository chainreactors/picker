---
title: DNS Reflection Update and Odd Corrupted DNS Requests, (Wed, Sep 25th)
url: https://isc.sans.edu/diary/rss/31296
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-26
fetch_date: 2025-10-06T18:30:35.974714
---

# DNS Reflection Update and Odd Corrupted DNS Requests, (Wed, Sep 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31292)
* [next](/diary/31298)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [DNS Reflection Update and Odd Corrupted DNS Requests](/forums/diary/DNS%2BReflection%2BUpdate%2Band%2BOdd%2BCorrupted%2BDNS%2BRequests/31296/)

**Published**: 2024-09-25. **Last Updated**: 2024-09-25 16:33:15 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/DNS%2BReflection%2BUpdate%2Band%2BOdd%2BCorrupted%2BDNS%2BRequests/31296/#comments)

Occasionally, I tend to check in on what reflective DNS denial of service attacks are doing. We usually see steady levels of attacks. Usually, they attempt to use spoofed requests for ANY records to achieve the highest possible amplification. Currently, I am seeing these two records used (among others):

### ANY nlrb.gov

The response for this query may be up to 5,826 bytes in size. With a query payload size of 37 bytes, this leads to a rather impressive implication. The original name server appears to do the right thing, and it ignores EDNS0, but that, of course, doesn't help with open resolvers.

### ANY ncca.mil

This domain is a bit odd. I only receive empty responses for ANY, NS, or other queries I tried. Maybe this domain was fixed after it got abused for DDoS attacks.

### ANY fnop.net

The response for this domain is also truncated. Likely also fixed.

### "Fixing" Amplification via ANY records

There are a few other defensive techniques that show up more often. Google's domain name service returns a "Not Implemented" error for ANY queries:

> % dig ANY dshield.org
>
> ; <<>> DiG 9.10.6 <<>> ANY dshield.org
> ;; global options: +cmd
> ;; Got answer:
> ;; ->>HEADER<<- opcode: QUERY, status: NOTIMP, id: 27119
> ;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

A few years ago, RFC 8492 was published which spe,cifically allows truncating ANY responses. I see more and more domains returning the "HINFO" record "RFC8492" instead of the full ANY response.

### Corrupt ANY Requests

But, while looking into the DNS responses, I also saw some odd malformed queries.

![screenshot of corrupt  ANY request from Arkime](https://isc.sans.edu/diaryimages/images/Screenshot%202024-09-25%20at%2011_26_43%E2%80%AFAM.png)

These are odd and somewhat interesting to a packet-focused person:

![](https://isc.sans.edu/diaryimages/images/Screenshot%202024-09-25%20at%2011_53_59%E2%80%AFAM.png)

(or as text:

`09:37:49.571420 IP 45.148.10.248.18177 > 70.91.145.9.53: 17767+ [1au] ANY? o^Cco. (33)
    0x0000:  4500 003d 762e 4000 f211 0291 2d94 0af8  [[email protected]](/cdn-cgi/l/email-protection)...
    0x0010:  465b 9109 4701 0035 0029 0000 4567 0100  F[..G..5.)..Eg..
    0x0020:  0001 0000 0000 0001 046f 0363 6f00 00ff  .........o.co...
    0x0030:  0001 0000 29ff ff00 0000 0000 00         ....)........`

I highlighted the IP header in yellow and underlined it with a dashed line. The UDP header is underlined using dots and highlighted in green. In red and enclosed in a box, you will see the hostname.

A couple of observations to start about the IP and UDP headers:

1. The TTL is large (0xf2, or 242), exceeding more normal starting TTLs of 128 and 64.
2. The UDP checksum is 0, which is valid for IPv4 and just indicates not to verify the UDP checksum

But the real interesting part is the hostname. DNS encodes hostnames in a zero terminated length-value format. Each label is preceded by a one byte length field. For example, "isc.sans.edu" would be encoded as "03"isc"04"sans"03"edu"00".

The sequence above,

> `04 6F 03 63 6F 00`

implies a single label with a length of 4 bytes. But one byte of the label is "03", which is not a printable ASCII character and not a valid byte value for a hostname. It is more likely that the author of this denial of service tool "messed up" and meant to say:

> `01 6F 02 63 6F 00`

Which would be a valid domain, "o.co", and it could work to amplify queries. The ANY record for the domain is short but contains invalid data:

> `;; QUESTION SECTION:
> ;o.co.                IN    ANY`
>
> `;; ANSWER SECTION:
> o.co.            900    IN    NSEC    \000.o.co. A NS SOA MX TXT RRSIG NSEC DNSKEY`

The hostname in the NSEC record starts with a NULL byte! No idea what this is about. Let me know if you can figure it all out :)

One more reason to love DNS. There is always a surprise waiting for you.

If you are interested in a video walkthrough, see this YouTube recording:

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [amplification](/tag.html?tag=amplification) [corrupt dns](/tag.html?tag=corrupt dns) [ddos](/tag.html?tag=ddos) [dns](/tag.html?tag=dns)

[1 comment(s)](/diary/DNS%2BReflection%2BUpdate%2Band%2BOdd%2BCorrupted%2BDNS%2BRequests/31296/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31292)
* [next](/diary/31298)

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