---
title: Trivy Hack Spreads Infostealer via Docker, Triggers Worm and Kubernetes Wiper
url: https://thehackernews.com/2026/03/trivy-hack-spreads-infostealer-via.html
source: The Hacker News
date: 2026-03-23
fetch_date: 2026-03-24T04:18:12.700913
---

# Trivy Hack Spreads Infostealer via Docker, Triggers Worm and Kubernetes Wiper

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Trivy Hack Spreads Infostealer via Docker, Triggers Worm and Kubernetes Wiper](https://thehackernews.com/2026/03/trivy-hack-spreads-infostealer-via.html)

**Ravie Lakshmanan**Mar 23, 2026Cloud Security / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3tECPxIu-t1cl5YE211vm5q8dB99cO4mW6hbz0jCRbtDjalNgI7gX42M9MQAkty0IsWyxB3cJDMOpKbqQlLSKMnjbGaBOJHB9QslmSQB6-96o4RlaFLKuTHEAq8HpO-KbprLYPIjSR64H9twUcA-fuV0CrB2qw7RlzNWhQUHEmyKboascQm-Udl5GPdwA/s1700-e365/docker.jpg)

Cybersecurity researchers have uncovered malicious artifacts distributed via Docker Hub following the [Trivy supply chain attack](https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html), highlighting the widening blast radius across developer environments.

The last known clean release of [Trivy](https://hub.docker.com/r/aquasec/trivy/tags) on Docker Hub is 0.69.3. The malicious versions 0.69.4, 0.69.5, and 0.69.6 have since been removed from the container image library.

"New image tags 0.69.5 and 0.69.6 were pushed on March 22 without corresponding GitHub releases or tags. Both images contain indicators of compromise associated with the same TeamPCP infostealer observed in earlier stages of this campaign," Socket security researcher Philipp Burckhardt [said](https://socket.dev/blog/trivy-docker-images-compromised).

The development comes in the wake a [supply chain compromise](https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html) of Trivy, a popular open-source vulnerability scanner maintained by Aqua Security, allowing the threat actors to leverage a compromised credential to push a credential stealer within trojanized versions of the tool and two related GitHub Actions "aquasecurity/trivy-action" and "aquasecurity/setup-trivy."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The attack has had downstream impacts, with the attackers leveraging the stolen data to compromise dozens of npm packages to distribute a self-propagating worm known as [CanisterWorm](https://thehackernews.com/2026/03/trivy-supply-chain-attack-triggers-self.html). The incident is believed to be the work of a threat actor tracked as TeamPCP.

According to the OpenSourceMalware team, the attackers have defaced all 44 internal repositories associated with Aqua Security's "[aquasec-com](https://github.com/aquasec-com)" GitHub organization by renaming each of them with a "tpcp-docs-" prefix, setting all descriptions to "TeamPCP Owns Aqua Security," and exposing them publicly.

It's worth noting that the "aquasec-com" account is distinct from the cloud security vendor's other well-known GitHub organization account, "aquasecurity," which hosts the impacted Trivy scanner and GitHub Actions, along with various open-source projects. The newly compromised organization contains proprietary source code, including source code for Tracee, internal Trivy forks, CI/CD pipelines, Kubernetes operators, and team knowledge bases.

All the repositories are said to have been modified in a scripted 2-minute burst between 20:31:07 UTC and 20:32:26 UTC on March 22, 2026. It's been assessed with high confidence that the threat actor leveraged a compromised "Argon-DevOps-Mgt" service account for this purpose.

"Our forensic analysis of the GitHub Events API points to a compromised service account token — likely stolen during TeamPCP's prior Trivy GitHub Actions compromise — as the attack vector," security researcher Paul McCarty [said](https://opensourcemalware.com/blog/teampcp-aquasec-com-github-org-compromise). "This is a service/bot account (GitHub ID 139343333, created 2023-07-12) with a critical property: it bridges both GitHub orgs."

"One compromised token for this account gives the attacker write/admin access to both organizations," McCarty added.

The development is the latest escalation from a threat actor that's has built a reputation for targeting cloud infrastructures, while progressively building capabilities to systemically exposed Docker APIs, Kubernetes clusters, Ray dashboards, and Redis servers to steal data, deploy ransomware, conduct extortion, and mine cryptocurrency.

Their growing sophistication is best exemplified by the emergence of a new wiper malware that spreads through SSH via stolen keys and exploits exposed Docker APIs on port 2375 across the local subnet.

A new payload attributed to TeamPCP has been found to go beyond credential theft to wiping entire Kubernetes (K8s) clusters located in Iran. The shell script uses the same ICP canister linked to CanisterWorm and then runs checks to identify Iranian systems.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-stories-xmcyber-d)

"On Kubernetes: deploys privileged DaemonSets across every node, including control plane," Aikido security researcher Charlie Eriksen [said](https://www.aikido.dev/blog/teampcp-stage-payload-canisterworm-iran). "Iranian nodes get wiped and force-rebooted via a container named 'kamikaze.' Non-Iranian nodes get the CanisterWorm backdoor installed as a systemd service. Non-K8s Iranian hosts get 'rm -rf / --no-preserve-root.'"

Given the ongoing nature of the attack, it's imperative that organizations review their use of Trivy in CI/CD pipelines, avoid using affected versions, and treat any recent executions as potentially compromised.

"This compromise demonstrates the long tail of supply chain attacks," OpenSourceMalware said. "A credential harvested during the Trivy GitHub Actions compromise months ago was weaponized today to deface an entire internal GitHub organization. The Argon-DevOps-Mgt service account — a single bot account bridging two orgs with a long-lived PAT — was the weak link."

"From cloud exploitation to supply chain worms to Kubernetes wipers, they are building capability and targeting the security vendor ecosystem itself. The irony of a cloud security company being compromised by a ...