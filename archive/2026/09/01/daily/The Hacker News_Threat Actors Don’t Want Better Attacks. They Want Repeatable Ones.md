---
title: Threat Actors Don’t Want Better Attacks. They Want Repeatable Ones
url: https://thehackernews.com/2026/09/threat-actors-dont-want-better-attacks.html
source: The Hacker News
date: 2026-09-01
fetch_date: 2026-09-02T06:41:52.756810
---

# Threat Actors Don’t Want Better Attacks. They Want Repeatable Ones

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Threat Actors Don’t Want Better Attacks. They Want Repeatable Ones](https://thehackernews.com/2026/09/threat-actors-dont-want-better-attacks.html)

**The Hacker News**Sep 01, 2026Social Engineering / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXRNAAGu1amxjm97oXzRGvVBD23d-thmuPvBbQm10hKlACH58ndu51swo4ggT2P2FJw1vbmWy6qdMZSyTRrgAXoi19O0Zf0vCcS47oMuhMuPSyKc1kL7bpIySVrQwgrIaYJkc4IiavU0rucYYMYWHwXgDCmsPLanV2LZv3mt__srP93r0vLWSz8Vp_L0o/s1700-nu-rw-lo-l85-e365/click.jpg)

The most common way into a company last year was to ask.

A web page tells the visitor to prove they are not a robot. While they read the instructions, it quietly places a command on their clipboard. Then it talks them through opening a terminal and pasting it in. The technique is called ClickFix, and it was [the most common initial access method Microsoft’s team observed last year](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025), accounting for 47% of the attacks in their notifications. Nothing arrives as an attachment, so there is nothing to scan. No vulnerability is used, so there is nothing to patch.

What happens next is just as ordinary. When Bitdefender [analyzed 700,000 security incidents](https://www.bitdefender.com/en-us/blog/businessinsights/700000-security-incidents-analyzed-living-off-land-tactics?cid=ref%7Cb%7C-CORE-EPP-PHASR-THN-AR), 84% of the high-severity ones involved binaries that were already on the machine - the same administrative tools your IT team uses every day. Nothing malicious was installed, because nothing malicious was needed.

Neither technique is clever, but both are winning. And the reason is not that attackers have run out of ideas. It is that they are not looking for ideas. They are looking for something that works the same way at the next company, and the one after that.

## This is a business, and businesses standardize

A criminal group that has to invent something new for every victim does not scale. One that has a procedure - a formula it can run against a list of targets, with predictable steps and a predictable result - can grow as fast as it can find targets.

You can watch that preference in the data. Verizon’s most recent [Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/dbir/) makes the exploitation of vulnerabilities “the most prominent initial access vector in our dataset this year, reaching the height of 31%, up from 20% last year” - a 55% increase in a single year, in the one category that rewards scanning over skill.

Edge devices are not popular because they are interesting. They are popular because the procedure is short enough to write on a card.

Watch for new CVEs in internet-facing devices. Filter for the ones that give remote code execution and require no authentication - the easy ones. Then wait. Someone will publish a working proof of concept on GitHub, usually within days. When they do, scan the internet at scale and take whatever has not been patched yet.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNQT5lQH7byx-3bI6m_IBYoxSCy5j09XzWSBg9C1HFQseRSM01bI5JqQ0Ns8sFhft25T5G1nyQtUnQc73bYr-ytpQL4MRa5Y5JZklYUxCzdkOBMc_OQXLxwKUrDNQSodS2fkpIAZi8ldnugNXCVrUez6dBheBvkxTCz8LOqlECPFUx8H68qul1KLj1188/s1700-nu-rw-lo-l85-e365/1.jpg)

Notice what is absent from that procedure. Nobody in that chain develops anything. The exploit arrives free, from a researcher, on a public repository, on a schedule somebody else sets. The only capability required is the ability to run other people’s code quickly and at volume. Exposure becomes the selection criterion, and who the victim turns out to be stops mattering very much.

There is a version of this in the legitimate economy. A generics manufacturer does not discover drugs. It waits for someone else’s research to become public, then produces a known formula at volume, competing on cost and speed to market rather than on invention. That is what this is. Not a research operation - a generics business, where the patent expires the day the proof of concept lands on GitHub.

You can also see the preference in who wins. For more than a year, the top position on the ransomware leak-site rankings belonged to Qilin, which claimed roughly 1,600 victims across that span, usually more than a hundred a month. In June it was displaced by The Gentlemen, with 121 claimed victims against Qilin’s 80. These are figures the groups publish about themselves, so they are claims rather than audited numbers - but the two have been trading the top position, and what they are competing on is throughput. The leaderboard counts victims, it does not count technical achievement.

The more telling detail is where the challenger came from. The Gentlemen branched out from a former Qilin affiliate, and as Bitdefender’s own [threat debrief](https://www.bitdefender.com/en-us/blog/businessinsights/bitdefender-threat-debrief-july-2026?cid=ref%7Cb%7C-CORE-EPP-PHASR-THN-AR) put it, they have demonstrated how successful ransomware “playbooks” are being recycled and improved. The procedure walked out of one organization and into another and worked just as well in new hands.

That is the clearest available statement of what these groups actually own. Not an exploit, not a tool, not a secret. A method that can be written down, handed over, and run again.

## ClickFix is a playbook for getting in

Look at ClickFix through that lens and its appeal is obvious.

There is no payload to rebuild when a detection lands, because there is no payload. There is no exploit to re-develop when a vendor ships a patch, because no vulnerability is being used. When a lure stops working, you rewrite the text on a web page. The technique degrades gracefully, which is exactly what you want from something you intend to run thousands of times.

It also works identically everywhere, because i...