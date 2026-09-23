---
title: Researcher Drops BigDiskBuster Zero-Day PoC That Blocks Microsoft Defender Updates
url: https://thehackernews.com/2026/09/researcher-drops-bigdiskbuster-zero-day.html
source: The Hacker News
date: 2026-09-22
fetch_date: 2026-09-23T06:54:52.979840
---

# Researcher Drops BigDiskBuster Zero-Day PoC That Blocks Microsoft Defender Updates

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

# [Researcher Drops BigDiskBuster Zero-Day PoC That Blocks Microsoft Defender Updates](https://thehackernews.com/2026/09/researcher-drops-bigdiskbuster-zero-day.html)

**Swati Khandelwal**Sep 22, 2026Vulnerability / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgf-fkqiHh6b0UEKMHUcsG54QVwJxghIbQLMNWeEG5LWKfUsicLMxisz4Mi8lXdfTdwVYDFpIrCFj5D7-JXXynq8lWhnNn1rJH2t8mgKUeZ4WMePwZktZRnIe2549JW3VXc2HYD9qpsvO8He0J0zCyAzsaRxWtiP46RSrd7jt4QnzKACJhfWnkmyWcFcQs/s1700-nu-rw-lo-l85-e365/ms-def.jpg)

A zero-day proof-of-concept tool that stops Microsoft Defender from installing platform and signature updates by filling all available disk space was [published on GitHub](https://github.com/MSNightmare/BigDiskBuster) on September 19.

The tool, called **BigDiskBuster**, has no patch, no CVE, and no Microsoft advisory. Its author, Abdelhamid Naceri, is a former Microsoft security researcher whose earlier Defender exploits were used in attacks.

When updates are blocked, Defender keeps running, but its detection content grows stale. The researcher's screenshot shows Defender returning a generic Windows error when trying to update, but whether the failure raises an automatic alert is not clear from the proof-of-concept alone.

Naceri said he was dismissed from Microsoft's Security Response Center in 2024 and has been releasing exploits without coordinating with the company since April.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

His first three Defender tools — BlueHammer, RedSun, and UnDefend — were all [exploited in live intrusions](https://thehackernews.com/2026/04/three-microsoft-defender-zero-days.html) before Microsoft [patched them](https://thehackernews.com/2026/05/microsoft-warns-of-two-actively.html) and CISA added all three to its Known Exploited Vulnerabilities catalog. He has since disclosed additional Defender and Windows flaws roughly monthly.

BigDiskBuster watches the C:\ drive for new directories under Defender's update paths. When Defender begins downloading a platform or definition update, the tool creates a hidden temporary file sized to fill all remaining free space, and the update fails.

Once the update fails and Defender removes its staging directory, the tool deletes the file and waits for the next attempt. It also opens a handle on MRT.exe, the Windows Malicious Software Removal Tool, in a way that would block Windows Update from replacing it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg50NjTZmHgO0V5QaqKxaMceKZoNsgytagGA2liHbvBvpkDnlkChU4Sy3RT-N8xqG1aguOwUnwMJjGTJ763T0_dASgNOIb58uyZKQqoDbzY18t6oat0cRM4atsZwGGC3KwG2jRt444CZCOg3IF2FfI-1BU91L94yhXB8JyoszMLTXcb4PcxS7kunzeM5eM/s1700-nu-rw-lo-l85-e365/ms-1.jpg)

Naceri describes the tool as "a bit buggy and needs some rewritting" and says it seems to work on all supported Windows versions. No independent researcher has confirmed the claimed behavior.

Naceri calls BigDiskBuster "similar to **UnDefend**," a Defender denial-of-service flaw he disclosed in April that blocked definition updates through a different method. Microsoft patched it in May as [CVE-2026-45498](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45498) in Antimalware Platform version 4.18.26040.7.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

The two tools work differently. UnDefend used uncontrolled resource consumption, while BigDiskBuster fills the disk so Defender's update directories cannot grow. Whether the May patch also covers this new technique is not established, and the different mechanism suggests it does not.

### What Defenders Should Do

No patch or vendor workaround exists for BigDiskBuster.

Administrators can check that Defender's signatures and platform version are current through Windows Security under Virus & threat protection, then Protection updates, then Check for updates. In PowerShell, Get-MpComputerStatus shows the current versions in the AMEngineVersion and AMProductVersion fields.

Monitoring for repeated Defender update failures, sustained low disk space on the system volume, and large hidden files in temporary directories would help detect the technique. Restricting execution of unknown binaries through WDAC or AppLocker would limit an attacker's ability to run the tool.

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

[endpoint security](https://thehackernews.com/search/label/endpoint%20security), [Microsoft](https://thehackernews.com/search/label/Microsoft), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Windows](https://thehackernews.com/search/label/Windows)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html)

[![The Hacker News](data:image/svg+xml;base64...)

Google Gemini Broke Into Real Company Systems After Security Test Domain Mix-Up](https://thehackernews.com/2026/09/google-gemini-broke-into-real-compan...