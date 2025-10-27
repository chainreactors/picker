---
title: IPFS phishing and the need for correctly set HTTP security headers, (Wed, Mar 15th)
url: https://isc.sans.edu/diary/rss/29638
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-16
fetch_date: 2025-10-04T09:46:03.856287
---

# IPFS phishing and the need for correctly set HTTP security headers, (Wed, Mar 15th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29634)
* [next](/diary/29642)

# [IPFS phishing and the need for correctly set HTTP security headers](/forums/diary/IPFS%2Bphishing%2Band%2Bthe%2Bneed%2Bfor%2Bcorrectly%2Bset%2BHTTP%2Bsecurity%2Bheaders/29638/)

**Published**: 2023-03-15. **Last Updated**: 2023-03-15 11:22:07 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/IPFS%2Bphishing%2Band%2Bthe%2Bneed%2Bfor%2Bcorrectly%2Bset%2BHTTP%2Bsecurity%2Bheaders/29638/#comments)

In the last couple of weeks, I’ve noticed a small spike in the number of phishing messages that carried links to fake HTML login pages hosted on the InterPlanetary File System (IPFS) – an interesting web-based decentralized/peer-to-peer data storage system. Unfortunately, pretty much any type of internet-connected data storage solution is used to host malicious content by threat actors these days, and the IPFS is no exception. In fact, it seems to have been used to host phishing pages since at least the beginning of 2022[[1](https://www.trendmicro.com/en_us/research/22/l/web3-ipfs-only-used-for-phishing---so-far.html)].

The recent wave of phishing messages is therefore not new in its use of the distributed file system, nor in the social engineering techniques it uses. What makes it somewhat interesting, besides the fact that it depends on IPFS, is that it also shows quite nicely the need for organizations to ensure that security-related headers are set by their web servers. This is because although, as you may see from the examples shown below, all the e-mails linking to pages hosted on IPFS were different…

[![](https://isc.sans.edu/diaryimages/images/23-03-15-phish1.png)](https://isc.sans.edu/diaryimages/images/23-03-15-phish1.png)

[![](https://isc.sans.edu/diaryimages/images/23-03-15-phish2.png)](https://isc.sans.edu/diaryimages/images/23-03-15-phish2.png)

…the HTML pages they linked to were very similar and all used the same clickjacking-related “login overlay over a legitimate website” trick.

This technique has been with us for a while now. It is based on the use of a HTML page, on which a fake login form is placed over an iframe, in which a legitimate website is loaded from a domain corresponding to the e-mail address of the recipient of the original phishing message. Since the e-mail address is (usually) passed to the phishing page in a parameter and the corresponding legitimate website is loaded dynamically, the result may look relatively believable, even though the fake login page was not tailor-made for a specific “target” individual or organization.

You may see an example of a reasonably good-looking result of this technique in the following image.

[![](https://isc.sans.edu/diaryimages/images/23-03-15-overlay1.png)](https://isc.sans.edu/diaryimages/images/23-03-15-overlay1.png)

However, if the Content Security Policy and/or the X-Frame-Options HTTP headers are set, which is one of the standard defenses against clickjacking[[2](https://owasp.org/www-community/attacks/Clickjacking)], the resulting login page is much less believable, as you may see in the following image…

[![](https://isc.sans.edu/diaryimages/images/23-03-15-overlay2.png)](https://isc.sans.edu/diaryimages/images/23-03-15-overlay2.png)

Since clickjacking defenses have historically been used primarily to protect websites with sensitive functionalities and/or login forms, relevant security headers may not always be set for the “main website” of an organization.

However, as this phishing shows (and as do many others we’ve seen before), the lack of these headers on almost any website can potentially be a problem. Therefore, maybe the time has come to make CSP and other HTTP security headers the norm and not the exception. Although their use can sometimes be a little problematic, the corresponding issues can always be solved, and the simple use of few HTTP headers can make phishing attempts, such as the ones mentioned above, much less effective.

[1] <https://www.trendmicro.com/en_us/research/22/l/web3-ipfs-only-used-for-phishing---so-far.html>
[2] <https://owasp.org/www-community/attacks/Clickjacking>

-----------
Jan Kopriva
[@jk0pr](https://twitter.com/jk0pr)
[Nettles Consulting](https://www.nettles.cz/)

Keywords: [HTTP](/tag.html?tag=HTTP) [HTML](/tag.html?tag=HTML) [Phishing](/tag.html?tag=Phishing)

[0 comment(s)](/diary/IPFS%2Bphishing%2Band%2Bthe%2Bneed%2Bfor%2Bcorrectly%2Bset%2BHTTP%2Bsecurity%2Bheaders/29638/#comments)

* [previous](/diary/29634)
* [next](/diary/29642)

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