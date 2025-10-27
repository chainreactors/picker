---
title: GitHub Mandates 2FA and Short-Lived Tokens to Strengthen npm Supply Chain Security
url: https://thehackernews.com/2025/09/github-mandates-2fa-and-short-lived.html
source: The Hacker News
date: 2025-09-24
fetch_date: 2025-10-02T20:36:51.770215
---

# GitHub Mandates 2FA and Short-Lived Tokens to Strengthen npm Supply Chain Security

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

# [GitHub Mandates 2FA and Short-Lived Tokens to Strengthen npm Supply Chain Security](https://thehackernews.com/2025/09/github-mandates-2fa-and-short-lived.html)

**Sep 23, 2025**Ravie LakshmananSupply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZQ-xcQ5PKzdd6Juz8x_31GctkkivtZYfhVKlnZ5tFKbTtwJTtmajAEiqsdZZslnaRPS9Vd3LH4mQTo9agSCG6_cEuoUU_7WCvb1e-MmDytS4hQ1x1xur0u-DTQOYAydatYghaAZjPeBttRMTKNJKmJjWtvxfYOE1UvyltBh-K5fRWNwXIsLh-lv7af27Q/s790-rw-e365/github-npm.jpg)

GitHub on Monday [announced](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/) that it will be changing its authentication and publishing options "in the near future" in response to a [recent wave](https://thehackernews.com/2025/08/malicious-nx-packages-in-s1ngularity.html) of [supply chain attacks](https://thehackernews.com/2025/09/20-popular-npm-packages-with-2-billion.html) targeting the npm ecosystem, including the [Shai-Hulud attack](https://thehackernews.com/2025/09/40-npm-packages-compromised-in-supply.html).

This includes steps to address threats posed by token abuse and self-replicating malware by allowing local publishing with required two-factor authentication (2FA), [granular tokens](https://docs.npmjs.com/about-access-tokens#about-granular-access-tokens) that will have a limited lifetime of seven days, and [trusted publishing](https://repos.openssf.org/trusted-publishers-for-all-package-repositories), which enables the ability to securely publish npm packages directly from CI/CD workflows using OpenID Connect (OIDC).

Trusted publishing, besides eliminating the need for npm tokens, establishes cryptographic trust by authenticating each publish using short-lived, workflow-specific credentials that cannot be exfiltrated or reused. Even more significantly, the npm CLI automatically generates and publishes provenance attestations for the package.

"Every package published via trusted publishing includes cryptographic proof of its source and build environment," GitHub [noted](https://github.blog/changelog/2025-07-31-npm-trusted-publishing-with-oidc-is-generally-available/) back in late July 2025. "Your users can verify where and how your package was built, increasing trust in your supply chain."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

To support these changes, the Microsoft-owned company said it will be enacting the following steps -

* Deprecate legacy classic tokens.
* Deprecate time-based one-time password (TOTP) 2FA, migrating users to FIDO-based 2FA.
* Limit granular tokens with publishing permissions to a shorter expiration.
* Set publishing access to disallow tokens by default, encouraging usage of trusted publishers or 2FA-enforced local publishing.
* Remove the option to bypass 2FA for local package publishing.
* Expand eligible providers for trusted publishing.

The development comes a week after a supply chain attack codenamed Shai-Hulud [injected](https://thehackernews.com/2025/09/40-npm-packages-compromised-in-supply.html) a self-replicating worm into hundreds of npm packages that scanned developer machines for sensitive secrets and transmitted them to an attacker-controlled server.

"By combining self-replication with the capability to steal multiple types of secrets (and not just npm tokens), this worm could have enabled an endless stream of attacks had it not been for timely action from GitHub and open source maintainers," GitHub's Xavier René-Corail said.

The changes to GitHub arrive days after the NuGet .NET package repository [added](https://learn.microsoft.com/en-us/nuget/nuget-org/trusted-publishing) support for [trusted publishing](https://devblogs.microsoft.com/dotnet/enhanced-security-is-here-with-the-new-trust-publishing-on-nuget-org/) and Ruby Central announced new measures to bolster supply chain security across RubyGems and RubyGems.

"Moving forward, only engineers employed or contracted by Ruby Central will hold administrative permissions to the RubyGems.org service," Ruby Central [said](https://rubycentral.org/news/strengthening-the-stewardship-of-rubygems-and-bundler/). "This includes both our production systems and GitHub repositories. In the near term we will temporarily hold administrative access to these projects while we finalize new policies that limit commit and organization access rights."

### Npm Package Includes QR Code-Based Technique

The disclosure comes as software supply chain security company Socket said it identified a malicious npm package named [fezbox](https://www.npmjs.com/package/fezbox) that's capable of harvesting browser passwords using a novel steganographic technique. The package is no longer available for download from npm. It attracted a total of [476 downloads](https://npm-stat.com/charts.html?package=fezbox) since it was [first published](https://secure.software/npm/packages/fezbox/versions) on August 21, 2025.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"In this package, the threat actor (npm alias janedu; registration email janedu0216@gmail[.]com) executes a payload within a QR code to steal username and password credentials from web cookies, within the browser," security researcher Olivia Brown [said](https://socket.dev/blog/malicious-fezbox-npm-package-steals-browser-passwords-from-cookies-via-innovative-qr-code).

Fezbox claims to be a JavaScript utility consisting of common helper functions. But, in reality, it harbors stealthy code to fetch a QR code from a remote URL, parse the QR code, and execute the obfuscated JavaScript payload embedded within it.

The payload, for its part, attempts to read [document.cookie](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie), extracts username and password information from the cookie, and transmits the information to an external server ("my-nest-app-production>.up.railway[.]app") via an HTTPS POST request.

"Most a...