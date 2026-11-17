---
title: Six Unpatched Danfoss Refrigeration Controller Flaws Could Allow Remote Takeover Without Login
url: https://thehackernews.com/2026/11/six-unpatched-danfoss-refrigeration.html
source: The Hacker News
date: 2026-11-16
fetch_date: 2026-11-17T09:57:54.699996
---

# Six Unpatched Danfoss Refrigeration Controller Flaws Could Allow Remote Takeover Without Login

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

# [Six Unpatched Danfoss Refrigeration Controller Flaws Could Allow Remote Takeover Without Login](https://thehackernews.com/2026/11/six-unpatched-danfoss-refrigeration.html)

**Swati Khandelwal**Nov 16, 2026Vulnerability / Operational Technology

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_1GngZ38pRRizZTrhUgdWx49U1Dk8N_Y1Wkfll2kXIjAeYMmX2R69d6OBvA9k-zb6rnYbNOZyouN9yj59QIlT8XxiTzmmhLTmwmEdU2bqiGc_XoSMlvKKN1qZtH3o73YN1miGEhR4vkDniji2WkWOHjSPPIn69ysWKPkFzr504FsViG2NQYxPDkD7sgw/s1700-nu-rw-lo-l85-e365/flaws.jpg)

Six flaws in **Danfoss AK-SM800A** refrigeration controllers could let a remote attacker take over a controller without logging in, Dutch security consultancy Midnight Blue said earlier this week.

No patch is available, and the researchers say the newest firmware, version 5.4.0, does not fix the flaws.

Government cybersecurity agencies in Belgium, Ireland and Germany told operators this week to take the controllers' management interfaces off the internet.

For a controller left on the internet, updating the firmware, changing default passwords or turning on Strict mode is not enough on its own, the Belgian and Irish agencies said. Strict mode is a login protection that requires encrypted connections and session tokens, but one of the six flaws is in the gateway that enforces it.

The AK-SM800A runs a store's fridges and freezers, and maintenance firms can manage it remotely. Such controllers were targeted in [attacks in France](https://thehackernews.com/2026/10/attackers-heat-french-supermarket.html) starting October 11, and in a [second wave](https://thehackernews.com/2026/11/second-wave-of-cyberattacks-hits.html) across Europe that began last week. The attacks caused unwanted defrost cycles and destroyed stock.

Germany's federal IT security agency, the BSI, says in a [security notice](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-306525-1032.pdf?__blob=publicationFile&v=2) that the AK-SM800A was involved in earlier incidents in which refrigeration units in several countries were tampered with.

The agency has no information about any exploitation of the six new flaws, and neither other agencies nor researchers link the flaws to those incidents.

The researchers examined firmware version 5.3.2, then the newest, and say every version up to and including it is affected.

No CVE identifiers have been assigned. The researchers are keeping technical details private while they work on disclosure with Danfoss, the Danish company that makes the controllers.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The vendor lists software package 5.4.0, dated November, as its newest release for the AK-SM800A. Its [5.4.0 readme](https://www.danfoss.com/en/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/license-agreement/) and November update guide cover upgrade steps, and the guide adds a stricter password rule. Neither mentions a fix for any vulnerability.

In a [follow-up statement](https://www.coolingpost.com/world-news/belgium-warns-of-new-danfoss-controller-vulnerabilities/) carried by trade publication Cooling Post, the researchers said 5.4.0 does not patch the flaws: "It's not really possible either because according to the file timestamp this firmware was likely built on October 29, before the second wave of cyber attacks and well before our vulnerability reports."

The German agency first said in a press release this week that 5.4.0 was not affected. Later the same day, it changed that in a [corrected statement](https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2026/261113_Kuehlgeraete-Danfoss.html): it cannot rule out for now that 5.4.0 is affected.

The vendor's [advisory page](https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/) lists no advisory for the six flaws as of today, and no date for a fix has been published.

Midnight Blue researcher Carlo Meijer found the six flaws in less than an hour of manual review, using firmware the vendor offers for download, and described them in a [technical write-up](https://www.midnightblue.nl/blog/multiple-rce-danfoss-aksm800a).

Five of the flaws are in web request handlers that do not require a login, inside a program that runs as root. Through one of them, the researchers ran code as root on older firmware, version 3.3.0, and they found the same bugs in 5.3.2.

Strict mode closes almost all of the controller's web attack surface to users who have not logged in, including the flaw used in that demonstration. The sixth flaw is in the gateway that enforces Strict mode, a separate program that blocks every request except the login until a user has logged in.

When the researchers ran firmware 5.3.2 in an emulator with Strict mode on, that flaw crashed the gateway. The crash could be turned into code execution with more work, the researchers say, and the gateway lacks basic exploit defenses such as stack canaries.

With code running as root, an attacker could change the controller's settings, start defrost cycles and hide that activity from its logs.

The controllers do not use secure boot, the researchers found, so an attacker could plant code that survives a factory reset and a firmware update. An attacker could also make a controller unusable until it is replaced.

The researchers say the code almost certainly holds more flaws like these, and they call patching flaws one by one or turning on Strict mode "a misallocation of scarce security and personnel resources."

### What Operators Can Do

Removing internet exposure must not wait for a patch, and it is needed even where firmware is current and Strict mode is on, the Centre for Cybersecurity Belgium says.

The [Belgian advisory](https://ccb.belgium.be/advisories/warning-six-new-danfoss-vulnerabilities-refrigeration-controllers-risk-immediate-action) and a similar [Irish advisory](ht...