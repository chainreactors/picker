---
title: Beware: Fake Google Meet Pages Deliver Infostealers in Ongoing ClickFix Campaign
url: https://thehackernews.com/2024/10/beware-fake-google-meet-pages-deliver.html
source: The Hacker News
date: 2024-10-19
fetch_date: 2025-10-06T18:58:04.043021
---

# Beware: Fake Google Meet Pages Deliver Infostealers in Ongoing ClickFix Campaign

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Beware: Fake Google Meet Pages Deliver Infostealers in Ongoing ClickFix Campaign](https://thehackernews.com/2024/10/beware-fake-google-meet-pages-deliver.html)

**Oct 18, 2024**Ravie LakshmananThreat Intelligence / Phishing Attack

[![Fake Google Meet](data:image/png;base64... "Fake Google Meet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUhAkevnWu1b4RY_HexCRxw0f00_cJZaHVbug7EUQ6b71293pUTvlOrgigpvXkQMCC7ygvVeqvYC26q_ZDSywIVcxUtsmNQBYcNkTpOvLbZmnU5-P1-ZD_mktLAo-Yt5Ig-aS7aOmDvNCMzZMoWQP43ANqCdbunglPyqnLtljVYfZv1-SN5IOMIjkIb6QP/s790-rw-e365/googlemeet.png)

Threat actors are leveraging fake Google Meet web pages as part of an ongoing malware campaign dubbed **ClickFix** to deliver infostealers targeting Windows and macOS systems.

"This tactic involves displaying fake error messages in web browsers to deceive users into copying and executing a given malicious PowerShell code, finally infecting their systems," French cybersecurity company Sekoia [said](https://blog.sekoia.io/clickfix-tactic-the-phantom-meet/) in a report shared with The Hacker News.

Variations of the ClickFix (aka ClearFake and OneDrive Pastejacking) campaign have been [reported](https://thehackernews.com/2024/07/onedrive-phishing-scam-tricks-users.html) [widely](https://thehackernews.com/2024/09/transportation-companies-hit-by.html) in [recent months](https://thehackernews.com/2024/10/ai-powered-rhadamanthys-stealer-targets.html), with threat actors employing different lures to redirect users to bogus pages that aim to deploy malware by urging site visitors to run an encoded PowerShell code to address a supposed issue with displaying content in the web browser.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

These pages are known to masquerade as popular online services, including Facebook, Google Chrome, PDFSimpli, and reCAPTCHA, and now Google Meet as well as potentially Zoom -

* meet.google.us-join[.]com
* meet.googie.com-join[.]us
* meet.google.com-join[.]us
* meet.google.web-join[.]com
* meet.google.webjoining[.]com
* meet.google.cdm-join[.]us
* meet.google.us07host[.]com
* googiedrivers[.]com
* us01web-zoom[.]us
* us002webzoom[.]us
* web05-zoom[.]us
* webroom-zoom[.]us

On Windows, the attack chain culminates in the deployment of [StealC](https://thehackernews.com/2023/02/researchers-discover-dozens-samples-of.html) and [Rhadamanthys](https://thehackernews.com/2024/10/ai-powered-rhadamanthys-stealer-targets.html) stealers, while Apple macOS users are served a booby-trapped disk image file ("Launcher\_v1.94.dmg") that drops another stealer known as [Atomic](https://thehackernews.com/2024/01/atomic-stealer-gets-upgrade-targeting.html).

This emerging social engineering tactic is notable for the fact that it cleverly evades detection by security tools, as it involves the users manually running the malicious PowerShell command directly on the terminal, as opposed to being automatically invoked by a payload downloaded and executed by them.

[![Fake Google Meet](data:image/png;base64... "Fake Google Meet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwyiTLE4gI7oAl_rVE-8_LaBU_EL-UiDiyJWvcX1WPerC2TFqo-uGOQkLKjd4s8r8mGQNz4VrJV5z1hR61N3AGYUZeFlTS97tPlvVHFPTlHEv_Vig1Z01LGmh7FlUoGDpKDm_d_9FxoEkPYyc1Ja2OV91AaZXB0x-Y8URpxTGesWgYrJpUZ6ABC0GEU3Q4/s790-rw-e365/chrome.png)

Sekoia has attributed the cluster impersonating Google Meet to two [traffers groups](https://thehackernews.com/2022/11/researchers-warn-of-cyber-criminals.html), namely Slavic Nation Empire (aka Slavice Nation Land) and Scamquerteo, which are sub-teams within [markopolo](https://thehackernews.com/2024/06/warning-markopolos-scam-targeting.html) and CryptoLove, respectively.

"Both traffers teams [...] use the same ClickFix template that impersonates Google Meet," Sekoia said. "This discovery suggests that these teams share materials, also known as 'landing project,' as well as infrastructure."

This, in turn, has raised the possibility that both the threat groups are making use of the same, as-yet-unknown cybercrime service, with a third-party likely managing their infrastructure.

The development comes amid the emergence of [malware campaigns](https://www.broadcom.com/support/security-center/protection-bulletin/thunderkitty-malware) distributing the open-source [ThunderKitty](https://medium.com/%40Engun_Mayor/this-new-malware-is-taking-over-discord-accounts-and-stealing-browser-data-what-you-need-to-know-90a4d91e38bc) [stealer](https://www.proofpoint.com/us/blog/threat-insight/security-brief-royal-mail-lures-deliver-open-source-prince-ransomware), which shares overlaps with [Skuld](https://thehackernews.com/2023/06/new-golang-based-skuld-malware-stealing.html) and [Kematian Stealer](https://thehackernews.com/2024/07/dark-web-malware-logs-expose-3300-users.html), as well as new stealer families named [Divulge, DedSec (aka Doenerium), Duck](https://www.cyfirma.com/research/the-will-of-d-a-deep-dive-into-divulge-stealer-dedsec-stealer-and-duck-stealer/), [Vilsa](https://www.cyfirma.com/research/vilsa-stealer/), and [Yunit](https://www.cyfirma.com/research/yunit-stealer/).

"The rise of open-source infostealers represents a significant shift in the world of cyber threats," cybersecurity company Hudson Rock [noted](https://www.infostealers.com/article/open-sourced-infostealers-about-to-fuel-new-wave-of-computer-infections/) back in July 2024.

"By lowering the barrier of entry and fostering rapid innovation, these tools could fuel a new wave of computer infections, posing challenges for cybersecurity professionals and increasing the overall risk to businesses and individuals."

### ClickFix Delivers Lumma Stealer; Targets WordPress Sites

Cybersecurity company Qualys has detailed a new ClickFix campaign that leverages [CAPTCHA-verification lures](https://www.gendigital.com/blog/news/innovation/global-surge-in-fake-captcha-attacks) on fake websites to trick users into copying and executing a Base64-encoded PowerShell script...