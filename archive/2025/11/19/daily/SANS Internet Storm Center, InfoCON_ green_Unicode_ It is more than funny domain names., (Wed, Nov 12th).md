---
title: Unicode: It is more than funny domain names., (Wed, Nov 12th)
url: https://isc.sans.edu/diary/rss/32472
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-19
fetch_date: 2025-11-20T03:10:13.586188
---

# Unicode: It is more than funny domain names., (Wed, Nov 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32468)
* [next](/diary/32474)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Unicode: It is more than funny domain names.](/forums/diary/Unicode%2BIt%2Bis%2Bmore%2Bthan%2Bfunny%2Bdomain%2Bnames/32472/)

**Published**: 2025-11-12. **Last Updated**: 2025-11-19 15:59:55 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Unicode%2BIt%2Bis%2Bmore%2Bthan%2Bfunny%2Bdomain%2Bnames/32472/#comments)

When people discuss the security implications of Unicode, International Domain Names (IDNs) are often highlighted as a risk. However, while visible and often talked about, IDNs are probably not what you should really worry about when it comes to Unicode. There are several issues that impact application security beyond confusing domain names.

At first sight, Unicode is a standard that assigns numbers to characters [1]. It extends the ASCII standard, which only allowed for 127 different characters, to an essentially unlimited range of characters. With Unicode, we also have various encoding schemes, such as UTF-8 and UTF-16, that regulate how the respective code is expressed as a multi-byte value.

Unicode version 17.0 defines 159,801 different characters. This includes not only characters for various languages but also emojis and math symbols.

Here are some of the issues that are often overlooked:

### Confusables

When discussing domain names, one issue that arises is the use of characters that are easily confused. The Unicode project has a tool to identify them [2]. But this issue goes beyond domain names. If you allow the full Unicode character set for usernames, users may be able to impersonate other users on your platform. This has frequently happened on X [3]. However, other platforms, such as internal messaging systems, could also be abused in similar ways.

### Normalization and Best Fit Mapping

These techniques aim to address the issue that some systems are unable to represent the entire Unicode character range, but offer similar characters that can be used to represent these "missing" characters. The "confusable" tool mentioned above is also helpful to identify them. In its worst form, this could convert an otherwise harmless character, like a "FULLWIDTH GRAVE ACCENT", into a single quote, bypassing filters to prevent injection vulnerabilities. The key defense is to avoid any conversion after a string has passed input validation. However, unintentional conversion can happen on some platforms as data is inserted into databases.

### Variant Selectors

"Variant Selectors" are non-printable ("invisible") Unicode code points that are used to specify an alternate representation of a given character. They may be used by first specifying a "normal" character, followed by a variant selector, and then an alternative character, such as an emoji. There are sixteen possible variant selectors. Selector-16 (#FE0F) would be used to define an emoji representation for a given character. Variant selectors were recently abused in the "Glass Worm" attack against VS Code extensions. In this case, variant selectors were used because they are not visible; they were used solely to encode obfuscated code snippets. The "Glass Worm" used sequences of variant selectors without following them up with an alternative glyph, which is not standard-compliant. Usually, each variant selector should be followed by a glyph.

### Text Direction

Most languages are written/read left to right, and this is the default in most operating systems and editors. However, some languages use right-to-left. Unicode defines a "right-to-left (0x200F)" and "left-to-right (0x200E)" mark to indicate the direction. The direction may be changed at any point in the document. There are a few other Unicode code points that allow swapping the direction text is rendered (0x202A-E). Different text directions can be abused to make code reviews more difficult. A human reviewer will typically not see the change in direction, while a compiler or interpreter will, and as a result the code execution is different from what the human reviewer observed. There is a nice demo of this issue at trojansource.code [5]

[1] https://unicode.org/
[2] https://util.unicode.org/UnicodeJsps/confusables.jsp
[3] https://isc.sans.edu/diary/28440
[4] https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace
[5] https://trojansource.codes/

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [unicode](/tag.html?tag=unicode)

[0 comment(s)](/diary/Unicode%2BIt%2Bis%2Bmore%2Bthan%2Bfunny%2Bdomain%2Bnames/32472/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32468)
* [next](/diary/32474)

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