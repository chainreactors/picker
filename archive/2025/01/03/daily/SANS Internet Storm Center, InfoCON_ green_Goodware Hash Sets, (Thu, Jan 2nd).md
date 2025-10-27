---
title: Goodware Hash Sets, (Thu, Jan 2nd)
url: https://isc.sans.edu/diary/rss/31556
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-03
fetch_date: 2025-10-06T20:11:52.751534
---

# Goodware Hash Sets, (Thu, Jan 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31554)
* [next](/diary/31560)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Goodware Hash Sets](/forums/diary/Goodware%2BHash%2BSets/31556/)

**Published**: 2025-01-02. **Last Updated**: 2025-01-02 15:21:40 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[1 comment(s)](/diary/Goodware%2BHash%2BSets/31556/#comments)

In the cybersecurity landscape, we all need hashes! A hash is the result of applying a special mathematical function (a “hash function”) that transforms an input (such as a file or a piece of text) into a fixed-size string or number. This output, often called a “hash value,” “digest,” or “checksum,” uniquely represents the original data. In the context of this diary, hashes are commonly used for data integrity checks. There are plenty of them (MD5, SHA-1, SHA-2, SHA-256, …), SHA256 being the most popular for a while because older like MD5 are considered as broken because researchers have demonstrated practical collision attacks.

Hashes are a nice way to identify malware samples, payload, or any type of suspicious files (I usually share the hash of the malware analyzed in my diaries). In your threat-hunting process, you can search for interesting files across your infrastructure via sets of malware hashes. Some of them are freely available like on Malware Bazaar[[1](https://bazaar.abuse.ch/export/)].

But, other sets of hashes are also interesting when they contain hashes for safe files. The approach is the same: Instead of searching for malicious files, you verify that files on your hosts are good.

Exacorn has released an interesting ZIP archive[[2](https://www.hexacorn.com/blog/2024/12/31/clean-hash-set-12m-rows/)] with “good ware” (as opposed to “malware”). The file (2GB) provides 12M hashes and filenames:

![](https://isc.sans.edu/diaryimages/images/isc-20250102-1.png)

Pay attention that some files might be flagged by some antivirus solutions. For example, I searched for "putty.exe" in the file. One of the returned hashes is: 6CDBE5323E1DEC7102D86C60458D6C7465807E80516D63F2EE509625C1DF2416[[3](https://www.virustotal.com/gui/file/6cdbe5323e1dec7102d86c60458d6c7465807e80516d63f2ee509625c1df2416)].

It’s a perfect opportunity to remind you that other projects exist. The ones that I use regularly:

* The National Software Reference Library (NSRL) project[[4](https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl/about-nsrl)]
* The CIRCL.lu Hash Lookup API[[5](https://www.circl.lu/services/hashlookup/)]
* Hashsets.com [[6](https://www.hashsets.com)] (not 100% free)

I like the second one because it includes the NSRL lists and can be used in an automated way.

We love hashes!

[1] <https://bazaar.abuse.ch/export/>
[2] <https://www.hexacorn.com/blog/2024/12/31/clean-hash-set-12m-rows/>
[3] <https://www.virustotal.com/gui/file/6cdbe5323e1dec7102d86c60458d6c7465807e80516d63f2ee509625c1df2416>
[4] <https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl/about-nsrl>
[5] <https://www.circl.lu/services/hashlookup/>
[6] <https://www.hashsets.com>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Hash](/tag.html?tag=Hash) [Hashset](/tag.html?tag=Hashset) [Hash Set](/tag.html?tag=Hash Set) [Goodware](/tag.html?tag=Goodware) [Malware](/tag.html?tag=Malware)

[1 comment(s)](/diary/Goodware%2BHash%2BSets/31556/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31554)
* [next](/diary/31560)

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