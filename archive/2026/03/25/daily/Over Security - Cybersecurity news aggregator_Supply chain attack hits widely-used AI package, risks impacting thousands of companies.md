---
title: Supply chain attack hits widely-used AI package, risks impacting thousands of companies
url: https://therecord.media/supply-chain-attack-hits-widely-used-ai-package
source: Over Security - Cybersecurity news aggregator
date: 2026-03-25
fetch_date: 2026-03-26T04:31:41.260640
---

# Supply chain attack hits widely-used AI package, risks impacting thousands of companies

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![enter hacker](https://cms.therecord.media/uploads/large_mohammad_mardani_MC_Pqw_Z_Exfx_M_unsplash_b240343335.jpg)

Image: Mohammad Mardani via Unsplash

[Alexander Martin](/author/alexander-martin)March 25th, 2026

# Supply chain attack hits widely-used AI package, risks impacting thousands of companies

LiteLLM, an open-source Python package widely used by artificial intelligence systems, has been compromised by hackers in a supply chain attack that researchers say could impact tens of thousands of corporate environments.

Compromised versions of the package (identified as 1.82.7 and 1.82.8) were published on the Python Package Index on Tuesday and unwittingly downloaded into development and cloud environments, according to security researchers.

Experts at Sonatype [said](https://www.sonatype.com/blog/compromised-litellm-pypi-package-delivers-multi-stage-credential-stealer) the compromised packages were available for at least two hours on March 24, adding that “given the package’s three million daily downloads” the hackers could have reached a “significant” number of victims during that time.

The incident highlights growing concerns over the security of the open-source software supply chain, where widely-used tools maintained by small teams can provide a gateway into thousands of organizations if compromised.

Last year, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) and software company Red Hat issued an [urgent alert](https://therecord.media/malicious-backdoor-code-linux-red-hat-cisa) about a backdoor embedded in the XZ Utils tool.

Similar attacks, including the [Shai Hulud worm](https://therecord.media/cisa-urges-software-reviews-malicious-packages), have seen attackers target software dependencies trusted by developers in order to scale their intrusions far beyond a single victim, embedding malicious code deep inside corporate systems.

In the liteLLM incident, the hackers introduced malicious code to the legitimate software package. How they managed to do so is unclear, although researchers say compromising a maintainer’s account is the most likely as the malicious versions were uploaded using valid publishing access.

The manipulated packages contained malicious code designed to extract sensitive data — including cloud credentials, API keys and cryptocurrency wallets — and maintain access by installing a persistent downloader allowing the attackers to gain deeper access and carry out follow-on intrusions.

Adam Reynolds, senior security researcher at Sonatype, said his team identified some unusual behaviours from the malware, including that it only reaches out to its command endpoint every 50 minutes.

That long delay could help evade sandbox environments that typically execute samples for shorter periods, or it could function as a heartbeat mechanism allowing the operators to distinguish real targets from researchers attempting to probe their infrastructure.

“In some cases the response from the server only contained a link to a song hosted on YouTube, which reinforces the idea that payload delivery is being selectively controlled,” said Reynolds.

It is not known how many organizations have been impacted by the incident, but Wiz Research [estimated](https://www.wiz.io/blog/teampcp-attack-kics-github-action) the package was present in roughly 36% of all cloud environments. Users have been warned to treat any credentials exposed in affected environments as potentially compromised.

Wiz researchers say the incident is part of a broader campaign claimed by a group calling itself TeamPCP, which uses a public Telegram channel to propagandize and solicit business from other cybercriminals.

“This isn’t just credential theft,” said Ben Read, director of strategic threat intelligence at Wiz. “By moving across widely used tools, they are creating a ‘snowball effect’ that enables further compromise.”

TeamPCP has previously claimed responsibility for an attack affecting Aqua Security’s Trivy vulnerability scanner — an incident [confirmed](https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23) by the company — and claims to be working with several other cybercriminal organizations, although this has not yet been confirmed.

The group said it intends to continue targeting widely-used open-source projects, although its claims could not be verified and such groups often overstate their successes.

A Telegram account claiming to be the group’s new leader said on Wednesday it was “actively sorting through the credential sets, this is an astronomical amount even for the man power and operational capacity between the teams, it will all be worth it though.”

While there have been no publicly-confirmed reports of widespread exploitation tied to the liteLLM incident, security experts warned that the downstream risks could be significant if stolen credentials are reused in subsequent attacks.

“For most individuals, the immediate risk is low unless they directly installed the affected versions,” said Reynolds. “This is first and foremost a supply chain compromise targeting developers, organizations, and technical environments using litellm. However, the downstream impact is where things get more serious.

“If organizations were compromised, the individuals whose data they hold could absolutely be affected. Because the malware targets such a broad range of credentials and litellm is widely used, this creates the potential for second- and third-order effects that may ripple outward over time, leading to further breaches, service disruptions, or misuse of sensitive data well beyond the initial point of compromise,” said Reynolds.

“This isn’t an isolated incident; it’s a systemic campaign,” Read said. “It will likely continue.”

*Additional reporting by [Jonathan Greig](https://therecord.media/author/jonathan-greig).*

* [Cybercrime](/police-dismantle-dark-web-network-exploiting-child-abuse-images)
* [News](/)
* [Technology](/news/technology)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

No previous article

No new articles

[![Alexander Martin](https://cms.therecord.media/uploads/headshot_79eb085f87.jpeg)](/author/alexander-martin)

[Alexander Martin](/author/alexander-martin)

is the UK Editor for Recorded Future News. He was previously a technology reporter for Sky News and a fellow at the European Cyber Conflict Research Initiative, now Virtual Routes. He can be reached securely using Signal on: AlexanderMartin.79

## Briefs

* [Ransomware attack disrupts operation at major Spanish fishing portMarch 25th, 2026](/port-of-vigo-ransomware)
* [Puerto Rico government agency cancels driver’s license appointments after cyberattackMarch 25th, 2026](/puerto-rico-gov-agency-cancels-driver-license-appointments-cyber-incident)
* [UK cyber chief urges ‘full court press’ to counter rising cyber threatsMarch 25th, 2026](/uk-cyber-chief-urges-full-court-press-to-counter-risks)
* [Dutch Finance Ministry probing cyber breach affecting internal systemsMarch 24th, 2026](/netherla...