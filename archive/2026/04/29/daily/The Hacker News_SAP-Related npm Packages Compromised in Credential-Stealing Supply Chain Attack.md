---
title: SAP-Related npm Packages Compromised in Credential-Stealing Supply Chain Attack
url: https://thehackernews.com/2026/04/sap-npm-packages-compromised-by-mini.html
source: The Hacker News
date: 2026-04-29
fetch_date: 2026-04-30T05:30:42.473791
---

# SAP-Related npm Packages Compromised in Credential-Stealing Supply Chain Attack

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [SAP-Related npm Packages Compromised in Credential-Stealing Supply Chain Attack](https://thehackernews.com/2026/04/sap-npm-packages-compromised-by-mini.html)

**Ravie Lakshmanan**Apr 29, 2026Supply Chain Attack / Malware

[![SAP-Related npm Packages Compromised](data:image/png;base64... "SAP-Related npm Packages Compromised")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7ILiV-4oJHtNRt3-K52GIsgOaNUuN9owB5ky-Mk8FvRE3QmcqDg33oV3sCrzjgWEyIUfwTtn110bcMYVU3Lp61ArknIlPAcmMvbgJJ5-WheKYivyblon2tp79ux9pJmnYNv_ShhIAA5of3Wx7QzQRZs2mNuSQs6lLG23LKMVonvElcNMy6MXp6yVZO73F/s1700-e365/sap-npm-hacks.jpg)

Cybersecurity researchers are sounding the alarm about a new supply chain attack campaign targeting SAP-related npm Packages with credential-stealing malware.

According to reports from [Aikido Security](https://www.aikido.dev/blog/mini-shai-hulud-has-appeared), [SafeDep](https://safedep.io/mini-shai-hulud-and-sap-compromise/), [Socket](https://socket.dev/blog/sap-cap-npm-packages-supply-chain-attack), [StepSecurity](https://www.stepsecurity.io/blog/a-mini-shai-hulud-has-appeared), and Google-owned [Wiz](https://www.wiz.io/blog/mini-shai-hulud-supply-chain-sap-npm), the campaign – calling itself the **mini [Shai-Hulud](https://thehackernews.com/2025/12/researchers-spot-modified-shai-hulud.html)** – has affected the [following packages](https://socket.dev/supply-chain-attacks/sap-cap-npm-packages-hit-by-supply-chain-attack) associated with SAP's JavaScript and cloud application development ecosystem -

* mbt@1.2.48
* @cap-js/db-service@2.10.1
* @cap-js/postgres@2.2.2
* @cap-js/sqlite@2.2.2

"The affected versions introduced new installation-time behavior that was not previously part of these packages' expected functionality," Socket said. "The compromised releases added a preinstall script that acts as a runtime bootstrapper, downloading a platform-specific Bun ZIP from GitHub Releases, extracting it, and immediately executing the extracted Bun binary."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agentic-guide-d-3)

"The implementation also follows HTTP redirects without validating the destination and uses PowerShell with -ExecutionPolicy Bypass on Windows, increasing the risk for affected developer and CI/CD environments."

Wiz noted that the malicious packages match several features present in previous [TeamPCP](https://thehackernews.com/2026/04/checkmarx-confirms-github-repository.html) operations, indicating that the same threat actor is likely behind the latest campaign.

The suspicious versions were published on April 29, 2026, between 09:55 UTC and 12:14 UTC. The poisoned packages introduce a new package.json preinstall hook that runs a file named "setup.mjs," which acts as a loader for the Bun JavaScript runtime to execute the credential stealer and propagation framework ("execution.js").

According to Aikido, the malware is designed to harvest local developer credentials, GitHub and npm tokens, GitHub Actions secrets, and cloud secrets from AWS, Azure, GCP, and Kubernetes. The stolen data is encrypted and exfiltrated to public GitHub repositories created on the victim's own account with the description "A Mini Shai-Hulud has Appeared." As of writing, there are more than [1,100 repositories](https://github.com/search?q=%22A%20Mini%20Shai-Hulud%20has%20Appeared%22&type=repositories) with descriptions.

In addition, the 11.6 MB payload comes with capabilities to self-propagate through developer and release workflows, specifically using the GitHub and npm tokens to inject a malicious GitHub Actions workflow into the victim's repositories to steal repository secrets and publish poisoned versions of the npm packages to the registry.

However, the latest incident bears significant differences from prior [Shai-Hulud waves](https://thehackernews.com/2025/12/researchers-spot-modified-shai-hulud.html) -

* All exfiltrated data is encrypted with AES-256-GCM and encapsulates the key using RSA-4096 with a public key embedded in the payload, effectively making it decipherable only to the attacker.
* It exists on Russian-locale systems.
* The payload commits itself into every accessible GitHub repository by injecting a ".claude/settings.json" file that abuses Claude Code's SessionStart hook and a ".vscode/tasks.json" file with ["runOn": "folderOpen"](https://thehackernews.com/2026/04/285-million-drift-hack-traced-to-six.html) setting so that any attempt to open the infected repository in Microsoft Visual Studio Code (VS Code) or Claude Code causes the malware to be executed.

"This is one of the first supply chain attacks to target AI coding agent configurations as a persistence and propagation vector," StepSecurity said.

Further analysis into the root cause has revealed that the attackers compromised RoshniNaveenaS's account for the three "@cap-js" packages, followed by pushing a modified workflow to a non-main branch and using the extracted npm OIDC token to publish the malicious packages without provenance. As for mbt, it's suspected to involve the compromise of the "cloudmtabot" static npm token through an as-yet-undetermined channel.

"The cds-dbs team migrated to npm OIDC trusted publishing in November 2025," SafeDep said. "Under this setup, GitHub Actions can request a short-lived npm token without storing any long-lived secrets in the repository. The attacker reproduced this exchange manually in a CI step and printed the resulting token."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

"The critical configuration gap: npm’s OIDC trusted publisher configuration for @cap-js/sqlite trusted any workflow in cap-js/cds-dbs, not just the canonical release-please.yml on main. A branch push could exchange an OIDC token on behalf of the package if the workflow had id-token: write permission and the environment: npm reference."

In response to the incident, the [maintainers](https://github.com/SAP/cloud-mta-build-tool) of the packages have [released](https://github.com/cap-js/cds-dbs/) new safe versions that supersede the compromised releases -

* sqlite: [v2.4.0](https://github.com/cap-js/cds-dbs/releases/tag/sqlite-v2.4.0), [v2.3.0](https://github.com/cap-js/cds-dbs/releases/tag/sqlite-v2.3.0)
* postgres: [v2.3.0](https://github.com/cap-js/cd...