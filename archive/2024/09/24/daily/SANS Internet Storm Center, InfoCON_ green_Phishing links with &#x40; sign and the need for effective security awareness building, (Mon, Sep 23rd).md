---
title: Phishing links with &#x40; sign and the need for effective security awareness building, (Mon, Sep 23rd)
url: https://isc.sans.edu/diary/rss/31288
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-24
fetch_date: 2025-10-06T18:30:29.928789
---

# Phishing links with &#x40; sign and the need for effective security awareness building, (Mon, Sep 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31282)
* [next](/diary/31292)

# [Phishing links with @ sign and the need for effective security awareness building](/forums/diary/Phishing%2Blinks%2Bwith%2Bsign%2Band%2Bthe%2Bneed%2Bfor%2Beffective%2Bsecurity%2Bawareness%2Bbuilding/31288/)

**Published**: 2024-09-23. **Last Updated**: 2024-09-23 07:40:22 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/Phishing%2Blinks%2Bwith%2Bsign%2Band%2Bthe%2Bneed%2Bfor%2Beffective%2Bsecurity%2Bawareness%2Bbuilding/31288/#comments)

While going over a batch of phishing e-mails that were delivered to us here at the Internet Storm Center during the first half of September, I noticed one message which was somewhat unusual. Not because it was untypically sophisticated or because it used some completely new technique, but rather because its authors took advantage of one of the less commonly misused aspects of the URI format – the ability to specify information about a user in the URI before its "host" part (domain or IP address).

RFC 3986 specifies[[1](https://datatracker.ietf.org/doc/html/rfc3986#section-3.2)] that a “user information” string (i.e., username and – potentially – other contextual data) may be included in a URI in the following format:

```

[ userinfo "@" ] host [ ":" port ]
```

In this instance, the threat actors used the user information string to make the link appear as if it was pointing to facebook.com, while it actually lead to an IPFS gateway[[2](https://isc.sans.edu/diary/30744)] ipfs.io.

[![](https://isc.sans.edu/diaryimages/images/24-09-23-mail.png)](https://isc.sans.edu/diaryimages/images/24-09-23-mail.png)

As you can see in the previous image, the full target for the link was:

```

hxxps[:]//facebook.com+login%3Dsecure+settings%3Dprivate@ipfs[.]io/ipfs/bafybeie2aelf7bfz53x7bquqxa4r3x2zbjplhmaect2pwxiyws6rlegzte/sept.html#[e-mail_address_of_recipient]
```

This approach is not new – threat actors have been misusing the user information string for a long time, sometimes more intensively, sometimes less so[[3](https://www.malwarebytes.com/blog/news/2022/05/long-lost-symbol-gets-new-life-obscuring-malicious-urls)] – nevertheless, it is something that can be quite effective if recipients aren’t careful about the links they click.

This specific technique is also only seldom mentioned in security awareness courses, and since I was recently asked to “add it in” one such course by a customer, I thought that the concept of effective security awareness building in relation to phishing deserved some small discussion.

The truth is that even if this technique is not covered in a security awareness course, this – by itself – doesn’t necessarily mean that such a course is useless. In fact, to my mind, it might be more effective than a course which includes it. Bear with me here…

It is undeniable that less can sometimes mean more when it comes to security awareness building. During an initial/on-boarding security training or a periodic security awareness training, we only have a limited time to teach non-specialists about a very complex field. This means that we need to necessarily cover the topic in as effective a manner as possible. And, when it comes to phishing, I don’t think that anyone would disagree that there are many more techniques than one can reasonable cover in the context of a one or two hour course (in fact, covering just a few of them is enough for a technical webinar[[4](https://www.youtube.com/watch?v=Fb2Z3bw-oJ8)]). So, this is one area where we probably shouldn’t try to “catch them all”. Rather, we should try to focus on those aspects of phishing that are common to most techniques, since these can help people to identify that something is wrong regardless of the specific approach the attacker might have taken. Which brings us back to the use of the “at” sign and the ability of threat actors to prepend an arbitrary user information string ahead of the host part of the URI.

Since this isn’t (by far) the only technique depending on users looking first at the beginning of a link (e.g., think of a threat actor using a well-chosen fifth or sixth level domain in their messages , such as “*https://isc.sans.edu.untrustednetwork.net/random*” to make it appear as if the link goes to *isc.sans.edu*), it might make more sense not to include information about the technique that uses the “at” sing specifically in a security awareness course, but rather to discuss how to find the domain part of any link by looking for the first standalone slash (so, not counting the two in http(s)://), and how to check the domain right to left to make sure that it is trustworthy, since this would cover any phishing technique where the link used would point to an untrustworthy domain.

This doesn’t mean that one can’t/shouldn’t mention the details of how threat actors can misues user information strings in URLs in – for example – a security awareness newsletter, however it probably isn’t something that we should devote time and space to during a 60 or 90-minute initial or periodic security awareness course for all employees of an organization.

[1] <https://datatracker.ietf.org/doc/html/rfc3986#section-3.2>
[2] <https://isc.sans.edu/diary/30744>
[3] <https://www.malwarebytes.com/blog/news/2022/05/long-lost-symbol-gets-new-life-obscuring-malicious-urls>
[4] <https://www.youtube.com/watch?v=Fb2Z3bw-oJ8>

-----------
Jan Kopriva
[@jk0pr](https://twitter.com/jk0pr) | [LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords:

[0 comment(s)](/diary/Phishing%2Blinks%2Bwith%2Bsign%2Band%2Bthe%2Bneed%2Bfor%2Beffective%2Bsecurity%2Bawareness%2Bbuilding/31288/#comments)

* [previous](/diary/31282)
* [next](/diary/31292)

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