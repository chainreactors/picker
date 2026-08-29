---
title: Some Malicious PE Stats, (Thu, Aug 27th)
url: https://isc.sans.edu/diary/rss/33292
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-28
fetch_date: 2026-08-29T08:32:42.529854
---

# Some Malicious PE Stats, (Thu, Aug 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33290)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [Some Malicious PE Stats](/forums/diary/Some%2BMalicious%2BPE%2BStats/33292/)

**Published**: 2026-08-27. **Last Updated**: 2026-08-28 07:04:13 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Some%2BMalicious%2BPE%2BStats/33292/#comments)

During my last FOR610 session, a student asked me if I had some statistics in mind about the compilers used to generate malicious PE files? A couple of months ago, I shared some stats about the trend in 64bits VS. 32bits malware[[1](https://isc.sans.edu/diary/2026%2B64Bits%2BMalware%2BTrend/32718)]. Can we go a bit further? I (vibe-)coded a Python script based on the pefile library[[2](https://github.com/erocarrera/pefile)] to extract some info from the PE headers. Indeed, the PE file format contains a lot of metadata! They can be accessed using a lot of tools, like Detect It Easy:

![](https://isc.sans.edu/diaryimages/images/isc-20260828-1.png)

Note: When you assess a PE file, a gold rule to follow is to never trust what you see because these metadata can be tempered!

I tried to detect the compiler using three techniques:

* The "Rich Header" is a block of data containing useful information (but undocumented by Microsoft). It's an XOR-obfuscated block that the Microsoft linker embeds between the DOS stub and the NT headers of PE files built with the MSVC toolchain. It records the @comp.id (product id + build number) and use-count of every object file that went into the link, which lets you fingerprint the exact compiler/linker/assembler build used, as well as, even the count of source files. pefile is able to handle these data smoothly.
* The .NET CLR header (IMAGE\_COR20\_HEADER) + CLR metadata root, for managed (C#/VB.NET/F#) binaries. This gives the CLR runtime version and the embedded metadata version string (e.g. "v4.0.30319"). This is manually parsed per the public ECMA-335 spec (there's no MSVC Rich Header in managed-only PEs).
* A light heuristic string scan for common non-Microsoft compiler signatures (GCC/MinGW, Clang/LLVM, Delphi/Borland, Free Pascal, Go, Rust), since none of those toolchains write a Rich Header. Just because strings are always easy to process and may reveal juicy information!

As said above, there is no official Microsoft documentation for the Rich Header, and no single authoritative mapping of every product-id -> tool/version exists. But they are community references that helps! The well-known "comp\_id.txt" is one of them and constantly updated[[3](https://github.com/dishather/richprint/blob/master/comp_id.txt)].

Now that we have a tool, where can we find fresh meat? Malware Bazaar is a good candidate because it is pretty popular and get new samples daily. They allow (but don't abuse) to download their data set for free! The first step was to download all the archive they offer[[4](https://bazaar.abuse.ch/export/)]. I downloaded a total of 1.3 TB of ZIP archives, one archive per day from 2020-02-24 to 2026-07-08.

Because PE files can be embedded into other files and to avoid using to much storage, I rewrote the script:

* To unzip files in memory and avoid touching the disk
* To perform a recursive scan up to 3 levels

Here are the stats I gathered after “a few days” of processing!

High level stats

|  |  |
| --- | --- |
| Total scanned files | 23.501.548 |
| Not PE | 22.580.068 |
| Valid PE | 690.689 |
| Encrypted or unreadable | 227.755 |
| Invalid PE | 1.508 |
| ZIP Bomb | 951 |
| Invalid ZIP | 519 |
| Error | 36 |
| Skipped Nested ZIP (> 3 levels) | 19 |
| File Too Large | 3 |

About the architecture:

|  |  |
| --- | --- |
| 32 Bits (or other architecture) | 565.179 |
| 64 Bits | 125.510 |

Interesting, this confirms my previous research: 32 bits PE file remain popular.

Rich Header:

|  |  |
| --- | --- |
| Rich Header Present | 371.103 |
| No Rich Header (Maybe stripping, a non-MSVC toolchain, tempeing,...) | 319.586 |

Top-10 linker versions:

|  |  |
| --- | --- |
| linker 48.0 | 102.307 |
| linker 6.0 | 91.788 |
| linker 9.0 | 62.070 |
| linker 8.0 | 47.829 |
| linker 2.25 | 36.673 |
| linker 10.0 | 36.549 |
| linker 14.0 | 29.786 |
| linker 11.0 | 25.784 |
| linker 14.29 | 24.655 |
| linker 80.0 | 22.691 |

Top MSVC Rich Header compiler builds (useful for clustering samples built in the same environment/campaign):

|  |  |
| --- | --- |
| build 26213 | 19.603 |
| build 24213 | 15.389 |
| build 30034 | 14.325 |
| build 26706 | 7.755 |
| build 24215 | 5.253 |
| build 32533 | 5.033 |
| build 33030 | 4.442 |
| build 31823 | 3.738 |
| build 25834 | 3.530 |
| build 27412 | 3.294 |

Finally, and the most interesting status, what tools are used by attackers?

|  |  |  |
| --- | --- | --- |
| Unidentified (no Rich Header, no signature match) | 272.439 | 39.4% |
| Microsoft toolchain (Rich Header present, no recognized C/C++ entry) | 216173 | 31.3% |
| Borland C++/Delphi | 20172 | 2.9% |
| Microsoft Visual C/C++ (Rich Header, compiler build 26213) | 19603 | 2.8% |
| GCC / MinGW | 13804 | 2.0% |
| Go | 6254 | 0.9% |
| Embarcadero/Borland Delphi | 6174 | 0.9% |
| Rust | 1329 | 0.2% |
| Clang/LLVM | 91 | 0.0% |
| Free Pascal (FPC) | 1 | 0.0% |

Interesting to see that arising programming languages like Go or Rust remain exotic in the data set! I expected more popularity!

[1] [https://isc.sans.edu/diary/2026+64Bits+Malware+Trend/32718](https://isc.sans.edu/diary/2026%2B64Bits%2BMalware%2BTrend/32718)
[2] <https://github.com/erocarrera/pefile>
[3] <https://github.com/dishather/richprint/blob/master/comp_id.txt>
[4] <https://bazaar.abuse.ch/export/>

Xavier Mertens (@xme)
Senior ISC Handler | SANS Principal Instructor | Freelance Consultant
[Xameco](https://xameco.be) | [PGP Key](https://xameco.be/pgpkey.txt)

Keywords: [Linker](/tag.html?tag=Linker) [Compiler](/tag.html?tag=Compiler) [PE](/tag.html?tag=PE) [Statistics](/tag.html?tag=Statistics) [Malware](/tag.html?tag=Malware)

[0 comment(s)](/diary/Some%2BMalicious%2BPE%2BStats/33292/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33290)

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

* [Link To Us](/lin...