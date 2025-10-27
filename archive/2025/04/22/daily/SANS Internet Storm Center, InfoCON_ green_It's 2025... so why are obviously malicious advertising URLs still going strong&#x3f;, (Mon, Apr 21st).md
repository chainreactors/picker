---
title: It's 2025... so why are obviously malicious advertising URLs still going strong&#x3f;, (Mon, Apr 21st)
url: https://isc.sans.edu/diary/rss/31880
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-22
fetch_date: 2025-10-06T22:08:15.454891
---

# It's 2025... so why are obviously malicious advertising URLs still going strong&#x3f;, (Mon, Apr 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31876)
* [next](/diary/31888)

# [It's 2025... so why are obviously malicious advertising URLs still going strong?](/forums/diary/Its%2B2025%2Bso%2Bwhy%2Bare%2Bobviously%2Bmalicious%2Badvertising%2BURLs%2Bstill%2Bgoing%2Bstrong/31880/)

**Published**: 2025-04-21. **Last Updated**: 2025-04-21 08:48:44 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[1 comment(s)](/diary/Its%2B2025%2Bso%2Bwhy%2Bare%2Bobviously%2Bmalicious%2Badvertising%2BURLs%2Bstill%2Bgoing%2Bstrong/31880/#comments)

While the old adage stating that “the human factor is the weakest link in the cyber security chain” will undoubtedly stay relevant in the near (and possibly far) future, the truth is that the tech industry could – and should – help alleviate the problem significantly more than it does today.

One clear example of this was provided by a phishing e-mail that was delivered to our mailbox here at the Internet Storm Center this morning.

For anyone aware of modern phishing techniques, the fact that the message was fraudulent would have been obvious at first glance, as you may see from the following picture… In fact, it even used a “standard” layout that has been commonly used in phishing campaigns for some time now.

[![](https://isc.sans.edu/diaryimages/images/25-04-21-mail.png)](https://isc.sans.edu/diaryimages/images/25-04-21-mail.png)

The same could be said for the web page to which the link in the e-mail pointed – it was a commonly used, generic “Webmail” login portal.

[![](https://isc.sans.edu/diaryimages/images/25-04-21-website.png)](https://isc.sans.edu/diaryimages/images/25-04-21-website.png)

Nevertheless, anyone not technically minded or not aware of common lures that phishing actors like to use, could, of course, fall for the scam. And after they clicked on one of the links, they would most likely reach the phishing site.

This was – among other reasons – because of the domain to which the links in the phishing e-mail pointed. While the URL would raise red flags for anyone with sufficient technical know-how, it wasn’t classified as malicious, because it came from a legitimate domain – specifically from “googleads.g.doubleclick.net”.

As its first part suggests, the domain in question is used by Google for redirecting traffic resulting from clicking on its display ads.

We can see where one would be redirected if we take a look at the URL in full:

```

hxxps[:]//googleads[.]g[.]doubleclick[.]net/pcs/click?xai=AKAOjssIdZGtK2LGw4coQMwtQcONuf8cVZUVHUrlFgT33_wiLCuxpoweUvHdBH9neY4iW-CZh2SzgITptx6j64F0B2pEU0uoeRfmKTeyn7LSG5Irubqjv6IFl9MeqTp84ZT99WRJlZDMgrwUaUI7QjgNwL22AVveJm980wuVNryiILT2WhxCPmcY8M7PVIOygAXT_382p7PUn7bIByn2OjlTfCiaqta3tAhZWCuROeXZPznm5cGhgUYspVywPb8Y8GbuT5pyEUyF89icmqe5zg&amp;sig=Cg0ArKJSzFtr0kI2Y6Ll&amp;adurl=hxxps[:]//eec086f678a65400d3fa7ba9c787d976.ip-ddns[.]com#[[email protected]]
```

The last parameter named “adurl” shows that the “advertising URL” was:

```

hxxps[:]//eec086f678a65400d3fa7ba9c787d976.ip-ddns[.]com#[[email protected]]
```

It is worth noting at this point that:

* ip-ddns.com is a Dynamic DNS service (i.e., a place where no real, benign landing pages for ads could ever be reasonably expected to be hosted),
* we saw the same phishing campaign last Monday (i.e., a week ago) using the same URL, and the Google Ads redirect still hasn’t been disabled,
* VirusTotal scores the domain eec086f678a65400d3fa7ba9c787d976.ip-ddns[.]com at 18/94[[1](https://www.virustotal.com/gui/domain/eec086f678a65400d3fa7ba9c787d976.ip-ddns.com)] at the time of writing, which – on its own – certainly indicates that something is probably amiss with it…

To sum up, the question is: how is it possible that after a week, an ad service provided by a company such as Google still redirects to a URL hosting an obvious credential stealing page and the company hasn’t automatically blocked it?

Shouldn’t it have?

Detecting malicious links and sites is admittedly non-trivial. Nevertheless, I would argue that the absolute least that any company whose business model is in part based on displaying ads should do, would be to:

1.    filter out links to domains that absolutely no one would ever even dream of using for hosting actual benign ads (such as domains belonging to any dynamic DNS services) and
2.    periodically (ideally with a period shorter than one week) check all URLs that any ads it publishes point to and evaluate whether the corresponding landing pages aren’t obviously malicious.

Although it would undoubtedly add significant overhead to any ad provider, I would argue that given our dependence on the internet, and the ever-present nature of digital ads in it, such behavior should be the bare minimum that modern society should expect from ad providers in 2025.

Especially if said ad providers are counted among the Fortune 500 companies  (Fortune 10, if we want to be technical) and do, themselves, offer services based on AI models that could easily be used to automatically determine whether a page that their ads point to is most likely malicious. At the very least, ad providers could periodically check whether an ad's destination domain exceeds some baseline detection score on VirusTotal, and automatically flag or block such content pending analysis.

What about it, Google? After all, you do own VirusTotal as well…

[1] <https://www.virustotal.com/gui/domain/eec086f678a65400d3fa7ba9c787d976.ip-ddns.com>

-----------
Jan Kopriva
[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords: [Ad](/tag.html?tag=Ad) [Google](/tag.html?tag=Google) [Phishing](/tag.html?tag=Phishing)

[1 comment(s)](/diary/Its%2B2025%2Bso%2Bwhy%2Bare%2Bobviously%2Bmalicious%2Badvertising%2BURLs%2Bstill%2Bgoing%2Bstrong/31880/#comments)

* [previous](/diary/31876)
* [next](/diary/31888)

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