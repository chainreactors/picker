---
title: Why TLP should not replace your internal information classification, (Sat, Oct 10th)
url: https://isc.sans.edu/diary/rss/33414
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-10
fetch_date: 2026-10-11T08:03:40.090780
---

# Why TLP should not replace your internal information classification, (Sat, Oct 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/33410)

Click HERE to learn more about classes Jan is teaching for SANS

# [Why TLP should not replace your internal information classification](/forums/diary/Why%2BTLP%2Bshould%2Bnot%2Breplace%2Byour%2Binternal%2Binformation%2Bclassification/33414/)

**Published**: 2026-10-10. **Last Updated**: 2026-10-10 09:11:34 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/Why%2BTLP%2Bshould%2Bnot%2Breplace%2Byour%2Binternal%2Binformation%2Bclassification/33414/#comments)

The Traffic Light Protocol (TLP)[[1](https://www.first.org/tlp/)], which is now in its second incarnation, is a wonderful standard that enables one to easily communicate whether information may be shared further (and if so, how far).

That being said, I've noticed a somewhat unfortunate trend in a number of organizations that try to fit TLP into a niche it was never supposed to occupy by attempting to use its labels as a replacement for traditional internal information classification schemes.

At first glance, this may seem quite reasonable. After all, TLP is a well-known standard, and it defines a simple set of labels for restricting the sharing of information (as you can see in the following table). And since most organizational classification schemes also consist of only a few levels, why not use TLP instead of maintaining a separate set of labels?

[![](https://isc.sans.edu/diaryimages/images/26-10-10-tlpv2.png)](https://isc.sans.edu/diaryimages/images/26-10-10-tlpv2.png)

Unfortunately, there are several reasons why this might not be the best idea.

The first is that TLP was never intended to be used in this way. In fact, the official TLP 2.0 standard explicitly states that “TLP is not a formal classification scheme” and that it was not designed to define information handling or encryption rules. Its purpose is to specify with whom information may be shared, not how it should be protected. While these two aspects are certainly related, they are far from being interchangeable.

An internal information classification scheme may, for example, define requirements for encryption, storage, access control or retention of information with different sensitivity levels. None of these requirements can be inferred from a TLP label alone.

For example, an organization may allow documents classified as "Sensitive" to be sent to customers, but only in encrypted e-mails or on encrypted USB drives. Even if a TLP label permits sharing with the intended recipients, it doesn't say anything about these requirements. To express them using TLP alone, the organization would have to add its own information handling rules to the labels – effectively creating a custom classification scheme.

Also – and perhaps more importantly – the sharing restrictions defined by TLP don't necessarily correspond to what one might expect from similarly named internal classification levels.

Consider, for example, an organization that uses TLP:GREEN to mark documents intended for internal use. According to the actual TLP definition, however, information marked with this label may be shared within a relevant community (which, unless otherwise specified, means the cybersecurity/defense community). If such a document were shared with an external security partner, the recipient might therefore quite legitimately distribute it further, even though this was never the intention of the original organization.

A similar problem may arise with TLP:AMBER, which permits sharing not only within the recipient's organization, but also with its clients on a need-to-know basis when necessary to protect them. And while TLP:AMBER+STRICT removes the latter possibility, neither designation necessarily corresponds to what an organization might consider "Confidential" information. TLP:RED, on the other hand, prohibits any further sharing beyond the original recipients without permission from the source, which would make it rather impractical for many types of internal documents.

A related problem arises when TLP labels are assigned according to how sensitive a document is considered to be, rather than who should be able to receive it. A network diagram might, for example, be marked TLP:RED simply because someone considers it "Highly Confidential", even though several teams or external contractors might need access to it. In such a case, the label would either make legitimate sharing unnecessarily difficult or end up being routinely ignored.

Of course, organizations can define additional restrictions or their own interpretations of these labels. However, doing so effectively means creating a custom classification scheme which only looks like TLP, and which may consequently lead to misunderstandings whenever information is exchanged with anyone who follows the actual standard.

This is not to say that TLP shouldn't be used within organizations. It certainly has its place there, especially when it comes to sharing threat intelligence and other security-related information. Nevertheless, it should complement an internal information classification scheme, rather than replace it.

After all, the main reason for using standardized labels is to make it easier for everyone to understand what they are allowed to do with specific information. And using the same labels to mean different things depending on who reads them seems like a rather good way to achieve the exact opposite...

[1] <https://www.first.org/tlp/>

-----------
Jan Kopriva
[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords:

[0 comment(s)](/diary/Why%2BTLP%2Bshould%2Bnot%2Breplace%2Byour%2Binternal%2Binformation%2Bclassification/33414/#comments)

Click HERE to learn more about classes Jan is teaching for SANS

* [previous](/diary/33410)

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