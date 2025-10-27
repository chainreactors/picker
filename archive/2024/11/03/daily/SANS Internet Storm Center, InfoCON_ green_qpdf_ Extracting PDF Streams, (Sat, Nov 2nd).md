---
title: qpdf: Extracting PDF Streams, (Sat, Nov 2nd)
url: https://isc.sans.edu/diary/rss/31406
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-03
fetch_date: 2025-10-06T19:18:30.859963
---

# qpdf: Extracting PDF Streams, (Sat, Nov 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31404)
* [next](/diary/31408)

# [qpdf: Extracting PDF Streams](/forums/diary/qpdf%2BExtracting%2BPDF%2BStreams/31406/)

**Published**: 2024-11-02. **Last Updated**: 2024-11-02 13:08:21 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/qpdf%2BExtracting%2BPDF%2BStreams/31406/#comments)

In diary entry "[Analyzing PDF Streams](https://isc.sans.edu/diary/Analyzing%2BPDF%2BStreams/30908)" I answer a question asked by a student of Xavier: "how can you export all streams of a PDF?". I explained how to do this with my [pdf-parser.py](https://blog.didierstevens.com/programs/pdf-tools/) tool.

I recently found another method, using the open-source tool [qpdf](https://github.com/qpdf/qpdf). Since version 11, you can extract streams with qpdf.

If you want the contents of the streams inside a single JSON object (BASE64 encoded), use this command:

> qpdf.exe --json --json-stream-data=inline exampl.pdf

And if you want the contents of the streams in separate files (filename prefix "stream"), use this command:

> qpdf.exe --json --json-stream-data=file --json-stream-prefix=stream exampl.pdf

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/qpdf%2BExtracting%2BPDF%2BStreams/31406/#comments)

* [previous](/diary/31404)
* [next](/diary/31408)

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