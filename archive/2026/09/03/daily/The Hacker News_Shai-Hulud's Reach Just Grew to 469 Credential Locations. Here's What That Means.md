---
title: Shai-Hulud's Reach Just Grew to 469 Credential Locations. Here's What That Means
url: https://thehackernews.com/2026/09/shai-huluds-reach-just-grew-to-469.html
source: The Hacker News
date: 2026-09-03
fetch_date: 2026-09-04T06:44:15.005423
---

# Shai-Hulud's Reach Just Grew to 469 Credential Locations. Here's What That Means

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Shai-Hulud's Reach Just Grew to 469 Credential Locations. Here's What That Means](https://thehackernews.com/2026/09/shai-huluds-reach-just-grew-to-469.html)

**The Hacker News**Sep 03, 2026Malware / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfx0JCqLgANXGkgF5NMg__RxJg5IJ8HgQcvr_2zxEM6HSYzesKdLjKbrqmtAegyIpBmLxnryF5CeJlRh4J09q3e1kOo8dEzGXjhQpunnmGoL6wzEW_6R7lsN4zE5IybADP50VCjGGrBercYm6OIMCYsSgbHJ6sN9AYY3v6kCqPof8TWzR2O_ybViE1aYo/s1700-nu-rw-lo-l85-e365/Shai-Hulud.gif)

In early August, GitGuardian researchers found that a recent [Shai-Hulud infostealer worm variant had evolved to scan for credentials across 469 locations across developer environments](https://blog.gitguardian.com/keyv-mini-shai-hulud/), Continuous Integration/Continuous Deployment (CI/CD) tooling, cloud configurations, and even AI tool configs.

Earlier variants of the infostealer worm only checked 189 paths. The jump says a lot. Attackers have stopped trying to break trust relationships and started using the credentials that already make those relationships work.

Software supply chains have always depended on trust.

Developers trust package registries. Organizations trust maintainers. CI/CD systems trust the credentials and identities they're given. Applications trust the dependencies they pull down during a build.

Attackers realized they don't need to break any of that. They just needed to find where the credentials and standing privileges already sit.

This is what is driving the current focus on software supply chain defense across multiple ecosystems. Protecting package registries and dependencies still matters, but the core of the problem, the actual required element for infostealer worms to succeed, sits underneath those systems.

Attackers are hunting for reusable authority. Preventing the next Shai-Hulud starts with addressing and securing the credential layer.

## Shai-Hulud turns stolen credentials into an ongoing supply chain attack

Shai-Hulud belongs to a growing class of supply chain attacks that search compromised environments for credentials they can use to continue the attack.

A token found on a developer workstation might open access to source code. That same code likely contains cloud credentials, which would grant access to the infrastructure. A GitHub token might allow write access to additional repositories. A package publishing credential can let an attacker publish software through a channel developers already trust. Credentials become the connective tissue between one compromised environment and the next.

The broader ecosystem has already seen how direct that path can be. A quick scan of any security industry news site or info feed will surface a never-ending supply of stories about new infections across multiple languages, package managers, and operating systems.

### Credential harvesting gives attackers somewhere to go next

Modern developer environments contain far more authentication material than the source repository alone. Credentials show up in expected places, like .env files, shell history, and package-manager configuration. But there are also secrets in CLI caches, CI/CD configurations, and IDE settings. Increasingly, teams are finding access keys in the configuration used by AI development tools.

This is why credential-harvesting malware creators keep broadening the search radius. The attacker doesn't necessarily know which credential matters most before collection begins. It can gather what's available and sort out what each credential unlocks afterward.

Defenders should work the problem in the opposite direction. Security teams must identify which credentials matter most and address their exposure before an attacker gets the chance to use them.

### The power to publish creates a path to propagation

Package publishing credentials deserve special attention because they turn credential theft into software distribution, forward propagating the attack.

Tokens that developers use to publish carry authority over a trusted package that other developers, build systems, and organizations will automatically consume. That trust is what attackers abuse. This creates an obvious first priority for defenders: to reduce the number of standing publishing credentials available to steal.

Organizations need to cut their dependence on long-lived publishing tokens. We should encourage all software makers to adopt short-lived, verified authentication via OpenID Connect (OIDC) or similarly scoped mechanisms. [Docker and GitHub Actions' recent updates](https://www.docker.com/blog/docker-oidc-connections-for-github-actions-available-for-docker-orgs/) have pushed the ecosystem further in this direction, including stronger authentication and greater use of trusted publishing.

Any long-lived publishing credential that remains should be treated as highly sensitive infrastructure.

### Credentials connect systems security teams manage separately

Security teams traditionally think about their orgs in terms of security types: source control security, CI/CD security, cloud security, endpoint security, and application security. Credentials span all of these divisions and separation-of-duties requirements. A single developer can authenticate to GitHub, npm, AWS, Kubernetes, internal APIs, and build infrastructure in one normal day, and CI/CD pipelines often carry an equally diverse set.

A credential left in a developer environment can represent authority somewhere completely different. The file might sit on a laptop while the credential controls a cloud resource or might grant package publication rights.

Where a secret is discovered only tells part of the story. Organizations working towards secrets management maturity also need to know whether the credential is valid, what identity it belongs to, what system accepts it, what privileges it carries, which environment it reaches, and who owns its remediation.

That turns secrets detection int...