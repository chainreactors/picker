---
title: Phishing e-mail that hides malicious link from Outlook users, (Wed, Jun 4th)
url: https://isc.sans.edu/diary/rss/32010
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-05
fetch_date: 2025-10-06T22:56:02.637887
---

# Phishing e-mail that hides malicious link from Outlook users, (Wed, Jun 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32006)
* [next](/diary/32014)

# [Phishing e-mail that hides malicious link from Outlook users](/forums/diary/Phishing%2Bemail%2Bthat%2Bhides%2Bmalicious%2Blink%2Bfrom%2BOutlook%2Busers/32010/)

**Published**: 2025-06-04. **Last Updated**: 2025-06-04 09:23:19 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[1 comment(s)](/diary/Phishing%2Bemail%2Bthat%2Bhides%2Bmalicious%2Blink%2Bfrom%2BOutlook%2Busers/32010/#comments)

I recently came across an interesting phishing e-mail. At first glance, it looked like a “normal” phishing that tried to pass itself off as a message from one of the Czech banks asking account holders to update their information…

[![](https://isc.sans.edu/diaryimages/images/25-06-04-phishing.png)](https://isc.sans.edu/diaryimages/images/25-06-04-phishing.png)

Nevertheless, when I hovered above the rectangle that a recipient was expected to click on, I was surprised to see that the link in the pop-up actually pointed to the legitimate domain of the bank.

[![](https://isc.sans.edu/diaryimages/images/25-06-04-link.png)](https://isc.sans.edu/diaryimages/images/25-06-04-link.png)

My first thought was that threat actors behind the phishing made a mistake. My assumption was that they used a real e-mail from the bank as a baseline that they wanted to modify to create a message that would point recipients to a malicious site, and mistakenly sent it out before it was finished – strange as it may sound, it wouldn’t have been nowhere near the first case of something like that I’ve seen.

Nevertheless, once I looked at the HTML code of the message, it quickly emerged that I was wrong. The threat actors actually used a technique which changes displayed content based on a “browser” it is opened in. The technique in question leverages HTML conditional statements *<!--[if mso]>* and *<!--[if !mso]>* that specify content that should be displayed if a  message/HTML page is opened in Outlook or in any other reader/browser.

Using it, threat actors behind the message caused the link shown/pointed to in Outlook to a benign one, while making it point to a – presumably – credential stealing website in any other e-mail client/browser…

```

<!--[if mso]>
    ...
    <a href=[benign link] >
    ...
<![endif]--><!--[if !mso]><!-->
    ...
    <a href=[malicious link] >
    ...
<!--<![endif]-->
```

In this case, threat actors likely used this technique with the intention of hiding the malicious link in corporate environments, where Outlook is commonly used (alongside security mechanisms that scan web traffic, DNS requests, etc.) and where users would probably be less likely to click, since an e-mail from a bank sent to their work e-mail, instead of a private one, would probably be a red flag on its own, while ensuring that recipients who opened the e-mail in a non-Outlook client would still be directed to the malicious website.

While this approach isn’t new – in fact, it has been documented since at least 2019[[1](https://www.libraesva.com/outlook-comments-abused-to-deliver-malware/)] – its use in the wild is not too common… And since it is therefore among the lesser-known phishing techniques I believe it is worthy of at least this short reminder of its existence.

[1] <https://www.libraesva.com/outlook-comments-abused-to-deliver-malware/>

-----------
Jan Kopriva
[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords:

[1 comment(s)](/diary/Phishing%2Bemail%2Bthat%2Bhides%2Bmalicious%2Blink%2Bfrom%2BOutlook%2Busers/32010/#comments)

* [previous](/diary/32006)
* [next](/diary/32014)

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