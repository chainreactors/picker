---
title: Hackers Use NeedyMantis to Maintain Long-Term Access in Breached Networks
url: https://thehackernews.com/2026/09/hackers-use-needymantis-to-maintain.html
source: The Hacker News
date: 2026-09-28
fetch_date: 2026-09-29T07:41:36.575293
---

# Hackers Use NeedyMantis to Maintain Long-Term Access in Breached Networks

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

# [Hackers Use NeedyMantis to Maintain Long-Term Access in Breached Networks](https://thehackernews.com/2026/09/hackers-use-needymantis-to-maintain.html)

**Swati Khandelwal**Sep 28, 2026Cyber Attack / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJgqNtFBBtX_6em5nY1VC9Q4M6HMG7gzxiQspFHsQRfQgm3LK5kTsHi-9SbwEx8kaeVv7BtKGFq3u1SmTGFEOe0z78fxFCxRFVEb09v0FMZ5tT-FNl7sUBnsGPPpDlAaQh4E_CSQQnwFakxNll2AvKiBvidb9ljEatmOzdJV4T4z8r5lmYG3DINHy-wR0/s1700-nu-rw-lo-l85-e365/hackers.jpg)

Hackers have used a malware family called **NeedyMantis** to maintain long-term access to networks they had already breached, Microsoft said in a technical analysis.

The malware has been seen in a small number of targeted intrusions at telecommunications organizations, universities, medical nonprofits, intergovernmental organizations, and government contractors. Its use goes back to at least October 2025.

Microsoft found [NeedyMantis](https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/) while following up on indicators from Kaspersky's investigation into the [supply chain attack on DAEMON Tools](https://thehackernews.com/2026/05/daemon-tools-supply-chain-attack.html). In that attack, official, signed installers for the DAEMON Tools Lite disk image program carried malicious code from April 8, 2026. The developer replaced them with a clean version on May 5.

Microsoft tracks the activity tied to that attack as Storm-3069. It says Storm-3069 is one group that uses NeedyMantis, though it has not seen the malware itself spread through a supply chain attack. Defenders can check their networks using the file hashes, domains, file paths, and hunting queries that Microsoft published and listed below.

### How NeedyMantis Runs

In the cases Microsoft examined, NeedyMantis arrived as a bundle of three parts: a copy of a legitimate program, a malicious DLL named after a file that program loads, and an encrypted archive with the same name as the DLL. When the program starts, it loads the malicious DLL. This is called DLL sideloading.

The legitimate programs used this way include the Poedit translation tool, curl, the Vim text editor, and the TightVNC remote access tool. The malware has also posed as DLL files from Microsoft Office, Broadcom, Intel, and NVIDIA.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

In the sample Microsoft analyzed in detail, the malicious file replaced WinSparkle.dll, the update component that Poedit uses.

In one intrusion, an operator who was already inside the network used the Impacket toolkit to copy the bundle from a network share and run it on a target machine. How attackers initially gain access to a network may differ from one intrusion to the next.

Once loaded, the DLL unpacks the next stage from the encrypted archive and runs it. That stage decodes the malware's main component. The main component connects to a command-and-control (C2) server over HTTPS and then switches to a WebSocket connection.

Through that connection, operators can load and unload extra modules and send data to them. Microsoft has not confirmed what those modules do.

An older version, seen in October 2025, included a persistence module that uses Windows services. Microsoft did not describe how the newer version it analyzed stays on a machine.

### Who Is Behind It

Storm-3069 is a temporary name. Microsoft [gives "Storm" names](https://learn.microsoft.com/en-us/defender-xdr/microsoft-threat-actor-naming) to new or developing groups until it is confident about who is behind them or where they come from.

Microsoft has also seen NeedyMantis outside Storm-3069's activity in the DAEMON Tools campaign, and it says more than one group may be using the malware. It has not determined whether all the activity comes from a single actor, nor has it explained what links Storm-3069 to NeedyMantis.

Storm-3069's activity appears to originate in China, Microsoft assesses, but the company has not tied the group to a Chinese nation-state actor. All the NeedyMantis activity Microsoft has seen so far fits the pattern of groups it links to China. Examples include targets that align with Chinese interests and the malware's use against only a few selected organizations.

When Kaspersky disclosed the DAEMON Tools attack in May, it found Chinese-language text in the malware but did not attribute it to any particular group.

Google Threat Intelligence Group [tracks the actor](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise) behind the DAEMON Tools campaign as UNC6863. In June, [Mandiant described UNC6863](https://security.googlecloudcommunity.com/security-validation-5/validation-content-update-june-24-2026-7779) as "a suspected China-nexus actor" that used the DAEMON Tools compromise to deploy malware. It is unclear whether UNC6863 and Storm-3069 belong to the same group.

### How to Check for NeedyMantis

Microsoft published these indicators of compromise:

* **SHA-256**: e842dd7642c8e04b5ec20b6393848a9c904e4832930950c16664fe7800ba382e (first-stage loader WinSparkle.dll, first seen May 21, 2026)
* **SHA-256**: 9cb68f986043a576e19d32184c583b7d8f571c7219d8dc0065dced1c13f077ef (encrypted archive named WinSparkle, first seen May 23, 2026)
* **SHA-256**: c82520eb03c084226be4eafbff46f56dca0aa8804a2a7f23a085a96afe71ef77 (encrypted archive named libcurl, older version, first seen October 3, 2025)
* **Domain**: corp.tripswithengine[.]com (C2 server, port 443)
* **User agent**: firefox/21.0 (hard-coded in the malware's communications DLL)

These are some of the file paths used by the malicious DLLs:

* %ProgramFiles%\Poedit\WinSparkle.dll
* %ProgramData%\USOShared\libcurl.dll
* %ProgramData%\VIM\vim64.dll
* %ProgramData%\TightVNC\VIM\vim64.dll
* %ProgramData%\office\dbghelp.dl...