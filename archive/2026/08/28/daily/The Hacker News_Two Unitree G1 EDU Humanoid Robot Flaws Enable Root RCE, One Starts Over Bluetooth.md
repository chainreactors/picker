---
title: Two Unitree G1 EDU Humanoid Robot Flaws Enable Root RCE, One Starts Over Bluetooth
url: https://thehackernews.com/2026/08/two-unitree-g1-edu-humanoid-robot-flaws.html
source: The Hacker News
date: 2026-08-28
fetch_date: 2026-08-29T08:33:12.437781
---

# Two Unitree G1 EDU Humanoid Robot Flaws Enable Root RCE, One Starts Over Bluetooth

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

# [Two Unitree G1 EDU Humanoid Robot Flaws Enable Root RCE, One Starts Over Bluetooth](https://thehackernews.com/2026/08/two-unitree-g1-edu-humanoid-robot-flaws.html)

**Swati Khandelwal**Aug 28, 2026Vulnerability / IoT Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKqNVrCXSaUDXfrGPJkoRoXBPQW4qwhdYqm2SMVaunZNwBrQ4FbURK-gtVawzaje20fK_m9q2dKepfj-dxmkvfKL4se3ZQ1YAI3iogqCft1UjVadJa_uBoQxFuoBpWfx2Dh3S4-jQLa7c4E9OOyQfVAT5BVKVShPykiPWEuYcchIPHFC4e5GduyW4iBio/s1700-e365/Humanoid.jpg)

Security researcher **Olivier Laflamme** has disclosed two independent root remote code execution (RCE) chains affecting the **Unitree G1 EDU**, including a Bluetooth Low Energy (BLE) path that can reach root on the robot's Locomotion PC.

The flaws are tracked as **CVE-2026-76639** and **CVE-2026-76640**, with the first involving a network-adjacent path through chat\_go and bashrunner and the second beginning from BLE proximity.

An exact fixed firmware release has not been verified in any accessible Unitree guidance, leaving G1 EDU owners without a confirmed release target for either vulnerability.

Laflamme said Unitree patched the cloud account-to-robot ownership check in July 2026. As of the August 27 disclosure, the current cloud-assisted route requires an account bound to the target G1 or the relevant key material already in hand.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Laflamme published the research on August 27, 2026, describing the two issues as separate root-RCE paths. The research timeline shows Laflamme upgraded the test robot to V1.5.2, but that sequence does not by itself establish V1.5.1.1 as affected.

In his [technical disclosure](https://boschko.ca/g1-ble-rce/), Laflamme said CVE-2026-76639 uses a path-traversal condition in chat\_go to reach bashrunner. Execution through bashrunner results in root code execution on the Locomotion PC.

Laflamme described CVE-2026-76639 as an independent RCE, although he reused it as one disclosure primitive while demonstrating the separate BLE chain tracked as CVE-2026-76640.

For CVE-2026-76640, the initial BLE write path accepts the bootstrap interaction without Bluetooth pairing. The bootstrap material itself remains protected, and the later Wi-Fi provisioning operations require the application's authenticated BLE state.

During Laflamme's research, Unitree's cloud service accepted a valid Unitree account for the key-recovery request but did not verify that the account owned the supplied robot.

That authorization gap allowed the account to recover key material associated with another G1 EDU. The recovered key could then be used to establish the authenticated BLE state required by the Wi-Fi provisioning operations.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The chain then reached the Wi-Fi provisioning code. Laflamme documented a buffer overflow there that produced root execution on the Locomotion PC.

Laflamme limited his propagation test to two G1 robots in one room. He said in the August 27 disclosure that the cloud authorization fix breaks that exact proof-of-concept flow.

Unitree's [official product page](https://www.unitree.com/g1/) distinguishes the G1 and G1 EDU as separate models, while broader applicability of the two new vulnerabilities to other Unitree robots remains unconfirmed.

The Hacker News has reached out to Unitree to confirm the fixed firmware versions, the affected product scope, and the current remediation status, and will update the story with any response.

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

[Bluetooth](https://thehackernews.com/search/label/Bluetooth), [Humanoid](https://thehackernews.com/search/label/Humanoid), [iot security](https://thehackernews.com/search/label/iot%20security), [network security](https://thehackernews.com/search/label/network%20security), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Wireless Security](https://thehackernews.com/search/label/Wireless%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Microsoft Patches Severe Entra ID Flaw (CVSS 10.0) Allowing Remote Code Execution](https://thehackernews.com/2026/08/microsoft-entra-id-flaw-cvss-100.html)

[![The Hacker News](data:image/svg+xml;base64...)

ThreatsDay: Gogs 10.0 RCE, n8n Workflow-to-RCE, $10M Reward, GLM-5.3 AI Exploit, and More](https://thehackernews.com/2026/08/threatsday-gogs-100-rce-n8n-workflow-to.html)

[![The Hacker News](data:image/svg+xml;base64...)

New Cryptographic Context Injection Attack Could Let Web Pages Steal Grok Chat Data](https://thehackernews.com/2026/08/new-cryptographic-context-injection.html)

[![The Hacker News](data:image/svg+xml;base64...)

Zombie Card Attack Can Revive Expired Visa Cards for Contactless Payments](https://thehackernews.com/2026/08/zombie-card-attack-can-revive-expired.html)

[![The Hacker News](data:image/svg+xml;base64...)

CDN Tsunami Attack Abuses HTTP/3 Translation for Up to 350x DoS Amplification](https:/...