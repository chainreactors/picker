---
title: A phishing with invisible characters in the subject line, (Tue, Oct 28th)
url: https://isc.sans.edu/diary/rss/32428
source: SANS Internet Storm Center, InfoCON: green
date: 2025-10-28
fetch_date: 2025-10-29T03:16:20.005779
---

# A phishing with invisible characters in the subject line, (Tue, Oct 28th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jim Clausing](/handler_list.html#jim-clausing "Jim Clausing")

Threat Level: [green](/infocon.html)

* [previous](/diary/32422)

# [A phishing with invisible characters in the subject line](/forums/diary/A%2Bphishing%2Bwith%2Binvisible%2Bcharacters%2Bin%2Bthe%2Bsubject%2Bline/32428/)

**Published**: 2025-10-28. **Last Updated**: 2025-10-28 10:12:32 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/A%2Bphishing%2Bwith%2Binvisible%2Bcharacters%2Bin%2Bthe%2Bsubject%2Bline/32428/#comments)

While reviewing malicious messages that were delivered to our handler inbox over the past few days, I noticed that the “subject” of one phishing e-mail looked quite strange when displayed in the Outlook message list…

[![](https://isc.sans.edu/diaryimages/images/25-10-28-shy-subject.png)](https://isc.sans.edu/diaryimages/images/25-10-28-shy-subject.png1)

As you can see, once the message was open, the subject was displayed as a normal, readable text. This suggested that some invisible characters were likely present…

A quick look at the e-mail headers proved this to be the case. The subject was composed of the following two lines:

```

Subject: =?UTF-8?B?WcKtb3XCrXIgUMKtYXPCrXN3wq1vwq1yZCBpwq1zIEHCrWLCrW91dCA=?=
	=?UTF-8?B?dMKtbyBFwq14wq1wwq1pcsKtZQ==?=
```

This formatting meant that the subject was included in the message in a MIME “encoded-word” format, which is described in RFC 2047 as having the following structure[[1](https://datatracker.ietf.org/doc/html/rfc2047)]:

```

encoded-word = "=?" charset "?" encoding "?" encoded-text "?="
```

In our case, the subject therefore consisted of two encoded words containing text written in the UTF-8 character set, which has been Base64 encoded.

Once both lines were decoded, one could clearly see that an invisible character was indeed being used in multiple places in the strings – specifically the soft hyphen, which has a Unicode code point U+00AD, and which is more commonly used as the &shy; HTML entity[[2](https://en.wikipedia.org/wiki/Soft_hyphen)].

[![](https://isc.sans.edu/diaryimages/images/25-10-28-subject-decoded.png)](https://isc.sans.edu/diaryimages/images/25-10-28-subject-decoded.png)

Although soft hyphens aren’t – strictly speaking – invisible, Outlook as well as most other e-mail clients don’t render them as visible text in most cases.

The use of the soft hyphen character – combined with splitting the subject into multiple MIME encoded-words – was clearly intended as an attempt at bypassing e-mail filtering mechanisms that are supposed to automatically detect potentially malicious messages.

Why is this approach noteworthy?

Because although the use of invisible characters in phishing e-mails in general (and of the use of the “shy” character in particular[[3](https://isc.sans.edu/diary/31626)]) is quite common when it comes to making the contents of e-mail messages less readable to security solutions, it is quite unusual to see it also applied to a subject of a message.

In fact, the only allusion to this technique I’ve been able to find with a quick Google search was a general mention in an article by Microsoft Threat Intelligence from 2021, which states that “In several observed campaigns, attackers inserted invisible Unicode characters to break up keywords in an email body or subject line in an attempt to bypass detection and automated security analysis”[[4](https://www.microsoft.com/en-us/security/blog/2021/08/18/trend-spotting-email-techniques-how-modern-phishing-emails-hide-in-plain-sight/)].

Since the use of invisible characters in e-mail subject lines doesn’t seem to be widely known, I have therefore decided that it would be worthwhile to dedicate this short diary to it.

It should be noted that the subject line wasn’t the only place where the soft hyphen character was used in the message – it was also heavily present in the text itself, where it was used to break up individual words…

[![](https://isc.sans.edu/diaryimages/images/25-10-28-contents.png)](https://isc.sans.edu/diaryimages/images/25-10-28-contents.png)

For completeness’s sake, we should also mention that the link in the phishing pointed to the URL hxxps[:]//stopsoriasis[.]co[.]il/Webmail/webmail.php?email=[[[email protected]](/cdn-cgi/l/email-protection)], where a generic “webmail login” credential stealing page was placed…

[![](https://isc.sans.edu/diaryimages/images/25-10-28-page.png)](https://isc.sans.edu/diaryimages/images/25-10-28-page.png)

[1] <https://datatracker.ietf.org/doc/html/rfc2047>
[2] <https://en.wikipedia.org/wiki/Soft_hyphen>
[3] <https://isc.sans.edu/diary/31626>
[4] <https://www.microsoft.com/en-us/security/blog/2021/08/18/trend-spotting-email-techniques-how-modern-phishing-emails-hide-in-plain-sight/>

-----------
Jan Kopriva
[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords: [Phishing](/tag.html?tag=Phishing)

[0 comment(s)](/diary/A%2Bphishing%2Bwith%2Binvisible%2Bcharacters%2Bin%2Bthe%2Bsubject%2Bline/32428/#comments)

* [previous](/diary/32422)

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