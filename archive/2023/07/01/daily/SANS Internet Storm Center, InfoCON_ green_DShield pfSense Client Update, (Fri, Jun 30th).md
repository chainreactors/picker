---
title: DShield pfSense Client Update, (Fri, Jun 30th)
url: https://isc.sans.edu/diary/rss/29994
source: SANS Internet Storm Center, InfoCON: green
date: 2023-07-01
fetch_date: 2025-10-04T11:57:39.198804
---

# DShield pfSense Client Update, (Fri, Jun 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29990)
* [next](/diary/29998)

# [DShield pfSense Client Update](/forums/diary/DShield%2BpfSense%2BClient%2BUpdate/29994/)

**Published**: 2023-06-30. **Last Updated**: 2023-06-30 00:01:06 UTC
**by** [Yee Ching Tok](https://poppopretn.com/aboutme/) (Version: 1)

[2 comment(s)](/diary/DShield%2BpfSense%2BClient%2BUpdate/29994/#comments)

The SANS Internet Storm Center (ISC) developed the DShield pfSense client in 2017 [1] to support the ingestion of pfSense firewall logs into the DShield project. The pfSense project has also evolved over the years, with some changes in the offerings [2]. With the advent of pfSense Community Edition (CE) 2.7.0 [3, 4] and pfSense Plus 23.01, updates to the DShield client were required to fix unintended issues.

I am pleased to share that the DShield pfSense client has been updated and tested to be working\* with pfSense CE 2.7.0 Release Candidate (RC) (just in time before pfSense CE 2.7.0-RELEASE is released on the targeted date of June 29, 2023), pfSense Plus 23.01-RELEASE as well as pfSense CE 2.6.0-RELEASE. To take a look at the DShield pfSense client, please visit the GitHub repository [here](https://github.com/jullrich/dshieldpfsense) [5]. If you are a pfSense user and would like to participate in the DShield project, please refer to my previous [diary](https://isc.sans.edu/diary/27240) [6] for the steps required to set it up.

[\* This release would not have been made possible without the understanding and support of my employers ([JT Consultancy & Management Pte. Ltd.](https://jtconsultancy.sg/) and [ASSET Research Group](https://asset-group.github.io)) that kindly allowed me to work on this quickly to resolve issues faced by the DShield pfSense users. I would also like to thank my colleagues, Hamilton Chan and Yong Xian Ng, for their kind assistance and support rendered in this release.]

**References:**
1. https://github.com/jullrich/dshieldpfsense/commit/13a891e5ba4ee86c3a35fea4dcda24cf8107e39b
2. https://www.netgate.com/blog/announcing-pfsense-plus
3. https://www.netgate.com/blog/pfsense-rc-2.7.0-and-23.05.1
4. https://www.netgate.com/blog/pfsense-2.7.0-and-23.05
5. https://github.com/jullrich/dshieldpfsense
6. https://isc.sans.edu/diary/27240

-----------
Yee Ching Tok, Ph.D., ISC Handler
[Personal Site](https://poppopretn.com)
[Mastodon](https://infosec.exchange/%40poppopretn)
[Twitter](https://twitter.com/poppopretn)

Keywords: [DShield](/tag.html?tag=DShield) [pfsense](/tag.html?tag=pfsense)

[2 comment(s)](/diary/DShield%2BpfSense%2BClient%2BUpdate/29994/#comments)

* [previous](/diary/29990)
* [next](/diary/29998)

### Comments

Please Disregard

#### <img src=xss onerror='alert(1)'>

#### Jun 30th 2023 2 years ago

Please disregard

#### &lt;img src=xss onerror='alert("XSS")'&gt;

#### Jun 30th 2023 2 years ago

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