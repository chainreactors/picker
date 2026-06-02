---
title: Miasma Supply Chain Attack Compromises Red Hat npm Packages with Credential-Stealing Worm
url: https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html
source: The Hacker News
date: 2026-06-01
fetch_date: 2026-06-02T06:33:15.958206
---

# Miasma Supply Chain Attack Compromises Red Hat npm Packages with Credential-Stealing Worm

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Miasma Supply Chain Attack Compromises Red Hat npm Packages with Credential-Stealing Worm](https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html)

**Ravie Lakshmanan**Jun 01, 2026Supply Chain Attack / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOyc2NTiIl0XKOTZBsFh1bTPqNpVXfDhASWkCsYz17d-nbiWVKlxCzoq3WthMD8kMomrRPPOYLM-XRmSdtXNKAxtk1QLtmZH47y2RExMGohBaBDPkpFp2PteUgaA16VcCs7tK-ImqCiLnpqyLg8Pwp6cWE5d9QT2_v0-QBduT7ovYrs7WSZ9t1MnQJ4EuO/s1700-e365/redhat.png)

A new [Mini Shai-Hulud](https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html) supply chain attack campaign, codenamed **Miasma**, has compromised @redhat-cloud-services packages to steal credentials and secrets from developer machines and deliver a self-propagating worm.

"This is effectively a Mini Shai-Hulud campaign: it uses the same core tactics of install-time execution, credential harvesting, CI/CD targeting, encrypted exfiltration, and potential downstream propagation," Socket [said](https://socket.dev/blog/mini-shai-hulud-campaign-hits-red-hat-cloud-services-npm-packages).

Exactly who is behind the attack activity is presently unknown given that TeamPCP, an infamous cybercrime group, has open-sourced the attack tools linked to the Shai-Hulud worm, opening the door for other threat actors to pull off similar attacks and making definitive attribution harder.

The names of some of the affected packages are listed below -

* @redhat-cloud-services/vulnerabilities-client
* @redhat-cloud-services/tsc-transform-imports
* @redhat-cloud-services/topological-inventory-client
* @redhat-cloud-services/sources-client
* @redhat-cloud-services/rule-components
* @redhat-cloud-services/remediations-client
* @redhat-cloud-services/rbac-client

Per analyses from [Aikido Security](https://www.aikido.dev/blog/red-hat-npm-packages-compromised-credential-stealing-worm), [JFrog](https://research.jfrog.com/post/shai-hulud-miasma-redhat-cloud-services/), [Microsoft](https://x.com/MsftSecIntel/status/2061485730958848188), [OX Security](https://www.ox.security/blog/new-npm-supply-chain-attack-redhat-cloud-services-compromised), [SafeDep](https://safedep.io/redhat-cloud-services-hit-by-mini-shai-hulud-npm-worm/), [StepSecurity](https://www.stepsecurity.io/blog/multiple-redhat-cloud-services-npm-packages-compromised), and [Wiz](https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages), the npm packages contain an obfuscated preinstall hook that's designed to collect GitHub Actions secrets, npm tokens, cloud credentials, Kubernetes and Vault material, SSH keys, Git credentials, and other sensitive files.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Like observed in prior Mini Shai-Hulud waves, the malware also contains encrypted exfiltration logic that transmits the data to "api.anthropic[.]com:443/v1/api" and uses GitHub as a fallback mechanism. This indicates attempts made by the attacker to both steal credentials and weaponize them to further poison the software supply chain.

"It commits the encrypted result envelope through the GitHub API," Socket said. "The commit message can include: IfYouInvalidateThisTokenItWillNukeTheComputerOfTheOwner:<token>."

Another noteworthy step carried out by the malware is to avoid execution on Russian-language systems, a pattern also observed in the [GlassWorm](https://thehackernews.com/2026/05/glassworm-malware-takedown-disrupts.html) supply chain campaigns.

"For npm, the payload calls the OIDC token exchange and whoami endpoints, repackages a tarball (updateTarball, package-updated.tgz), and signs the artifact through Sigstore," SafeDep said. "Stolen credentials exfiltrate to attacker-created public GitHub repositories, each carrying the description Miasma: The Spreading Blight."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhORC_YvikOzAygGwJ1HFGJePm594z3zlUFKSKKdN0iltmsIOHeADbUCUXBQsuHx2wm0qYJWdbOQir9_OPLjMQdRCdtqF9Tgq_prOZU7hqDSOBca13vd2JC-7Cw7CSmyJhtKfWgDGA4w8jnNPyxoa6OSzoeevR7XDzBxTeuAJS4LkcgFqZfNWlWt2SbWX3b/s1700-e365/ox.jpg)

The first commit containing the "Miasma: The Spreading Blight" string appeared on May 29, 2026, OX Security noted, indicating that either this variant was active since then, or the threat actor started testing around that time.

As for GitHub, the malware enumerates repositories the token can write to, reads action.yml/action.yaml via GraphQL, and commits a workflow through the createCommitOnBranch mutation so that the commit appears as a verified, signed change. Other actions carried out by the malware are listed below -

* Attempt privilege escalation by launching a container that bind-mounts the host /etc/sudoers.d and grants the CI runner passwordless sudo
* Check for endpoint protection from CrowdStrike, SentinelOne, Carbon Black, and StepSecurity Harden-Runner before commencing the malicious actions
* Establish persistence by injecting a SessionStart hook to Anthropic Claude Code and a tasks.json with "runOn": "folderOpen" for Microsoft Visual Studio Code projects so that the malware is automatically launched during every session

"One of the main changes in this new variant is the addition of new data collectors focused on cloud identities," Wiz researchers said. "Specifically, collectors for GCP and Azure identities were added that collect all identities the infected machine has access to. While previous versions of the malware primarily focused on extracting secrets from these environments, this variant suggests an increased attacker focus on gaining and leveraging access to the cloud itself.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGTVg27aWl6zkTByCCDer2yrvEpvzzikpo4e0Lc38OuKHhaJqSbyIxuTyDNMpPwFUJvkv-SeI6KAZKdQMyM68xnIgiCaKUwmq7t2gvlSS7Tz16sOhpjEQyICRVduoZ9OZHZThQFvRvywX43N9wuFKbrEwopVTP9E9VUqp9T5mP0FeceAjgero62yLAWtLc/s...