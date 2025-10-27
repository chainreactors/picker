---
title: Quickie: Mass BASE64 Decoding, (Fri, Nov 29th)
url: https://isc.sans.edu/diary/rss/31470
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-30
fetch_date: 2025-10-06T19:19:42.512619
---

# Quickie: Mass BASE64 Decoding, (Fri, Nov 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31468)
* [next](/diary/31472)

# [Quickie: Mass BASE64 Decoding](/forums/diary/Quickie%2BMass%2BBASE64%2BDecoding/31470/)

**Published**: 2024-11-29. **Last Updated**: 2024-11-29 05:38:37 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Quickie%2BMass%2BBASE64%2BDecoding/31470/#comments)

I was asked how one can decode a bunch of BASE64 encoded IOCs with my tools.

I'm going to illustrate my method using the phishing SVG samples I found on VirusTotal (see "[Increase In Phishing SVG Attachments](https://isc.sans.edu/diary/Increase%20In%20Phishing%20SVG%20Attachments/31456)").

In these phishing SVG files, the victim's email address is encoded in BASE64:

![](https://isc.sans.edu/diaryimages/images/20241124-133749.png)

With grep, I can select all these lines with BASE64 encoded email addresses:

![](https://isc.sans.edu/diaryimages/images/20241124-130849.png)

Then I can pipe this into [base64dump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py), my tool to handle BASE64 (and other encodings):

![](https://isc.sans.edu/diaryimages/images/20241124-130911.png)

You can see the email address in the "Decoded" column (they are redacted to protect the victims).

To get just this info (decoded email addresses), you can use option -s a to select all decoded items, and option -d to dump the decoded values to stdout, like this:

![](https://isc.sans.edu/diaryimages/images/20241124-130927.png)

The problem now is that all email addresses are concatenated together. To add a newline (or carriage return - newline in Windows) after each email address, use option -s A (uppercase a):

![](https://isc.sans.edu/diaryimages/images/20241124-130943.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Quickie%2BMass%2BBASE64%2BDecoding/31470/#comments)

* [previous](/diary/31468)
* [next](/diary/31472)

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