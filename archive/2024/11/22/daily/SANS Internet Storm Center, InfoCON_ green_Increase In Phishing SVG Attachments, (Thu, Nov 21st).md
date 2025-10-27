---
title: Increase In Phishing SVG Attachments, (Thu, Nov 21st)
url: https://isc.sans.edu/diary/rss/31456
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-22
fetch_date: 2025-10-06T19:20:01.185416
---

# Increase In Phishing SVG Attachments, (Thu, Nov 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31452)
* [next](/diary/31460)

# [Increase In Phishing SVG Attachments](/forums/diary/Increase%2BIn%2BPhishing%2BSVG%2BAttachments/31456/)

**Published**: 2024-11-21. **Last Updated**: 2024-11-21 03:26:19 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Increase%2BIn%2BPhishing%2BSVG%2BAttachments/31456/#comments)

There is an [increase in SVG](https://www.bleepingcomputer.com/news/security/phishing-emails-increasingly-use-svg-attachments-to-evade-detection/) attachments used in phishing emails ([Scalable Vector Graphics](https://en.wikipedia.org/wiki/SVG), an XML-based vector image format).

I took a look at the some samples mentioned in the [Bleeping Computer article](https://www.bleepingcomputer.com/news/security/phishing-emails-increasingly-use-svg-attachments-to-evade-detection/), and searched more samples on VirusTotal.

These samples contain HTML & JavaScript code to display a blurry Excel PNG image, and a phishing form asking for credentials. Like this one:

![](https://isc.sans.edu/diaryimages/images/20241120-185056.png)

It contains 3 PNG files as [data URIs](https://en.wikipedia.org/wiki/Data_URI_scheme), which can easily be extracted with [base64dump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py):

![](https://isc.sans.edu/diaryimages/images/20241120-191233.png)

You have the blurry Excel PNG:

![](https://isc.sans.edu/diaryimages/images/20241120-191641.png)

An Excel logo:

![](https://isc.sans.edu/diaryimages/images/20241120-191714.png)

And a Microsoft logo:

![](https://isc.sans.edu/diaryimages/images/20241120-191734.png)

I made some small changes to the sample, so that it would display an example.com email address, instead of a real victim's address that I would have to redact. The email address is hardcoded in BASE64 in the SVG file.

Here I made another example, using a SANS email address:

![](https://isc.sans.edu/diaryimages/images/20241120-185139.png)

Do you see a difference, besides the SANS email address?

The SANS logo appears in the form!

![](https://isc.sans.edu/diaryimages/images/20241120-192608.png)

Where did that logo come from, it's not embedded in the SVG file!

That logo is retrieved using a web service: logo[.]clearbit[.com].

As an example, here is the retrieval of the Wikipedia logo:

![](https://isc.sans.edu/diaryimages/images/20241120-185427.png)

Here are the URLs in this SVG file:

![](https://isc.sans.edu/diaryimages/images/20241120-193042.png)

There's JavaScript code inside this SVG file to make a web request and display the appropriate logo (or the embedded Microsoft logo, if the service doesn't provide a logo).

And the last URL you see in this screenshot, is where the form data will be posted (the phished credentials).

That one is the most prevalent in the samples I got from VirusTotal, but there are some other ones:

![](https://isc.sans.edu/diaryimages/images/20241120-193547.png)

And I have one sample with heavily obfuscated JavaScript, without cleartext URLs. I'll keep that one for another diary entry ...

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Increase%2BIn%2BPhishing%2BSVG%2BAttachments/31456/#comments)

* [previous](/diary/31452)
* [next](/diary/31460)

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