---
title: GitHub Launches npm Firewall to Block Malicious Packages Before Installation
url: https://thehackernews.com/2026/10/github-launches-npm-firewall-to-block.html
source: The Hacker News
date: 2026-10-29
fetch_date: 2026-10-30T07:56:34.159686
---

# GitHub Launches npm Firewall to Block Malicious Packages Before Installation

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [GitHub Launches npm Firewall to Block Malicious Packages Before Installation](https://thehackernews.com/2026/10/github-launches-npm-firewall-to-block.html)

**Ravie Lakshmanan**Oct 29, 2026DevSecOps / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJ7hXo0MoiQiXCSLnOj0h2YUqDhIHl13Le4XxOU3UxV7X2mm4_YGJKOT6akyW58uRaMhslGN6NY9B_1u7V-y_fy0kYJHKoVA-yBWVt53xqBk06_syRpASgWezvnVIZs9goRlwNrp_HMVj_Pu8rzXmIsfJBV1YzhJ8IAd-1g7FFVhFWqc9HegTk4Jok5kR9/s1700-nu-rw-lo-l85-e365/github.gif)

GitHub has announced that it's introducing a new package firewall as a preview to block installation of suspicious npm packages during installation time.

"The firewall inspects both metadata requests and package downloads for signs of malicious activity, acting as an install-time policy gate," GitHub [said](https://github.blog/changelog/2026-10-20-github-package-firewall-in-public-preview/).

The feature, which currently supports only npm packages, is available in public preview for all GitHub Enterprise Cloud customers, including data-resident GitHub Enterprise Cloud.

According to the Microsoft subsidiary, the firewall is placed between endpoints or internal registries and the upstream package repositories so as to deter malware attacks that compromise systems when packages are installed.

This behavior can expose users to severe security risks, especially when artificial intelligence (AI) agents and CI runners automatically install dependencies to complete a task or build without their explicit permission.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The idea is that endpoints like coding agents and CI/CD hosts use the firewall for their requests instead of directly pointing to the public package registries. The firewall then checks package downloads against policy controls such as minimum package age and malware advisories, and blocks downloads that do not meet those policies.

To use the firewall, administrators are [required](https://docs.github.com/en/enterprise-cloud%40latest/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/protecting-endpoints-with-package-firewall) to configure policy controls, such as the ones listed below -

* Block known malware by checking against the [GitHub Advisory Database](https://github.com/advisories) for active malware advisories
* Block packages based on the severity of vulnerabilities by checking the GitHub Advisory Database for flaws that affect the requested package version. The control defaults to "Critical only" as the severity level that blocks an installation, although users can choose "High or higher," "Medium or higher," or "Any severity."
* Block attestation downgrades by comparing attestations for the requested package version with those of earlier versions and stop the download if the requested version does not have an SLSA attestation.
* Block newly-introduced install scripts by checking whether the package recently added scripts that run using preinstall or postinstall hooks, which can be abused to steal sensitive data.

Block packages based on a cooldown period that prevents versions that are newer than the configured minimum age from being installed. The value can range from 1 to 365 days. The default value is 1 day. Users can disable it by setting it to 0.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibKYDqs7uj7FfPNFhcDva0WE1FBavHs_x6guDnl12vmfcd-d-A3a0sovkR4h4GixSXVsy-RzdzfZCSvqO1KVJwdhpGhG9PFXjF2-OYZSo_DCU6fZQb5IXxyfuYzWtU6c0blrdwiCjJQ_OUhn7mTZeO79DEIItwp3x9t3YNEyt-8BZ1mup0uMWGA0xfBapf/s1700-nu-rw-lo-l85-e365/protect_endpoint_header.jpeg)

Users who need access to a package that gets blocked erroneously by the firewall can submit an exception request, which can then be approved by enterprise administrators and security managers.

The development comes as Rust 1.100, which is scheduled for release on November 12, 2026, readies to add support for a configurable minimum publish age, allowing security scanners and maintainers time to flag and block malicious crate releases before they can be installed or used by users.

The value, defined via the "[global-min-publish-age](https://doc.rust-lang.org/beta/cargo/reference/config.html#registryglobal-min-publish-age)" option in "cargo/config.toml," allows users to specify a minimum publication age in days or weeks. If left unspecified, a seven-day waiting period is applied by default to skip releases published within that window.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Over the past year, [similar waiting periods](https://thehackernews.com/2026/07/github-adds-3-day-dependabot-cooldown.html) have been [implemented](https://thehackernews.com/2026/06/vs-code-adds-2-hour-extension-auto.html) across [open-source ecosystems](https://cloudsmith.com/blog/how-to-configure-time-for-cooldown-policies), including npm, Python, Microsoft Visual Studio Code, Ruby, Bun, pnpm, and Yarn, as a way to bolster software supply chain security by reducing the chance that a newly published, unreviewed version is immediately pulled into a build.

Cooldown periods help add friction and slow down attacks in which a bad actor publishes a poisoned version of a popular package after seizing control of a maintainer account, thereby preventing rapid spread through manual or automated installations.

"The tradeoff is that legitimate fixes have to wait, too, unless developers make an exception," Socket [said](https://socket.dev/blog/rust-cargo-cooldowns). "Malicious code also doesn't magically become harmless with age. A release that escapes detection can simply outlast the cooldown. The value is in buying researchers, maintainers, and registries time to act before the next dependency update carries an attack further."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQkl...