---
title: PDF Object Streams, (Mon, Nov 11th)
url: https://isc.sans.edu/diary/rss/31430
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-12
fetch_date: 2025-10-06T19:21:24.535640
---

# PDF Object Streams, (Mon, Nov 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31428)
* [next](/diary/31438)

# [PDF Object Streams](/forums/diary/PDF%2BObject%2BStreams/31430/)

**Published**: 2024-11-11. **Last Updated**: 2024-11-11 08:21:35 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/PDF%2BObject%2BStreams/31430/#comments)

The first thing to do, when analyzing a potentially malicious PDF, is to look for the /Encrypt name as explained in diary entry [Analyzing an Encrypted Phishing PDF](https://isc.sans.edu/diary/Analyzing%2Ban%2BEncrypted%2BPhishing%2BPDF/31404).

The second thing to do, is to look for the /ObjStm name, as I will explain in this diary entry.

Take this [phishing PDF](https://www.virustotal.com/gui/file/bf5946578933837cd7827cd657c00d80a7951cc223778c43ae96c709c304ff77) and analyze it with [pdfid.py](https://blog.didierstevens.com/programs/pdf-tools/), like this:

![](https://isc.sans.edu/diaryimages/images/20241111-085541.png)

The presence of name /ObjStm tells us that there are Object Streams inside the PDF: an Object Stream is an object with a stream, that contains other objects (without stream). Since streams are usually compressed, pdfid.py is not able to find the keywords of the objects inside the Object Stream (since pdfid is a kind of string search tool that doesn't parse the structure of PDF documents). You need to use pdf-parser.py in stead.

Use option -a to let pdf-parser.py produce statistics and option -O to parse Object Streams. Like this:

![](https://isc.sans.edu/diaryimages/images/20241111-091032.png)

At the end of the statistics report, you will see the search keywords report, reporting names similar to pdfid.py's names report.

But here, you also get the index of the objects with these names, not just a counter like pdfid.py does. So there is 1 /URI name, and it is in object 6.

Next we take a look at object 6 with pdf-parser.py:

![](https://isc.sans.edu/diaryimages/images/20241111-091424.png)

And that reveals the phishing URL.

Another method to find URIs is to use the keyword option (-k), like this:

![](https://isc.sans.edu/diaryimages/images/20241111-091601.png)

To summarize: first look for /Encrypt, then /ObjStm, and then start your analysis.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/PDF%2BObject%2BStreams/31430/#comments)

* [previous](/diary/31428)
* [next](/diary/31438)

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