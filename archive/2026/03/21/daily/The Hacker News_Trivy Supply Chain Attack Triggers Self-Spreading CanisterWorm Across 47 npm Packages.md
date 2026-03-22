---
title: Trivy Supply Chain Attack Triggers Self-Spreading CanisterWorm Across 47 npm Packages
url: https://thehackernews.com/2026/03/trivy-supply-chain-attack-triggers-self.html
source: The Hacker News
date: 2026-03-21
fetch_date: 2026-03-22T04:19:22.747884
---

# Trivy Supply Chain Attack Triggers Self-Spreading CanisterWorm Across 47 npm Packages

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

# [Trivy Supply Chain Attack Triggers Self-Spreading CanisterWorm Across 47 npm Packages](https://thehackernews.com/2026/03/trivy-supply-chain-attack-triggers-self.html)

**Ravie Lakshmanan**Mar 21, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJqn31IC9aCQ9LMLCLRXgpwsa1gvtzXlYk20-1yRmCMYVM_MwGHedfSgbKl24yaeTx4fqRc4-vscge-d3P6sN8sErQBVGD0kgxMGzV-mDCI1wGFh87BB8me019zcennhvA6xyMHLnH9IKZ-txSWs9OwL5cGbg0X8sx_KZ2tj5A5awErRRRMbdSrw_cXs6a/s1700-e365/npm-malware.jpg)

The threat actors behind the [supply chain attack](https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html) targeting the popular Trivy scanner are suspected to be conducting follow-on attacks that have led to the compromise of a large number of npm packages with a previously undocumented self-propagating worm dubbed **CanisterWorm**.

The name is a reference to the fact that the malware uses an [ICP canister](https://docs.internetcomputer.org/building-apps/essentials/canisters), which refers to tamperproof smart contracts on the Internet Computer blockchain, as a [dead drop resolver](https://attack.mitre.org/techniques/T1102/001/). The development marks the first publicly documented abuse of an ICP canister for the explicit purpose of fetching the command-and-control (C2) server, Aikido Security researcher Charlie Eriksen [said](https://www.aikido.dev/blog/teampcp-deploys-worm-npm-trivy-compromise).

The list of affected packages is below -

* 28 packages in the @EmilGroup scope
* 16 packages in the @opengov scope
* @teale.io/eslint-config
* @airtm/uuid-base32
* @pypestream/floating-ui-dom

The development comes within a day after threat actors leveraged a compromised credential to publish malicious trivy, trivy-action, and setup-trivy releases containing a credential stealer. A cloud-focused [cybercriminal operation](https://cyble.com/threat-actor-profiles/teampcp/) known as [TeamPCP](https://thehackernews.com/2026/02/teampcp-worm-exploits-cloud.html) is suspected to be behind the attacks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The infection chain involving the npm packages involves leveraging a postinstall hook to execute a loader, which then drops a Python backdoor that's responsible for contacting the ICP canister dead drop to retrieve a URL pointing to the next-stage payload. The fact that the dead drop infrastructure is decentralized makes it [resilient and resistant to takedown efforts](https://thehackernews.com/2025/10/north-korean-hackers-use-etherhiding-to.html).

"The canister controller can swap the URL at any time, pushing new binaries to all infected hosts without touching the implant," Eriksen said.

Persistence is established by means of a systemd user service, which is configured to automatically start the Python backdoor after a 5-second delay if it gets terminated for some reason by using the "[Restart=always](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)" directive. The systemd service masquerades as PostgreSQL tooling ("pgmon") in an attempt to fly under the radar.

The backdoor, as mentioned before, phones the [ICP canister](https://dashboard.internetcomputer.org/canister/tdtqy-oyaaa-aaaae-af2dq-cai) with a spoofed browser User-Agent every 50 minutes to fetch the URL in plaintext. The URL is subsequently parsed to fetch and run the executable.

"If the URL contains youtube[.]com, the script skips it," Eriksen explained. "This is the canister's dormant state. The attacker arms the implant by pointing the canister at a real binary, and disarms it by switching back to a YouTube link. If the attacker updates the canister to point to a new URL, every infected machine picks up the new binary on its next poll. The old binary keeps running in the background since the script never kills previous processes."

It's worth noting that a similar youtube[.]com-based kill switch has also been flagged by Wiz in connection with the trojanized Trivy binary (version 0.69.4), which reaches out to the same ICP canister via another Python dropper ("sysmon.py"). As of writing, the URL returned by the C2 is a [rickroll YouTube video](https://en.wikipedia.org/wiki/Rickrolling).

The Hacker News found that the ICP canister [supports](https://dashboard.internetcomputer.org/canister/tdtqy-oyaaa-aaaae-af2dq-cai) three methods – get\_latest\_link, http\_request, update\_link – the last of which allows the threat actor to modify the behavior at any time to serve an actual payload.

In tandem, the packages come with a "deploy.js" file that the attacker runs manually to spread the malicious payload to every package a stolen npm token provides access to in a programmatic fashion. The worm, assessed to be vibe-coded using an artificial intelligence (AI) tool, makes no attempt to conceal its functionality.

"This isn't triggered by npm install," Aikido said. "It's a standalone tool the attacker runs with stolen tokens to maximize blast radius."

To make matters worse, a subsequent iteration of CanisterWorm detected in "@teale.io/eslint-config" versions 1.8.11 and 1.8.12 has been found to self-propagate on its own without the need for manual intervention.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/cyber-comm-guide-d)

Unlike "deploy.js," which was a self-contained script the attacker had to execute with the pilfered npm tokens to push a malicious version of the npm packages to the registry, the new variant incorporates this functionality in "index.js" within a findNpmTokens() function that's run during the postinstall phase to collect npm authentication tokens from the victim's machine.

The main difference here is that the postinstall script, after installing the persistent backdoor, attempts to locate every npm token from the developer's environment and spawns the worm right away with those tokens by launching "deploy.js" as ...