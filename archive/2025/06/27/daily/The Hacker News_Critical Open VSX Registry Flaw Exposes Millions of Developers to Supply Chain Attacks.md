---
title: Critical Open VSX Registry Flaw Exposes Millions of Developers to Supply Chain Attacks
url: https://thehackernews.com/2025/06/critical-open-vsx-registry-flaw-exposes.html
source: The Hacker News
date: 2025-06-27
fetch_date: 2025-10-06T22:57:05.345369
---

# Critical Open VSX Registry Flaw Exposes Millions of Developers to Supply Chain Attacks

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

# [Critical Open VSX Registry Flaw Exposes Millions of Developers to Supply Chain Attacks](https://thehackernews.com/2025/06/critical-open-vsx-registry-flaw-exposes.html)

**Jun 26, 2025**Ravie LakshmananOpen Source / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEEHqPrHq7VmKAMERwPU9ds2PToOWXTPMLkzIZ3Or4-l3pIxtUnHLaajhJccDlqLZ91_9S7Np90S2W7dJibBBGcTUqmBeVo5WJoJlHcfB_W9oPMoqedq0gi3iPdKGWNSPb3TAlrBqk0KSLXUzI6aCTiNUlLyheRA7TG_nUUjXuTrEJse0LIiuPMRfF9xsV/s790-rw-e365/openvsx.png)

Cybersecurity researchers have disclosed a critical vulnerability in the Open VSX Registry ("open-vsx[.]org") that, if successfully exploited, could have enabled attackers to take control of the entire Visual Studio Code extensions marketplace, posing a severe supply chain risk.

"This vulnerability provides attackers full control over the entire extensions marketplace, and in turn, full control over millions of developer machines," Koi Security researcher Oren Yomtov [said](https://blog.koi.security/marketplace-takeover-how-we-couldve-taken-over-every-developer-using-a-vscode-fork-f0f8cf104d44). "By exploiting a CI issue a malicious actor could publish malicious updates to every extension on Open VSX."

Following responsible disclosure on May 4, 2025, multiple rounds of fixes were proposed by the maintainers, before a final patch was deployed on June 25.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Open VSX Registry is an open-source project and alternative to the Visual Studio Marketplace. It's [maintained](https://newsroom.eclipse.org/news/announcements/open-vsx-registry-vendor-neutral-open-source-alternative-visual-studio) by the Eclipse Foundation. Several code editors like Cursor, Windsurf, Google Cloud Shell Editor, Gitpod, and others integrate it into their services.

"This widespread adoption means that a compromise of Open VSX is a supply-chain nightmare scenario," Yomtov said. "Every single time an extension is installed, or an extension update fetched silently in the background, these actions go through Open VSX."

The vulnerability discovered by Koi Security is rooted in the [publish-extensions repository](https://github.com/EclipseFdn/publish-extensions), which includes scripts to publish open-source VS Code extensions to open-vsx.org.

Developers can [request](https://github.com/EclipseFdn/open-vsx.org/wiki/Auto-Publishing-Extensions) their extension to be auto-published by submitting a pull request to add it to the extensions.json file present in the repository, after which it's approved and merged.

In the backend, this plays out in the form of a [GitHub Actions workflow](https://github.com/EclipseFdn/publish-extensions/actions/workflows/publish-extensions.yml) that's [daily run](https://github.com/EclipseFdn/publish-extensions/blob/master/.github/workflows/publish-extensions.yml) at 03:03 a.m. UTC that takes as input a list of comma-separated extensions from the JSON file and publishes them to the registry using the [vsce npm package](https://www.npmjs.com/package/%40vscode/vsce).

"This workflow runs with privileged credentials including a secret token (OVSX\_PAT) of the @open-vsx service account that has the power to publish (or overwrite) any extension in the marketplace," Yomtov said. "In theory, only trusted code should ever see that token."

"The root of the vulnerability is that npm install runs the arbitrary build scripts of all the auto-published extensions, and their dependencies, while providing them with access to the OVSX\_PAT environment variable."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This means that it's possible to obtain access to the @open-vsx account's token, enabling privileged access to the Open VSX Registry, and providing an attacker with the ability to publish new extensions and tamper with existing ones to insert malicious code.

The risk posed by extensions has not gone unnoticed by MITRE, which has introduced a new "[IDE Extensions](https://attack.mitre.org/techniques/T1176/002/)" technique in its ATT&CK framework [as of April 2025](https://attack.mitre.org/resources/updates/updates-april-2025/), stating it could be abused by malicious actors to establish persistent access to victim systems.

"Every marketplace item is a potential backdoor," Yomtov said. "They're unvetted software dependencies with privileged access, and they deserve the same diligence as any package from PyPI, npm, Hugginface, or GitHub. If left unchecked, they create a sprawling, invisible supply chain that attackers are increasingly exploiting."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[GitHub Actions](https://thehackernews.com/search/label/GitHub%20Actions)[IDE Security](https://thehackernews.com/search/label/IDE%20Security)[MITRE ATT&CK](https://thehackernews.com/search/label/MITRE%20ATT%26CK)[NPM](https://thehackernews.com/search/label/NPM)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Open VSX](https://thehackernews.com/search/label/Open%20VSX)[Supply Chain Security](https://theha...