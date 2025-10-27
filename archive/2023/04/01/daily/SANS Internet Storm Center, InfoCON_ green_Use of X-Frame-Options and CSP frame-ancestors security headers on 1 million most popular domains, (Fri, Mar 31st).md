---
title: Use of X-Frame-Options and CSP frame-ancestors security headers on 1 million most popular domains, (Fri, Mar 31st)
url: https://isc.sans.edu/diary/rss/29698
source: SANS Internet Storm Center, InfoCON: green
date: 2023-04-01
fetch_date: 2025-10-04T11:24:39.822022
---

# Use of X-Frame-Options and CSP frame-ancestors security headers on 1 million most popular domains, (Fri, Mar 31st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29696)
* [next](/diary/29700)

# [Use of X-Frame-Options and CSP frame-ancestors security headers on 1 million most popular domains](/forums/diary/Use%2Bof%2BXFrameOptions%2Band%2BCSP%2Bframeancestors%2Bsecurity%2Bheaders%2Bon%2B1%2Bmillion%2Bmost%2Bpopular%2Bdomains/29698/)

**Published**: 2023-03-31. **Last Updated**: 2023-03-31 12:57:26 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/Use%2Bof%2BXFrameOptions%2Band%2BCSP%2Bframeancestors%2Bsecurity%2Bheaders%2Bon%2B1%2Bmillion%2Bmost%2Bpopular%2Bdomains/29698/#comments)

In my last Diary[[1](https://isc.sans.edu/forums/diary/IPFS%2Bphishing%2Band%2Bthe%2Bneed%2Bfor%2Bcorrectly%2Bset%2BHTTP%2Bsecurity%2Bheaders/29638/)], I shortly mentioned the need for correctly set Content Security Policy and/or the obsolete[[2](https://w3c.github.io/webappsec-csp/#frame-ancestors-and-frame-options)] X-Frame-Options HTTP security headers (not just) in order to prevent phishing pages, which overlay a fake login prompt over a legitimate website, from functioning correctly. Or, to be more specific, to prevent them from dynamically loading a legitimate page in an iframe under the fake login prompt, since this makes such phishing websites look much less like a legitimate login page and thus much less effective.

Discussion of the aforementioned headers has led me to a question of how common use of these headers is and how they are commonly set. Which is what we will take a short look at today.

Although data about general trends in the use of these headers may be found online[[3](https://trends.builtwith.com/docinfo/X-Frame-Options),[4](https://trends.builtwith.com/docinfo/Content-Security-Policy)], I wanted to go a little bit more in-depth. I have therefore written a short Python script, which would go through the current Tranco list of one million most popular domains[[5](https://tranco-list.eu/)] and gather data about which HTTP security-related headers were used on each one (provided the domains pointed to a HTTP server).

In total, the script gathered data about 21 different headers (e.g., X-XSS-Protection, Strict-Transport-Security, Cross-Origin-Resource-Policy, etc.) and their specific settings. Since results for the other headers might be interesting as well, I might write another diary discussing those once I’ve had more time to go over the data. For now, however, let us take a look at how common the use of the two headers which may be used to set restrictions for embedding a websites in an iframe or other object is. Specifically, we will look at the use of X-Frame-Options header and the use of CSP policies containing the frame-ancestors directive (since CSP doesn’t block the behavior we are interested in – the so called “framing attacks” – without this directive in place, we will only focus on CSP headers in which the directive is present).

As you may see from the following chart, at the time of writing, over 27.1% of the top 1000 most popular domains according to the Tranco list used either one or both of the aforementioned headers to prevent embedding of their content on undesirable domains. Of the top 100k domains, it was however only 20.6% and of the top 1 million domains, it was only a little more than 14.4%.

[![](https://isc.sans.edu/diaryimages/images/23-03-31-x-frame-csp.png)](https://isc.sans.edu/diaryimages/images/23-03-31-x-frame-csp.png)

On the following charts, you may see how different X-Frame-Options and CSP frame-ancestors directives were represented in different sample sizes.

[![](https://isc.sans.edu/diaryimages/images/23-03-31-x-frame-options.png)](https://isc.sans.edu/diaryimages/images/23-03-31-x-frame-options.png)

[![](https://isc.sans.edu/diaryimages/images/23-03-31-csp.png)](https://isc.sans.edu/diaryimages/images/23-03-31-csp.png)

From the available data, it appears that while the X-Frame-Options HTTP header is used on more than 13.84% of the top 1 million domains, CSP with the frame-ancestors directive is set only by 1.91% web servers hosted on such domains.

Since one can reasonably assume that the domains listed on the Tranco list would have above-average, or at least average security measures in place, it would seem that when it comes to protecting us from framing attacks (and from the aforementioned phishing pages which take advantage of them), the deprecated X-Frame-Options header is still the most commonly used mechanism on the internet... Which is supported even by results from Shodan[[6](https://www.shodan.io/search?query=HTTP+%22x-frame-options%22),[7](https://www.shodan.io/search?query=HTTP+%22content-security-policy%22+%22frame-ancestors%22)], which, at the time of writing, detected X-Frame-Options header on more than 41 million public IPs and CSP with the frame-ancestors directive only on approximately 12 million IPs.

[1] [https://isc.sans.edu/forums/diary/IPFS+phishing+and+the+need+for+correctly+set+HTTP+security+headers/29638/](https://isc.sans.edu/forums/diary/IPFS%2Bphishing%2Band%2Bthe%2Bneed%2Bfor%2Bcorrectly%2Bset%2BHTTP%2Bsecurity%2Bheaders/29638/)
[2] <https://w3c.github.io/webappsec-csp/#frame-ancestors-and-frame-options>
[3] <https://trends.builtwith.com/docinfo/X-Frame-Options>
[4] <https://trends.builtwith.com/docinfo/Content-Security-Policy>
[5] <https://tranco-list.eu/>
[6] <https://www.shodan.io/search?query=HTTP+%22x-frame-options%22>
[7] <https://www.shodan.io/search?query=HTTP+%22content-security-policy%22+%22frame-ancestors%22>

-----------
Jan Kopriva
[@jk0pr](https://twitter.com/jk0pr)
[Nettles Consulting](https://www.nettles.cz/)

Keywords: [Clickjacking](/tag.html?tag=Clickjacking) [XFrameOptions](/tag.html?tag=XFrameOptions) [CSP](/tag.html?tag=CSP) [HTTP](/tag.html?tag=HTTP) [Phishing](/tag.html?tag=Phishing)

[0 comment(s)](/diary/Use%2Bof%2BXFrameOptions%2Band%2BCSP%2Bframeancestors%2Bsecurity%2Bheaders%2Bon%2B1%2Bmillion%2Bmost%2Bpopular%2Bdomains/29698/#comments)

* [previous](/diary/29696)
* [next](/diary/29700)

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