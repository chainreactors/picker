---
title: Critical React Native CLI Flaw Exposed Millions of Developers to Remote Attacks
url: https://thehackernews.com/2025/11/critical-react-native-cli-flaw-exposed.html
source: The Hacker News
date: 2025-11-04
fetch_date: 2025-11-05T03:12:46.908965
---

# Critical React Native CLI Flaw Exposed Millions of Developers to Remote Attacks

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Critical React Native CLI Flaw Exposed Millions of Developers to Remote Attacks](https://thehackernews.com/2025/11/critical-react-native-cli-flaw-exposed.html)

**Nov 04, 2025**Ravie LakshmananVulnerability / Supply Chain Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfNjN6vslUO_G4CduAbYSiA-CSV2SWczVdx8dOAdaWXrulZW9P3iJ6fkO1bN_PlrN1g7pExIbB5QdeO9h7yNQE2yVdSzg2OfbL1N6_K-bNhsguE9GHUilLuEuzpfybL2So0N9yP9J3UiTjjZhyphenhyphen571M1PCgZc4nv-woAH4Ja7q8rl8GZ3rQr4I7tPDhQu4p/s2600/code.jpg)

Details have emerged about a now-patched critical security flaw in the popular "[@react-native-community/cli](https://www.npmjs.com/package/%40react-native-community/cli)" npm package that could be potentially exploited to run malicious operating system (OS) commands under certain conditions.

"The vulnerability allows remote unauthenticated attackers to easily trigger arbitrary OS command execution on the machine running react-native-community/cli's development server, posing a significant risk to developers," JFrog Senior Security Researcher Or Peles [said](https://jfrog.com/blog/cve-2025-11953-critical-react-native-community-cli-vulnerability) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The vulnerability, tracked as **[CVE-2025-11953,](https://nvd.nist.gov/vuln/detail/CVE-2025-11953)** carries a CVSS score of 9.8 out of a maximum of 10.0, indicating critical severity. It also affects the "@react-native-community/cli-server-api" package versions 4.8.0 through 20.0.0-alpha.2, and has been [patched](https://github.com/react-native-community/cli/commit/15089907d1f1301b22c72d7f68846a2ef20df547) in [version 20.0.0](https://github.com/react-native-community/cli/releases/tag/v20.0.0) released early last month.

The [command-line tools package](https://github.com/react-native-community/cli), which is maintained by Meta, enables developers to build React Native mobile applications. It receives approximately 1.5 million to 2 million downloads per week.

According to the software supply chain security firm, the vulnerability arises from the fact that the [Metro development server](https://reactnative.dev/docs/metro) used by React Native to build JavaScript code and assets binds to external interfaces by default (instead of localhost) and exposes an "/open-url" endpoint that is susceptible to OS command injection.

"The server's '/open-url' endpoint handles a POST request that includes a user-input value that is passed to the unsafe open() function provided by the open NPM package, which will cause OS command execution," Peles said.

As a result, an unauthenticated network attacker could weaponize the flaw to send a specially crafted POST request to the server and run arbitrary commands. On Windows, the attackers can also execute arbitrary shell commands with fully controlled arguments, while on Linux and macOS, it can be abused to execute arbitrary binaries with limited parameter control.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

While the issue has since been addressed, developers who use React Native with a framework that doesn't rely on Metro as the development server are not impacted.

"This zero day vulnerability is particularly dangerous due to its ease of exploitation, lack of authentication requirements and broad attack surface," Peles said. "It also exposes the critical risks hidden in third-party code."

"For developer and security teams, this underscores the need for automated, comprehensive security scanning across the software supply chain to ensure easily exploitable flaws are remediated before they impact your organization."

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

[Command Injection](https://thehackernews.com/search/label/Command%20Injection)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[JFrog](https://thehackernews.com/search/label/JFrog)[Meta](https://thehackernews.com/search/label/Meta)[Open Source](https://thehackernews.com/search/label/Open%20Source)[React Native](https://thehackernews.com/search/label/React%20Native)[Software Vulnerability](https://thehackernews.com/search/label/Software%20Vulnerability)[Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-ai-security)

Trending News

[![⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens](data:image/svg+xml;base64... "⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens")

⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens](https://thehackernews.com/2025/10/weekly-recap-wsus-exploited-lockbit-50.html)

[![ThreatsDay Bulletin: $176M Crypto Fine, Hacking Formula 1, Chromium Vulns, AI Hijack and More](data:image/svg+xml;base64... "ThreatsDay Bulletin: $176M Crypto Fine, Hacking Formula 1, Chromium Vulns, AI Hijack and More")

ThreatsDay Bulletin: $176M Crypto Fine, Hacking Formula 1, Chromium Vulns, AI Hijack and More](https://thehackernews.com/2025/10/threatsday-bullet...