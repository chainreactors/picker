---
title: WebRTC Skimmer Bypasses CSP to Steal Payment Data from E-Commerce Sites
url: https://thehackernews.com/2026/03/webrtc-skimmer-bypasses-csp-to-steal.html
source: The Hacker News
date: 2026-03-26
fetch_date: 2026-03-27T04:33:40.895023
---

# WebRTC Skimmer Bypasses CSP to Steal Payment Data from E-Commerce Sites

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [WebRTC Skimmer Bypasses CSP to Steal Payment Data from E-Commerce Sites](https://thehackernews.com/2026/03/webrtc-skimmer-bypasses-csp-to-steal.html)

**Ravie Lakshmanan**Mar 26, 2026Malware / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDIJhct-gQspWhgoCYGYYTokFv7FUIEMJqaILu_8IfMO3siPXFxR9g6eek-vKmgpFFO5QKCLBvl7pK8gFOGf8ZQuR6wVxOeBOxDm43bCBdmLDhPTyIGhoFssJGBUn9in_jfKwIvcyf9TERfomsZOjcPs4CKnYsYyW_jLaX3jbgm-LT4TORzq4g3ik0cB10/s1700-e365/cards.jpg)

Cybersecurity researchers have discovered a new [payment skimmer](https://thehackernews.com/2026/01/long-running-web-skimming-campaign.html) that uses [WebRTC data channels](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels) as a means to receive payloads and exfiltrate data, effectively bypassing security controls.

"Instead of the usual HTTP requests or image beacons, this malware uses WebRTC data channels to load its payload and exfiltrate stolen payment data," Sansec [said](https://sansec.io/research/webrtc-skimmer) in a report published this week.

The attack, which targeted a car maker's e-commerce website, is said to have been facilitated by [PolyShell](https://thehackernews.com/2026/03/magento-polyshell-flaw-enables.html), a new vulnerability impacting Magento Open Source and Adobe Commerce that allows unauthenticated attackers to upload arbitrary executables via the REST API and achieve code execution.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

Notably, the vulnerability has since come under mass exploitation since March 19, 2026, with more than 50 IP addresses participating in the scanning activity. The Dutch security company said it has found PolyShell attacks on 56.7% of all vulnerable stores.

The skimmer is designed as a self-executing script that establishes a WebRTC peer connection to a hard-coded IP address ("202.181.177[.]177") over UDP port 3479 and retrieves JavaScript code that's subsequently injected into the web page for stealing payment information.

The use of WebRTC marks a significant evolution in skimmer attacks, as it bypasses Content Security Policy ([CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)) directives.

"A store with a strict CSP that blocks all unauthorized HTTP connections is still wide open to WebRTC-based exfiltration," Sansec noted. "The traffic itself is also harder to detect. WebRTC DataChannels run over DTLS-encrypted UDP, not HTTP. Network security tools that inspect HTTP traffic will never see the stolen data leave."

Adobe released a fix for PolyShell in [version 2.4.9-beta1](https://experienceleague.adobe.com/en/docs/commerce-operations/release/notes/adobe-commerce/2-4-9?lang=en#highlights-in-v249-beta1) released on March 10, 2026. But the patch has yet to reach the production versions.

As mitigations, site owners are recommended to block access to the "pub/media/custom\_options/" directory and scan the stores for web shells, backdoors, and other malware.

### More Details About PolyShell Emerge

The development comes as Searchlight Cyber's Assetnote team [shared](https://slcyber.io/research-center/magento-polyshell-unauthenticated-file-upload-to-rce-in-magento-apsb25-94/) additional details of the PolyShell vulnerability, stating it's rooted in a function named ImageProcessor::processImageContent(), which accepts any "valid" image as input and move the file to destination folder (i.e., "pub/media/custom\_options/quote/<FIRST\_CHAR>/<SECOND\_CHAR>/<FILE\_NAME>").

As for what constitutes a valid image, the code checks that it's not empty, has a size, has a valid MIME type, and does not have blocked characters in its file name. In other words, there is no validation to ensure that the file extension actually matches the MIME type.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-stories-xmcyber-d)

This allows an attacker to upload a polyglot shell via an HTTP POST request to the "/rest/default/V1/guest-carts/{cart\_id}/items" endpoint and invoke that file to achieve code execution. An important caveat here is that the uploaded file is only accessible if the web server is misconfigured; any attempt to access it will result in a 404 error message.

"If you're using Adobe’s suggested Nginx/Apache configurations, then the files are inaccessible and not executable," security researcher Tomais Williamson said. "However, any deviations from this configuration (or missing .htaccess files) may lead to instances being impacted."

"For Nginx instances, Magento ships with an example configuration file that should block access to the folders and any uploaded PHP files. Deviations from this configuration that remove the deny all clauses locations affecting the pub/media/custom\_options path can lead to XSS, and removing .php execution restrictions will lead to those files being executable."

*(The story was updated after publication to include insights from Searchlight Cyber about PolyShell.)*

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

[Adobe Commerce](https://thehackernews.com/search/label/Adobe%20Commerce), ...