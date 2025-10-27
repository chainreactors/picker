---
title: Phishing Again and Again, (Mon, Feb 27th)
url: https://isc.sans.edu/diary/rss/29588
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-28
fetch_date: 2025-10-04T08:15:57.531901
---

# Phishing Again and Again, (Mon, Feb 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29584)
* [next](/diary/29592)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Phishing Again and Again](/forums/diary/Phishing%2BAgain%2Band%2BAgain/29588/)

**Published**: 2023-02-27. **Last Updated**: 2023-02-27 06:51:44 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[2 comment(s)](/diary/Phishing%2BAgain%2Band%2BAgain/29588/#comments)

A quick finding while hunting last weekend! Despite many security awareness campaigns, phishing has remained a common threat. You can be targeted by a « personal » phishing attacks that tries to steal credentials to access your corporate account (like a fake VPN login page). But phishing also targets well-known brands. I found a ZIP archive containing many well-designed HTML pages that mimic many classic brands targeted by phishing campaigns.

Example:

![](https://isc.sans.edu/diaryimages/images/isc-20230227-1.png)

Here is the list of pages:

* Apple italy.html
* Apple letter (1)New.html
* BOA letter.html
* BOA scampage.html
* CVE-2018.html
* Chase Final letter.html
* Letter Best paypal!.html
* Letter Netlix [Norwegian].html
* Letter Paypal1.html
* Letter Paypal2.html
* Letter [ANything].html
* New sign on iOS and macOS.html
* Office-Letter.html
* PayPal Final letter(1).html
* PayPal best letter.html
* PayPal final letter.html
* PayPal letter.html
* Secure My Account.html
* Spotify Subscription Payment Failure.html
* TOP PADDING Trusted Sender.html
* Your iCloud storage is full.html
* [PP] Unusual activity.html
* amazon.html
* amex.html
* apple check activity.html
* apple-Confirmation.html
* apple-invoice.html
* apple-nyolong.html
* apple-nyolong2.html
* apple.html
* apple2.html
* apple3.html
* applebagus.html
* applejapan.html
* authorize payment paypal.html
* bbletter (4) (2) (2).html
* chase-Your credit card statement is ready.html
* chase.html
* chase1.html
* discover.html
* ebay.html
* gaenandewe.html
* google.html
* icloud.html
* icloud2.html
* kata limited paypal.html
* kecilpaypal.html
* new signin.html
* new.html
* paypal-limited-lang[ID].html
* paypal.html
* renyahpp.html
* revisi apple.html
* spotify failure payment.html
* spotify.html
* still-aol.html
* unusual.html
* yahoo-apple.html
* yahoo-apple2.html
* yahoojapan.html

Some pages contain a valid URL defined to receive credentials provided by victims other don't, but they are almost ready to be reused in new campaigns...

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Phishing](/tag.html?tag=Phishing)

[2 comment(s)](/diary/Phishing%2BAgain%2Band%2BAgain/29588/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29584)
* [next](/diary/29592)

### Comments

Question: Any hashes for those files?

#### scan-man

#### Feb 27th 2023 2 years ago

What scan-man said...

Also, a list of forwarding URLs would be handy.

Then we could track domain ownership and block or have the owner fix the problem.

#### [[email protected]](/cdn-cgi/l/email-protection)

#### Mar 2nd 2023 2 years ago

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