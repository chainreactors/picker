---
title: Critical Flaw in Python’s Popular Pillow Image Library Allows Code Execution via a Crafted Image
url: https://thehackernews.com/2026/10/critical-flaw-in-pythons-popular-pillow.html
source: The Hacker News
date: 2026-10-23
fetch_date: 2026-10-24T06:48:22.384542
---

# Critical Flaw in Python’s Popular Pillow Image Library Allows Code Execution via a Crafted Image

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Critical Flaw in Python’s Popular Pillow Image Library Allows Code Execution via a Crafted Image](https://thehackernews.com/2026/10/critical-flaw-in-pythons-popular-pillow.html)

**Swati Khandelwal**Oct 23, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGp9s38cCmrESabSZezAPkJaYoavpBM8Ehckei0ZrhKfBSoSXMyrWkzooakGExz1GBYVgi0izvW8wyKH2CEX7vpzLExRkK7uNW8wDdMzJ_k7NR8u6q-WA9e8Aoc19LNfJbFKgB6GkbAKbXW69_lOdM4sz4t5fmpKsLxHWKJPOugq5g_45Q5_WmCm_vA6U/s1700-nu-rw-lo-l85-e365/python-image.jpg)

**Pillow**, the most widely used image library for Python, can be made to run operating system commands on a server by specifying the name of a file it is told to open.

The flaw, [CVE-2026-112900](https://www.cve.org/CVERecord?id=CVE-2026-112900), is in the way Pillow handles EPS images, which it opens by passing the file's name to **Ghostscript**, a separate program it runs to turn the image into pixels, without checking the name first.

Ghostscript can read a name chosen by an attacker as instructions rather than as a file, and point it to a second file that carries commands to run. Pillow's maintainers fixed it in [version 13.0.0](https://pillow.readthedocs.io/en/stable/releasenotes/13.0.0.html), released on October 16.

Pillow turns up almost everywhere Python handles images: web upload forms, avatar and thumbnail tools, document and PDF pipelines, and most machine-learning projects pull it in. OX Security, the firm whose report drew attention to the flaws, estimates the library is downloaded [about 436 million times a month](https://www.ox.security/blog/three-critical-pillow-cves-rce-and-heap-overflows-in-pythons-imaging-library-cve-2026-112900-cve-2026-112393-cve-2026-112403/).

Version 13.0.0 is a large security release, with fixes across four severity levels, from low to critical, two of which are rated critical by the maintainers. None of the flaws is known to be under attack.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The weakness is the filename, not the picture. "The flaw is triggered by the filename, not by anything in the PostScript document," [the advisory](https://github.com/python-pillow/Pillow/security/advisories/GHSA-w889-685w-c8fh) says, meaning a harmless EPS file can still cause damage when an attacker sets its name. That makes upload endpoints that keep or build a stored file's name from user input the realistic target.

The flaw only reaches Ghostscript on hosts that have the gs program installed, which Pillow needs to open EPS at all. It affects Pillow from version 2.6.0 up to 12.3.0.

The maintainers rate it moderate, because the attacker has to control the filename. The CVE record assigned by GitHub rates it 9.2 out of 10 and marks it as the same condition.

Two of the fixes sit in the maintainers' top "critical" tier. One is a separate memory bug, described in the release notes as stale image data reused after a mode change. The other covers two overflow flaws in Pillow's JPEG decoding.

One of those JPEG flaws, in the [FlashPix (FPX) format](https://github.com/python-pillow/Pillow/security/advisories/GHSA-5x8w-8jj5-q52h), was shown to run an attacker's command from a single call to Image.open() on a crafted file, as long as the optional olefile package is installed. Pillow recognizes these files by their content, not their extension, so a server that opens untrusted uploads can be hit with no user action.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgK4gH2e5N4QBctTdKiUWRZ4ncA0jC3plMfFYVIqjGP6N-SqNtPPctt1ACJ8A4cl8hBRlK5wgAqsJRG4El7Tapm5n9wZXGo4CHGPcSUbBa09oVhdHd9UPRz0r6r-NS0BD9SbgBkm9LpVyyYBGJILIFuZsvWnM_GCJqBAqbnvjjaKGzleTT9YtT-K6_9OQY/s1700-nu-rw-lo-l85-e365/ox.jpg)

The other, CVE-2026-112403, overflows a memory buffer when a program makes a thumbnail of a crafted lossless JPEG. Its [advisory](https://github.com/python-pillow/Pillow/security/advisories/GHSA-8g5g-8vmr-9782) reports a crash, not code execution. The bug was "found by Anthropic using Claude to study the security of open-source software, validated manually by Ada Logics," the advisory says, part of a wider effort by the company that has [turned up hundreds of flaws in open-source libraries](https://thehackernews.com/2026/02/claude-opus-46-finds-500-high-severity.html).

A third flaw, [CVE-2026-112393](https://github.com/python-pillow/Pillow/security/advisories/GHSA-332p-7hrc-92wf), has been in Pillow since 2013. It overflows a memory buffer when a program saves a compressed TIFF image to memory rather than to a file on disk, the common pattern for a service that re-encodes an upload and hands it back. The advisory says the reporters crashed the process with it, and turned it into code execution only with the help of a second, separate flaw that leaked memory addresses. Saving to a real file on disk is not affected.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The CVE records, assigned by GitHub, score the EPS, TIFF, and JPEG-thumbnail flaws 9.2 out of 10, a critical rating. Each depends on conditions the score does not carry, and the maintainers' own ratings for the batch run from moderate to critical. In the CVE records, CISA's analysts mark no known exploitation for the EPS flaw and a public proof of concept for the TIFF one.

### What to do

Upgrade to [Pillow 13.0.0](https://pypi.org/project/pillow/13.0.0/), which fixes all of these, and rebuild any containers, wheels, or base images that bundle an older copy. Pillow 13 drops Python 3.10, so installs still on 3.10 need Python 3.11 or newer as well.

```
pip install -U "Pillow>=13.0.0"
```

Until you can upgrade, [Pillow's security guidance](https://pillow.readthedocs.io/en/stable/handbook/security.html) and the advisories point to steps that cut each path:

* **EPS / Ghostscript:** keep the `gs` program off any host that processes untrusted up...