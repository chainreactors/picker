---
title: Broken Phishing URLs, (Thu, Feb 5th)
url: https://isc.sans.edu/diary/rss/32686
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-05
fetch_date: 2026-02-06T04:10:21.329896
---

# Broken Phishing URLs, (Thu, Feb 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32682)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

# [Broken Phishing URLs](/forums/diary/Broken%2BPhishing%2BURLs/32686/)

**Published**: 2026-02-05. **Last Updated**: 2026-02-05 08:43:02 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[1 comment(s)](/diary/Broken%2BPhishing%2BURLs/32686/#comments)

For a few days, many phishing emails that landed into my mailbox contain strange URLs. They are classic emails asking you to open a document, verify your pending emails, …

![](https://isc.sans.edu/diaryimages/images/isc-20260205-1.png)

But the format of the URLs is broken! In a URL, parameters are extra pieces of information added after a question mark (?) to tell a website more details about a request; they are written as name=value pairs (for example “email=user@domain”), and multiple parameters are separated by an ampersand (&).

Here are some examples of detected URLs:

```

hxxps://cooha0720[.]7407cyan[.]workers[.]dev/?dC=handlers@isc[.]sans[.]edu&*(Df
hxxps://calcec7[.]61minimal[.]workers[.]dev/?wia=handlers@isc[.]sans[.]edu&*(chgd
hxxps://couraol-02717[.]netlify[.]app/?dP=handlers@isc[.]sans[.]edu&*(TemP
hxxps://shiny-lab-a6ef[.]tcvtxt[.]workers.dev/?kpv=handlers@isc[.]sans[.]edu&*(lIi
```

You can see that the parameters are broken… “&\*(Df” is invalid! It’s not an issue for browsers that will just ignore these malformed parameters, so the malicious website will be visited.

I did not see this for a while but it seems that the technique is back on stage. Threat actors implement this to break security controls. Many of them assume a “key=value" format. It may also break regex-based detectionn, URL normalization routines or IOC extraction pipelines…

Of course, we can track such URLs using a regex to extract the last param:

![](https://isc.sans.edu/diaryimages/images/isc-20260205-2.png)???????

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Broken](/tag.html?tag=Broken) [Parameter](/tag.html?tag=Parameter) [Phishing](/tag.html?tag=Phishing) [Regex](/tag.html?tag=Regex) [URL](/tag.html?tag=URL)

[1 comment(s)](/diary/Broken%2BPhishing%2BURLs/32686/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

* [previous](/diary/32682)

### Comments

Hi Xavier,

Just a note that the Keybase link in your signature is showing an error
SELF-SIGNED PUBLIC KEY NOT FOUND

#### AnalystChris

#### Feb 5th 2026 13 hours ago

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