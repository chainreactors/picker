---
title: Unpatched Broadcom Wi-Fi Flaw Lets Attackers in Range Run Code as Root on Routers
url: https://thehackernews.com/2026/10/unpatched-broadcom-wi-fi-flaw-lets.html
source: The Hacker News
date: 2026-10-19
fetch_date: 2026-10-20T06:53:58.903177
---

# Unpatched Broadcom Wi-Fi Flaw Lets Attackers in Range Run Code as Root on Routers

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Unpatched Broadcom Wi-Fi Flaw Lets Attackers in Range Run Code as Root on Routers](https://thehackernews.com/2026/10/unpatched-broadcom-wi-fi-flaw-lets.html)

**Swati Khandelwal**Oct 19, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKR22_EY_V4kc68OQN7vGigoOrsBiy_aMnJVifzUg15itznrR-KdvcSdcaVSGnA6A2kAgMCSUNbIoqzh10gy8wQzkpK55LJPTjPPoV73VzoJlNCtZOn0LltkE7gq8PwH29hLNlUn41qQV8A7fTGkCwHu2LQ0OtvvTFtNRHll7xY0_PUfQ5K08JtCWriXg/s1700-nu-rw-lo-l85-e365/wifi.gif)

A flaw in Broadcom's Wi-Fi setup software lets an attacker within radio range run code as root on Broadcom-based routers, without the network password or any pairing step, security researcher Quentin Kaiser [disclosed](https://quentinkaiser.be/security/2026/10/16/one-parser-two-bugs/) on October 16.

He showed the attack working against home gateways supplied by three Belgian internet providers, in one case reading the Wi-Fi password off the device and in another opening a remote shell over the air. No CVE has been assigned to the flaw, and no fix has been deployed to the affected routers, Kaiser says.

The flaw is in Broadcom's version of Wi-Fi Protected Setup (WPS), the feature that lets a device join a Wi-Fi network without the password being typed in. Broadcom's code mishandles the reassembly of fragmented WPS setup messages, so an attacker in range can send crafted messages that corrupt the router's memory. From there, Kaiser built two things: a way to read memory back off the device, and a way to run his own code on it.

Against an Orange Belgium gateway, the Askey TCG3000 read the Wi-Fi password (the PSK) from the router's stored settings, sent it back over the air, and then joined the network with it.

Against a Proximus gateway, the Sagemcom-built BBOX3V+, the exploit opened a reverse shell, a remote command line, carried over Wi-Fi frames, so no outside server was needed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

Both ran without any login, and the attack works at a distance, not only up close, Kaiser says. He reports no real-world attacks using the flaw. The working exploits are his own.

### What's Affected

Broadcom's WPS code is embedded in routers and access points from dozens of vendors, and Kaiser estimates that millions of devices worldwide are affected.

The vulnerable chips fall into two families: older eCos-based models (the BCM3380, BCM3383 and BCM33834), where he found no usable fix and calls the bug a permanent "forever day," meaning a flaw that will never be patched on those devices, and newer Linux-based models (the BCM3390, BCM65xx and BCM68xx), which could be fixed if their makers switch Wi-Fi software.

In Belgium, Kaiser found the flaw present and exploitable on gateways from three of the four big providers: Proximus, Orange Belgium and VOO. A fourth, Telenet, may be affected too, but he could not test one.

A wider list he published, ranging from Cisco small-business access points to Huawei and ARRIS routers, mixes confirmed and unconfirmed entries, and some rest on an automated check that only flags a device as "likely vulnerable."

The Belgian per-provider counts, he says, run into the hundreds of thousands of gateways, but are rough estimates.

### Why There's No Patch, and No CVE

The flaw is old. Kaiser traces the code back to at least 2010 and says Broadcom shipped an incomplete fix in 2018, then told customers to switch to a different Wi-Fi software package, called hostapd, rather than relying on the fix. On the older eCos chips, he says, no working fix was ever shipped, which is why he calls it a forever day.

No CVE, the tracking identifier that lets defenders and vendors follow a flaw, has been assigned to it. Kaiser says Broadcom told him it has known about the bug since 2018 and had heard about it from others, but would not register a CVE or say anything publicly, which he believes is why so many device makers never patched.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

When he took the case to the CERT Coordination Center, it was closed the same day, because Broadcom itself holds the authority to assign CVEs for its products and would not do so. The Hacker News found no CVE for the flaw as of October 19.

### What Defenders Can Do

There is no patch to install, and no setting Kaiser points to that blocks the attack over the air. What he provides instead is a way to find affected gear: [YARA rules](https://github.com/qkaiser/broadcom-wps) that spot the vulnerable code in extracted firmware, and a script that listens to a live access point and reports whether it looks vulnerable.

Both are triage aids, he notes: a patched device can still match the rules, so a hit is a reason to check further, not a confirmed finding. For gear that will never be fixed, replacement is the practical option.

Kaiser frames the bug as well suited to attackers who reach a target over nearby Wi-Fi rather than the internet, a technique Russian state hackers [have used](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/) to breach networks from across the street.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_...