---
title: Another PDF Streams Example: Extracting JPEGs, (Fri, May 17th)
url: https://isc.sans.edu/diary/rss/30924
source: SANS Internet Storm Center, InfoCON: green
date: 2024-05-18
fetch_date: 2025-10-06T16:52:48.683283
---

# Another PDF Streams Example: Extracting JPEGs, (Fri, May 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30920)
* [next](/diary/30926)

# [Another PDF Streams Example: Extracting JPEGs](/forums/diary/Another%2BPDF%2BStreams%2BExample%2BExtracting%2BJPEGs/30924/)

**Published**: 2024-05-17. **Last Updated**: 2024-05-17 12:04:03 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Another%2BPDF%2BStreams%2BExample%2BExtracting%2BJPEGs/30924/#comments)

In my diary entry "[Analyzing PDF Streams](https://isc.sans.edu/diary/Analyzing%2BPDF%2BStreams/30908)" I showed how to use my tools [file-magic.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/file-magic.py) and [myjson-filter.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/myjson-filter.py) together with my PDF analysis tool [pdf-parser.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/pdf-parser.py) to analyze PDF streams en masse.

In this diary entry, I will show how file-magic.py can augment JSON data produced by pdf-parser.py with file-type information that an then be used by myjson-filter.py to filter out files you are interested in. As an example, I will extract all JPEGs from a PDF document.

First, let's produce statistics with pdf-parser.py's option -a:

![](https://isc.sans.edu/diaryimages/images/20240512-103432.png)

This confirms that there are many "Indirect objects with a stream" in this document.

Next, I let pdf-parser.py produce JSON output (--jsonoutput) with the content of the unfiltered streams, and I let file-magic.py consume this JSON output (--jsoninput) to try to identify the file type of each stream based on its content (since streams don't have a filename, there is no filename extension and we need to look at the content):

![](https://isc.sans.edu/diaryimages/images/20240512-103517.png)

If we use option -t to let file-magic.py just output the file type (and not the file/stream name), we can make statistics with my tool count.py and see that the PDF document contains many JPEG files:

![](https://isc.sans.edu/diaryimages/images/20240512-103553.png)

Now we want to write all of these JPEG images to disk. We use file-magic.py again in JSON mode, but let it also output the same JSON data augmented with file-type information (--jsonoutput):

![](https://isc.sans.edu/diaryimages/images/20240512-103639.png)

Next, this JSON data is consumed by myjson-filter.py and filtered with regular expression (case sensitive) JPEG on the file type: -t JPEG.

![](https://isc.sans.edu/diaryimages/images/20240512-103716.png)

Finally, we write the JPEG images to disk with -W hashext:jpeg: this writes each JPEG stream to disk with a filename consisting of the sha256 of the file's content and extension .jpeg.

![](https://isc.sans.edu/diaryimages/images/20240512-103751.png)

By using the hash of the content as filename, there are no duplicate pictures:

![](https://isc.sans.edu/diaryimages/images/20240512-103815.png)

Should you want to reproduce the commands in these diary entries with the exact same PDF files I used, my old ebook on PDF analysis can be found [here](https://blog.didierstevens.com/2010/09/26/free-malicious-pdf-analysis-e-book/) and the analysis on TLS backdoors done by a colleague can be found [here](https://www.nviso.eu/blog/nviso-analyzes-tls-n-day-backdoors-sparkcockpit-sparktar).

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Another%2BPDF%2BStreams%2BExample%2BExtracting%2BJPEGs/30924/#comments)

* [previous](/diary/30920)
* [next](/diary/30926)

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