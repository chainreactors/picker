---
title: Zoom Annotation Flaws Could Let a Meeting Participant Hijack Another Attendee's Client
url: https://thehackernews.com/2026/08/zoom-annotation-flaws-could-let-meeting.html
source: The Hacker News
date: 2026-08-11
fetch_date: 2026-08-12T04:02:49.012959
---

# Zoom Annotation Flaws Could Let a Meeting Participant Hijack Another Attendee's Client

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

![cybersecurity](data:image/svg+xml;base64...)

# [Zoom Annotation Flaws Could Let a Meeting Participant Hijack Another Attendee's Client](https://thehackernews.com/2026/08/zoom-annotation-flaws-could-let-meeting.html)

**Swati Khandelwal**Aug 11, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIX-dcsP7VVws3iI-g-myaz7Wyt8fgrlR9U3CtweEsSriOayyy8r9uyB_1mVcMhSBPyulDXj47SOLsWhl7XQjgMpLYGSjF79fiMTw7zEVOAceKqtAlHCVAMs38paehT0bmDN1zdAyMjHgvdUfYzqRCGEU1StMPyrYW5xIkJzG6DIHh9R9gemNCus_Mwlc/s1700-e365/zoomsday.jpg)

Anyone sharing their screen on a Zoom call could have taken over the computers of everyone watching, and anyone watching could have taken over the presenter's.

The flaw sat in the annotation tool, the feature that lets participants draw and type on a shared screen, and it asked nothing of the victim beyond being in the meeting. No click, no download, no prompt, and nothing on screen to show it had happened.

The patches are not new. Client fixes shipped in June and July, roughly two months before the flaws were made public, and no exploitation has been reported as of publication. None of the three identifiers appear in CISA's Known Exploited Vulnerabilities catalog.

The versions that close them:

* Zoom Workplace, all supported platforms, before 7.1.5 and 7.0.6 in their respective branches
* Zoom Workplace VDI Client for Windows, before 7.0.11 and 6.6.16
* Zoom Rooms and Zoom Meeting SDK, all platforms, before 7.1.0, and before 7.1.5 for the third flaw

The research came from "**A Security**," an Israeli-founded offensive-security startup that left stealth in June with $37 million in funding. It says it went from finding the flaw to a working exploit in under a day, using fewer than 20 prompts on publicly available AI models.

Nobody outside the company can check that claim: the writeup names no model. The vendor also rates the bugs lower than the firm does, and credits one of the three to its own internal team.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Zoom has published no technical detail, so the internals come from [the firm's own reverse engineering](https://a.security/blog/asecurity-zoomsday). A drawing does not cross the network as a picture. The client turns it into a structured object and sends it as a run of counts followed by data, and the receiver trusts those counts to decide how much to read.

One of them fills a fixed 128-byte buffer with no check that the data fits, and because it is the object's last field, an oversized count runs past the end and over the return address.

What makes one malformed drawing reach the whole room is a missing check on where a message came from. Every viewer holds a channel to whoever is sharing, and the sharer holds one back that is meant to carry acknowledgements.

On the paths the researchers traced, the dispatcher reads a message's type number off the wire and hands it to the matching parser without asking which seat the sender occupied. 0x10001 means here is an object; 0x10002 means I received yours. Send the first where the second belongs, and the victim's client rebuilds the object in full.

Zoom tracks the flaws as CVE-2026-53413 (CVSS score: 8.3), a buffer over-write, and CVE-2026-53414 (CVSS score: 6.5), a buffer over-read, both covered by [ZSB-26015](https://www.zoom.com/en/trust/security-bulletin/zsb-26015/) and [ZSB-26016](https://www.zoom.com/en/trust/security-bulletin/zsb-26016/), plus CVE-2026-53415 (CVSS score: 8.3), a use-after-free, in [ZSB-26017](https://www.zoom.com/en/trust/security-bulletin/zsb-26017/).

The firm puts all three at 9.0 under CVSS 4.0, a score that appears in none of the bulletins. Zoom issues its own CVE records, and [NIST no longer routinely re-scores them](https://thehackernews.com/2026/04/nist-limits-cve-enrichment-after-263.html), so the lower figures will likely stand. All three vendor vectors also mark user interaction as required, which sits badly beside the zero-click framing.

The two accounts diverge furthest on the over-read. The firm says it recovered uninitialized heap memory from a victim's client holding live code and vtable pointers, the material an address-randomization bypass needs.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The advisory says the same bug may let a participant "conduct a denial of service," and scores its confidentiality impact at none. Credit splits as well: two bulletins name Idan Levcovich of **A Security**, while the one covering the use-after-free credits Zoom Offensive Security, the in-house team behind the 9.8-rated account takeover flaw [the company patched in July](https://thehackernews.com/2026/07/zoom-patches-critical-windows-flaw-that.html).

The startup's post lists all three as its own, while acknowledging that Zoom already knew about the third and had filtered it server-side before the report arrived. Its account of the AI work is also messier than its own summary.

The first pass, an automated ranking of functions reachable from the Java layer, produced a queue of 3,762 functions across 70 libraries and missed the vulnerable library completely, ranking it 45th. It surfaced only when they traced the running client through a live call, feature by feature. Levcovich writes that the barrier to building this class of exploit "has collapsed, and it will not come back."

The disclosure follows OpenAI [splitting its Daybreak program](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/) a day earlier and releasing [GPT-5.6-Cyber](https://thehackernews.com/2026/08/openai-launches-gpt-56-cyber-with.html) to vetted partners only, on the argument that this capability needs gating. The startup says it got its result from models anyone can use. By OpenAI's own measure, its guardrailed public model answers 1.5% of advanced offensive-security prompts, against 95% for the restricted one.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#li...