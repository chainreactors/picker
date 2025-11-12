---
title: Researchers Detect Malicious npm Package Targeting GitHub-Owned Repositories
url: https://thehackernews.com/2025/11/researchers-detect-malicious-npm.html
source: The Hacker News
date: 2025-11-11
fetch_date: 2025-11-12T03:13:04.993389
---

# Researchers Detect Malicious npm Package Targeting GitHub-Owned Repositories

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

# [Researchers Detect Malicious npm Package Targeting GitHub-Owned Repositories](https://thehackernews.com/2025/11/researchers-detect-malicious-npm.html)

**Nov 11, 2025**Ravie LakshmananSoftware Supply Chain / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCsz1QgtB3DAorATUJtM4NKEDKSftFK-LplwEwazMvy2CJl8Ua-T_nRLa6hpR968DBP4cjFK1rhd70vBYd_gx4s24AQepRSFpjXkFezP9hKo2lrYQm-WgcHBKvJQrU3AYRBltbe6Qw8xpGCcTFje-h3a24Pb04JtJMlUX3Ug7XtR1inGNz7fVkzpfLT_KZ/s790-rw-e365/hacker-code.jpg)

Cybersecurity researchers have discovered a malicious npm package named "@acitons/artifact" that typosquats the legitimate "[@actions/artifact](https://github.com/actions/toolkit/blob/main/packages/artifact)" package with the intent to target GitHub-owned repositories.

"We think the intent was to have this script execute during a build of a GitHub-owned repository, exfiltrate the tokens available to the build environment, and then use those tokens to publish new malicious artifacts as GitHub," Veracode [said](https://www.veracode.com/blog/malicious-npm-package-targeting-github-actions/) in an analysis.

The cybersecurity company said it observed six versions of the package – from 4.0.12 to 4.0.17 – that incorporated a post-install hook to download and run malware. That said, the latest version [available for download](https://www.npmjs.com/package/%40acitons/artifact?activeTab=versions) from npm is 4.0.10, indicating that the threat actor behind the package, [blakesdev](https://www.npmjs.com/~blakesdev), has removed all the offending versions.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The package was first uploaded on October 29, 2025, and has since accrued 31,398 weekly downloads. In total, it has been [downloaded 47,405 times](https://npm-stat.com/charts.html?package=%40acitons%2Fartifact), according to data from npm-stat. Veracode also said it identified another npm package named "8jfiesaf83" with similar functionality. It's no longer available for download, but it appears to have been [downloaded 1,016 times](https://npm-stat.com/charts.html?package=8jfiesaf83).

Further analysis of one of the malicious versions of the package has revealed that the postinstall script is configured to download a binary named "harness" from a now-removed [GitHub account](https://github.com/jmasdg). The binary is an obfuscated shell script that includes a check to prevent execution if the time is after 2025-11-06 UTC.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYMdavPmHa3pQqTQPE6UJUv5DHzDnwFdqAoJLerXVFI2ieURxmfj0_iCSXSFr8K-qgknm1BY_HwhDrs1wxfhT-amjZKQXQFm639pt_tDLo2n3w706VjQkuTHZKEhQtVPM6qfZzgtWXwo8AmIpC8j3o6jB3tr3v9lC7RdyxLwoVMH-2QFae9sacDYeS3GZo/s790-rw-e365/code-gif.jpg)

It's also designed to run a JavaScript file named "verify.js" that checks for the presence of certain GITHUB\_ variables that are set as part of a GitHub Actions workflow, and exfiltrates the collected data in encrypted format to a text file hosted on the "app.github[.]dev" subdomain.

"The malware was only targeting repositories owned by the GitHub organization, making this a targeted attack against GitHub," Veracode said. "The campaign appears to be targeting GitHub's own repositories as well as a user y8793hfiuashfjksdhfjsk which exists but has no public activity. This user account could be for testing."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data exfiltration](https://thehackernews.com/search/label/data%20exfiltration)[GitHub](https://thehackernews.com/search/label/GitHub)[Malware](https://thehackernews.com/search/label/Malware)[NPM](https://thehackernews.com/search/label/NPM)[Open Source Security](https://thehackernews.com/search/label/Open%20Source%20Security)[Package Manager](https://thehackernews.com/search/label/Package%20Manager)[Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Veracode](https://thehackernews.com/search/label/Veracode)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-ai-security)

Trending News

[![⚡ Weekly Recap: Lazarus Hits Web3, Intel/AMD TEEs Cracked, Dark Web Leak Tool and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Lazarus Hits Web3, Intel/AMD TEEs Cracked, Dark Web Leak Tool and More")

⚡ Weekly Recap: Lazarus Hits Web3, Intel/AMD TEEs Cracked, Dark Web Leak Tool and More](https://thehackernews.com/2025/11/weekly-recap-lazarus-hits-web3-intelamd.html)

[![ThreatsDay Bulletin: AI Tools in Malware, Botnets, GDI Flaws, Election Attacks](data:image/svg+xml;base64... "ThreatsDay Bulletin: AI Tools in Malware, Botnets, GDI Flaws, Election Attacks")

ThreatsDay Bulletin: AI Tools in Malware, Botnets, GDI Flaws, Election Attacks and More](https://thehackernews.com/2025/11/threatsday-bulletin-ai-tools-in-malware.html)

[![Microsoft Detects SesameOp Backdoor Using OpenAI's API as a Stealth Command Channel](data:image/svg+xml;base64... "Microsoft Detects SesameOp Backdoor Using OpenAI's API as a Stealth Command Channe...