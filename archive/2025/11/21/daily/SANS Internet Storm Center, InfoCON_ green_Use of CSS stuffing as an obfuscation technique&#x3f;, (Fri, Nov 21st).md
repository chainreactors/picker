---
title: Use of CSS stuffing as an obfuscation technique&#x3f;, (Fri, Nov 21st)
url: https://isc.sans.edu/diary/rss/32510
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-21
fetch_date: 2025-11-22T03:08:37.820304
---

# Use of CSS stuffing as an obfuscation technique&#x3f;, (Fri, Nov 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/32506)

# [Use of CSS stuffing as an obfuscation technique?](/forums/diary/Use%2Bof%2BCSS%2Bstuffing%2Bas%2Ban%2Bobfuscation%2Btechnique/32510/)

**Published**: 2025-11-21. **Last Updated**: 2025-11-21 09:48:20 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[1 comment(s)](/diary/Use%2Bof%2BCSS%2Bstuffing%2Bas%2Ban%2Bobfuscation%2Btechnique/32510/#comments)

From time to time, it can be instructive to look at generic phishing messages that are delivered to one’s inbox or that are caught by basic spam filters. Although one usually doesn’t find much of interest, sometimes these little excursions into what should be a run-of-the-mill collection of basic, commonly used phishing techniques can lead one to find something new and unusual. This was the case with one of the messages delivered to our handler inbox yesterday…

[![](https://isc.sans.edu/diaryimages/images/25-11-21-phish.png)](https://isc.sans.edu/diaryimages/images/25-11-21-phish.png)

The message in question looked quite unremarkable at first glance, as the link it contained pointed to an HTML page located in a Google Firebase Storage, which has been commonly misused by threat actors to save malicious content for many years now[[1](https://blog.knowbe4.com/phishing-campaigns-using-google-firebase-storage)].

The interesting part still wasn’t apparent when I first opened the page, since, as you can see, it appeared to be a fairly typical credential harvesting page that tried to overlay a fake login prompt over a legitimate page loaded (unsuccessfully, in the case of isc.sans.edu, due to our Content Security Policy and X-Frame-Options settings) from a domain extracted from a personalized link sent to the recipient of the original phishing message…

[![](https://isc.sans.edu/diaryimages/images/25-11-21-page1.png)](https://isc.sans.edu/diaryimages/images/25-11-21-page1.png)

What turned out to be unusual was the source code of this page. Although it was 449 KB in size, it contained only about 10 KB (or roughly 250 lines of code) that was actually used when the page was rendered. The remaining hundreds of kilobytes were made up of unused style data – most of it was renamed and/or slightly modified copy-pasted CSS code that was actually used in the page, and about a third of it consisted of a copy of bootstrap.min.css.

Since the copy-pasting of CSS code was certainly intentional, this “CSS stuffing” approach (along with the use of <html lang="zxx"> in the page header[[2](https://www.w3.org/International/questions/qa-no-language)]) seems to me to have been a fairly unusual attempt at bypassing some of the less effective security filtering mechanisms.

While the size of the file on its own would most likely not be enough to bypass any security scanner used to analyze HTTP traffic altogether, given that most of these tend to have scan limits for file sizes at least in the tens of megabytes range, the amount of benign-looking CSS code might perhaps be enough to change the statistical profile of the HTML page sufficiently to enable the file to pass through some heuristic or machine-learning based systems unnoticed.

Admittedly, this is just speculation, but it is certainly the best explanation for this strange use of CSS code I can think of…

[1] <https://blog.knowbe4.com/phishing-campaigns-using-google-firebase-storage>
[2] <https://www.w3.org/International/questions/qa-no-language>

-----------
Jan Kopriva
[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords: [CSS](/tag.html?tag=CSS) [Phishing](/tag.html?tag=Phishing)

[1 comment(s)](/diary/Use%2Bof%2BCSS%2Bstuffing%2Bas%2Ban%2Bobfuscation%2Btechnique/32510/#comments)

* [previous](/diary/32506)

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