---
title: Major Cyber Attacks in March 2026: OAuth Phishing, SVG Smuggling, Magecart, and More
url: https://any.run/cybersecurity-blog/major-cyber-attacks-march-2026/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-01
fetch_date: 2026-04-02T04:31:09.987450
---

# Major Cyber Attacks in March 2026: OAuth Phishing, SVG Smuggling, Magecart, and More

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* + Search

![Major Cyber Attacks in March 2026: OAuth Phishing, SVG Smuggling, Magecart, and More ](/cybersecurity-blog/wp-content/uploads/2026/03/5-Major-Cyber-Attacks-in-February-2026_cover.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Major Cyber Attacks in March 2026: OAuth Phishing, SVG Smuggling, Magecart, and More

April 1, 2026

[Add comment](#comments-19709)
790 views
13 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Major Cyber Attacks in March 2026: OAuth Phishing, SVG Smuggling, Magecart, and More

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2026/03/5-Major-Cyber-Attacks-in-February-2026_cover-1024x497.png)

  #### Major Cyber Attacks in March 2026: OAuth Phishing, SVG Smuggling, Magecart, and More

  790
  0](/cybersecurity-blog/major-cyber-attacks-march-2026/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Cross-Platform Threat Analysis with macOS, SSL Decryption, and 1,300+ New Detections

  1900
  0](/cybersecurity-blog/release-notes-march-2026/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/03/RSAC_cover-1024x497.png)

  #### ANY.RUN at RSAC™ 2026: Highlights & Industry Recognition

  878
  0](/cybersecurity-blog/rsac-2026-highlights/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Major Cyber Attacks in March 2026: OAuth Phishing, SVG Smuggling, Magecart, and More

March 2026 brought a wave of cyber attacks that reflected how quickly modern threats can move from subtle early signals to serious business impact. [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=major-cyber-attacks-march-2026&utm_term=010426&utm_content=linktolanding) analysts identified and explored several major threats this month, exposing phishing campaigns, stealthy malware, payment-skimming activity, and resilient botnet infrastructure affecting organizations across industries.

From Microsoft 365 token abuse and registry-hidden RAT delivery to card theft, macOS backdoor activity, and multi-vector DDoS operations, the threat landscape in March showed how much harder early detection has become for security teams.

## Key Business Risks That Stood Out in March Attacks

* Trusted services and normal-looking workflows were repeatedly used to hide malicious activity, increasing the risk of delayed detection across enterprise email, cloud, payment, and endpoint environments.

* Attacks observed in March affected industries including **government,**[**finance**](https://any.run/by-industry/finance/)**, healthcare, technology, education, manufacturing, and energy**, with risks extending beyond initial access into token abuse, remote access, card theft, and broader malware deployment.

* Stealthy, multi-stage delivery methods made early signals weaker and investigations slower, raising the likelihood of escalation before security teams could confirm malicious behavior.

* For organizations, the business impact was not limited to infection alone, but included **fraud, downtime, deeper compromise, and higher operational costs tied to delayed response**.

Reduce  the risk of delayed detection

Help your team investigate faster and respond earlier

[Power up your SOC](https://any.run/enterprise/?utm_source=anyrunblog&utm_medium=article&utm_campaign=major-cyber-attacks-march-2026&utm_term=010426&utm_content=linktoenterprise#contact-sales)

## 1. EvilTokens: OAuth Device Code Phishing Enables M365 Account Takeover Without Credential Theft

[Post on X](https://x.com/anyrun_app/status/2029171336719810710)

[Check detailed breakdown](https://any.run/cybersecurity-blog/oauth-device-code-phishing/)

ANY.RUN analysts observed a sharp rise in **EvilTokens**, a phishing campaign abusing Microsoft’s OAuth Device Code flow, with more than **180 phishing URLs detected in just one week**. Instead of stealing credentials on a fake login page, attackers trick victims into entering a verification code on **microsoft[.]com/devicelogin**, which causes Microsoft to issue OAuth tokens directly to the attacker.

![](/cybersecurity-blog/wp-content/uploads/2026/04/HCkQkhaWAAAle4c-768x1024.jpeg)

This makes EvilTokens especially dangerous for organizations relying on traditional phishing detection. The user signs in through a legitimate Microsoft page, completes MFA, and never submits credentials to the phishing site. As a result, the compromise shifts from **password theft to token abuse**, giving attackers access to Microsoft 365 resources while blending into normal authentication activity.

Because the workflow runs over encrypted HTTPS and uses legitimate Microsoft infrastructure, key attack signals are often hidden from security teams. That delays validation, extends investigations, and increases the chance of escalation before analysts can confirm what happened.

[See full attack flow exposed in ANY.RUN Sandbox](https://app.any.run/tasks/885afc1c-b616-46d7-9bc3-81185ee07fe3?utm_source=anyrunblog&utm_medium=article&utm_campaign=major-cyber-attacks-march-2026&utm_term=010426&utm_content=linktoservice)

![Fake verification granting access to external client](/cybersecurity-blog/wp-content/uploads/2026/04/oauth_3-1024x657.png)

Inside ANY.RUN Sandbox, automatic **SSL decryption** revealed the hidden JavaScript and backend communication used to orchestrate the phishing flow. In this case, analysts uncovered high-confidence network indicators such as:

* /api/device/start

* /api/device/status/\*

* X-Antibot-Token

When seen in HTTP requests to non-legitimate hosts, these artifacts become strong hunting signals for identifying related phishing infrastructure and improving detection coverage.

To investigate similar activity and validate detection logic, use this [TI Loo...