---
title: Microsoft Links 30+ Rotating Domains to MacSync Stealer Infrastructure
url: https://thehackernews.com/2026/08/microsoft-links-30-rotating-domains-to.html
source: The Hacker News
date: 2026-08-19
fetch_date: 2026-08-20T02:56:57.027929
---

# Microsoft Links 30+ Rotating Domains to MacSync Stealer Infrastructure

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Microsoft Links 30+ Rotating Domains to MacSync Stealer Infrastructure](https://thehackernews.com/2026/08/microsoft-links-30-rotating-domains-to.html)

**Swati Khandelwal**Aug 19, 2026Malware / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLR2UjD4FhPqPT7MZpKuuqDl82K13qHQ_ob2-S_fK62g7UtwW6jn6YafX4RcZcqFgZWFbXiuCTkLbeD9zC_ws4mOUL0xVJgJ315fMiFlqxDFnhyphenhyphenIe2K8IXv3Vn1ZfWJevZywKd01wSpTS0BT08VlGtSoksz8y0ihBug5XqbRN48jy_NoQx-4fRc52Khzg/s1700-e365/apple-macos.jpg)

Microsoft Defender Experts have linked more than 30 web domains to MacSync Stealer, a macOS-focused information stealer, after correlating recurring endpoint and network behaviors across changing infrastructure, tracing the malware from payload retrieval through data collection, staging, and exfiltration.

The tech giant said it required multiple endpoint and network behaviors to align before treating a domain as connected, including process ancestry, command-line patterns, request paths, headers, and upload parameters.

Microsoft did not disclose a victim count or attribute the activity to a named threat actor in the report published Tuesday. "The investigation also confirmed active data exfiltration, not just beaconing," the company said.

According to [the analysis](https://www.microsoft.com/en-us/security/blog/2026/08/18/hunting-macsync-stealer-infrastructure-through-behavioral-pivots/), observed execution began from an interactive `zsh` Terminal session consistent with ClickFix social engineering, followed by `curl` retrieving attacker-controlled content over a recurring `/curl/` path and native utilities such as Base64 and `gunzip` decoding or unpacking the payload.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The payload uses `osascript` for AppleScript-assisted execution alongside native macOS and Unix utilities, before collecting host and user information, macOS Keychain material, browser credentials and cookies, session data, Apple Notes, Secure Shell (SSH) keys, Amazon Web Services (AWS) credentials, Kubernetes configurations, browser history, and sensitive files from common user directories.

Collected data is staged under `/tmp/sync*`, compressed into `/tmp/osalogging.zip`, split into multiple chunks, and uploaded with `curl` through HTTP PUT requests using recurring parameters such as `upload_id`, `chunk_index`, and `total_chunks`. The malware removes temporary archives, staging folders, lock files, and other artifacts after exfiltration.

The disclosure builds on [RST Cloud's May 8 analysis](https://www.rstcloud.com/macsync-stealer-c2-infrastructure-rotation/), which documented a static API key across four confirmed command-and-control (C2) domains and identified 11 additional candidate domains through recurring `/dynamic?txd=` and `/gate?buildtxd=` URI patterns.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_fJtIEbvseASpXKbhONoV03mXkBGe_AyyYEEjmi8REC2-tRjWxbubkPibiFNQwOK9Ia5_TFFY9RZvvsIqLMBguMXa0fWZqdySq4IIIuePHrqFUzFGSbFdywas-_r1X-4WH5NYyPbZdcRo1ukAOMEAdK4G22wPTlrZHOVKI3PFDB3gEVGGK4EKl_29L-0/s1700-e365/ms.jpg)

Several candidates had overlapping submission windows, which RST Cloud said was consistent with parallel C2 operation rather than strict sequential rotation between hostnames. "The hex build token rotates per deployment, the api-key does not," RST Cloud said.

A comparison of the two published indicator sets by The Hacker News found that four domains Microsoft now lists, `lalandscapelighting[.]com`, `lumenagnet[.]com`, `nailscanai[.]com`, and `numericagent[.]com`, also appeared in RST Cloud's May candidate cluster. RST Cloud classified those domains as URI-pattern bound rather than API-key confirmed because it had not retrieved samples from each candidate to validate the static API-key match.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwgJi45eiznQp4Ord8poeG_cENPU7QnpWGBhYetSXv3uVvv3CzkgU1rR1EfCxw_4qmYqd_cmZuIb2rq8aXyqAPdYLHYzq5JP-y0OfWP6lfa-UJ_LH1lhc-SVncHF1j5uZ1Iw11WrLRGlF6oP9KQGmNYQfO63B7tBG2XpsN6OtgdW9zR2M5KNme_X82X3s/s1700-e365/c2.jpg)

Microsoft refers to API-key headers as a recurring [MacSync](https://thehackernews.com/2026/03/clickfix-campaigns-spread-macsync-macos.html) trait, but its August 18 post does not publish the static value documented by RST Cloud or state that the same value appears across every domain in the current set.

Microsoft said the recurring network traits include the `/curl/`, `/dynamic?txd=`, and `/gate?buildtxd=` paths, macOS User-Agent strings, API-key headers, and HTTP PUT uploads carrying the same chunk-management parameters.

The researchers used those request shapes together with endpoint execution context to identify related infrastructure as the domains changed.

Microsoft shared the following point-in-time domain indicators observed in activity consistent with MacSync Stealer -

* `aihealthring[.]com`
* `cabinrentalsnc[.]com`
* `chatbasedos[.]com`
* `commercialroofingsd[.]com`
* `dogtrainersgeorgia[.]com`
* `fintelliganceai[.]com`
* `homeinspectionsdelaware[.]com`
* `intopython[.]com`
* `lalandscapelighting[.]com`
* `lumenagnet[.]com`
* `marbellaresales[.]com`
* `miamipcsupport[.]com`
* `moldinspectiondayton[.]com`
* `nailscanai[.]com`
* `newjerseypetsitter[.]com`
* `numericagent[.]com`
* `oaklandwaterdamage[.]com`
* `oklahomawarehousing[.]com`
* `olympiapetemergency[.]com`
* `peaecagent[.]com`
* `plasmaticsystems[.]com`
* `plethorawallet[.]com`
* `premierrentalpurchase[.]com`
* `ricewaterbeauty[.]com`
* `rvieragent[.]com`
* `sandiegotkd[.]com`
* `secueragent[.]com`
* `shiledagent[.]com`
* `syracusefertilitycenter[.]com`
* `vastbets[.]com`
* `wvaeagent[.]com`

Microsoft advised organizations to perform the following steps -

* Educate users not to paste or run Terminal commands from untrusted websites, chat messages, apps, files, or phone-based instructions.
* Monitor unusu...