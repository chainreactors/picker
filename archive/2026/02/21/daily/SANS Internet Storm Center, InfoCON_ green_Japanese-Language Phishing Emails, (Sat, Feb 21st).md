---
title: Japanese-Language Phishing Emails, (Sat, Feb 21st)
url: https://isc.sans.edu/diary/rss/32734
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-21
fetch_date: 2026-02-22T04:10:32.503311
---

# Japanese-Language Phishing Emails, (Sat, Feb 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/32730)

# [Japanese-Language Phishing Emails](/forums/diary/JapaneseLanguage%2BPhishing%2BEmails/32734/)

**Published**: 2026-02-21. **Last Updated**: 2026-02-21 06:03:36 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[0 comment(s)](/diary/JapaneseLanguage%2BPhishing%2BEmails/32734/#comments)

***Introduction***

For at least the past year or so, I've been receiving Japanese-language phishing emails to my blog email addresses at @malware-traffic-analysis.net.  I'm not Japanese, but I suppose my blog's email addresses ended up on a list used by the group sending these emails. They're all easily caught by my spam filters, so they're not especially dangerous in my situation. However, they could be effective for the Japanese-speaking recipients with poor spam filtering.

Despite the different companies impersonated, they all follow a similar pattern for the phishing page URLs and email-sending addresses.

This diary reviews three examples of these phishing emails.

[![](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-01.jpg)](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-01a.jpg)
*Shown above: The spam folder for my blog's admin email account.*

***Screenshots***

The first screenshot shows an example of a phishing email impersonating the Japanese airline ANA (All Nippon Airways). Both the sending email address and the link for the phishing page use domains with a .cn top-level domain (TLD).

[![](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-02.jpg)](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-02a.jpg)
*Shown above: Example of a Japanese phishing email impersonating ANA.*

The second screenshot shows an example of a phishing email impersonating the shipping/logistics company DHL. Like the previous example, both the sending email address and the link for the phishing page use domains with a .cn top-level domain (TLD).

[![](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-03c.jpg)](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-03a.jpg)
*Shown above: Example of a Japanese phishing email impersonating DHL.*

Finally, the third screenshot shows an example of a phishing email impersonating the utilities company myTOKYOGAS. Like the previous two examples, both the sending email address and the link for the phishing page use domains with a .cn top-level domain (TLD).

[![](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-04.jpg)](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-04a.jpg)
*Shown above: Example of a Japanese phishing email impersonating myTOKYOGAS.*

As noted earlier, these emails have different themes, but they have similar patterns that indicate these were sent from the same group.

***Indicators of the Activity***

Example 1:

* Received: from ncqjw[.]cn (unknown [150.5.129[.]136])
* Date: Thu, 19 Feb 2026 21:52:36 +0800
* From: "ANA" <member.llbyzmf@ncqjw[.]cn>
* X-mailer: Foxmail 6, 13, 102, 15 [cn]
* Link for phishing page: hxxps[:]//branchiish.aayjlc[.]cn/amcmembr\_Loginam/

Example 2:

* Received: from obpwnrl[.]cn (unknown [101.47.78[.]193])
* Date: Fri, 20 Feb 2026 12:29:35 +0800
* From: "DHL" <dmail.elthr@obpwnrl[.]cn>
* X-mailer: Foxmail 6, 13, 102, 15 [cn]
* Link for phishing page: hxxps[:]//decideosity.ykdyrkye[.]cn/portal\_login\_exp/getQuoteTab/

Example 3:

* Received: from cwqfvzp[.]cn (unknown [150.5.130[.]42])
* Date: Fri, 20 Feb 2026 23:50:56 +0800
* From: "myTOKYOGAS" <reportogkfgkbye@cwqfvzp[.]cn>
* X-mailer: Foxmail 6, 13, 102, 15 [cn]
* Link for phishing page: hxxps[:]//impactish.rexqm[.]cn/mtgalogin/

***Final Words***

The most telling indicator that these emails were sent from the same group is the X-mailer: Foxmail 6, 13, 102, 15 [cn] line in the email headers.

I'm not likely to be tricked into giving up information for accounts that I don't have, like for myTOKYOGAS or for DHL.  Other recipients could be tricked by these, though, assuming they make it past a recipient's spam filter.

I'm curious how effective these phishing emails are, because the group behind this activity appears to be casting a wide net that reaches non-Japanese speakers.

If anyone else has received these types of phishing emails, feel free to leave a comment or submit an example via our [contact page](https://isc.sans.edu/contact.html).

Bradley Duncan
brad [at] malware-traffic-analysis.net

Keywords: [email](/tag.html?tag=email) [phishing](/tag.html?tag=phishing)

[0 comment(s)](/diary/JapaneseLanguage%2BPhishing%2BEmails/32734/#comments)

* [previous](/diary/32730)

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