---
title: Malicious KICS Docker Images and VS Code Extensions Hit Checkmarx Supply Chain
url: https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html
source: The Hacker News
date: 2026-04-22
fetch_date: 2026-04-23T04:45:14.250024
---

# Malicious KICS Docker Images and VS Code Extensions Hit Checkmarx Supply Chain

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [Malicious KICS Docker Images and VS Code Extensions Hit Checkmarx Supply Chain](https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html)

**Ravie Lakshmanan**Apr 22, 2026Cloud Security / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimocxAyADkuC5qBKZquZhHtUaDSArR1yrr0eRW7dQ_qo4yJpHxj2VYF0qQBxxYfhwOv5g3PJ6raoVwGHrns8DiRFppR_OPFhc2NUoVxlMc0W3fwVyR8J0daGZ_a8IOSuqL1kXJmY6Sj1bvqJ7OwkZfJQB2Cha4WldeRwCcAopoTllcER15ca3eFwsibt6i/s1700-e365/kics.jpg)

Cybersecurity researchers have warned of malicious images pushed to the official "[checkmarx/kics](https://hub.docker.com/r/checkmarx/kics)" Docker Hub repository.

In an alert published today, software supply chain security company Socket [revealed](https://socket.dev/blog/checkmarx-supply-chain-compromise) that unknown threat actors managed to have overwritten existing tags, including v2.1.20 and alpine, while also introducing a new v2.1.21 tag that does not correspond to an official release. The Docker repository has been archived as of writing.

"Analysis of the poisoned image indicates that the bundled KICS binary was modified to include data collection and exfiltration capabilities not present in the legitimate version," Socket said.

"The malware could generate an uncensored scan report, encrypt it, and send it to an external endpoint, creating a serious risk for teams using KICS to scan infrastructure-as-code files that may contain credentials or other sensitive configuration data."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agentic-guide-d-3)

Further analysis of the incident has uncovered that related Checkmarx developer tooling may also have been affected, such as recent Microsoft Visual Studio Code extension releases that come with malicious code to download and run a remote addon through the Bun runtime.

"The behavior appeared in versions 1.17.0 and 1.19.0, was removed in 1.18.0, and relied on a hardcoded GitHub URL to fetch and run additional JavaScript without user confirmation or integrity verification," Socket added.

Organizations that may have used the affected KICS image to scan Terraform, CloudFormation, or Kubernetes configurations should treat any secrets or credentials exposed to those scans as likely compromised.

"The evidence suggests this is not an isolated Docker Hub incident, but part of a broader supply chain compromise affecting multiple Checkmarx distribution channels," the company noted.

The Hacker News has contacted Checkmarx for further information, and we will update the story if we hear back.

*(This is a developing story. Please check back for more details.)*

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

[Checkmarx](https://thehackernews.com/search/label/Checkmarx), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Docker](https://thehackernews.com/search/label/Docker), [Malware](https://thehackernews.com/search/label/Malware), [software security](https://thehackernews.com/search/label/software%20security), [supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack), [Visual Studio Code](https://thehackernews.com/search/label/Visual%20Studio%20Code)

Trending News

[![108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](data:image/svg+xml;base64... "108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users")

108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html)

[![Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads](data:image/svg+xml;base64... "Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads")

Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads](https://thehackernews.com/2026/04/mirax-android-rat-turns-devices-into.html)

[![New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released](data:image/svg+xml;base64... "New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released")

New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released](https://thehackernews.com/2026/04/new-php-composer-flaws-enable-arbitrary.html)

[![OpenAI Launches GPT-5.4-Cyber with Expanded Access for Security Teams](data:image/svg+xml;base64... "OpenAI Launches GPT-5.4-Cyber with Expanded Access for Security Teams")

OpenAI Launches GPT-5.4-Cyber with Expanded Access for Security Teams](https://thehackernews.com/2026/04/openai-launches-gpt-54-cyber-with.html)

[![Microsoft Issues Patches for SharePoint Zero-Day and 168 Other New Vulnerabilities](data:image/svg+xml;base64... "Microsoft Issues Patches for SharePoint Zero-Day and 168 Other New Vulnerabilities")

Microsoft Issues Patches for SharePoint Zero-Day and 168 Other New Vulnerabilities](https://thehackernews.com/2026/04/microsoft-issues-patches-for-sharepoint.html)

[![Actively Exploited nginx-ui Flaw (CVE-2026-33032) Enables Full Nginx Server Takeover](data:image/svg+xml;base64... "Actively Exploited nginx-ui Flaw (CVE-2026-33032) Enables Full Nginx Server Takeover")

Actively Exploited nginx-ui Flaw (CVE-2026-33032) Enables Full Nginx Server Takeover](https://thehackernews.com/2026/04/critical-nginx-ui-vulnerability-cve.html)

[![n8n Webhooks Abused Si...