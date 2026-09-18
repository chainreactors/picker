---
title: China-Aligned FamousSparrow Deploys SparroWocky Backdoor Across Latin America
url: https://thehackernews.com/2026/09/china-aligned-famoussparrow-deploys.html
source: The Hacker News
date: 2026-09-17
fetch_date: 2026-09-18T06:53:39.483472
---

# China-Aligned FamousSparrow Deploys SparroWocky Backdoor Across Latin America

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

# [China-Aligned FamousSparrow Deploys SparroWocky Backdoor Across Latin America](https://thehackernews.com/2026/09/china-aligned-famoussparrow-deploys.html)

**Ravie Lakshmanan**Sep 17, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOuXwG1YyG0uUU23HOcrfuGGEs6q0HvIDe8f7tcoTc3Vg049ITdUDCK_oyfFs8F68GEANNMqayc_75ARq5bBdbIu8qplp_nwC8hWxALOjCCGyf_Pb76GvNjEEfoWybq1nM9WXuxoPvYiRN_vJewkghj5IAYOaCh9JulsW4DnZLCEOhg_mXL_ykI0_oJwah/s1700-nu-rw-lo-l85-e365/chinese-hackers.jpg)

The China-aligned state-sponsored threat actor known as **FamousSparrow** has been observed deploying a previously unreported backdoor called **SparroWocky** in attacks targeting multiple countries in Latin America since at least August 2025.

"SparroWocky is a modular, C++ backdoor," ESET security researchers Alexandre Côté Cyr and Romain Dumont [said](https://www.welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/#latin-america-in-the-crosshairs) in a technical report shared with The Hacker News ahead of publication. "Its architecture and the techniques used by its authors indicate strong knowledge of anti-analysis tricks and Windows internals."

SparroWocky is so named for the fact that early iterations of the malware have been found to contain the first stanza of [Jabberwocky](https://www.poetryloverspage.com/poets/carroll/jabberwocky/literary-analysis), a famous nonsense poem written by the English author, poet, and mathematician Lewis Carroll in around 1855.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The latest findings from ESET indicate that the [cyber espionage group](https://thehackernews.com/2025/03/new-sparrowdoor-backdoor-variants-found.html), which shares some level of overlap with Earth Estries and Salt Typhoon, has replaced SparrowDoor with SparroWocky as its primary implant. The threat actor is assessed to be active since at least 2019.

SparroWocky features the ability to execute arbitrary files, act as a TCP proxy, and run commands. It can also collect general information about the compromised machine and the IP addresses of its network interfaces, as well as exfiltrate files, take periodic screenshots, perform file operations, and delete itself from the host.

Furthermore, it makes use of various public projects for communications and defense evasion -

* [Mbed TLS](https://github.com/Mbed-TLS/mbedtls), to establish a secure communication channel with its command-and-control (C2) server ("216.238.110[.]120") over TLS
* [MinHook](https://github.com/TsudaKageyu/minhook), to hide the start address of newly created threads from security products
* [COFF Loader](https://github.com/trustedsec/COFFLoader), to enable dynamic loading and execution of in-memory plugins in the form of COFF objects
* A variant of [SilentMoonwalk](https://github.com/klezVirus/SilentMoonwalk) (or StackMoonwalk), to spoof the call stacks originating from MinHook routines

"FamousSparrow still uses open-source offensive tooling for its own malicious ends," ESET said. "Previously, these tools were mainly used side by side with the group's backdoor. With SparroWocky, we can observe that it also has the development capabilities to integrate open-source code directly into its own custom backdoor."

Despite switching to a distant malware family, the underlying techniques remain the same. As observed in the case of SparrowDoor, the malware is triggered by means of a DLL sideloading chain. The legitimate executable is used to launch a loader DLL that then decrypts and launches the main payload. The initial access vector used in these attacks is unknown.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

What's more, FamousSparrow appears to be more focused on targeting high-profile entities across Latin America starting July 2025, with the new backdoor deployed against governmental entities in Argentina, Ecuador, Guatemala, Honduras, Panama, Peru, Puerto Rico, and Venezuela. ESET said 90% of the group’s targets recorded in its telemetry have been located in the region.

"It is not clear whether the group’s apparent focus on Latin America may reflect a formal, geographical mandate, or whether this focus is only temporary and dictated by the current geopolitical circumstances," the Slovak cybersecurity company said.

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage), [Malware](https://thehackernews.com/search/label/Malware), [Nation-State](https://thehackernews.com/search/label/Nation-State), [Windows Security](https://thehackernews.com/search/label/Windows%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html)

[![The Hacker News](data:image/svg+xml;base64...)

GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure](https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-fla...