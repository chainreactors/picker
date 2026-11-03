---
title: Google Disrupts 1.3 Million-Device Android Botnet, Says TV Box Maker Sold Criminal Access
url: https://thehackernews.com/2026/11/google-disrupts-13-million-device.html
source: The Hacker News
date: 2026-11-02
fetch_date: 2026-11-03T08:51:44.847443
---

# Google Disrupts 1.3 Million-Device Android Botnet, Says TV Box Maker Sold Criminal Access

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Google Disrupts 1.3 Million-Device Android Botnet, Says TV Box Maker Sold Criminal Access](https://thehackernews.com/2026/11/google-disrupts-13-million-device.html)

**Swati Khandelwal**Nov 02, 2026Botnet / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkbU6vLZjF0nlz7vqN6UVf3kN1IcdUfIpAmVWlh2II4gGbMMmSuiE1S8HLzP4JV-ImeCa64hU-cEaa-yGXWqUO_XHOurKtEw61DFvjGOJhM7gHpRPpegBcCFYrXkd59wGX-PoV6zm7z7uq6PpXjc4GLhDRzcinR5IIjcOVZEVl8FMQ0v0Dt3CV9sRxZNk/s1700-nu-rw-lo-l85-e365/android-tv-botnet.jpg)

A botnet of more than 1.3 million Android devices, mostly TV set-top boxes, lost control of its servers in late October in a takedown led by Google.

Google [says](https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet/) it is highly confident that device maker **Videostrong** intentionally put a backdoor in the boxes and sold access to criminals.

They used the boxes for ad fraud and to pass other people's internet traffic through owners' home connections. The backdoor is still on the boxes, and owners cannot remove it themselves.

Videostrong, based in Shenzhen, China, makes Android TV boxes and other devices under its own name and for other brands. The backdoor, called x.cpe, was built into many device models and brands over several years. Google does not believe a rogue insider or a mistake was to blame.

Google used legal action to take down the domains and servers that controlled the botnet. It also took down the control domains of more than a dozen malware families loaded through the backdoor. Japan's National Police Agency, Lumen, HUMAN Security, Plume, Synthient and TrendAI worked with Google on the operation.

Because the criminals behind that malware also spread it in other ways, Google expects the action to cut off their access to at least 10 million more infected devices. It warns that backdoor operators and the criminals who buy from them quickly switch to new tools when one part of their setup is disrupted.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Google has cut ties with Videostrong. It banned the company, and any future subsidiaries or affiliates, from building or selling certified Android devices and from supplying software to other certified device makers.

### What the Backdoor Did

The x.cpe backdoor runs as a system app inside the firmware, with system-level access, according to Google's analysis. It reports to the botnet's command-and-control (C2) servers and waits for orders. To install software silently, it first turns off the app checks in Google Play Protect, Android's built-in security feature.

Through the backdoor, the botnet's operators could install apps without the owner knowing, run commands, capture the screen and map the network the box sits on.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaYgAoeSj4eCCZeGMBh02O0O5MaXLNWnGRJ9ZNBCJh-e0l2FncVv3wQjPyEDprRyHenu7fDl2TuVJtNYBN3ixn7_NjfWvy92osmsmG0K-dnBIH_Ce61h0-TdIzM90VEn9bVHWupetq7T4mkaAvnkUG0Tiljb3pZlInRbWjz2vSdNJpb2CVO6N60bbSSl0/s1700-nu-rw-lo-l85-e365/tv.png)

Google says it saw Videostrong's operators use some of these powers. They took live screenshots, sent keystrokes, copied out account details, device information, app lists and system logs, and opened reverse shells, which give a remote command line into the box.

Most of the criminals' modules, the add-on programs loaded through the backdoor, turned the boxes into residential proxies or sold their spare bandwidth. A residential proxy service sells access to a home internet connection, so a customer's traffic appears to come from an ordinary household. Other modules faked views of online ads.

Most infected devices are Android TV set-top boxes, but the backdoor also turned up on telehealth devices, karaoke machines and digital signage.

[TrendAI](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/trendaitm-research-helps-disrupt-android-tv-botnet-of-more-than-13-million-pre-infected-devices), Trend Micro's enterprise business unit, counted 1,472,554 infected devices across 206 models between June 3 and October 1, and says the real number is at least that high. Malaysia, Brazil, Iraq, Mexico and Taiwan had the most. The U.S., Germany, the U.K., Australia and Canada each had about 26,000 to 42,000.

### What Owners Can Do

[Synthient](https://synthient.com/blog/the-internals-of-a-badbox-operation), which tracks proxy networks and botnets, has published [a list of 182 device model names](https://github.com/synthient/public-research/blob/main/2026/11/Videostrong/README.md) seen in the campaign. The list warns that a model name alone does not confirm that a box is infected.

Synthient's report focuses on MECOOL-branded boxes, which it links to Videostrong. It bought a MECOOL KM9PRO Max and found the backdoor preinstalled. [Plume](https://www.plume.com/xcpe-botnet-whitepaper-pdf), which makes Wi-Fi software for internet providers, found more than a dozen different devices using the botnet's control server, most of them from MECOOL.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNeznatXrzd68j-HfyPH00S_xs88E0m7TabGvyVy804L16ry3x-KrNfWLYnjxsKFKKutI2ZjWjsdH_VNlp6DELO4cdN3cU31nF-ZHM2CAzoNoKoD7pArdBzjq20p0hEbn3CVFzikShbN6Yfblskx91kbZLoDzdNs-pEQYbqcGKDlcY8L3krKGgVNQGckA/s1700-nu-rw-lo-l85-e365/map.jpg)

Because x.cpe is part of the firmware, removing it does not stick. It reinstalls itself when the box restarts. TrendAI says the backdoor runs as a system app signed with the maker's key, so cleanup needs "vendor action, platform protection or replacement of the device."

Plume recommends a full factory reset, because the modules may have installed more backdoors, but it does not say whether a reset removes x.cpe itself. Synthient goes further, telling consumers to throw the boxes away for good because they pose a high risk...