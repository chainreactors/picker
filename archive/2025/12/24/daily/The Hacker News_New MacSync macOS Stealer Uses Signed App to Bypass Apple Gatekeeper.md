---
title: New MacSync macOS Stealer Uses Signed App to Bypass Apple Gatekeeper
url: https://thehackernews.com/2025/12/new-macsync-macos-stealer-uses-signed.html
source: The Hacker News
date: 2025-12-24
fetch_date: 2025-12-25T03:27:10.425611
---

# New MacSync macOS Stealer Uses Signed App to Bypass Apple Gatekeeper

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [New MacSync macOS Stealer Uses Signed App to Bypass Apple Gatekeeper](https://thehackernews.com/2025/12/new-macsync-macos-stealer-uses-signed.html)

**Dec 24, 2025**Ravie LakshmananMalware / Endpoint Security

[![MacSync macOS Stealer](data:image/png;base64... "MacSync macOS Stealer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjm_PuMhZ0HFVFeZcWU-pTmZixk1HyEXwA1hMDHRyhd3_vUKfniwEMpjAW60vTPiDnzD9yNm9zITdAQswlvy0Uc2MyvAmjJHkTuEe1n_hAvfyrUD_1KUGcGVS2jyV_gH90K8Ji1dvIe6zMvY4zdMZASLUZRSP-WyILYIah2n3peSJpumHgOx9YnSo00gTeD/s790-rw-e365/apple-macos.jpg)

Cybersecurity researchers have discovered a new variant of a macOS information stealer called **MacSync** that's delivered by means of a digitally signed, notarized Swift application masquerading as a messaging app installer to bypass Apple's Gatekeeper checks.

"Unlike earlier MacSync Stealer variants that primarily rely on drag-to-terminal or [ClickFix](https://thehackernews.com/2025/11/large-scale-clickfix-phishing-attacks.html)-style techniques, this sample adopts a more deceptive, hands-off approach," Jamf researcher Thijs Xhaflaire [said](https://www.jamf.com/blog/macsync-stealer-evolution-code-signed-swift-malware-analysis/).

The Apple device management firm and security company said the latest version is distributed as a code-signed and notarized Swift application within a disk image (DMG) file named "zk-call-messenger-installer-3.9.2-lts.dmg" that's hosted on "zkcall[.]net/download."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ransomware_dragon_d)

The fact that it's signed and notarized means it can be run without being blocked or flagged by built-in security controls like Gatekeeper or XProtect. Despite this, the installer has been found to display instructions prompting users to right-click and open the app – a common tactic used to sidestep such safeguards. Apple has since revoked the code signing certificate.

The Swift-based dropper then performs a series of checks before downloading and executing an encoded script through a helper component. This includes verifying internet connectivity, enforcing a minimum execution interval of around 3600 seconds to enforce a rate limit, and removing quarantine attributes and validating the file prior to execution.

"Notably, the curl command used to retrieve the payload shows clear deviations from earlier variants," Xhaflaire explained. "Rather than using the commonly seen -fsSL combination, the flags have been split into -fL and -sS, and additional options like --noproxy have been introduced."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWIw6jGEm45DAri5d3Nji6xP1P6xz-nZxOoHMJRY5WV9PCTREH4FlDLCwsVFAG1Z-ui4ITx0cY4U6cswpKzHdMD6Jmtu5PDFEvtXc8GHU3n8a9xRqmhVqPDV9ISaScxtjXtQCNRoNfroNBEUaGOMDZr49VjRV04JgTCmbTMdz7ThjXJmcsN3Ou_-e0jBes/s790-rw-e365/macos.jpg)

"These changes, along with the use of dynamically populated variables, point to a deliberate shift in how the payload is fetched and validated, likely aimed at improving reliability or evading detection."

Another evasion mechanism used in the campaign is the use of an unusually large DMG file, inflating its size to 25.5 MB by embedding unrelated PDF documents.

The Base64-encoded payload, once parsed, corresponds to [MacSync](https://g0njxa.medium.com/approaching-stealers-devs-a-brief-interview-with-macsync-ex-mentalpositive-62504db3e761), a rebranded version of [Mac.c](https://moonlock.com/new-mac-stealer-spreading) that first emerged in April 2025. MacSync, per MacPaw's Moonlock Lab, [comes fitted](https://moonlock.com/macc-stealer-macsync-backdoor) with a fully-featured Go-based agent that goes beyond simple data theft and enables remote command and control capabilities.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

It's worth noting that code-signed versions of malicious DMG files mimicking Google Meet have also been observed in attacks propagating other macOS stealers like [Odyssey](https://www.jamf.com/blog/signed-and-stealing-uncovering-new-insights-on-odyssey-infostealer/). That said, threat actors have continued to rely on unsigned disk images to deliver [DigitStealer](https://www.jamf.com/blog/jtl-digitstealer-macos-infostealer-analysis/) as recently as last month.

"This shift in distribution reflects a broader trend across the macOS malware landscape, where attackers increasingly attempt to sneak their malware into executables that are signed and notarized, allowing them to look more like legitimate applications," Jamf said.

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

[Apple](https://thehackernews.com/search/label/Apple)[code signing](https://thehackernews.com/search/label/code%20signing)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[digital signature](https://thehackernews.com/search/label/digital%20signature)[endpoint security](https://thehackernews.com/search/label/endpoint%20security)[Information Stealer](https://thehackernews.com/search/label/Information%20Stealer)[MacOS](https://thehackernews.com/search/label/MacOS)[Malware](https://thehackernews.com/search/label/Malware)

Trending News

[![Featured Chrome Browser Extension Caugh...