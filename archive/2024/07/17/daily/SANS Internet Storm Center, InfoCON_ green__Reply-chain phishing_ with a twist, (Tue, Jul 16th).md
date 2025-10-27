---
title: "Reply-chain phishing" with a twist, (Tue, Jul 16th)
url: https://isc.sans.edu/diary/rss/31084
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-17
fetch_date: 2025-10-06T17:42:43.803439
---

# "Reply-chain phishing" with a twist, (Tue, Jul 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31078)
* [next](/diary/31086)

# ["Reply-chain phishing" with a twist](/forums/diary/Replychain%2Bphishing%2Bwith%2Ba%2Btwist/31084/)

**Published**: 2024-07-16. **Last Updated**: 2024-07-16 12:45:28 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/Replychain%2Bphishing%2Bwith%2Ba%2Btwist/31084/#comments)

Few weeks ago, I was asked by a customer to take a look at a phishing message which contained a link that one of their employees clicked on. The concern was whether the linked-to site was only a generic credential stealing web page or something targeted/potentially more dangerous. Luckily, it was only a run-of-the-mill phishing kit login page, nevertheless, the e-mail message itself turned out to be somewhat more interesting, since although it didn’t look like anything special, it did make it to the recipient’s inbox, instead of the e-mail quarantine where it should have ended up.

The reason for this probably was that the message in question contained what looked like a reply to a previous e-mail exchange. This might have made it appear more trustworthy to the spam/phishing detection mechanisms that were employed to scan it, since – as far as my understanding goes – automated spam/phishing detection mechanisms tend to consider messages with reply-chains to be somewhat more trustworthy than plain, unsolicited e-mails from unknown senders.

It should be mentioned that threat actors commonly use replies to legitimate messages in account takeover/BEC-style phishing attacks, however, in this case, the situation was somewhat different – the original (replied-to) message was from someone not associated with the targeted organization in any way. Use of this approach (i.e., “replying” to a message with no relevance to the recipient) can sometimes be seen in generic phishing, however, if someone receives an e-mail which contains a reply to a message from someone they have never even heard of, it doesn’t exactly make the message appear trustworthy… Which is where the slight twist, which was used in this message, comes in.

In the message, the ”reply” part was hidden from the recipient bellow a long list of empty paragraphs (well, paragraphs containing a non-breaking space). And although this technique is not new, since the aforementioned customer’s IT specialists weren’t aware of it, and a quick Google search failed to provide any write-ups of it, I thought it might be worthwhile to go over it here.

As the following example from my “phishing collection” shows, at first glance, an e-mail messages, in which this technique is used, would look quite normal, and a recipient might not notice anything suspicious (besides the overall “this is an obvious phishing” vibe).

[![](https://isc.sans.edu/diaryimages/images/24-07-16-phishing.png)](https://isc.sans.edu/diaryimages/images/24-07-16-phishing.png)

Only if one noticed that the scrollbar on the right side of the window seems to indicate that there is (literally) much more to the message than it appears to be, would one probably discover the text of the original reply-chain... Which, in this instance, is hidden bellow 119 empty paragraphs.

[![](https://isc.sans.edu/diaryimages/images/24-07-16-reply.png)](https://isc.sans.edu/diaryimages/images/24-07-16-reply.png)

Although the aforementioned technique is hardly the most common (or most dangerous) one when it comes to phishing, since it is being used “in the wild”, a short mention of it might make a good addition to any security awareness training (e.g., something along the lines of “if you see a large scrollbar next to the body of a short e-mail, it is a definite indicator that something is amiss”)…

-----------
Jan Kopriva
[@jk0pr](https://twitter.com/jk0pr) | [LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords: [Phishing](/tag.html?tag=Phishing) [replychain](/tag.html?tag=replychain)

[0 comment(s)](/diary/Replychain%2Bphishing%2Bwith%2Ba%2Btwist/31084/#comments)

* [previous](/diary/31078)
* [next](/diary/31086)

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