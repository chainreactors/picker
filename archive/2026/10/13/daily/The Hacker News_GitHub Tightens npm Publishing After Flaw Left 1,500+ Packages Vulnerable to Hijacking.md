---
title: GitHub Tightens npm Publishing After Flaw Left 1,500+ Packages Vulnerable to Hijacking
url: https://thehackernews.com/2026/10/github-tightens-npm-publishing-after.html
source: The Hacker News
date: 2026-10-13
fetch_date: 2026-10-14T06:53:24.530615
---

# GitHub Tightens npm Publishing After Flaw Left 1,500+ Packages Vulnerable to Hijacking

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [GitHub Tightens npm Publishing After Flaw Left 1,500+ Packages Vulnerable to Hijacking](https://thehackernews.com/2026/10/github-tightens-npm-publishing-after.html)

**Ravie Lakshmanan**Oct 13, 2026DevSecOps / Supply Chain Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3aDWaWT6PmRDL9d6tHPDisxclb_Ak7YZIxuS02EUFvNaWrc4_UKwUqW0RI1KT3r8zsneOguD6b85yg8mf3gAzZZOGuLi-mXckG_yzwmXXb3IchTBSVeRvPlUo7QU4Kp4yiM6QqPshmo4p0GQ55XZPTEDc0DZn9N84S_ZibZ4rkXuhZ3OvoHNCYH-wk0k-/s1700-nu-rw-lo-l85-e365/git-npm.jpg)

GitHub has taken the step of expiring unvalidated npm trusted publishing configurations 48 hours after creation after researchers found that it was possible for an attacker to push new versions of a different user's package without having to steal their credentials.

"Your configuration becomes validated and exempt from expiry after its first successful publish," the Microsoft-owned subsidiary [said](https://github.blog/changelog/2026-10-02-unvalidated-npm-trusted-publishing-configurations-now-expire/). "Changing the repository or project identity requires a new trust relationship with a fresh 48-hour validation window -- ordinary edits don't restart the deadline."

The change contains the risk associated with trusting a repository or project name that changes ownership, GitHub said, adding npm also rejects trusted publishing tokens from GitHub Actions issue\_comment events going forward, along with the Existing [pull\_request\_target](https://thehackernews.com/2026/06/github-updates-actionscheckout-to-block.html) restriction.

In an update to its documentation, GitHub [states](https://docs.npmjs.com/trusted-publishers#trusted-publisher-configuration-expiry) that a newly created trusted publisher configuration must complete its first successful publish within two days, which validates the configuration and binds it to the "repository's immutable identity."

The development comes in response to findings from Bloom Security, which [discovered](https://bloom.security/blog/slugfest-millions-of-ai-agents-download-exposed-npm-packages) a loophole within npm's trusted publishing to take over thousands of packages and trigger a [Shai-Hulud-style](https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html) cascading supply chain attack. The findings were reported to GitHub on June 6, 2026.

"Imagine this: an attacker compromises a single package. An AI agent on a popular package maintainer's device autonomously pulls it for a project," security researcher Golan Myers said. "That single endpoint is used to push malicious code to the popular package. All the package users are exposed. All because one person with the correct access was exposed."

Trusted publishing was [introduced](https://github.blog/changelog/2025-07-31-npm-trusted-publishing-with-oidc-is-generally-available/) in npm in July 2025 as a credential-free authentication method that allows developers to push npm packages from a CI/CD platform, such as GitHub Actions, using OpenID Connect (OIDC) tokens.

When trusted publishing is configured, the developer's CI/CD provider generates a short-lived cryptographic token for a specific workflow run that the npm registry verifies against a [pre-authorized configuration](https://docs.npmjs.com/trusted-publishers#step-2-configure-your-cicd-workflow).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

This eliminates the need to store, rotate, or manually manage long-lived npm secrets, reducing the risk of credential leaks. It also automatically generates [provenance attestations](https://docs.npmjs.com/generating-provenance-statements) for npm packages, allowing users to establish where a package was built and who published it, thereby strengthening software supply chain security.

However, as Bloom Security found, this security architecture suffered from a problem in how it identified that repository, also called a slug (i.e, the combination of the owner or organization and the repository name that's formatted as "owner/repository").

"It records the repository's address, [...] instead of the permanent ID GitHub assigns it, at least until a version is first published from that repository," Myers explained. "It is like a lock that checks the address on the door rather than who owns the house: when the owner moves out, whoever moves in gets the key."

Put differently, the numeric IDs that survive through repository renaming and transfers are carried by GitHub's OIDC tokens, but are completely ignored by npm until the first successful publish from that repository.

This means the trust is anchored to a name as opposed to an immutable repository ID, a loophole that can be abused by claiming abandoned slugs to inherit their trust. For this attack to succeed, the only prerequisite is that the victim's trusted publisher points to a GitHub slug an attacker can claim, and the repository has never been used to publish a version of the package to npm.

Once such a slug becomes available for use after a maintainer renames, transfers, or deletes a repository, an attacker can follow the steps below -

* Create a repository at the freed slug at the "owner/repository" path, which causes GitHub to issue a fresh repository ID.
* Create and trigger an npm publish workflow, which mints an OIDC token carrying the reclaimed slug and the new numeric repository ID
* Submit the token to the npm exchange endpoint. Npm finds that the repository claim matches the stored slug and issues a publish credential.
* The attacker receives a time-limited publish token for a package they do not own and pushes malicious changes to the registry.

An attack of this kind, codenamed **SlugFest**, can be abused to publish a new "malicious" version of the victim package under the legitimate package name, while inheriting existing reputation, download counts, and dependent relationships. This, in turn, can le...