---
title: Thermo Fisher Patches Flaw That Could Make DNA File Tampering Nearly Undetectable
url: https://thehackernews.com/2026/08/thermo-fisher-patches-flaw-that-could.html
source: The Hacker News
date: 2026-08-03
fetch_date: 2026-08-04T05:01:12.660483
---

# Thermo Fisher Patches Flaw That Could Make DNA File Tampering Nearly Undetectable

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

# [Thermo Fisher Patches Flaw That Could Make DNA File Tampering Nearly Undetectable](https://thehackernews.com/2026/08/thermo-fisher-patches-flaw-that-could.html)

**Swati Khandelwal**Aug 03, 2026Data Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMO8eh_7kmo0QAAphjdYIXsjfGspFVU9gV5XInqqhs4WnFNCm_hP-EBdmVln7vSrwWkmo9pdvoxAQbaC17M8sYg7VzBX8RJnRIb6E6pBr5euW9WweOeeZk9XpN8O5I5vF_OGypfqp9WO-SO_C81D4DDui3uTp0jBvV5_C7qIjuRgtoMd4bKQ1y8QEnC3c/s1700-e365/dna.jpg)

Thermo Fisher Scientific has patched a flaw in select Applied Biosystems human identification software that could allow data files to be altered before analysis software loads them.

The vendor's July 31 security bulletin says nearly undetectable changes to .fsa and .hid outputs could occur if laboratory controls are circumvented.

Thermo Fisher tracks the issue as **CVE-2026-17583** and rates it High with a CVSS v4.0 score of 8.2. Five supported product lines have received updates that add digital signatures, while three end-of-life data collection products will receive no vendor update.

Thermo Fisher credits Nathan Adams, Kevin Dyer and Laura Gaydosh Combs, together with the U.S. Cybersecurity and Infrastructure Security Agency, with identifying the issue and coordinating disclosure.

Thermo Fisher urged customers to install the applicable updates. For customers unable to implement the updates or use another third-party analysis platform, the company recommends controls covering file custody, storage, access, privilege and network connectivity.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The public bulletin does not address exploitation, but Thermo Fisher separately told [The Wall Street Journal](https://www.wsj.com/tech/cybersecurity/security-flaw-placed-30-years-of-dna-evidence-at-risk-of-hacking-1932775a) that it knew of no instances in which the vulnerability had been exploited.

In its [security bulletin](https://documents.thermofisher.com/TFS-Assets/CORP/Product-Guides/fsa_hid_bulletin.pdf), Thermo Fisher says the files can be modified before analysis software loads them. The updates implement digital signatures that, moving forward, help customers verify that data files have not been changed.

The Journal reported that Nathan Adams, a systems engineer at Forensic Bioinformatics, tested the issue using a public data set. Adams said his first successful file modification using Anthropic's Claude took about 45 minutes.

In a demonstration viewed by the Journal, his code combined scans from two individual DNA profiles into a new file that appeared untouched since 2015. The modified file raised no warning in analysis software used by many laboratories.

Thermo Fisher's bulletin does not specify the access required. The researchers told the Journal that an attacker would need local or remote access to a laboratory's servers and enough knowledge of how DNA testing works.

The updates cover five Applied Biosystems human identification product lines:

* 3500/3500xL Series Data Collection Software 4.0.2 and earlier, fixed in 4.0.3
* 3730/3730xL Series Data Collection Software 5.0.2 and earlier, fixed in 5.0.3
* SeqStudio Genetic Analyzer Data Collection Software 1.2.5 and earlier, fixed in 1.2.6
* SeqStudio Flex Series Instrument Software 1.2.0 and earlier, fixed in 1.2.1. Labs using SeqStudio Flex with security, audit, and electronic signature (SAE) enabled must first install the latest SAE profile on the SAE Admin Console
* GeneMapper ID-X Software v1.7.3 and earlier, fixed in v1.7.4

Three older lines get nothing: 3130 Series Data Collection Software 4.1 and earlier, ABI PRISM 3100/3100-Avant Data Collection Software 2.0 and earlier, and ABI PRISM 310 Data Collection Software 3.1 and earlier. Thermo Fisher says each has reached end of life and will receive no update.

Thermo Fisher's recommended measures for customers unable to implement the updates or use another third-party analysis platform include maintaining chain of custody, storing files on encrypted and password-protected media, restricting access, applying least privilege on instrument and analysis systems, and limiting internet connectivity to trusted sources.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

As of August 3, 2026, exact-identifier checks by The Hacker News found Thermo Fisher's bulletin but no separate [CVE.org](https://www.cve.org/) or [National Vulnerability Database](https://nvd.nist.gov/vuln/search) detail page for CVE-2026-17583.

The identifier was not listed in CISA's [Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). Thermo Fisher's [public security-bulletin index](https://corporate.thermofisher.com/us/en/index/about/information-security/Protecting-Our-Products/security-bulletins.html) also did not list the July 31 notice.

Thermo Fisher says the signatures will help customers verify files "moving forward." The bulletin does not explain whether files generated before the updates can be validated retroactively or how laboratories should validate them. The Hacker News found no public primary source linking altered casework to the flaw as of August 3, 2026.

The researchers told the Journal that the vulnerability likely existed in digital files produced by crime-lab machines since 1995 and that they had not found a way to detect prior tampering if it occurred.

hermo Fisher's bulletin does not confirm that historical scope. The reported weakness affects digital records generated from DNA testing, not the underlying physical DNA samples.

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
[**Share on...