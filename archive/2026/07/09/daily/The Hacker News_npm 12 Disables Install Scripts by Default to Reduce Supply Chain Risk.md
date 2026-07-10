---
title: npm 12 Disables Install Scripts by Default to Reduce Supply Chain Risk
url: https://thehackernews.com/2026/07/npm-12-disables-install-scripts-by.html
source: The Hacker News
date: 2026-07-09
fetch_date: 2026-07-10T06:00:13.067531
---

# npm 12 Disables Install Scripts by Default to Reduce Supply Chain Risk

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [npm 12 Disables Install Scripts by Default to Reduce Supply Chain Risk](https://thehackernews.com/2026/07/npm-12-disables-install-scripts-by.html)

**Ravie Lakshmanan**Jul 09, 2026Supply Chain Security / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbP2w2lzNWbB041oSXvx2Nb1uOJaf81XNUBioDv_3K73S-JnzIU4OnUHfwG3Q3RLbf_p2wJBpHC0m2M4cQhCMfcSRRx1MY9n2vCVSNI4ddai3uJ3eE2Kb-d_ryU_HSEx_R2Rjoxz2D3TBcZCgLRWf-rOBf9k73Vi1Q04aWNG9Ux-A5AOf-v1HjSGD3YZcg/s1700-e365/npm-security.jpg)

GitHub has officially [announced](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/) the release of npm version 12 with install scripts disabled by default, along with deprecating granular access tokens (GATs) designed to bypass two-factor authentication (2FA).

The Microsoft-owned subsidiary noted that the following npm install behaviors that used to run automatically before have been made opt-in -

* allowScripts defaults to off, meaning dependency lifecycle scripts (i.e., preinstall, install, postinstall) and implicit node-gyp builds no longer run unless explicitly allowed.
* --allow-git defaults to none, meaning --allow-git defaults to none: Git dependencies (direct or transitive) are no longer resolved unless explicitly allowed.
* --allow-remote defaults to none, meaning dependencies from remote URLs (e.g., https tarballs) are no longer resolved unless explicitly allowed.

To review and approve trusted scripts, users are now required to run: "npm approve-scripts --allow-scripts-pending," then commit the resulting allowlist in the "package.json" file.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

It's worth noting that these changes were [previewed](https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html) last month, with GitHub recommending developers to upgrade to npm 11.16.0 or newer, run the normal install command, and review the warnings displayed.

The latest npm release version also introduces two new changes -

* npm GATs configured to bypass 2FA will no longer be able to perform sensitive account, package, and organization management actions. This includes creating or deleting tokens, generating recovery codes and changing npm account password, email, profile, or 2FA configuration, changing package access, maintainers, or trusted publishing configuration, and managing organization and team membership as well as their package grants.
* npm GATs will no longer retain the ability to publish directly. Their publishing surface will be limited to reading private packages and staging a publish, where a package only becomes public after a human 2FA approval.

The first of two changes is expected to take effect in early August 2026. In the interim, it's advised to stop using 2FA-bypass tokens for the aforementioned operations and perform them interactively with 2FA. The second change is scheduled for January 2027.

"To prepare, plan to move automated publishing to trusted publishing (OIDC) or staged publishing with a human approval step, rather than a long-lived publish token," GitHub said.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

The development comes as pnpm 11.10 [introduces](https://pnpm.io/blog/releases/11.10) a new "\_auth" setting for configuring registry authentication as a single structured, URL-keyed value.

"The security benefit is that the credential and the host it belongs to travel together, and pnpm reads \_auth only from the environment or the global config, never from a project's files," Socket [explained](https://socket.dev/blog/pnpm-11-1-hardens-registry-authentication).

"That means a malicious or compromised pnpm-workspace.yaml or .npmrc inside a repository cannot point a valid token at a different host. A tampered project file is a common way attackers get a foothold, and redirecting a registry token is a direct route to stealing it, so closing that path removes exposure."

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

[Authentication](https://thehackernews.com/search/label/Authentication), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [DevSecOps](https://thehackernews.com/search/label/DevSecOps), [GitHub](https://thehackernews.com/search/label/GitHub), [NPM](https://thehackernews.com/search/label/NPM), [Open Source](https://thehackernews.com/search/label/Open%20Source), [Package Management](https://thehackernews.com/search/label/Package%20Management), [Software Development](https://thehackernews.com/search/label/Software%20Development), [Software Security](https://thehackernews.com/search/label/Software%20Security), [Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security)

⚡ Top Stories This Week

[![ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware +...