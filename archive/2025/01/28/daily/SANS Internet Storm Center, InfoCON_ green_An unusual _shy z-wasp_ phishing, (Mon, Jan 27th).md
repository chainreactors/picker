---
title: An unusual "shy z-wasp" phishing, (Mon, Jan 27th)
url: https://isc.sans.edu/diary/rss/31626
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-28
fetch_date: 2025-10-06T20:12:29.702480
---

# An unusual "shy z-wasp" phishing, (Mon, Jan 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31620)
* [next](/diary/31630)

# [An unusual "shy z-wasp" phishing](/forums/diary/An%2Bunusual%2Bshy%2Bzwasp%2Bphishing/31626/)

**Published**: 2025-01-27. **Last Updated**: 2025-01-27 10:45:52 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[2 comment(s)](/diary/An%2Bunusual%2Bshy%2Bzwasp%2Bphishing/31626/#comments)

Threat actors who send out phishing messages have long ago learned that zero-width characters and unrendered HTML entities can be quite useful to them. Inserting a zero-width character into a hyperlink can be used to bypass some URL security checks without any negative impact on the function of the link, while any unrendered entities can be used to break up any suspicious words or sentences that might lead to the message being classified as a potential phishing, without the recipient being aware of their inclusion.

![](https://isc.sans.edu/diaryimages/images/25-01-27-html.png)

One of the better-known techniques that depend on the use of zero-width characters (e.g., a Zero-Width Space – &#8203; a Zero-Width Non-Joiner – &#8204; a Zero-Width Joiner – &#8205; etc.)  was named Z-WASP by the researchers in Avanan who first discovered it being used to bypass O365 security filters in 2018 [[1](https://emailsecurity.checkpoint.com/blog/zwasp-microsoft-office-365-phishing-vulnerability)]. Nevertheless, the aforementioned practice of using “invisible” characters in phishing messages is far older – for example, the soft hyphen or “SHY” html entity (&shy;) has been used by threat actors at least since 2010[[2](https://threatpost.com/spammers-using-shy-character-hide-malicious-urls-100710/74558/)].

Both of these techniques are relevant to the topic of today’s diary – an interesting phishing message that arrived in our hander mailbox late last week.

At first glance, it looked like any other run of the mill phishing message (apart from the use of an unusually small font and a somewhat difficult to see red spot under the “KEEP MY PASSWORD” link)…

[![](https://isc.sans.edu/diaryimages/images/25-01-27-phishing.png)](https://isc.sans.edu/diaryimages/images/25-01-27-phishing.png)

However, a look at the underlaying HTML code proved to be quite interesting. As the following (somewhat cleaned-up) excerpt shows, authors of the message decided to use both of the aforementioned techniques to break up the message text – the zero-width joiners (&#8205;) were used in the title, while the SHY HTML entity (&shy;) was used everywhere else…

[![](https://isc.sans.edu/diaryimages/images/25-01-27-html.png)](https://isc.sans.edu/diaryimages/images/25-01-27-html.png)

Although this “shy z-wasp” combination has most likely been used before, it is certainly unusual – if nothing else, it is the first time I’ve ever noticed these two techniques being used in the same e-mail… And it goes to show that even quite old techniques (speaking of the use of SHY entity) are not necessarily irrelevant.

Regardless of the use of the unrendered characters, in this instance, it is obvious at first glance that the message is not legitimate. However, this might not be the case with some other messages in which threat actors might decide to use the same techniques… Which leaves us with a question of whether there is anything we can do to increase chances of detecting such messages on a human level, should the use of "invisible" characters lead to them bypassing any e-mail security filters we might have in place.

While we certainly can’t teach non-technical recipients to read HTML code of e-mail messages, and look for hidden characters, for those who use Outlook, we can do the next best thing – we can teach them to look at a message without HTML formatting. This can be done surprisingly easily – all one has to do is move the message into the Junk folder (if such a folder or its regional equivalent exits/is configured), and Outlook will remove most formatting and also display targets of any links in-line with the text they are related to…

[![](https://isc.sans.edu/diaryimages/images/25-01-27-no-formatting.png)](https://isc.sans.edu/diaryimages/images/25-01-27-no-formatting.png)

This might not always lead to a “this is obviously malicious” conclusion on the part of the recipient, but it is quick and, in some cases (as in this one), can certainly show that something is amiss with an otherwise trustworthy looking message.

So, if you work at a company which makes use of Microsoft’s e-mail client, and you are responsible for security awareness building, teaching users to drag-and-drop any message they are unsure of into the Junk folder might be advisable… Especially if you don’t have a security operations team who could analyze suspicious messages submitted by employees on a continuous basis.

[1] <https://emailsecurity.checkpoint.com/blog/zwasp-microsoft-office-365-phishing-vulnerability>
[2] <https://threatpost.com/spammers-using-shy-character-hide-malicious-urls-100710/74558/>

-----------
Jan Kopriva
[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords:

[2 comment(s)](/diary/An%2Bunusual%2Bshy%2Bzwasp%2Bphishing/31626/#comments)

* [previous](/diary/31620)
* [next](/diary/31630)

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