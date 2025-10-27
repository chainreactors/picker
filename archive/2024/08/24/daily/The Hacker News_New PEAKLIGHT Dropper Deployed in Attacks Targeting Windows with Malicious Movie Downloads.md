---
title: New PEAKLIGHT Dropper Deployed in Attacks Targeting Windows with Malicious Movie Downloads
url: https://thehackernews.com/2024/08/new-peaklight-dropper-deployed-in.html
source: The Hacker News
date: 2024-08-24
fetch_date: 2025-10-06T18:07:12.543796
---

# New PEAKLIGHT Dropper Deployed in Attacks Targeting Windows with Malicious Movie Downloads

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

# [PEAKLIGHT Downloader Deployed in Attacks Targeting Windows with Malicious Movie Downloads](https://thehackernews.com/2024/08/new-peaklight-dropper-deployed-in.html)

**Aug 23, 2024**Ravie LakshmananMalware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7_TCso49CtXpOV9F3h8Ki_GlIQng09ovFCncGVVr8kDD13LPETF_-kreyrCopzrDfC3LK7hJwo_ttlIJ_P9UYhCYmpc8cvKRBCnCw1VlhcnbFejaoG9if9Tc72vB1rPzAbYIWf8LF3pl424LtqB4ub5vtPhgYbn7XRMimNfXBwjuxtXPt6jkodAk1wVA5/s790-rw-e365/main.jpg)

Cybersecurity researchers have uncovered a never-before-seen dropper that serves as a conduit to launch next-stage malware with the ultimate goal of infecting Windows systems with information stealers and loaders.

"This memory-only dropper decrypts and executes a PowerShell-based downloader," Google-owned Mandiant [said](https://cloud.google.com/blog/topics/threat-intelligence/peaklight-decoding-stealthy-memory-only-malware/). "This PowerShell-based downloader is being tracked as PEAKLIGHT."

Some of the malware strains distributed using this technique are [Lumma Stealer](https://thehackernews.com/2023/11/lummac2-malware-deploys-new.html), [Hijack Loader](https://thehackernews.com/2024/07/fakebat-loader-malware-spreads-widely.html) (aka DOILoader, IDAT Loader, or SHADOWLADDER), and [CryptBot](https://thehackernews.com/2023/04/google-gets-court-order-to-take-down.html), all of which are advertised under the malware-as-a-service (SaaS) model.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The starting point of the attack chain is a Windows shortcut (LNK) file that's downloaded via drive-by download techniques -- e.g., when users look up a movie on search engines. It's worth pointing out that the LNK files are distributed within ZIP archives that are disguised as pirated movies.

The LNK file connects to a content delivery network (CDN) hosting an obfuscated memory-only JavaScript dropper. The dropper subsequently executes the PEAKLIGHT PowerShell downloader script on the host, which then reaches out to a command-and-control (C2) server to fetch additional payloads.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVET5ktAba8gNKd-eWq95Zt7qiNfysGkxB5sHJeuZqvJBAuE0dgWATfTWxowMD1ic47nUTyLSOrqyOR48ijC2qCy4_M-l8gA26yMB4hEU-JnX6CoPKDuKyHbex892CdI4Aplzi4llxGPGcqGRF0tYqkBsgUywe82s3YAMlYOgul03OVdK7uMzMmkbexZN-/s790-rw-e365/malware.jpg)

Mandiant said it identified different variations of the LNK files, some of which leverage asterisks (\*) as wildcards to launch the legitimate mshta.exe binary to discreetly run malicious code (i.e., the dropper) retrieved from a remote server.

In a similar vein, the droppers have been found to embed both hex-encoded and Base64-encoded PowerShell payloads that are eventually unpacked to execute PEAKLIGHT, which is designed to deliver next-stage malware on a compromised system while simultaneously downloading a legitimate movie trailer, likely as a ruse.

"PEAKLIGHT is an obfuscated PowerShell-based downloader that is part of a multi-stage execution chain that checks for the presence of ZIP archives in hard-coded file paths," Mandiant researchers Aaron Lee and Praveeth D'Souza said.

"If the archives do not exist, the downloader will reach out to a CDN site and download the remotely hosted archive file and save it to disk."

This is not the first time users searching for pirated movies have been targeted by malware. Earlier this June, Kroll [detailed](https://thehackernews.com/2024/07/fakebat-loader-malware-spreads-widely.html) a complex infection chain that led to the deployment of Hijack Loader after attempting to download a video file from a movie download site.

Kroll security researcher Dave Truman told The Hacker News that the dropper "does appear to have the entirely same code" as the malware observed in the June campaign, adding both the activities are likely the work of the same threat actor.

The disclosure comes as Malwarebytes [detailed](https://www.malwarebytes.com/blog/news/2024/08/fraudulent-slack-ad-shows-malvertisers-patience-and-skills) a [malvertising campaign](https://www.malwarebytes.com/blog/scams/2024/08/dozens-of-google-products-targeted-by-scammers-via-malicious-search-ads) that employs fraudulent Google Search ads for Slack, an enterprise communications platform, to direct users to phony websites hosting malicious installers that culminate in the deployment of a remote access trojan named [SectopRAT](https://thehackernews.com/2024/04/cybercriminals-targeting-latin-america.html).

### Update

Cybersecurity firm Sekoia, which is tracking PEAKLIGHT under the name Emmenhtal loader, said alternate attack chains distributing the malware involve downloading the LNK file directly from a WebDAV server to which victims are redirected to via a drive-by compromise while visiting pirated movie websites.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's worth noting that this behavior was previously also [highlighted](https://www.orangecyberdefense.com/global/blog/cert-news/emmenhtal-a-little-known-loader-distributing-commodity-infostealers-worldwide) by Orange Cyberdefense in August 2024.

"This method of using WebDAV to host malicious .LNK files that trigger the download of Emmenhtal via 'mshta.exe' represents an evasive tactic," Sekoia [said](https://blog.sekoia.io/webdav-as-a-service-uncovering-the-infrastructure-behind-emmenhtal-loader-distribution/). "The separation of the hosting server for the initial '.LNK' files and the payload server hinder detection and attribution efforts, making it a preferred strategy among advanced threat actors."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjaa6yO1CizPInjizu5pVv5sLmvSwkAOyWc5yPpbZY35BDlAURkUEJK-3FVp4kOeVQgUe1TU1ulSd5XDYBCe2Q0JDTrdAVIV3kDl5ag2dceGPuggePMrvYH8zsL4z4QGW5zihf49z5NxVraY9d8e2ND8UVD6HWqM8aF5Mk_P0h2e61D4TMxhjVjZWgqPgP6/s79...