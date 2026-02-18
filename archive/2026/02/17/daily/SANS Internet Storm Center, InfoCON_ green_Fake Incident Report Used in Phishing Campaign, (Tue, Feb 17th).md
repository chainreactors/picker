---
title: Fake Incident Report Used in Phishing Campaign, (Tue, Feb 17th)
url: https://isc.sans.edu/diary/rss/32722
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-17
fetch_date: 2026-02-18T04:16:15.570294
---

# Fake Incident Report Used in Phishing Campaign, (Tue, Feb 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32718)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

# [Fake Incident Report Used in Phishing Campaign](/forums/diary/Fake%2BIncident%2BReport%2BUsed%2Bin%2BPhishing%2BCampaign/32722/)

**Published**: 2026-02-17. **Last Updated**: 2026-02-17 07:41:46 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Fake%2BIncident%2BReport%2BUsed%2Bin%2BPhishing%2BCampaign/32722/#comments)

This morning, I received an interesting phishing email. I’ve a “love & hate” relation with such emails because I always have the impression to lose time when reviewing them but sometimes it’s a win because you spot interesting “TTPs” (“tools, techniques &  procedures”). Maybe one day, I'll try to automate this process!

Today's email targets Metamask[[1](https://metamask.io)] users. It’s a popular software crypto wallet available as a browser extension and mobile app. The mail asks the victim to enable 2FA:

![](https://isc.sans.edu/diaryimages/images/isc-20260217-1.png)

The link points to an AWS server: hxxps://access-authority-2fa7abff0e[.]s3.us-east-1[.]amazonaws[.]com/index.html

But it you look carefully at the screenshots, you see that there is a file attached to the message: “Security\_Reports.pdf”. It contains a fake security incident report about an unusual login activity:

![](https://isc.sans.edu/diaryimages/images/isc-20260217-2.png)

The goal is simple: To make the victim scary and ready to “increase” his/her security by enabled 2FA.

I had a look at the PDF content. It’s not malicious. Interesting, it has been generated through ReportLab[[2](http://www.reportlab.com)], an online service that allows you to create nice PDF documents!

```

6 0 obj
<<
/Author (\(anonymous\)) /CreationDate (D:20260211234209+00'00') /Creator (\(unspecified\)) /Keywords () /ModDate (D:20260211234209+00'00') /Producer (ReportLab PDF Library - www.reportlab.com)
  /Subject (\(unspecified\)) /Title (\(anonymous\)) /Trapped /False
>>
endobj
```

They also provide a Python library to create documents:

```

pip install reportlab
```

The PDF file is the SHA256 hash 2486253ddc186e9f4a061670765ad0730c8945164a3fc83d7b22963950d6dcd1.

Besides the idea to use a fake incident report, this campaign remains at a low quality level because the "From" is not spoofed, the PDF is not "branded" with at least the victim's email. If you can automate the creation of a PDF file, why not customize it?

[1] <https://metamask.io>
???????[2] <http://www.reportlab.com>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [2FA](/tag.html?tag=2FA) [Email](/tag.html?tag=Email) [Fake](/tag.html?tag=Fake) [Incident Report](/tag.html?tag=Incident Report) [Metamask](/tag.html?tag=Metamask) [Phishing](/tag.html?tag=Phishing)

[0 comment(s)](/diary/Fake%2BIncident%2BReport%2BUsed%2Bin%2BPhishing%2BCampaign/32722/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

* [previous](/diary/32718)

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