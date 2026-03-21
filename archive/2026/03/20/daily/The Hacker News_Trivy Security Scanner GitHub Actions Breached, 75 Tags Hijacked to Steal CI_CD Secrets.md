---
title: Trivy Security Scanner GitHub Actions Breached, 75 Tags Hijacked to Steal CI/CD Secrets
url: https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html
source: The Hacker News
date: 2026-03-20
fetch_date: 2026-03-21T04:08:40.824169
---

# Trivy Security Scanner GitHub Actions Breached, 75 Tags Hijacked to Steal CI/CD Secrets

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

# [Trivy Security Scanner GitHub Actions Breached, 75 Tags Hijacked to Steal CI/CD Secrets](https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html)

**Ravie Lakshmanan**Mar 20, 2026DevSecOps / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNf7vYlImTCJ7BCjYYEhoFZXTawhHcJJad9cFjQn98oQjaPY9HY6Qgpp6pAyqkq7CNHyVXI9fR8hcyVNlW_knYia3f0BhAlK7fZb2gplznk9v9QCFGKtIbMLTSu-erTslOxZCHd8jkJKXIcCYhK8QkKLuWjG8yxjhPBaEWUDzwY0sUkX5JvhBtzFxyfp_q/s1700-e365/scan.jpg)

Trivy, a popular open-source vulnerability scanner maintained by Aqua Security, was compromised a second time within the span of a month to deliver malware that stole sensitive CI/CD secrets.

The latest incident impacted GitHub Actions "[aquasecurity/trivy-action](https://github.com/aquasecurity/trivy-action)" and "[aquasecurity/setup-trivy](https://github.com/aquasecurity/setup-trivy)," which are used to scan Docker container images for vulnerabilities and set up GitHub Actions workflow with a specific version of the scanner, respectively.

"We identified that an attacker force-pushed 75 out of 76 version tags in the aquasecurity/trivy-action repository, the official GitHub Action for running Trivy vulnerability scans in CI/CD pipelines," Socket security researcher Philipp Burckhardt [said](https://socket.dev/blog/trivy-under-attack-again-github-actions-compromise). "These tags were modified to serve a malicious payload, effectively turning trusted version references into a distribution mechanism for an infostealer."

The payload executes within GitHub Actions runners and aims to extract valuable developer secrets from CI/CD environments, such as SSH keys, credentials for cloud service providers, databases, Git, Docker configurations, Kubernetes tokens, and cryptocurrency wallets.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The [development](https://www.stepsecurity.io/blog/trivy-compromised-a-second-time---malicious-v0-69-4-release) marks the second supply chain incident involving Trivy. Towards the end of February and early March 2026, an autonomous bot called hackerbot-claw [exploited](https://thehackernews.com/2026/03/five-malicious-rust-crates-and-ai-bot.html#ai-powered-bot-exploits-github-actions) a "pull\_request\_target" workflow to steal a Personal Access Token (PAT), which was then weaponized to seize control of the GitHub repository, delete several release versions, and push two malicious versions of its Visual Studio Code (VS Code) extension to Open VSX.

The first sign of the compromise was [flagged](https://www.linkedin.com/posts/mccartypaul_heads-up-trivy-version-0694-has-been-share-7440548547609079808-Uloi/) by security researcher Paul McCarty after a new compromised release (version 0.69.4) was published to the "aquasecurity/trivy" GitHub repository. The rogue version has since been removed. According to [Wiz](https://www.wiz.io/blog/trivy-compromised-teampcp-supply-chain-attack), version 0.69.4 starts both the legitimate Trivy service and the malicious code responsible for a series of tasks -

* Conduct data theft by scanning the system for environmental variables and credentials, encrypting the data, and exfiltrating it via an HTTP POST request to scan.aquasecurtiy[.]org.
* Set up persistence by using a [systemd service](https://redcanary.com/blog/threat-detection/attck-t1501-understanding-systemd-service-persistence/) after confirming that it's running on a developer machine. The systemd service is configured to run a Python script ("sysmon.py") that polls an external server to retrieve the payload and execute it.

In a statement, Itay Shakury, vice president of open source at Aqua Security, [said](https://github.com/aquasecurity/trivy/discussions/10425) the attackers abused a compromised credential to publish malicious trivy, trivy-action, and setup-trivy releases. In the case of "aquasecurity/trivy-action," the adversary force-pushed 75 version tags to point to the malicious commits containing the Python infostealer payload without creating a new release or pushing to a branch, as is standard practice. Seven "aquasecurity/setup-trivy" tags were force-pushed in the same manner.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsNwdNYcc_SnbNdxXfi9Z2gA_5jJdCiAKz8loJAdu_wzQ6thlkYX6YqoWqXJiZH23-6Ueynq2OCUQe1XZPs6o5h7y7uKqxxn9XEhvkKZbGHzA3OwDpbSRKDJ4Wk7Hulv0f405D5dx_exOCwmWjAuHOrmmYbk1TBvYNkDiuYycm9fpfHSKj0kvI7Od86FVq/s1700-e365/hacked.jpg)

"So in this case, the attacker didn't need to exploit Git itself," Burckhardt told The Hacker News. "They had valid credentials with sufficient privileges to push code and rewrite tags, which is what enabled the tag poisoning we observed. What remains unclear is the exact credential used in this specific step (e.g., a maintainer PAT vs automation token), but the root cause is now understood to be credential compromise carried over from the earlier incident."

The security vendor also acknowledged that the latest attack stemmed from incomplete containment of the hackerbot-claw incident. "We rotated secrets and tokens, but the process wasn't atomic, and attackers may have been privy to refreshed tokens," Shakury said. "We are now taking a more restrictive approach and locking down all automated actions and any token in order to thoroughly eliminate the problem."

The stealer operates in three stages: harvesting environment variables from the runner process memory and the file system, encrypting the data, and exfiltrating it to the attacker-controlled server ("scan.aquasecurtiy[.]org").

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTs_Xbm79NyRtl34MoMryBBxX2p3v8k361tx6itvNRs0MoHA9DdPF2qpowGORL_xJUoV-FG9fGzE7ERmep4LBZwPcdx_3qtAy-vMnMos-yKwGt_yq5R5-N20k2AG9baRQMDEC9jzuCaLeymAl0AlUveuLLCe6vwajgXAUTIAGAw7jRo1a3bAxMvhoJYc2E/s1700-e365/git-actions.jpg)

Should the exfiltrat...