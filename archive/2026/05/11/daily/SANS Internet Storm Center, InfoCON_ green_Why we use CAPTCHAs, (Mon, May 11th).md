---
title: Why we use CAPTCHAs, (Mon, May 11th)
url: https://isc.sans.edu/diary/rss/32974
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-11
fetch_date: 2026-05-12T05:39:17.509054
---

# Why we use CAPTCHAs, (Mon, May 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32970)
* [next](/diary/32976)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Why we use CAPTCHAs](/forums/diary/Why%2Bwe%2Buse%2BCAPTCHAs/32974/)

**Published**: 2026-05-11. **Last Updated**: 2026-05-11 14:20:16 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Why%2Bwe%2Buse%2BCAPTCHAs/32974/#comments)

A few months ago, I implemented Cloudflare's Turnstile CAPTCHA on some pages. The reason for implementing these CAPTCHAs is obvious: Bots make up a large percentage of traffic and affect site performance.

So I figured it was a good time to look back and see how effective these CAPTCHA are. The quick number: Out of about 300 requests, only 1 passed the test. Or 99.7% of requests came from bots. And this is after we have been running this for a few months. Some bots may have stopped scanning the page.

But what about false positives? One false positive I noted from the login page was people clicking "Submit" on the login form before the CAPTCHA test was completed. This was easily fixed with a bit of JavaScript, which enabled the button only after a test was completed.

Some of the top offenders:

* 219.117.237.208. - resolves to 219.117.237.208.static.zoot.jp and appears to be some kind of spider
* 18.229.88.75 - an AWS host, also attempting to download our IP data
* 164.52.120.0/24 - Cloud provider in HK
* 2a03:2880:f806::/48 - Facebook Ireland

So far, I have received only a few complaints about false positives (aside from the now fixed login page issue).

Why I selected "Turnstile" over other CAPTCHA options:

* Cloudflare's turnstile implementation appears to have fewer privacy issues than others, like Google Recaptcha
* They are in my opinion, low impact to the user
* Implementing them on the site wasn't too difficult
* We already use Cloudflare as a CDN.
* They work well enough

CAPTCHA can often be bypassed. The right CAPTCHA solution makes it hard enough for an attacker to bypass that the value of the data they would be getting is not worth the effort.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Why%2Bwe%2Buse%2BCAPTCHAs/32974/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/32970)
* [next](/diary/32976)

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