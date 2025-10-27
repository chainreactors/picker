---
title: Spear Phishing Handlers for Username/Password, (Sat, Feb 18th)
url: https://isc.sans.edu/diary/rss/29560
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-19
fetch_date: 2025-10-04T07:31:10.910297
---

# Spear Phishing Handlers for Username/Password, (Sat, Feb 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29556)
* [next](/diary/29562)

# [Spear Phishing Handlers for Username/Password](/forums/diary/Spear%2BPhishing%2BHandlers%2Bfor%2BUsernamePassword/29560/)

**Published**: 2023-02-18. **Last Updated**: 2023-02-18 19:21:22 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Spear%2BPhishing%2BHandlers%2Bfor%2BUsernamePassword/29560/#comments)

Reviewing my ISC mail inbox, I noticed that I had been receiving multiple phishing email that were very similar. Putting my cursor over each embedded pictures, I noticed the domain involved was the same for all of them. I copied the URL and started checking around for known threat intel on ipfs[.]io against various sites and found on urlscan.io [[1](https://urlscan.io/search/#page.domain%3Aipfs.io)], there was over 10000+ samples listed.

![](https://isc.sans.edu/diaryimages/images/email_cursor_ipfs_io.PNG)

All these emails are asking the recipient to login to capture email address and password and the entries are Secured by Norton!

![](https://isc.sans.edu/diaryimages/images/Login_email1.PNG)

**First Email (Received 2 copies with the same URL)**
https://ipfs[.]io/ipfs/Qma2GtsUgbKKCxnLNjZv8euBKM1BK7Y48zX3BBjUQqpc26?filename=OWGH%20PIU1%20PJHMD%20QHGK%20UUG%20QGUP%20WPOKG.htm#[[email protected]](/cdn-cgi/l/email-protection)

![](https://isc.sans.edu/diaryimages/images/phish_email1.PNG)

**Second Email**
https://ipfs[.]io/ipfs/QmaU5FjjeFiDzWs2s6gZ5SyPqL2wvQa2652LHPb3d1U3XC?filename=QUPG%20WGWG%20WDOUH%20UDGW%20URZ%20PKDB%20UKLM.htm#[[email protected]](/cdn-cgi/l/email-protection)

![](https://isc.sans.edu/diaryimages/images/phish_email2.PNG)

**Third Email**

https://ipfs[.]io/ipfs/Qma2GtsUgbKKCxnLNjZv8euBKM1BK7Y48zX3BBjUQqpc26?filename=OWGH%20PIU1%20PJHMD%20QHGK%20UUG%20QGUP%20WPOKG.htm#[[email protected]](/cdn-cgi/l/email-protection)

![](https://isc.sans.edu/diaryimages/images/phish_email3.PNG)

**Indicator**

ipfs[.]io

**Final Word**

Last, a blog post by Lance Spitzner published on the 13 Feb 2023 about "Phishing - It's No Longer About Malware (or Even Email)" [[5](https://www.sans.org/blog/phishing-its-no-longer-about-malware-or-even-email/)] highlight some of the changes on the phishing goals and some of the common indicators worth reading including two indicators are no longer recommended: misspellings and hovering of the link "except for highly technical audiences. One problem with this method is that you have to teach people how to decode a URL, which can be a confusing, time consuming, and technical skill."[[5](https://www.sans.org/blog/phishing-its-no-longer-about-malware-or-even-email/)]

[1] https://urlscan.io/search/#page.domain%3Aipfs.io
[2] https://www.virustotal.com/gui/url/2c8a881b916d2396ff68ed18c41a6b8a13ba8e869de65d87a23b869a95fd0c63?nocache=1
[3] https://www.virustotal.com/gui/domain/ipfs.io/detection
[4] https://cybergordon.com/result.html?id=12ef23f1-a775-4619-81ec-c7aaaae7e4a4
[5] https://www.sans.org/blog/phishing-its-no-longer-about-malware-or-even-email/

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [email](/tag.html?tag=email) [infosec](/tag.html?tag=infosec) [password](/tag.html?tag=password) [phishing](/tag.html?tag=phishing)

[0 comment(s)](/diary/Spear%2BPhishing%2BHandlers%2Bfor%2BUsernamePassword/29560/#comments)

* [previous](/diary/29556)
* [next](/diary/29562)

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