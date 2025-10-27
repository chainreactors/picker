---
title: No Holiday Season for Attackers, (Tue, Dec 31st)
url: https://isc.sans.edu/diary/rss/31552
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-01
fetch_date: 2025-10-06T20:10:21.219598
---

# No Holiday Season for Attackers, (Tue, Dec 31st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31550)
* [next](/diary/31554)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [No Holiday Season for Attackers](/forums/diary/No%2BHoliday%2BSeason%2Bfor%2BAttackers/31552/)

**Published**: 2024-12-31. **Last Updated**: 2024-12-31 07:09:10 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/No%2BHoliday%2BSeason%2Bfor%2BAttackers/31552/#comments)

While most of us are preparing the switch to a new year (If it’s already the case for you: Happy New Year!), Attackers never stop and implement always new tricks to defeat our security controls. For a long time now, we have been flooded by sextortion emails. This is a kind of blackmail where someone threatens to share explicit images or videos unless the victim meets their demands. Even today, I receive regularly some of them.

Rapidly, security controls have been implemented to detect classic sentences in such emails and block them. With one condition: strings must be readable by the system in charge of detecting suspicious strings. Yesterday, I received another one that caught my eye:

![](https://isc.sans.edu/diaryimages/images/isc-20241231-1.png)

If you read carefully, some characters do not look usual. Some have another form, some have a “dot” on top of them, etc.

![](https://isc.sans.edu/diaryimages/images/isc-20241231-2.png)

The text contains Unicode characters that look like normal letters (especially when displayed with small fonts on a big screen):

![](https://isc.sans.edu/diaryimages/images/isc-20241231-3.png)

It looks so dumb but if your security controls can't handle Unicode (and a lot of them don't), this will break classic filters. One way to access the normal text could be to make the security control decode or read it. I did a quick test with a Python script that performs OCR ("Optical Character Recognition") on the screenshot of the email:

```

remnux@remnux:/MalwareZoo/20241231$ cat ocr-test.py
import sys
import pytesseract
from PIL import Image

image = Image.open(‘email.png’)
extracted_text = pytesseract.image_to_string(image)
with open(‘strings.txt', 'w') as file:
   file.write(extracted_text)

remnux@remnux:/MalwareZoo/20241231$ python ocr-test.py
remnux@remnux:/MalwareZoo/20241231$ head strings.txt
Hello dear,
There is no reason to relax at all but you don’t need to panic and have to read my message carefully.
It is really important, moreover, it’s crucial for you.

Joking aside, I mean it. you don’t know who I am but I am more than familiar with you.
Probably, now the only question that torments your mind is how, am I correct?
well, your internet behavior was very indiscreet and I’m pretty sure, you know it well. So do I.

you were browsing embarrassing videos, clicking unsafe links and visiting websites that no ordinary man would visit.
I secretly embedded malware into an adult site, and you unknowingly wandered right into it. Just like a blind kitten,
```

Now, security controls will probably trigger some detection rules on the decoded text. However, OCR is not a perfect tool: It may misinterpret some characters and it consumes a lot of CPU. This was just a quick test.

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Spam](/tag.html?tag=Spam) [Sextorsion](/tag.html?tag=Sextorsion) [Unicode](/tag.html?tag=Unicode) [OCR](/tag.html?tag=OCR) [Python](/tag.html?tag=Python)

[0 comment(s)](/diary/No%2BHoliday%2BSeason%2Bfor%2BAttackers/31552/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31550)
* [next](/diary/31554)

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