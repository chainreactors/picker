---
title: Docker Fixes Critical Two-Year-Old Hub Flaw That Let One User Push Images as Another
url: https://thehackernews.com/2026/10/docker-fixes-critical-two-year-old-hub.html
source: The Hacker News
date: 2026-10-13
fetch_date: 2026-10-14T06:53:24.160771
---

# Docker Fixes Critical Two-Year-Old Hub Flaw That Let One User Push Images as Another

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

# [Docker Fixes Critical Two-Year-Old Hub Flaw That Let One User Push Images as Another](https://thehackernews.com/2026/10/docker-fixes-critical-two-year-old-hub.html)

**Swati Khandelwal**Oct 13, 2026

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEile879Rmv8zAdU5PMclUp5RnNGDb3h1u3aVZ-VigGjnO0RFcyCQ03s7_lIqMGDiow5ilPumq3B2_bsvewqRlepch4lFwLvOUEDQZPYd9Vv8untJVZFmrv5Zhgvj54cs4J_vCYW4GVY-XsQl7SXD-yrXbED6KpiWbTq-kL_0aNwef3xjV3cBGQ3dsodqAM/s1700-nu-rw-lo-l85-e365/dock.jpg)

A flaw in Docker Hub, the registry where container images are published and downloaded, let one user push, pull, or delete images as another user. Docker fixed the flaw on September 30 and says it found no evidence that anyone exploited it.

The flaw was in the feature that [converts a personal account](https://docs.docker.com/accounts/organization/setup/convert-account/) into an organization, Docker said in a [security advisory](https://www.docker.com/blog/docker-hub-security-advisory-cve-2026-105445/) on October 12. Conversion transferred the account's personal access tokens (PATs) to the user designated as the organization's owner. A PAT is used in place of a password in the registry, and the person who created each token can still use it.

The access was limited to the registry. It did not reach the Docker Hub web interface, and it could not be used to change a password, email address, or two-factor settings, or to take over an account.

Docker tracks the flaw as CVE-2026-105445 and rated it critical. The [CVE record](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/105xxx/CVE-2026-105445.json) it published on October 13 gives the flaw a CVSS 4.0 score of 9.4.

The flaw was open from August 26, 2024, until the fix, a little over two years. Docker made the fix on Docker Hub itself, so there is no update to install.

Docker Hub cannot move a repository from one account to another. A user instead converts a personal account into an organization that keeps the same name, and must name an existing account as its owner.

Each [personal access token](https://docs.docker.com/security/access-tokens/personal-access-tokens/) acts as the account that owns it, at a permission level chosen when the token is created. While the flaw was open, conversion changed the owner recorded for each token and left its secret unchanged.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

An attacker could abuse this by creating a token on an account they controlled, converting that account into an organization, and naming another user as its owner. The token would then work at the registry as that user.

The named owner was not asked to confirm the change and was not notified, according to Docker and the researchers who reported the flaw. Docker's conversion page has included the sentence "The new owner receives a notification email" since at least August 2024.

Within the token's permission level, a transferred token could pull, push, or delete images in the named owner's repositories and in organizations the owner could access.

Docker rated the flaw critical because that access "includes publishing images under a legitimate name," it said.

In March and April, attackers used [stolen publisher credentials](https://www.docker.com/blog/trivy-kics-and-the-shape-of-supply-chain-attacks-so-far-in-2026/) to push [malicious Trivy images](https://thehackernews.com/2026/03/trivy-hack-spreads-infostealer-via.html) and [malicious KICS images](https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html) to the publishers' own Docker Hub repositories, according to Docker.

Peter Molnar and Krisztian Hozak of mptrdev.com found the flaw and reported it to Docker, which says it deployed the fix less than four hours after receiving their report. They named the flaw GhostPat.

In their [technical write-up](https://ghostpat.com/), the two say they reproduced the flaw twice on consenting test accounts. They logged in to the registry as the target account, created and pushed to a repository in its namespace, pushed to an organization it belonged to, and pulled its private repositories.

### What Docker's Review Covered

Docker reviewed every account conversion made while the flaw was open and compared them with registry logs and token records. It looked for any token used under more than one identity and examined every push made with a transferred token, about 304,000 in all.

"We found no evidence that the vulnerability was exploited," the company said.

Every one of those pushes went to a repository belonging to the converted organization or to its named owner, according to Docker. In the large majority of cases, both accounts belonged to the same person or team.

Where it could not confirm that one person controlled both accounts, Docker analyzed the highest-risk public images without running them and found no malware or tampering.

Docker's registry logs show when a token is used, not that it exists, so a transferred token that was never used left no record in the logs. For that reason, Docker treated every token transferred by a conversion while the flaw was open as possibly affected, whether or not it had been used.

The advisory reports results for pushes. It does not say what Docker found for pulls or deletions made with transferred tokens, including pulls from private repositories.

### Who Was Notified and What to Check

On October 2, Docker emailed the users whose accounts had received transferred tokens and, separately, the owners of the organizations involved. Each email listed the tokens by description and creation date.

The advisory does not say how many users or tokens that covers, calling the group only a "limited number" of users.

Anyone who did not receive the email was not exposed and has nothing to do, according to Docker.

On October 8, Docker deactivated the transferred tokens it had identified. Tokens t...