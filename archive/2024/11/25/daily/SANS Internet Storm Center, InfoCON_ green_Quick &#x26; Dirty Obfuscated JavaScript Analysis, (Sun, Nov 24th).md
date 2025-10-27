---
title: Quick &#x26; Dirty Obfuscated JavaScript Analysis, (Sun, Nov 24th)
url: https://isc.sans.edu/diary/rss/31468
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-25
fetch_date: 2025-10-06T19:15:40.484975
---

# Quick &#x26; Dirty Obfuscated JavaScript Analysis, (Sun, Nov 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31466)
* [next](/diary/31470)

# [Quick & Dirty Obfuscated JavaScript Analysis](/forums/diary/Quick%2BDirty%2BObfuscated%2BJavaScript%2BAnalysis/31468/)

**Published**: 2024-11-24. **Last Updated**: 2024-11-24 09:22:41 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Quick%2BDirty%2BObfuscated%2BJavaScript%2BAnalysis/31468/#comments)

As mentioned in diary entry "[Increase In Phishing SVG Attachments](https://isc.sans.edu/diary/Increase%20In%20Phishing%20SVG%20Attachments/31456)", I have a [phishing SVG sample with heavily obfuscated JavaScript](https://www.virustotal.com/gui/file/953d83642b6aae079afd82a6270651bd073ec1cdf5a3e97e05b98619f4257593).

![](https://isc.sans.edu/diaryimages/images/20241124-095202.png)

As I didn't want to spend time doing static analysis, I did a quick dynamic analysis instead. TL;DR: I open the SVG file in a VM disconnected from the Internet, and use Edge's developer tools to view the deobuscated URL.

First I make sure the VM is disconnected from the network:

![](https://isc.sans.edu/diaryimages/images/20241124-091029.png)

Then I open the SVG file in Edge (Chrome works too):

![](https://isc.sans.edu/diaryimages/images/20241124-091126.png)

I open the developer tools:

![](https://isc.sans.edu/diaryimages/images/20241124-091149.png)

I switch to the Network tab:

![](https://isc.sans.edu/diaryimages/images/20241124-091211.png)

And then I type a dummy password and click on the Download button:

![](https://isc.sans.edu/diaryimages/images/20241124-091235.png)

I can then view the deobfuscated URL:

![](https://isc.sans.edu/diaryimages/images/20241124-091321.png)

And also the payload:

![](https://isc.sans.edu/diaryimages/images/20241124-091340.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Quick%2BDirty%2BObfuscated%2BJavaScript%2BAnalysis/31468/#comments)

* [previous](/diary/31466)
* [next](/diary/31470)

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