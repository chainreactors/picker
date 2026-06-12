---
title: GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks
url: https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html
source: The Hacker News
date: 2026-06-11
fetch_date: 2026-06-12T06:28:10.951825
---

# GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks](https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html)

**Ravie Lakshmanan**Jun 11, 2026Developer Security / Software Supply Chain

[![Supply Chain Attacks](data:image/png;base64... "Supply Chain Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_yyoUTLr71Ug2Ge0R7qFSnlGjB3TzlrQ-2NDR5jpPSBjivUSxhxRV1eCg5E6Af15RbJLZpqg9Ohp9ZW9YC9D2oc3VcHrNYQetavvvarn-Pn1P4VWnMw2C-hXbFgplFW9O8pe-zSP9ABGkkR-LM8hhu370dXMgeV-TGQT2p9N7hd7Friim3UkdK5FfyHHp/s1700-e365/npm-github.jpg)

GitHub has [announced](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/) what it said are "breaking changes" coming to npm version 12, one of which turns off install scripts by default to combat software supply chain threats.

The changes aim to combat [attack techniques](https://thehackernews.com/2026/05/malicious-npm-package-stole-files-from.html) that abuse the "npm install" command to trigger the execution of malicious code using npm lifecycle hooks. "Npm install" is used to download and install all the necessary dependencies for a Node.js project. Version 12 is scheduled for release next month.

Describing install-time lifecycle scripts as the "single largest code-execution surface in the npm ecosystem," GitHub [said](https://github.com/orgs/community/discussions/198547) the "npm install" command runs scripts from every transitive dependency, as a result of which a single compromised package anywhere in the dependency tree can run arbitrary code on a developer machine or CI runner.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

By blocking such behaviours, the idea is to require explicit user approval before code execution is initiated automatically during "npm install" as opposed to being trusted by default. "Making script execution opt-in closes that path while keeping it one command away for the packages you trust," GitHub said.

The changes are listed below -

* npm install will no longer execute preinstall, install, or postinstall scripts from dependencies unless they are explicitly allowed in the project.
* npm install will no longer resolve Git dependencies, either direct or transitive, unless explicitly allowed via --allow-git.
* npm install will no longer resolve dependencies from remote URLs, such as https tarballs, unless explicitly allowed via --allow-remote.

"This includes native node-gyp builds (i.e., a package with a binding.gyp and no explicit install script still gets blocked, because npm runs an implicit node-gyp rebuild for it)," the Microsoft-owned subsidiary said about changes to the default "allowScripts" behavior. "prepare scripts from git, file, and link dependencies are blocked the same way."

By defaulting "--allow-git" to "none," the setting closes out a code execution path where a Git dependency's .npmrc configuration file used could override the Git executable, even with [--ignore-scripts](https://www.nodejs-security.com/blog/npm-ignore-scripts-best-practices-as-security-mitigation-for-malicious-packages), a flag that prevents packages specified in a package.json file from automatically running built-in lifecycle scripts during the installation process.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

GitHub recommends that developers prepare for these changes by upgrading to npm 11.16.0 or newer, running the normal install, and reviewing the warnings displayed.

"Use npm approve-scripts --allow-scripts-pending to see which packages have scripts, approve the ones you trust, and commit the updated package.json," it added. "After that, only the scripts you approved keep running once you upgrade. Anything you leave unapproved will stop."

Earlier this year, npm also [introduced](https://thehackernews.com/2026/06/vs-code-adds-2-hour-extension-auto.html) "min-release-age," a setting that tells npm to reject any package version published less than a specified number of days as a safeguard against newly published malicious packages.

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

[CI](https://thehackernews.com/search/label/CI), [Code Execution](https://thehackernews.com/search/label/Code%20Execution), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Developer Security](https://thehackernews.com/search/label/Developer%20Security), [GitHub](https://thehackernews.com/search/label/GitHub), [Malware](https://thehackernews.com/search/label/Malware), [node.js](https://thehackernews.com/search/label/node.js), [NPM](https://thehackernews.com/search/label/NPM), [Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)

⚡ Top Stories This Week

[![Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now](data:image/svg+xml;base64... "Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now")

Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now](https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html)

[![New FROST Attack Lets Websites Track What Sites and Apps You Open via SSD Timing](data...