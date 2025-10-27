---
title: Self-Replicating Worm Hits 180+ Software Packages
url: https://krebsonsecurity.com/2025/09/self-replicating-worm-hits-180-software-packages/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-17
fetch_date: 2025-10-02T20:15:18.797774
---

# Self-Replicating Worm Hits 180+ Software Packages

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Self-Replicating Worm Hits 180+ Software Packages

September 16, 2025

[33 Comments](https://krebsonsecurity.com/2025/09/self-replicating-worm-hits-180-software-packages/#comments)

At least 187 code packages made available through the JavaScript repository **NPM** have been infected with a self-replicating worm that steals credentials from developers and publishes those secrets on **GitHub**, experts warn. The malware, which briefly infected multiple code packages from the security vendor **CrowdStrike**, steals and publishes even more credentials every time an infected package is installed.

![](https://krebsonsecurity.com/wp-content/uploads/2025/09/shai-hulud.png)

The novel malware strain is being dubbed **Shai-Hulud** — after the name for the giant sandworms in Frank Herbert’s *Dune* novel series — because it publishes any stolen credentials in a new public GitHub repository that includes the name “Shai-Hulud.”

“When a developer installs a compromised package, the malware will look for a npm token in the environment,” said **Charlie Eriksen**, a researcher for the Belgian security firm [Aikido](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again). “If it finds it, it will modify the 20 most popular packages that the npm token has access to, copying itself into the package, and publishing a new version.”

At the center of this developing maelstrom are code libraries available on [**NPM**](https://www.npmjs.com/) (short for “Node Package Manager”), which acts as a central hub for JavaScript development and provides the latest updates to widely-used JavaScript components.

The Shai-Hulud worm emerged just days after unknown attackers [launched a broad phishing campaign](https://krebsonsecurity.com/2025/09/18-popular-code-packages-hacked-rigged-to-steal-crypto/) that spoofed NPM and asked developers to “update” their multi-factor authentication login options. That attack led to malware being inserted into at least two-dozen NPM code packages, but the outbreak was quickly contained and was narrowly focused on siphoning cryptocurrency payments.

![](https://krebsonsecurity.com/wp-content/uploads/2025/09/shai-hulud-packages.png)

In late August, another compromise of an NPM developer resulted in malware being added to “**nx**,” an open-source code development toolkit with as many as six million weekly downloads. In the nx compromise, the attackers introduced code that scoured the user’s device for authentication tokens from programmer destinations like GitHub and NPM, as well as SSH and API keys. But instead of sending those stolen credentials to a central server controlled by the attackers, the malicious nx code created a new public repository in the victim’s GitHub account, and published the stolen data there for all the world to see and download.

Last month’s attack on nx did not self-propagate like a worm, but this Shai-Hulud malware does and bundles reconnaissance tools to assist in its spread. Namely, it uses the open-source tool [TruffleHog](https://github.com/trufflesecurity/trufflehog) to search for exposed credentials and access tokens on the developer’s machine. It then attempts to create new GitHub actions and publish any stolen secrets.

“Once the first person got compromised, there was no stopping it,” Aikido’s Eriksen told KrebsOnSecurity. He said the first NPM package compromised by this worm appears to have been altered on Sept. 14, around 17:58 UTC.

The security-focused code development platform **socket.dev** [reports](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages) the Shai-Halud attack briefly compromised at least 25 NPM code packages managed by CrowdStrike. Socket.dev said the affected packages were quickly removed by the NPM registry.

In a written statement shared with KrebsOnSecurity, CrowdStrike said that after detecting several malicious packages in the public NPM registry, the company swiftly removed them and rotated its keys in public registries.

“These packages are not used in the Falcon sensor, the platform is not impacted and customers remain protected,” the statement reads, referring to the company’s widely-used endpoint threat detection service. “We are working with NPM and conducting a thorough investigation.”

A [writeup on the attack](https://www.stepsecurity.io/blog/ctrl-tinycolor-and-40-npm-packages-compromised) from **StepSecurity** found that for cloud-specific operations, the malware enumerates AWS, Azure and Google Cloud Platform secrets. It also found the entire attack design assumes the victim is working in a Linux or macOS environment, and that it deliberately skips Windows systems.

StepSecurity said Shai-Hulud spreads by using stolen NPM authentication tokens, adding its code to the top 20 packages in the victim’s account.

“This creates a cascading effect where an infected package leads to compromised maintainer credentials, which in turn infects all other packages maintained by that user,” StepSecurity’s **Ashish Kurmi** wrote.

Eriksen said Shai-Hulud is still propagating, although its spread seems to have waned in recent hours.

“I still see package versions popping up once in a while, but no new packages have been compromised in the last ~6 hours,” Eriksen said. “But that could change now as the east coast starts working. I would think of this attack as a ‘living’ thing almost, like a virus. Because it can lay dormant for a while, and if just one person is suddenly infected by accident, they could restart the spread. Especially if there’s a super-spreader attack.”

For now, it appears that the web address the attackers were using to exfiltrate collected data was disabled due to rate limits, Eriksen said.

**Nicholas Weaver** is a researcher with the **International Computer Science Institute**, a nonprofit in Berkeley, Calif. Weaver called the Shai-Hulud worm “a supply chain attack that conducts a supply chain attack.” Weaver said NPM (and all other similar package repositories) need to immediately switch to a publication model that requires explicit human consent for every publication request using a phish-proof 2FA method.

“Anything less means attacks like this are going to continue and become far more common, but switching to a 2FA method would effectively throttle these attacks before they can spread,” Weaver said. “Allowing purely automated processes to update the published packages is now a proven recipe for disaster.”

*This entry was posted on Tuesday 16th of September 2025 10:08 AM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[Aikido](https://krebsonsecurity.com/tag/aikido/) [Ashish Kurmi](https://krebsonsecurity.com/tag/ashish-kurmi/) [Charlie Eriksen](https://krebsonsecurity.com/tag/charlie-eriksen/) [GitHub](https://krebsonsecurity.com/tag/github/) [International Computer Science Institute](https://krebsonsecurity.com/tag/international-computer-science-institute/) [Nicholas Weaver](https://krebsonsecurity.com/tag/nicholas-...