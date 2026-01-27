---
title: Malicious VS Code AI Extensions with 1.5 Million Installs Steal Developer Source Code
url: https://thehackernews.com/2026/01/malicious-vs-code-ai-extensions-with-15.html
source: The Hacker News
date: 2026-01-26
fetch_date: 2026-01-27T03:39:24.087240
---

# Malicious VS Code AI Extensions with 1.5 Million Installs Steal Developer Source Code

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

# [Malicious VS Code AI Extensions with 1.5 Million Installs Steal Developer Source Code](https://thehackernews.com/2026/01/malicious-vs-code-ai-extensions-with-15.html)

**Ravie Lakshmanan**Jan 26, 2026AI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg49NKLNdavByN_ZLXIkm8VafhlYDmDWXS4I1YT6O2_xyZmEjr6jrSZekKsG_okVhIyWfOrpoYKeafU7Rcr0bcyAv26yFlLaPSVUxcHRAxCh3s-buWWhYNucoT4PAi8SAXbqFaB4hTCKo34VYBLEw58w6KwxmClWkaJbRwOIkyAW-PEGKQWRfb3gYzsSsw8/s1700-e365/vscode.jpg)

Cybersecurity researchers have [discovered](https://www.koi.ai/blog/maliciouscorgi-the-cute-looking-ai-extensions-leaking-code-from-1-5-million-developers) two malicious Microsoft Visual Studio Code (VS Code) extensions that are advertised as artificial intelligence (AI)-powered coding assistants, but also harbor covert functionality to siphon developer data to China-based servers.

The extensions, which have 1.5 million combined installs and are still available for download from the official [Visual Studio Marketplace](https://github.com/microsoft/vsmarketplace/blob/main/RemovedPackages.md), are listed below -

* ChatGPT - 中文版 (ID: whensunset.chatgpt-china) - 1,340,869 installs
* ChatGPT - ChatMoss（CodeMoss）(ID: zhukunpeng.chat-moss) - 151,751 installs

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

Koi Security said the extensions are functional and work as expected, but they also capture every file being opened and every source code modification to servers located in China without users' knowledge or consent. The campaign has been codenamed MaliciousCorgi.

"Both contain identical malicious code -- the same spyware infrastructure running under different publisher names," security researcher Tuval Admoni said.

What makes the activity particularly dangerous is that the extensions work exactly as advertised, providing autocomplete suggestions and explaining coding errors, thereby avoiding raising any red flags and lowering the users' suspicion.

At the same time, the embedded malicious code is designed to read all of the contents of every file being opened, encode it in Base64 format, and send it to a server located in China ("aihao123[.]cn"). The process is triggered for every edit.

The extensions also incorporate a real-time monitoring feature that can be remotely triggered by the server, causing up to 50 files in the workspace to be exfiltrated. Also present in the extension's web view is a hidden zero-pixel iframe that loads four commercial analytics software development kits (SDKs) to fingerprint the devices and create extensive user profiles.

The four SDKs used are Zhuge.io, GrowingIO, TalkingData, and Baidu Analytics, all of which are major data analytics platforms based in China.

## PackageGate Flaws Affect JavaScript Package Managers

The disclosure comes as the supply chain security company said it [identified](https://www.koi.ai/blog/post-shai-hulud-6-zero-days-in-js-package-managers-but-npm-wont-act) six zero-day vulnerabilities in JavaScript package managers like npm, pnpm, vlt, and Bun that could be exploited to defeat security controls put in place to skip the automatic execution of lifecycle scripts during package installation. The flaws have been collectively named PackageGate.

Defenses such as disabling lifecycle scripts ("--ignore-scripts") and committing lockfiles ("package-lock.json") have become crucial mechanisms to confronting [supply chain attacks](https://thehackernews.com/2025/12/researchers-spot-modified-shai-hulud.html), especially in the aftermath of [Shai-Hulud](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/), which leverages postinstall scripts to spread in a worm-like manner to hijack npm tokens and publish malicious versions of the packages to the registry.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

However, Koi found that it's possible to bypass script execution and lockfile integrity checks in the four package managers. Following responsible disclosure, the issues have been addressed in pnpm ([version 10.26.0](https://github.com/pnpm/pnpm/releases/tag/v10.26.0)), vlt ([version 1.0.0-rc.10](https://github.com/vltpkg/vltpkg/releases/tag/v1.0.0-rc.10)), and [Bun](https://bun.com/blog/bun-v1.3.5#security) ([version 1.3.5](https://github.com/oven-sh/bun/releases/tag/bun-v1.3.5)). Pnpm is tracking the two vulnerabilities as [CVE-2025-69264](https://github.com/pnpm/pnpm/security/advisories/GHSA-379q-355j-w6rj) (CVSS score: 8.8) and [CVE-2025-69263](https://github.com/pnpm/pnpm/security/advisories/GHSA-7vhp-vf5g-r2fw) (CVSS score: 7.5).

Npm, however, has opted not to fix the vulnerability, stating "users are responsible for vetting the content of packages that they choose to install." When reached for comment, a GitHub spokesperson told The Hacker News that's working actively to address the new issue as npm actively scans for malware in the registry.

"If a package being installed through git contains a prepare script, its dependencies and devDependencies will be installed. As we shared when the ticket was filed, this is an intentional design and works as expected," the company said. "When users install a git dependency, they are trusting the entire contents of that repository, including its configuration files."

The Microsoft-owned subsidiary has also urged projects to [adopt trusted publishing](https://github.blog/security/supply-chain-security/strengthening-supply-chain-security-preparing-for-the-next-malware-campaign/) and granular access tokens with enforced two-factor authentication (2FA) to secure the software supply chain. As of September 2025, GitHub has [deprecated](https://thehackernews.com/2025/09/github-mandates-2fa-and-short-lived.html) legacy classic tokens, limited granular tokens with publishing permissions to a shorter expiration, and removed the option to bypass 2FA for local package publishing.

"The standard advice, disable scripts and commit your lockfiles, is still worth following," security researcher Oren Yomtov said. "But it's not the complete picture. Until PackageGate is fully addressed, organizations need to make their own informed choices about risk."

*(The story was updated after publica...