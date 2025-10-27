---
title: CyberArk and HashiCorp Flaws Enable Remote Vault Takeover Without Credentials
url: https://thehackernews.com/2025/08/cyberark-and-hashicorp-flaws-enable.html
source: The Hacker News
date: 2025-08-10
fetch_date: 2025-10-07T00:47:47.208420
---

# CyberArk and HashiCorp Flaws Enable Remote Vault Takeover Without Credentials

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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [CyberArk and HashiCorp Flaws Enable Remote Vault Takeover Without Credentials](https://thehackernews.com/2025/08/cyberark-and-hashicorp-flaws-enable.html)

**Aug 09, 2025**Ravie LakshmananVulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDkIaNlR28X3sy64dylpySxWL_x9gQVG2zLdT30DLovuaM9jRfB2Gp9TumFZhqhvVJAwtQZrBaaXlsmIwtohBQ_FGI1iZtwzLvl4uINvF7i8gVLEPO_dJka0AACDxXEmTk55kumz7kWjuo2yRFARk4NcCkoXyXWMA534BPMcZZaduLDUR4Di8m9K1-sEIm/s790-rw-e365/vault-flaw.jpg)

Cybersecurity researchers have discovered over a dozen vulnerabilities in enterprise secure vaults from CyberArk and HashiCorp that, if successfully exploited, can allow remote attackers to crack open corporate identity systems and extract enterprise secrets and tokens from them.

The 14 vulnerabilities, collectively named [Vault Fault](https://cyata.ai/vault-fault/), affect CyberArk Secrets Manager, Self-Hosted, and Conjur Open Source and HashiCorp Vault, according to a report from an identity security firm Cyata. Following responsible disclosure in May 2025, the flaws have been addressed in the following versions -

* [CyberArk Secrets Manager and Self-Hosted 13.5.1 and 13.6.1](https://github.com/cyberark/conjur/releases/tag/v1.22.1)
* [CyberArk Conjur Open Source 1.22.1](https://github.com/cyberark/conjur/releases/tag/v1.22.1)
* [HashiCorp Vault Community Edition 1.20.2 or Vault Enterprise 1.20.2, 1.19.8, 1.18.13, and 1.16.24](https://discuss.hashicorp.com/t/hcsec-2025-22-multiple-vulnerabilities-impacting-hashicorp-vault-and-vault-enterprise/76096)

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

These include authentication bypasses, impersonation, privilege escalation bugs, code execution pathways, and root token theft. The most severe of the issues allows for remote code execution, allowing attackers to takeover the vault under certain conditions without any valid credentials -

* **CVE-2025-49827** (CVSS score: 9.1) - Bypass of IAM authenticator in CyberArk Secrets Manager
* **CVE-2025-49831** (CVSS score: 9.1) - Bypass of IAM authenticator in CyberArk Secrets Manager via a misconfigured network device
* **CVE-2025-49828** (CVSS score: 8.6) - Remote code execution in CyberArk Secrets Manager
* **CVE-2025-6000** (CVSS score: 9.1) - Arbitrary remote code execution via plugin catalog abuse in HashiCorp Vault
* **CVE-2025-5999** (CVSS score: 7.2) - Privilege escalation to root via policy normalization in HashiCorp Vault

In addition, vulnerabilities have also been discovered in HashiCorp Vault's lockout protection logic, which is designed to throttle brute-force attempts, that could permit an attacker to infer which usernames are valid by taking advantage of a timing-based side channel and even reset the lockout counter by changing the case of a known username (e.g., admin to Admin).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQjURf-Yq7W6PJ6Gc7ak4X2KpAS5zxiipvbpCSRGROEPsH5f1cV-4LmVLm1wW7qftceZkM2qqjaHSFjccwMLX_me-wkX6BcPXwRqXpIVOurgGjVx_B5IxylcBzW7Dd0vmlEecgk-kwWNZFBhACu__My76dWImqH9lTY7qSWJRGnE21Z2ydzFsTx5i7Eftv/s790-rw-e365/vault.jpg)

Two other shortcomings identified by the Israeli company made it possible to weaken lockout enforcement and bypass multi-factor authentication (MFA) controls when username\_as\_alias=true in the LDAP auth configuration and MFA enforcement is applied at the EntityID or IdentityGroup level.

In the attack chain detailed by the cybersecurity company, it's possible to leverage a certificate entity impersonation issue (CVE-2025-6037) with CVE-2025-5999 and CVE-2025-6000 to break the authentication layer, escalate privileges, and achieve code execution. CVE-2025-6037 and CVE-2025-6000 are said to have existed for over eight and nine years, respectively.

Armed with this capability, a threat actor could further weaponize the access to delete the "core/hsm/\_barrier-unseal-keys" file, effectively turning a security feature into a ransomware vector. What's more, the Control Group feature can be undermined to send HTTP requests and receive responses without being audited, creating a stealthy communication channel.

"This research shows how authentication, policy enforcement, and plugin execution can all be subverted through logic bugs, without touching memory, triggering crashes, or breaking cryptography," security researcher Yarden Porat [said](https://cyata.ai/blog/cracking-the-vault-how-we-found-zero-day-flaws-in-authentication-identity-and-authorization-in-hashicorp-vault/).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In a similar vein, the vulnerabilities [discovered](https://www.cyberark.com/resources/product-insights-blog/addressing-recent-vulnerabilities-and-our-commitment-to-security) in CyberArk Secrets Manager/Conjur allow for authentication bypass, privilege escalation, information disclosure, and arbitrary code execution, effectively opening the door to a scenario where an attacker can craft an exploit chain to obtain unauthenticated access and run arbitrary commands.

The attack sequence unfolds as follows -

* IAM authentication bypass by forging valid-looking GetCallerIdentity responses
* Authenticate as a policy resource
* Abuse the Host Factory endpoint to create a new host that impersonates a valid policy template
* Assigned a malicious Embedded Ruby (ERB) payload directly to the host
* Trigger the execution of the attached ERB by invoking the Policy Factory endpoint

"This exploit chain moved from unauthenticated access to full remote code execution without ever supplying a password, token, or AWS credentials," Porat [noted](https://cyata.ai/blog/exploiting-a-full-chain-of-trust-flaws-how-we-went-from-unauthenticated-to-arbitrary-remote-code-execution-rce-in-cyberark-conjur/).

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWld...