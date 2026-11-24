---
title: Webworm Suspected of Modifying SoftEther VPN to Evade Detection and Hide Remote Access
url: https://thehackernews.com/2026/11/webworm-suspected-of-modifying.html
source: The Hacker News
date: 2026-11-23
fetch_date: 2026-11-24T11:49:19.356241
---

# Webworm Suspected of Modifying SoftEther VPN to Evade Detection and Hide Remote Access

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Webworm Suspected of Modifying SoftEther VPN to Evade Detection and Hide Remote Access](https://thehackernews.com/2026/11/webworm-suspected-of-modifying.html)

**Ravie Lakshmanan**Nov 23, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9_mXkFA2_QQWa_ajcGxgoc3rSAfxGJqP-uIREqPGAfJGM7D7-mLrjwSE_F1egX-pwVRvMRinRGs4QbcBE1yJrmHFw4Fa_ILg6ZuTIOy1bf86-wPQ-Zgsqa-6hqdBapRROk97rOeT-Vfa002vHuWF6fCSE1KPttjswyjUeBxjrJzrmVU9KY724e75Giq1T/s1700-nu-rw-lo-l85-e365/chinese-malware.jpg)

The China-aligned threat actor known as **Webworm** is suspected to be using a custom version of the open-source SoftEther VPN Bridge tool in an attempt to remove recognizable detection fingerprints, while disguising it as network-monitoring software to establish covert remote access to compromised networks.

The modified variant "implements various tricks to hide itself from security tools," Rapid7 [said](https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge/) in an analysis, attributing it to the adversarial collective with moderate confidence.

First publicly detailed by Broadcom-owned Symantec in September 2022, [Webworm](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html) is the name assigned to a China-aligned nation-state group that has targeted government entities, IT services, and electric power companies across Russia, Georgia, Mongolia, and several other Asian nations.

One of the tools used by the threat actor is a legitimate software called [SoftEther VPN](https://www.softether.org/4-docs/1-manual/5._SoftEther_VPN_Bridge_Manual), with the bridge acting as a pathway connecting the compromised network and the attacker-controlled infrastructure.

The latest findings from Rapid7 revolve around a Windows executable ("[netcapa.exe](https://www.virustotal.com/gui/file/90e70c0b04ecb9dfa1d5c60fe7de901846ebf0b54754ea12dde1ccb77623a6e8)"), which is a modified build of SoftEther VPN Bridge ("vpnbridge\_x64.exe") version 4.44, build 9807. The mutated version, rebranded as NtMonitor VPN, masquerades itself as Network Monitor Software from a company called Network Systems Solutions Inc. The artifact was uploaded to VirusTotal around mid-January 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

"The PDB path included in the executable reads C:\Users\Administrator\Desktop\SoftEtherVPN\_Stable\SoftEtherVPN\_Stable\SoftEtherVPN\_Stable\src\DebugFiles\pdb\x64\_Release\vpnbridge.pdb," the cybersecurity company said. "As such, the tool doesn't hide its identity from reverse engineers, only external interactions."

The renaming is also said to be inconsistent, with many registry key paths still referencing the program as "SoftEther Project," even though a number of other occurrences of "SoftEther VPN" have been replaced by "NtMonitor VPN."

One of the most noticeable changes identified in the altered version is the use of innocuous-looking HTTP endpoints "/update/alive.cgi" and "/update/picture.cgi" to replace "/vpnsvc/vpn.cgi" and "/vpnsvc/connect.cgi," respectively, so that they look like ordinary web application activity.

It also changes the protocol watermark used by SoftEther VPN as part of the handshake process when initiating communication to help the tool distinguish protocol traffic from ordinary HTTP requests. When the connecting client is found to speak the expected protocol, it proceeds with the handshake. If the check fails, the server returns a decoy HTTP response.

The modified version swaps the GIF-based watermark used by the stock SoftEther VPN utility for a PNG-based watermark so as to bypass existing detection signatures based on the GIF watermark.

Some of the other changes introduced to the program are listed below -

* Reducing a resource archive named hamcore.se2 used by SoftEther VPN to its bare minimum, as it's required to be present at runtime, and embedding it directly into the executable, causing the binary's size to increase by about 1.5 MB.
* Changing the name of the configuration file from "vpn\_bridge.config" to "setting.conf" and making its contents encrypted with a custom algorithm. The encrypted configuration starts with the magic bytes "RCEN" in ASCII.

What's interesting here is that the attackers have not been found to introduce any new functionality to the tool, indicating the primary focus was on stealth.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"It seems like they methodically analyzed SoftEther's detection surface and implemented counter-measures to all of the easy ways a detection engineer may target it," Rapid7 said, calling the latest evolution a hybrid approach that brings together the attacker's use of custom malware and dual-use tools.

"We are observing a sort of hybrid of the two — stock SoftEther software that is not trojanized, but rebuilt from source in a way that erases much of its detection fingerprint."

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage), [Defense E...