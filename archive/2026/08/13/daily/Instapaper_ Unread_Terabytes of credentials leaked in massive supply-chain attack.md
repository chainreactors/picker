---
title: Terabytes of credentials leaked in massive supply-chain attack
url: https://arstechnica.com/security/2026/08/terabytes-of-credentials-leaked-in-massive-supply-chain-attack/
source: Instapaper: Unread
date: 2026-08-13
fetch_date: 2026-08-14T04:01:09.586341
---

# Terabytes of credentials leaked in massive supply-chain attack

[Skip to content](#main)
[Ars Technica home](https://arstechnica.com/)

Sections

[Forum](/civis/)[Subscribe](/subscribe/)[Search](/search/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

* [Feature](/features/)
* [Reviews](/reviews/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

[Forum](/civis/)[Subscribe](/subscribe/)

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Pin to story

Theme

* HyperLight
* Day & Night
* Dark
* System

[Search](/search/ "Search")

Sign In

Sign in dialog...

Sign in

TEAMPCP’S RAMPAGE CONTINUES

# Terabytes of credentials leaked in massive supply-chain attack

The data was scraped and exfiltrated from 2,500 users of a compromised AI package.

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
–

Aug 12, 2026 5:43 pm
| [69](https://arstechnica.com/security/2026/08/terabytes-of-credentials-leaked-in-massive-supply-chain-attack/#comments "69 comments")

[![A cartoon man runs across a white field of ones and zeroes.](https://cdn.arstechnica.net/wp-content/uploads/2021/07/data-breach-300x163.jpeg)
![A cartoon man runs across a white field of ones and zeroes.](https://cdn.arstechnica.net/wp-content/uploads/2021/07/data-breach.jpeg)](https://cdn.arstechnica.net/wp-content/uploads/2021/07/data-breach.jpeg)

Credit:
[Getty Images](https://www.gettyimages.com/)

Credit:
[Getty Images](https://www.gettyimages.com/)

Text
settings

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Minimize to nav

Terabytes worth of credentials, many belonging to the world’s biggest and most sensitive organizations, have been exposed in a supply-chain attack on LiteLLM, an open source tool that streamlines AI-driven software development. Microsoft, Amazon, Cisco, Samsung, and Salesforce are only a handful of the entities whose access secrets were exposed.

The revelation was posted on [Tuesday](https://www.cloudsek.com/blog/ai-supply-chain-breach-2500-companies-434000-cicd-pipelines) and [Wednesday](https://www.hudsonrock.com/blog/largest-ai-supply-chain-breach-of-2026-litellm-hack-impacts-thousands-of-global-enterprises-claim-your-ethical-disclosure) by security firms CloudSEK and Hudson Rock. CloudSEK said it found cloud keys, repository tokens, SSH keys, Kubernetes secrets, package publishing credentials, environment variables, and AI provider keys that could allow attackers to gain access to more than 2,500 organizations.

## 40 minutes is all it takes

The credentials were extracted during a 40-minute window in March while the victims used compromised versions of LiteLLM downloaded from the package’s official location in the Python Package Index repository. Hudson Rock said it made the discovery after analyzing a 195TB file that it obtained. Neither firm identified the source of the information.

The LiteLLM compromise was the result of a [previous supply-chain attack](https://arstechnica.com/security/2026/03/widely-used-trivy-scanner-compromised-in-ongoing-supply-chain-attack/) that infected the widely used vulnerability scanner Trivy. Other software infected in the campaign includes [KICS](https://www.kics.io/) and the [Telnyx Python SDK](https://developers.telnyx.com/development/sdk/python). TeamPCP, a ramshackle but extremely capable gang largely made up of teenagers, took credit for the attack, and researchers have largely corroborated the claim.

“I’ve confirmed the data is legit, by the way, multiple victim orgs,” independent security researcher Kevin Beaumont [said](https://infosec.exchange/%40GossiTheDog%40cyberplace.social/117082985466021541). “It contains a significant volume of sensitive content at orgs. It’s a massive supply chain breach due to poor AI security—not because AI is the threat, but teens can run circles around orgs obsessed with rushing out AI and poor DevOps security.”

The compromised versions of all four software packages contained code that accessed the memory of infected machines, scraped its contents, and exfiltrated it through an attacker-controlled channel. The data is filled with an assortment of information. Interspersed in the wall of data are credentials to software pipelines maintained by the tens of thousands of organizations that ran LiteLLM during the 40-minute span that the supply-chain attack remained active.

In all, both security firms said some 434,000 CI/CD (continuous integration/continuous delivery) software pipelines had credentials exposed after running the compromised LiteLLM versions. In many cases, researchers at CloudSEK and Hudson Rock had trouble identifying the organizations the credentials belonged to. For instance, an email address in the dump from the domain @siriusxm.com ultimately didn’t indicate a breach at the satellite broadcaster, but rather one within the infrastructure of SiriusXM subsidiary AdsWizz.

[![](https://cdn.arstechnica.net/wp-content/uploads/2026/08/microsoft-azure-credentials-640x392.png)](https://cdn.arstechnica.net/wp-content/uploads/2026/08/microsoft-azure-credentials.png)

A trove of internal corporate secrets, exposing sensitive tokens for platforms such as Salesforce (SALESFORCE\_CLIENT\_SECRET), Slack (SLACK\_SIGNING\_SECRET), and Microsoft Azure environments.

Credit:
Hudson Rock

A trove of internal corporate secrets, exposing sensitive tokens for platforms such as Salesforce (SALESFORCE\_CLIENT\_SECRET), Slack (SLACK\_SIGNING\_SECRET), and Microsoft Azure environments.
Credit:
Hudson Rock

A full list of organizations is [here](https://exposure.cloudsek.com/ai-supply-chain-incident). The researchers had high confidence that these organizations had their credentials exposed:

* Nvidia Corporation
* Amazon Web Services (AWS)
* Samsung Electronics
* samsung.com
* Salesforce, Inc.
* Cisco Systems, Inc.
* F. Hoffmann-La Roche AG
* ServiceNow
* Siemens AG
* S&P Global
* Airbus US Space & Defense
* John Deere
* Regeneron Pharmaceuticals, Inc.
* London Stock Exchange Group (LSEG)
* Thomson Reuters
* FedEx
* Munich Remunichre.com
* MediaTek Inc.
* Volkswagen AG
* Deloitte
* The Kroger Co.
* Siemens Energy
* Thales Group
* X Corp (Twitter)
* Zscaler, Inc.
* Epic Games
* Orange S.A.
* HP Inc.
* Philips
* Fortum Oyj
* Vodafone Group Plc
* Carl Zeiss AG
* Deutsche Bahn AG
* NGINX, Inc.
* BT Group
* Liebherr
* Krungthai Bank Public Company Limited
* Roku, Inc.

“Many CI/CD pipelines are configured generically,” Hudson Rock said. “The dumped variables contain active database passwords, third-party API keys, and cloud credentials without any identifiable company email, custom domain string, or internal server name. This means countless organizations currently have active secrets sitting in this database, completely unaware of their exposure.”

## Welcome to the new world of supply-chain attacks

Both firms are urging all organizations that used the compromised versions of LiteLLM—particularly those listed in the high-confidence section of the list—to thoroughly r...