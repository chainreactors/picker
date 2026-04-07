---
title: How often are redirects used in phishing in 2026&#x3f;, (Mon, Apr 6th)
url: https://isc.sans.edu/diary/rss/32870
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-06
fetch_date: 2026-04-07T04:30:39.784907
---

# How often are redirects used in phishing in 2026&#x3f;, (Mon, Apr 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/32864)

Click HERE to learn more about classes Jan is teaching for SANS

# [How often are redirects used in phishing in 2026?](/forums/diary/How%2Boften%2Bare%2Bredirects%2Bused%2Bin%2Bphishing%2Bin%2B2026/32870/)

**Published**: 2026-04-06. **Last Updated**: 2026-04-06 08:50:27 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/How%2Boften%2Bare%2Bredirects%2Bused%2Bin%2Bphishing%2Bin%2B2026/32870/#comments)

In one of his recent diaries, Johannes discussed how open redirects are actively being sought out by threat actors[[1](https://isc.sans.edu/diary/Open%2BRedirects%2BA%2BForgotten%2BVulnerability/32742)], which made me wonder about how commonly these mechanisms are actually misused…

Although open redirect is not generally considered a high-impact vulnerability on its own, it can have multiple negative implications. Johannes already covered one in connection with OAuth flows, but another important (mis)use case for them is phishing.

The reason is quite straightforward – links pointing to legitimate domains (such as google.com) included in phishing messages may appear benign to recipients and can also evade simpler e-mail scanners and other detection mechanisms.

Even though open redirect has not been listed in OWASP Top 10 for quite some time, it is clear that attackers have never stopped looking for it or using it. If I look at traffic on almost any one of my own domains, hardly a month goes by when I don’t see attempts to identify potentially vulnerable endpoints, such as:

```

/out.php?link=https://domain.tld/
```

While these attempts are not particularly frequent, they are generally consistent.

We also continue to see open redirect used in phishing campaigns. Last year, I wrote about a campaign using a “half-open” (i.e., easily abusable) redirect mechanism on Google [[2](https://isc.sans.edu/diary/Another%2Bday%2Banother%2Bphishing%2Bcampaign%2Babusing%2Bgooglecom%2Bopen%2Bredirects/31950)], and similar cases still seem to appear regularly.

But how regular are they, actually?

To find out, I reviewed phishing e-mails collected through my own filters and spam traps, as well as samples sent to us here at the ISC (either by our professional colleagues, or by threat actors themselves), over the first quarter of this year. Although the total sample only consisted of slightly more than 350 individual messages (and is therefore far from statistically representative), it still provided quite interesting results.

Redirect-based phishing accounted for a little over 21 % of all analyzed messages sent out over the first 3 months of 2026 – specifically for 32 % in January, 18 % in February and 16.5 % in March.

It should be noted that if a message contained multiple malicious links and at least one of them used a redirect, the entire message was counted exclusively as a redirect sample, and that not all redirect cases were classic "open redirects". In fact, the abused redirect mechanisms varied widely.

Some behaved similarly to the aforementioned Google-style “half-open” redirects (see details below), while others were fully open. In some cases, the redirectors were part of tracking or advertising systems, while in others, they were implemented as logout endpoints or similar mechanisms. It should be noted that URL shorteners were also counted as redirectors (although these were not particularly common).

As we mentioned, the Google-style redirects are not fully open. They do require a specific valid token to work, however, since these tokens are typically reusable, have a very long lifetime, and are not tied to any specific context (such as IP address or session), they can be – and are – readily reused in phishing campaigns.

An example of such a phishing message and subsequent redirection can be seen in the following images. Though, to avoid focusing solely on Google, it should be mentioned that similar redirect mechanisms on other platforms (e.g., Bing) are also being abused in the same way.

[![](https://isc.sans.edu/diaryimages/images/26-04-06-mail.png)](https://isc.sans.edu/diaryimages/images/26-04-06-mail.png)

[![](https://isc.sans.edu/diaryimages/images/26-04-06-redirect.png)](https://isc.sans.edu/diaryimages/images/26-04-06-redirect.png)

As we can see, although open redirect is commonly considered more of a nuisance issue than an actual high-risk vulnerability these days, it doesn’t keep malicious actors from misusing it quite heavily… Which means we shouldn’t just ignore it.

At the very least, it is worth ensuring that our own applications do not expose endpoints that can be misused in this way. And where any redirection functionality is strictly required, it should be monitored for abuse and restricted as necessary.

[1] [https://isc.sans.edu/diary/Open+Redirects+A+Forgotten+Vulnerability/32742](https://isc.sans.edu/diary/Open%2BRedirects%2BA%2BForgotten%2BVulnerability/32742)
[2] [https://isc.sans.edu/diary/Another+day+another+phishing+campaign+abusing+googlecom+open+redirects/31950](https://isc.sans.edu/diary/Another%2Bday%2Banother%2Bphishing%2Bcampaign%2Babusing%2Bgooglecom%2Bopen%2Bredirects/31950)

-----------
Jan Kopriva
[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords:

[0 comment(s)](/diary/How%2Boften%2Bare%2Bredirects%2Bused%2Bin%2Bphishing%2Bin%2B2026/32870/#comments)

Click HERE to learn more about classes Jan is teaching for SANS

* [previous](/diary/32864)

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