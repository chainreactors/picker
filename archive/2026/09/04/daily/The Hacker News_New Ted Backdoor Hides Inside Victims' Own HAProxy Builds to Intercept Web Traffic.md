---
title: New Ted Backdoor Hides Inside Victims' Own HAProxy Builds to Intercept Web Traffic
url: https://thehackernews.com/2026/09/new-ted-backdoor-hides-inside-victims.html
source: The Hacker News
date: 2026-09-04
fetch_date: 2026-09-05T06:30:36.148796
---

# New Ted Backdoor Hides Inside Victims' Own HAProxy Builds to Intercept Web Traffic

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

# [New Ted Backdoor Hides Inside Victims' Own HAProxy Builds to Intercept Web Traffic](https://thehackernews.com/2026/09/new-ted-backdoor-hides-inside-victims.html)

**Swati Khandelwal**Sep 04, 2026Malware / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzLyhHupZwRy1pOQzT93Qhs5waZ8gqtlgDJUKgt1f37dz3KqIDDZY8uNo8QguZNccBHivdA_ecnY8cQUyhZQAvLH4APu3imxP-rwo2dYLZtKnJ92IkRPFmwepmJgRk9GrLrJiN_IbInwvNXaW7N5761YfEB1IIK4uDdNBTy6Koz8uXgOSXaQWixXM1Wts/s1700-nu-rw-lo-l85-e365/HAProxy.jpg)

A previously undocumented Linux toolkit has been found compiled directly into the trojanized **HAProxy** load balancers of two South Korean organizations, where it intercepted web traffic and served altered pages to selected visitors.

The attackers named the implant **ted** in debug strings left in the binary. It is not a HAProxy vulnerability, and installing it requires code execution on the host and the ability to replace the running binary.

Rapid7 Labs attributed the toolkit with medium confidence to North Korean state-sponsored actors and put the two victims in South Korea's automotive and media sectors.

Command-and-control (C2) requests never reach a backend server and are erased from HAProxy's own connection counters, so neither the backend logs nor the load balancer's statistics record them.

"Further evidence is necessary to make a more definitive assessment," Rapid7 said.

A request for one specific image path puts the filter into C2 mode, Rapid7 said in [a report published Friday](https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/). The implant decrements HAProxy's live connection counters, thereby dropping the connection from the load balancer's statistics. It writes the command body to a named pipe under /tmp. Zeroing the request channel afterwards leaves nothing to forward, and the command terminates at the load balancer.

Output returns on the raw socket under a standard HTTP/1.0 200 OK header, which is what makes the exchange look like ordinary web traffic.

Through that channel, the operator can beacon, upload and download files, run shell commands, and replace the implant's configuration. Only requests clearing four checks receive a modified page.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The request has to carry a User-Agent and match a rule whose URL and referer patterns both fit. Delivery then falls to either whitelist membership on the client address, checked exactly and again at the /24 level, or an operator key in the Accept-Language header that overrides the address filtering entirely.

The implant rewrites the content type and length on the way out, forces the response status to 200, and deletes the Accept-Ranges header so a client cannot request byte ranges and notice the size change.

Rapid7 said its evidence was not enough to establish a timeline or determine how the attackers first got in.

Its hypothesis that they came in through an exposed Groupware portal, a class of Korean enterprise collaboration software, rests on [the ENKI research it points to](https://www.enki.co.kr/en/media-center/blog/analysis-of-kimsuky-s-attack-on-a-south-korean-groupware-vendor-using-a-new-gomir-family-variant). That report documented Kimsuky compromising a groupware vendor through a mail server flaw.

The stager deploys only where HAProxy or cron is already running, and it verifies root before dropping anything. It overwrites the legitimate crond binary and gives the replacement the creation timestamp of /usr/bin/ssh. It then strips the keywords tmp, wget, cron and crond from root's bash history and from six system logs, among them auth.log and audit/audit.log.

A trojanized sshd in the same toolkit encrypts captured plaintext passwords and writes them to a fixed path.

Rapid7 found the same code in trojanized agetty, atd, and polkitd binaries. A companion remote access trojan (RAT) that Rapid7 calls curlRAT beacons every 12 hours by default and drops to a 30-second interval when the operator sets a flag. It aborts unless it finds a marker file showing the host is virtualized.

curlRAT is distinct from CurlBack RAT, [a separate family of that name](https://thehackernews.com/2025/04/pakistan-linked-hackers-expand-targets.html) attributed to the Pakistan-linked SideCopy group.

Rapid7 shared the following indicators of compromise (IoCs) -

* **Domain** - img.monderhouse[.]space
* **Domain** - img.smartnords[.]site
* **Domain** - img.darklights[.]store
* **Domain** - img.responsive.pstatic[.]autos
* **Domain** - img.socialteams[.]store
* **Domain** - img.worksongo[.]store
* **File** - ~/cache/haproxy-1000.cache
* **File** - /var/lib/sshd/c8c68e629bba773a10ac80012d10bf19
* **File** - /var/lib/snapd/g580
* **File** - /tmp/jasper-log
* **SHA-256** - 72e70936f0dbe459142a1d867617c35f8d0cce5d18c6a49e1090a2a5adc8e558
* **SHA-256** - 4bb923eb040aa13ca8fd409c31ee4729c60ddff32e350efe1c5a4a9168a065f5

The Hacker News confirmed on September 4 that none of the six domains resolves, returning NXDOMAIN, meaning no such name exists, for both A and NS records via Google Public DNS. They are useful for reviewing historical logs rather than for blocking live traffic.

Part of the attribution rests on a listing of those domains under APT37 in maltrail, an open-source detection project. [The maltrail file Rapid7 links](https://github.com/stamparm/maltrail/blob/master/trails/static/malware/apt_37.txt) stopped resolving after [a repository restructure in August](https://github.com/stamparm/maltrail/blob/master/CHANGELOG) moved the project's static trail data elsewhere.

The Hacker News confirmed on September 4 that all six are present at the new location, each labelled as APT37 infrastructure. [maltrail's APT37 source file](https://github.com/stamparm/trails/blob/master/malware/apt_37.txt) credits those entries to two posts on X from July 2025 and c...