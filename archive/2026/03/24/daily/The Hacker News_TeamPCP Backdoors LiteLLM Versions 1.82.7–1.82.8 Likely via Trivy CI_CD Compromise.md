---
title: TeamPCP Backdoors LiteLLM Versions 1.82.7–1.82.8 Likely via Trivy CI/CD Compromise
url: https://thehackernews.com/2026/03/teampcp-backdoors-litellm-versions.html
source: The Hacker News
date: 2026-03-24
fetch_date: 2026-03-25T04:18:08.576186
---

# TeamPCP Backdoors LiteLLM Versions 1.82.7–1.82.8 Likely via Trivy CI/CD Compromise

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

# [TeamPCP Backdoors LiteLLM Versions 1.82.7–1.82.8 Likely via Trivy CI/CD Compromise](https://thehackernews.com/2026/03/teampcp-backdoors-litellm-versions.html)

**Ravie Lakshmanan**Mar 24, 2026Cloud Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmubYXPf6QmmyAgoyu58-O141BOTc-D3aKKUtKXg1IFX6pn4Wav7yspHRPiWKScygEd1vsHmeH5zQLjwG38pOlDggYgjBN7MzUTrb_3jQv_lXum7s7PXGo8aqvSws4QEkrC587wgBhgF5tmPEmhK_OCeTLm8YlcWxyw2-nQMiM9VS8VdC22-tDkVM5MEsb/s1700-e365/lite.jpg)

[TeamPCP](https://thehackernews.com/2026/03/teampcp-hacks-checkmarx-github-actions.html), the threat actor behind the recent compromises of Trivy and KICS, has now compromised a popular Python package named [litellm](https://pypi.org/project/litellm/), pushing two malicious versions containing a credential harvester, a Kubernetes lateral movement toolkit, and a persistent backdoor.

Multiple security vendors, including [Endor Labs](https://www.endorlabs.com/learn/teampcp-isnt-done) and [JFrog](https://research.jfrog.com/post/litellm-compromised-teampcp/), revealed that litellm versions 1.82.7 and 1.82.8 were [published](https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/) on March 24, 2026, likely stemming from the [package's use of Trivy](https://github.com/BerriAI/litellm/blob/9343aeefca37aa49a6ea54397d7615adae5c72c9/ci_cd/security_scans.sh#L80) in their CI/CD workflow. Both the backdoored versions have since been removed from PyPI.

"The payload is a three-stage attack: a credential harvester sweeping SSH keys, cloud credentials, Kubernetes secrets, cryptocurrency wallets, and .env files; a Kubernetes lateral movement toolkit deploying privileged pods to every node; and a persistent systemd backdoor (sysmon.service) polling 'checkmarx[.]zone/raw' for additional binaries," Endor Labs researcher Kiran Raj said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

As observed in previous cases, the harvested data is exfiltrated as an encrypted archive ("tpcp.tar.gz") to a command-and-control domain named "models.litellm[.]cloud" via an HTTPS POST request.

In the case of 1.82.7, the malicious code is embedded in the "litellm/proxy/proxy\_server.py" file, with the injection performed during or after the wheel build process. The code is engineered to be executed at module import time, such that any process that imports "litellm.proxy.proxy\_server" triggers the payload without requiring any user interaction.

The next iteration of the package adds a "more aggressive vector" by incorporating a malicious "litellm\_init.pth" at the wheel root, causing the logic to be executed automatically on every Python process startup in the environment, not just when litellm is imported.

Another aspect that makes 1.82.8 more dangerous is the fact that the .pth launcher spawns a child Python process via [subprocess.Popen](https://docs.python.org/3/library/subprocess.html#popen-constructor), which allows the payload to be run in the background.

"Python .pth files placed in site-packages are processed automatically by site.py at interpreter startup," Endor Labs said. "The file contains a single line that imports a subprocess and launches a detached Python process to decode and execute the same Base64 payload."

The payload decodes to an orchestrator that unpacks a credential harvester and a persistence dropper. The harvester also leverages the Kubernetes service account token (if present) to enumerate all nodes in the cluster and deploy a privileged pod to each one of them. The pod then [chroots](https://en.wikipedia.org/wiki/Chroot) into the host file system and installs the persistence dropper as a systemd user service on every node.

The systemd service is configured to launch a Python script ("~/.config/sysmon/sysmon.py") – the same name used in the [Trivy compromise](https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html) – that reaches out to "checkmarx[.]zone/raw" every 50 minutes to fetch a URL pointing to the next-stage payload. If the URL contains youtube[.]com, the script aborts execution – a kill switch pattern common to all the incidents observed so far.

"This campaign is almost certainly not over," Endor Labs said. "TeamPCP has demonstrated a consistent pattern: each compromised environment yields credentials that unlock the next target. The pivot from CI/CD (GitHub Actions runners) to production (PyPI packages running in Kubernetes clusters) is a deliberate escalation."

With the latest development, TeamPCP has waged a relentless supply chain attack campaign that has spawned five ecosystems, including GitHub Actions, Docker Hub, npm, Open VSX, and PyPI, to expand its targeting footprint and bring more and more systems into its control.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2MLE-4dZUVruezq6H1P8KknTiMCxU1F6FA_JERQY6dlH44l4gmecsbB3WAW4njsQJvmN_7WIm62kDgQi3fG2w9UFQVfYE5WZGBd5UPYsxvD7GPT1JzUjD6U9bJOQ5bnZmhmYq4C9uSH5_m0cQb1vReiTAfa3_jLvRv_yaPq9FfRwSl2KNkizaUQ2wgTVQ/s1700-e365/telegram.jpg)

"TeamPCP is escalating a coordinated campaign targeting security tools and open source developer infrastructure, and is now openly taking credit for multiple follow-on attacks across ecosystems," Socket [said](https://socket.dev/blog/teampcp-targeting-security-tools-across-oss-ecosystem). "This is a sustained operation targeting high-leverage points in the software supply chain."

In a message [posted](https://t.me/team_pcp/98) on their Telegram channel, TeamPCP said: "These companies were built to protect your supply chains yet they can't even protect their own, the state of modern security research is a joke, as a result we're gonna be around for a long time stealing terrabytes [sic] of trade secrets with our new partners."

"The snowball effect from this will be massive, we are already partnering with other teams to perpetuate the chaos, many of your favourit...