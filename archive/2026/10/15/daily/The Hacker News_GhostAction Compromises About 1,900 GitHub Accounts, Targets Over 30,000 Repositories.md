---
title: GhostAction Compromises About 1,900 GitHub Accounts, Targets Over 30,000 Repositories
url: https://thehackernews.com/2026/10/ghostaction-compromises-about-1900.html
source: The Hacker News
date: 2026-10-15
fetch_date: 2026-10-16T06:37:56.010932
---

# GhostAction Compromises About 1,900 GitHub Accounts, Targets Over 30,000 Repositories

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

# [GhostAction Compromises About 1,900 GitHub Accounts, Targets Over 30,000 Repositories](https://thehackernews.com/2026/10/ghostaction-compromises-about-1900.html)

**Ravie Lakshmanan**Oct 15, 2026Supply Chain Attack / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiddFchlm_nV3vywI0BM2-8IaZb-wHXwE8DplGqZYkRmcYkeXiSLfVmnVAU-jM4yikWW7SWokanh_S4hq88cVHjAnaWDGkl3VVAtPdv9SHWp0MNb0CIOAA-I73EuwwUSE-wNMnXEzbIdDYorJn2hIuBZQ5Jh_5I2IntiXuUYZz3sKax-wfRoaxy_pD9kGx0/s1700-nu-rw-lo-l85-e365/ghost-git.jpg)

The credential-theft campaign known as **GhostAction** has ramped up, targeting more than 30,000 repositories across 3,000 users and organizations.

The spike, according to GitGuardian, was observed on October 8 and 9, 2026.

"This resulted from compromising the GitHub accounts of about 1,900 users. It attempted to extract 3,174 secrets from public repositories' CI," security researchers Gaetan Ferry and Guillaume Valadon [said](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/).

[GhostAction](https://threats.wiz.io/all-incidents/ghostaction-campaign) is the moniker for a supply chain attack campaign targeting developer infrastructure on GitHub. Originally discovered in September 2025, it involves threat actors compromising legitimate developer accounts to inject malicious GitHub Actions automation workflows into software repositories.

Attackers have been found to gain write access to repositories using stolen Personal Access Tokens (PATs) or credentials harvested from infostealer logs and dumps. Using the hijacked maintainer account, they push a malicious workflow file disguised under deceptive names such as Security Audit ("security-audit.yml") or GitHub Actions Security ("github\_actions\_security.yml").

The end goal of the activity is the large-scale theft of continuous integration and continuous deployment (CI/CD) secrets, cloud credentials, package registry tokens (like npm, PyPI, and DockerHub), and artificial intelligence (AI) provider API keys.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

A new wave of GhostAction has been [observed](https://thehackernews.com/2026/10/credential-stealing-github-actions.html) since August 31, 2026, with the malicious workflow pushed to hundreds of repositories.

"This new wave seems more experimental and manual than previous ones, with the payload evolving over time," GitGuardian said. "Compared with the original GhostAction payload, the first version of this new payload added a git history secret-scanning feature."

As previously outlined by Socket and StepSecurity, the history-scanning functionality features secret-detection regular expressions covering AWS key IDs, GitHub and GitLab tokens, AI-related secrets, and cloud API keys.

A second version of the payload also captures about two lines of context around every AWS key ID hit so as to pair them with their matching secret access keys. A third and final variant of the payload includes support for retrieving the secret context during the git history scan.

"This payload was deployed in multiple phases," GitGuardian said. "First to 160 previously observed victims, then, 20 minutes later, to 28,000 new repositories between October 8 and 9. New waves have been observed, using the same payload, on October 10 and 12. However, GitHub started preventing the malicious workflow from running starting October 9. Those two subsequent waves therefore could not extract any secrets."

Interestingly, a subset of the victims from this new burst were previously compromised in the September 2025 and August 2026 waves, indicating the threat actors are banking on unrotated secrets to pull them off.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Credential Theft](https://thehackernews.com/search/label/Credential%20Theft), [GitHub](https://thehackernews.com/search/label/GitHub), [Supply Chain](https://thehackernews.com/search/label/Supply%20Chain)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

P7 DarkSword iOS Exploit Kit Adds Crypto Wallet Data Theft and Remote Commands](https://thehackernews.com/2026/10/p7-darksword-ios-exploit-kit-adds.html)

[![The Hacker News](data:image/svg+xml;base64...)

Anthropic Cuts Live Internet Access for Internal AI Tests After Claude Exploits Injection Flaws](https://thehackernews.com/2026/10/anthropic-cuts-live-internet-access-for.html)

[![The Hacker News](data:image/svg+xml;base64...)

FBI Arrests Another ShinyHunters Suspect Reportedly Involved in Its Jobs Portal Hack](https://thehackernews.com/2026/10/fbi-arrests-another-shinyhunters.html)

[![The Hacker News](data:image/svg+xml;base64...)

TP-Link Sued by Four More U.S. States Over Router Security and China Ties](https://thehackernews.com/2026/10/tp-link-sued-by-four-more-us-states.html)

[![The Hacker News](data:image/svg+xml;base64...)

Anthropic Launches Free AI Vulnerability Scanner for Open-Source Projects](https://thehackernews.com/2026/10/anthropic-launches-free-a...