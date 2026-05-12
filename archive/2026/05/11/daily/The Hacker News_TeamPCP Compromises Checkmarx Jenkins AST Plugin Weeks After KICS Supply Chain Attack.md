---
title: TeamPCP Compromises Checkmarx Jenkins AST Plugin Weeks After KICS Supply Chain Attack
url: https://thehackernews.com/2026/05/teampcp-compromises-checkmarx-jenkins.html
source: The Hacker News
date: 2026-05-11
fetch_date: 2026-05-12T05:39:06.641100
---

# TeamPCP Compromises Checkmarx Jenkins AST Plugin Weeks After KICS Supply Chain Attack

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [TeamPCP Compromises Checkmarx Jenkins AST Plugin Weeks After KICS Supply Chain Attack](https://thehackernews.com/2026/05/teampcp-compromises-checkmarx-jenkins.html)

**Ravie Lakshmanan**May 11, 2026Supply Chain Attack / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiq0A3_8O89uC968dpFnFxE4v3J4fpr5nEqC-2QiSJ_rtZlgPocPYIaowCvCMeONhcrFiaoSdBVeNsuTa2ipAZZ3HBMUDcfO8DZ06pughteYJItHhMLeBr_jnfLL-5WX6xBE_EjIfPDGjCYyDCa6aImjimPNl7FtM1evdnTUVEk54x9pczRaFlmEZy1Cv8B/s1700-e365/Jenkins.jpg)

Checkmarx has confirmed that a modified version of the [Jenkins AST plugin](https://plugins.jenkins.io/checkmarx-ast-scanner/) was published to the Jenkins Marketplace.

"If you are using Checkmarx Jenkins AST plugin, you need to ensure that you are using the version 2.0.13-829.vc72453fa\_1c16 that was published on December 17, 2025 or previously," the cybersecurity company [said](https://checkmarx.com/blog/ongoing-security-updates/) in a statement over the weekend.

As of writing, Checkmarx has released 2.0.13-848.v76e89de8a\_053 on both GitHub and the Jenkins Marketplace, although its incident update still notes that it's "in the process of publishing a new version of this plugin." It did not disclose how the malicious plugin version was published.

The development is the latest attack orchestrated by TeamPCP targeting Checkmarx. It arrives a couple of weeks after the notorious cybercrime group was [attributed](https://thehackernews.com/2026/04/checkmarx-confirms-github-repository.html) to the compromise of its KICS Docker image, two VS Code extensions, and a GitHub Actions workflow to push credential-stealing malware.

The breach, in turn, resulted in the [brief compromise](https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html) of the Bitwarden CLI npm package to serve a similar stealer that can harvest a wide range of developer secrets.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

TeamPCP has been linked to a series of breaches since March 2026 as part of a sprawling campaign that exploits the inherent trust in the software supply chain to propagate its malware and expand its reach.

According to details shared by security researcher [Adnan Khan](https://x.com/adnanthekhan/status/2053156381616676928) and [SOCRadar](https://socradar.io/blog/checkmarx-jenkins-plugin-teampcp-backdoor/), TeamPCP is said to have gained unauthorized access to the plugin's GitHub repository and renamed it to "Checkmarx-Fully-Hacked-by-TeamPCP-and-Their-Customers-Should-Cancel-Now."

The defaced repository was also updated to include the description: "Checkmarx fails to rotate secrets again. with love – TeamPCP."

"The fact that TeamPCP is back inside Checkmarx systems just weeks later points to one of two possibilities: either the initial remediation was incomplete and credentials were not fully rotated, or the group retained a foothold that wasn't identified during the March response," SOCRadar said.

"A second Checkmarx incident happening this soon suggests the group is actively watching for re-entry points, testing the depth of past remediations, and capitalizing on any gaps."

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

[Checkmarx](https://thehackernews.com/search/label/Checkmarx), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [DevSecOps](https://thehackernews.com/search/label/DevSecOps), [GitHub](https://thehackernews.com/search/label/GitHub), [Jenkins](https://thehackernews.com/search/label/Jenkins), [Malware](https://thehackernews.com/search/label/Malware), [software security](https://thehackernews.com/search/label/software%20security), [supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack), [TeamPCP](https://thehackernews.com/search/label/TeamPCP)

⚡ Top Stories This Week

[![30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign](data:image/svg+xml;base64... "30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign")

30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign](https://thehackernews.com/2026/05/30000-facebook-accounts-hacked-via.html)

[![Trellix Confirms Source Code Breach With Unauthorized Repository Access](data:image/svg+xml;base64... "Trellix Confirms Source Code Breach With Unauthorized Repository Access")

Trellix Confirms Source Code Breach With Unauthorized Repository Access](https://thehackernews.com/2026/05/trellix-confirms-source-code-breach.html)

[![⚡ Weekly Recap: AI-Powered Phishing, Android Spying Tool, Linux Exploit, GitHub RCE and More](data:image/svg+xml;base64... "⚡ Weekly Recap: AI-Powered Phishing, Android Spying Tool, Linux Exploit, GitHub RCE and More")

⚡ Weekly Recap: AI-Powered Phishing, Android Spying Tool, Linux Exploit, GitHub RCE and More](https://thehackernews.com/2026/05/weekly-recap-ai-powered-phishing.html)

[![Progress Patches Critical MOVEit Automation Bug Enabling Authentication Bypass](data:image/svg+xml;base64... "Progress Patches Critical MOVEit Automation Bug Enabling Authentication Bypass")

Progress Patches Critical MOVEit Automation Bug Enabling Authenticatio...