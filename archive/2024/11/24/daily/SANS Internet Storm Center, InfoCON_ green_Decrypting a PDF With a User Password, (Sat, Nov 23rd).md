---
title: Decrypting a PDF With a User Password, (Sat, Nov 23rd)
url: https://isc.sans.edu/diary/rss/31466
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-24
fetch_date: 2025-10-06T19:16:25.282309
---

# Decrypting a PDF With a User Password, (Sat, Nov 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31464)
* [next](/diary/31468)

# [Decrypting a PDF With a User Password](/forums/diary/Decrypting%2Ba%2BPDF%2BWith%2Ba%2BUser%2BPassword/31466/)

**Published**: 2024-11-23. **Last Updated**: 2024-11-23 17:06:46 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Decrypting%2Ba%2BPDF%2BWith%2Ba%2BUser%2BPassword/31466/#comments)

In diary entry "[Analyzing an Encrypted Phishing PDF](https://isc.sans.edu/diary/Analyzing%2Ban%2BEncrypted%2BPhishing%2BPDF/31404)", I decrypted a phishing PDF document. Because the PDF was encrypted for DRM (owner password), I didn't have to provide a password.

What happens if you try this with a PDF encrypted for confidentiality (user password), where a password is needed to open the document?

The PDF is encrypted, according to [pdfid.py](https://blog.didierstevens.com/programs/pdf-tools/):

![](https://isc.sans.edu/diaryimages/images/20241123-174151.png)

[qpdf](https://github.com/qpdf/qpdf) --show--encryption tells us that we supplied an incorrect password:

![](https://isc.sans.edu/diaryimages/images/20241123-173902.png)

We did not provide a password to qpdf: this means that the user password is set (not empty), and that we have to provide it to be able to decrypt the document. We can verify the password as follows (if you don't know the password, you can try to [crack it](https://blog.didierstevens.com/2017/12/29/cracking-encrypted-pdfs-conclusion/)):

![](https://isc.sans.edu/diaryimages/images/20241123-174009.png)

And then decrypt the PDF like this:

![](https://isc.sans.edu/diaryimages/images/20241123-174054.png)

And you can verify with pdfid.py that the PDF is no longer encrypted, and suitable for further analysis:

![](https://isc.sans.edu/diaryimages/images/20241123-174130.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Decrypting%2Ba%2BPDF%2BWith%2Ba%2BUser%2BPassword/31466/#comments)

* [previous](/diary/31464)
* [next](/diary/31468)

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