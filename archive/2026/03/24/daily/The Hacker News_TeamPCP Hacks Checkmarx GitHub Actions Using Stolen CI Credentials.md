---
title: TeamPCP Hacks Checkmarx GitHub Actions Using Stolen CI Credentials
url: https://thehackernews.com/2026/03/teampcp-hacks-checkmarx-github-actions.html
source: The Hacker News
date: 2026-03-24
fetch_date: 2026-03-25T04:18:09.358761
---

# TeamPCP Hacks Checkmarx GitHub Actions Using Stolen CI Credentials

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

# [TeamPCP Hacks Checkmarx GitHub Actions Using Stolen CI Credentials](https://thehackernews.com/2026/03/teampcp-hacks-checkmarx-github-actions.html)

**Ravie Lakshmanan**Mar 24, 2026DevSecOps / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhs6mMRIch1O4gn0txxM6yMSRtvi7D0xmBbphFA0WJimqGO4k48KNvAbF_-an7swi-N0ZHOB2jt1WtJQjubozx7WzJH6Kr0CA0rCkP4TNUHR2NkC8NS6RaJDF9WUyZeyzUIG1NQtK_Betxs3h0gaxKqHMs7laaHTVXSiCMo-vbS_owFokGrDqN9NG7jdwRf/s1700-e365/git-check.jpg)

Two more GitHub Actions workflows have become the latest to be compromised by credential-stealing malware by a threat actor known as TeamPCP, the cloud-native cybercriminal operation also behind the [Trivy supply chain attack](https://thehackernews.com/2026/03/trivy-hack-spreads-infostealer-via.html).

The workflows, both maintained by the supply chain security company Checkmarx, are listed below -

* [checkmarx/ast-github-action](https://github.com/Checkmarx/ast-github-action)
* [checkmarx/kics-github-action](https://github.com/Checkmarx/kics-github-action)

Cloud security company Sysdig said it observed an identical credential stealer as the one used in TeamPCP's operations targeting Aqua Security's Trivy vulnerability scanner and its associated GitHub Actions, about four days after the breach on March 19, 2026. The Trivy supply chain compromise is being tracked under the CVE identifier [CVE-2026-33634](https://nvd.nist.gov/vuln/detail/CVE-2026-33634) (CVSS score: 9.4).

"This suggests that the stolen credentials from the Trivy compromise were used to poison additional actions in affected repositories," Sysdig [said](https://www.sysdig.com/blog/teampcp-expands-supply-chain-compromise-spreads-from-trivy-to-checkmarx-github-actions).

The stealer, referred to as "TeamPCP Cloud stealer," is designed to steal credentials and secrets related to SSH keys, Git, Amazon Web Services (AWS), Google Cloud, Microsoft Azure, Kubernetes, Docker, .env files, databases, and VPNs, along with CI/CD configurations, data from cryptocurrency wallets, and Slack and Discord webhook URLs.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

Like in the case of Trivy, the threat actors have been found to force-push tags to malicious commits containing the stealer payload ("setup.sh"). The stolen data is exfiltrated to the domain "checkmarx[.]zone" (IP address: 83.142.209[.]11:443) in the form of an encrypted archive ("tpcp.tar.gz").

The new version creates a "docs-tpcp" repository using the victim's GITHUB\_TOKEN to stage the stolen data as a backup method if the exfiltration to the server fails. In the Trivy incident, the threat actors used the repository name "tpcp-docs" instead.

"The use of vendor-specific typosquat domains for each poisoned action is a deliberate deception technique," Sysdig said. "An analyst reviewing CI/CD logs would see curl traffic to what appears to be the action's own vendor domain, reducing the likelihood of manual detection."

The fact that the stealer's primary function is to harvest credentials from CI runner memory allows the operators to extract GitHub personal access tokens (PATs) and other secrets from when a compromised Trivy action executes in a workflow. To make matters worse, if those tokens have write access to repositories that also use Checkmarx actions, the attacker can weaponize them to push malicious code.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-UP7rY9_9nhSVu2wUcsBDpcFmenvbxOQFOM7nGQnx-qrxbLEXTzUHrqdyho52x2mihYwvhED9O6A5cqnhCW1WaMWR7qtvqB4SGH4wTDG4UveQ4Xxf6KstcIY8jFWvhal2FVI6T3wVrPGcz_CmMkzh56w12viIlMVqZZx_kR6C9j5NQ1FAOYeL9gGjDnrK/s1700-e365/check.png)

This, in turn, opens the door to a cascading supply chain compromise, where one poisoned action captures secrets that are used to facilitate the poisoning of other actions.

"The identical payload, encryption scheme, and tpcp.tar.gz naming convention confirm this is the same threat actor expanding their reach beyond the initial Trivy compromise," Sysdig noted. "Code review and dependency scanning failed here because the malicious code was injected into a trusted action at the source."

According to Wiz, the attack appears to have been carried out via the compromise of the "cx-plugins-releases" service account, with the attackers also [publishing trojanized versions](https://x.com/ReversingLabs/status/2036193573796978729) of the "[ast-results](https://open-vsx.org/extension/checkmarx/ast-results/)" (version 2.53.0) and "[cx-dev-assist](https://open-vsx.org/extension/checkmarx/cx-dev-assist)" (version 1.7.0) Open VSX extensions. The VS Code Marketplace versions are not affected.

Once the extension is activated, the malicious payload checks whether the victim has credentials for at least one cloud service provider, such as GitHub, AWS, Google Cloud, and Microsoft Azure. If any credentials are detected, it proceeds to fetch a next-stage payload from the same domain ("checkmarx[.]zone").

"The payload attempts execution via npx, bunx, pnpx, or yarn dlx. This covers major JavaScript package managers," Wiz researchers Rami McCarthy, James Haughom, and Benjamin Read [said](https://www.wiz.io/blog/teampcp-attack-kics-github-action). "The retrieved package contains a comprehensive credential stealer. Harvested credentials are then encrypted, using the keys as elsewhere in this campaign, and exfiltrated to 'checkmarx[.]zone/vsx' as tpcp.tar.gz."

"On non-CI systems, the malware installs persistence via a systemd user service. The persistence script polls https://checkmarx[.]zone/raw every 50 minutes for additional payloads, with a kill switch that aborts if the response contains "youtube". Currently, the link redirects to The Show Must Go On by Queen."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-stories-xmcyber-d)

To mitigate the threat, users are advised to perform the following ac...