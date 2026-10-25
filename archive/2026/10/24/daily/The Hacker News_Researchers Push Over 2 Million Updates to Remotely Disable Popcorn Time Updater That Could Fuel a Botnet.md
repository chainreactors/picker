---
title: Researchers Push Over 2 Million Updates to Remotely Disable Popcorn Time Updater That Could Fuel a Botnet
url: https://thehackernews.com/2026/10/researchers-push-over-2-million-updates.html
source: The Hacker News
date: 2026-10-24
fetch_date: 2026-10-25T07:10:52.921617
---

# Researchers Push Over 2 Million Updates to Remotely Disable Popcorn Time Updater That Could Fuel a Botnet

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

# [Researchers Push Over 2 Million Updates to Remotely Disable Popcorn Time Updater That Could Fuel a Botnet](https://thehackernews.com/2026/10/researchers-push-over-2-million-updates.html)

**Swati Khandelwal**Oct 24, 2026Vulnerability / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuy-T7iQPeiRqkJd7yhxd2WVQzxURRnLyHG9yz5fUXxIhjUW-bv_yAAt13dnTE1ecuh1w6cRjenRXL3In2b55rL22lXnBhpKrVvS9c5Qb6Bv0TeQPLeAXYoafNYnqYxYQwWnZBCO3e8ZW-HS8Y2GMbQuGz58-_wG7gT6Pcok3j53J4iiZ7jw6kLoGGtWU/s1700-nu-rw-lo-l85-e365/popcorn.jpg)

Between November 2025 and March 2026, the Dutch security firm **Eye Security** pushed more than 2 million updates to computers it did not own to switch off a background updater that it said could have allowed an outsider to take over the machine.

The updater belongs to **Time4Popcorn**, an abandoned copy of Popcorn Time, a free app that streamed pirated films and TV over BitTorrent.

Popcorn Time was popular about a decade ago, and the original shut down in 2014, but several copies kept running under the same name. A separate, legal project that took the Popcorn Time name in early 2025 is unrelated to it.

Eye Security, which monitors client networks for threats, found the updater during a routine threat hunt: a program called Updater.exe on one client's laptop kept trying to reach a web address that was no longer registered.

The firm registered the address itself to see what would connect, and about 50 requests a second poured in. It later laid out the operation, which it named Operation IXIM, in a [write-up](https://labs.eye.security/operation-ixim-preventing-a-botnet-of-millions-of-popcorn-time-users/) and a [talk at Hack.lu](https://pretalx.com/hack-lu-2026/talk/FAGXJE/) on October 22.

Over six months, those requests carried more than 3.8 million different hardware IDs. The IDs proved an unreliable way to count machines, because some Windows PCs shared one and some Macs changed theirs, so Eye revised its estimate to 2.5 to 3 million Windows computers and 250,000 to 350,000 Macs.

The updater ran in the background on Windows and Mac from the moment the computer started. It checked for new versions over an unencrypted connection and installed whatever it was sent, at the highest privilege level, called SYSTEM on Windows and root on Mac, without checking who sent it.

Because the web addresses it called had been abandoned, Eye said, anyone who registered the right one could have served their own program to every machine still calling it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

On a machine with that access, an attacker could install ransomware, steal saved passwords, or pull the computer into a botnet, Eye said. Mapping a sample of the connecting addresses, the firm said it saw home users around the world, as well as machines on government, military, and corporate networks, though it added that it is "hard to draw conclusions" from that.

Eye had [disclosed the flaw](https://labs.eye.security/cve-2026-30612-a-vulnerability-in-time4popcorn-popcorntime/), now tracked as [CVE-2026-30612](https://www.cve.org/CVERecord?id=CVE-2026-30612), in June. The U.S. Cybersecurity and Infrastructure Security Agency rates it 9.8 out of 10. It affects three versions of the Time4Popcorn software:

* Windows, up to and including 6.2.1.18
* Mac, up to and including 6.2.1.17
* Android, up to and including 3.5.0.173

### Turning the Updater Against Itself

With no company left to fix the software and no patch coming, Eye decided to use the updater against itself. After taking legal advice, it served the machines an update that does one thing: it stops and disables the updater, deleting no files and collecting nothing.

Eye compared the step to [Operation Ladybird](https://thehackernews.com/2021/01/european-authorities-disrupt-emotet.html) in 2021, when Dutch police pushed an update to computers infected with the Emotet botnet to disable the malware on them.

The difference, Eye said, is that Emotet's victims never chose to be infected, while Popcorn Time's users installed the app themselves. Still, the firm said, "none of them chose to have a forgotten updater running in the background for years."

Soon after the updates began, someone uploaded Eye's update to VirusTotal, and antivirus engines started flagging it as malware, a fair description of a program that disables a Windows service. Because every product that blocked it left the vulnerable updater running, Eye reworked the update until only one scanner continued to flag it.

By December 2025, Eye had updated more than 1 million systems and cut the traffic to its web addresses by about 90 percent. By March 1, it was sending about 5,000 updates a day, a 98 percent reduction. Judging the remaining numbers too small to interest a botnet operator, Eye stopped, having sent more than 2 million update downloads in all.

In late March, Eye handed the 15 web addresses it controlled to the [Shadowserver Foundation](https://www.shadowserver.org/), a non-profit that takes abandoned and malicious domains out of circulation, so a trusted party would hold them rather than Eye.

Public registration records for one of them, popcorntimeupd[.]xyz, now point to Shadowserver's sinkhole servers, with a transfer dated March 20, 2026. Other addresses the updater calls were never Eye's to take and remain with outside owners, the firm said, so machines that reach those are still exposed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Eye found no sign that anyone else was serving code through the addresses: the ones already registered by other people were parked or up for sale, not pushing updates to the machines calling them. The flaw is not listed in CISA's catalog of known exploited vulnerabilities as of October 23, 2026.

### What Popcorn Time Users Should Do

Switching off the updater does not make the app safe...