---
title: TeamViewer Flaw Lets Remote Computers Attack Users Who Connect to Control Them
url: https://thehackernews.com/2026/10/teamviewer-flaw-lets-remote-computers.html
source: The Hacker News
date: 2026-10-30
fetch_date: 2026-10-31T07:49:06.550740
---

# TeamViewer Flaw Lets Remote Computers Attack Users Who Connect to Control Them

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

# [TeamViewer Flaw Lets Remote Computers Attack Users Who Connect to Control Them](https://thehackernews.com/2026/10/teamviewer-flaw-lets-remote-computers.html)

**Swati Khandelwal**Oct 30, 2026Vulnerability / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEge-ZayNgwlu4fhpD2BSyGgkMYehkV0atRJINisISPLpiubkgyXopa4NWVnxOZs9gi-DEYTNEQ5G2pu-X5iSHyMp8pguzp-Q6g-1-mGwcy3so4AkeuYFuYoaotOcmF5A-2oVDvnxd0B_FaZ7JJt8W3zrNFot6kBlJp7WffHkb7m92C9bNQnwFLwnNgXpDk/s1700-nu-rw-lo-l85-e365/teamviewer-flaw.jpg)

TeamViewer has fixed a flaw that lets the machine being controlled in a remote session attack the computer that connected to control it. In a TeamViewer session, the computer that connects and takes control is the viewer, and the machine it controls is the host.

A malicious or compromised host can exploit the flaw to crash the viewer's TeamViewer and, depending on the platform, may also run code on the viewer's computer. This works only after the user starts a remote-control session to that host. The fix is in TeamViewer version 15.83.

The flaw is tracked as [CVE-2026-111585](https://www.cve.org/CVERecord?id=CVE-2026-111585) and scored 8.8 out of 10, in the high range. It affects the TeamViewer Full Client on Windows, Linux, and macOS, the Windows Portable edition, and the Android Remote Control app, in all versions before 15.83.

For this flaw, TeamViewer's [bulletin](https://www.teamviewer.com/en/resources/trust-center/security-bulletins/tv-2026-1011/) lists the Full Client, Portable, and Android app, but not the Host. The same 15.83 update fixes two other flaws in that bulletin that do affect the Host, so people running the Host should update as well.

Omri Dar, a researcher at security firm Remedio, published a [technical account](https://remedio.io/research/vulnerability-disclosures/remote-code-execution-in-teamviewer/) of the flaw on October 29. In this bug, he wrote, *"the attacker is the host and the victim is the viewer."*

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

In a remote session, the host tells the viewer how large its screen image is. The viewer uses that size to set aside memory, but the calculation can overflow and reserve too little. Screen data that arrives afterward is then written past the end of that space.

At a minimum, this crashes the viewer's TeamViewer session, and the host can trigger the crash again whenever they want.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXcHFAQ5DpoADCIGU3FMHcSJzNSDbam0DMfLBkavUWIdVqandjD6CmQCEreboyBU8azpt8wzTscvi553d4hKy4y_ZgIZh9d7VEg5u8tDVG_6v6Tr7YbkEfYuWYSDqeDO3daGc81dxSoVTFkAig8tjGEwct3qwAlYBo3T8nD0h-K4IpLFqkpiw2nm73tdA/s1700-nu-rw-lo-l85-e365/team.gif)

On Windows, Remedio says it took the bug further, bypassing the operating system's built-in exploit defenses and running code of its choosing in the viewer. The demonstration used a stand-in on the host to supply part of the attack data, so it is not yet an attack carried out entirely over the network.

That result was shown only on Windows. Whether the same works on macOS, Linux, or Android is not covered in the write-up. TeamViewer only says that code execution is possible, depending on the platform.

The attack needs no password and no extra click beyond accepting the session, and it works in TeamViewer's default setup, Dar wrote. The flaw affects all versions before 15.83, including 15.82, the security update TeamViewer [released in September](https://www.teamviewer.com/en/resources/trust-center/security-bulletins/tv-2026-1010/). Updating last month did not remove it.

### What to Do

The only fix TeamViewer offers is to update, and it lists no workaround. Current users should move to 15.83 or later. The fixed builds for older supported branches are in the table above.

The same 15.83 update also fixes two other high-severity flaws in the same bulletin, including a separate code-execution flaw affecting Linux and macOS. A [companion bulletin](https://www.teamviewer.com/en/resources/trust-center/security-bulletins/tv-2026-1012/) the same day, TV-2026-1012, fixes six more flaws in TeamViewer's Remote Management add-ons, delivered by automatic update.

TeamViewer said that when it published the fix, it was unaware of any attacks exploiting the flaw. The vulnerability is not in CISA's Known Exploited Vulnerabilities catalog as of its October 29 listing. Remedio reported no attacks in the wild and did not release exploit code.

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
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[endpoint security](https://thehackernews.com/search/label/endpoint%20security), [Remote Access Security](https://thehackernews.com/search/label/Remote%20Access%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Unpatched Broadcom Wi-Fi Flaw Lets Attackers in Range Run Code as Root on Routers](https://thehackernews.com/2026/10/unpatched-broadcom-wi-fi-flaw-lets.html)

[![The Hacker News](data:image/svg+xml;base64...)

OpenCode Console Breach May Have Exposed OpenAI, An...