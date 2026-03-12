---
title: Credential Stuffing in 2025 – How Combolists, Infostealers and Account Takeover Became an Industry
url: https://www.darknet.org.uk/2026/03/credential-stuffing-in-2025-how-combolists-infostealers-and-account-takeover-became-an-industry/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2026-03-11
fetch_date: 2026-03-12T04:07:01.483624
---

# Credential Stuffing in 2025 – How Combolists, Infostealers and Account Takeover Became an Industry

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

You are here: [Home](https://www.darknet.org.uk/) / [Hacking News](https://www.darknet.org.uk/category/hacking-news/) / Credential Stuffing in 2025 – How Combolists, Infostealers and Account Takeover Became an Industry

# Credential Stuffing in 2025 – How Combolists, Infostealers and Account Takeover Became an Industry

March 11, 2026

Views: 182

Stolen credentials are now the single most reliable entry point into enterprise networks. Compromised credentials accounted for 22% of all confirmed data breaches in the period covered by [Verizon’s extended credential stuffing analysis accompanying the 2025 DBIR](https://www.verizon.com/business/resources/articles/credential-stuffing-attacks-2025-dbir-research/), making it the most common initial access vector for the third consecutive year. Credential stuffing, the automated replay of stolen username-password pairs at scale, requires minimal skill, costs almost nothing to run, and succeeds at rates that make it economically rational to run campaigns against thousands of targets simultaneously. Multi-factor authentication (MFA) remains the single most effective control against it, yet deployment gaps persist across sectors that should know better.

![Credential Stuffing in 2025 - How Combolists, Infostealers and Account Takeover Became an Industry](https://www.darknet.org.uk/wp-content/uploads/2026/03/Credential-Stuffing-in-2025-How-Combolists-Infostealers-and-Account-Takeover-Became-an-Industry-640x335.png)

## The Credential Supply Chain

Credential stuffing depends on a supply chain that runs from infostealer malware through dark web markets to attack tooling. Malware families, including Lumma, RedLine, StealC, and Acreed, scrape browser password vaults, saved cookies, and autofill data from compromised machines. The harvested data is identical to what tools like [DumpBrowserSecrets extract during post-exploitation](https://www.darknet.org.uk/2026/03/dumpbrowsersecrets-browser-credential-harvesting-with-app-bound-encryption-bypass/): saved passwords, session cookies, OAuth refresh tokens, and autofill entries pulled directly from Chrome, Edge, Firefox, and every other major browser. Attackers package that raw material into structured files known as combolists, formatted as email: password pairs, cleaned of duplicates, and categorised by service type or geography before selling them on.

Combolists trade freely across dark web forums, Telegram channels, and dedicated cracking communities. The [initial access broker ecosystem documented throughout 2025](https://www.darknet.org.uk/2025/11/initial-access-brokers-iab-in-2025-from-dark-web-listings-to-supply-chain-ransomware-events/) has normalised validated credentials as a commodity. Fresh lists built from recent infostealer logs command significantly higher prices than aged database dumps because they have higher validity rates. The Verizon analysis found that only 49% of a user’s passwords across different services are distinct. That figure is what makes credential stuffing economically viable: breach one service, and there is roughly a 50% chance the same password works elsewhere. Across millions of accounts, that probability becomes near-certainty.

The tooling that drives attacks is openly available. OpenBullet and its successor, SilverBullet, are credential-stuffing frameworks originally released as penetration testing utilities, now standard tools in account-takeover (ATO) operations. They automate the full attack loop: loading combolists, rotating through residential proxies to dodge rate limiting and IP blocks, sending login requests that mimic legitimate browser behaviour, and logging successful hits. Attackers also buy and sell custom configuration files, known as configs, that define the authentication flow for specific target services. Unofficial marketplaces offer configs for specific banking portals, SaaS platforms, and enterprise single sign-on (SSO) providers alongside combolists and proxy subscriptions.

## Three Case Studies from 2025

In late March 2025, coordinated credential stuffing attacks hit five major Australian superannuation funds simultaneously: AustralianSuper, Rest Super, Hostplus, Australian Retirement Trust, and Insignia Financial. As [BleepingComputer reported on the coordinated attacks](https://www.bleepingcomputer.com/news/security/australian-pension-funds-hit-by-wave-of-credential-stuffing-attacks/), attackers compromised over 20,000 accounts across the five funds, with four AustralianSuper members losing a combined AUD 500,000. The attackers used combolists from prior unrelated breaches. AustralianSuper offered MFA but did not enforce it at login, a gap that regulators identified as the primary enabling factor. Retirement funds make attractive targets because account balances are high, withdrawals are slow to reverse, and many members check their accounts infrequently.

In April 2025, VF Corporation notified customers of a credential-stuffing attack against the North Face online store. [BleepingComputer’s coverage of the April incident](https://www.bleepingcomputer.com/news/security/the-north-face-warns-customers-of-april-credential-stuffing-attack/) confirmed that attackers used credentials from earlier unrelated breaches to access accounts and exfiltrate names, email addresses, shipping addresses, phone numbers, purchase history, and dates of birth. Payment card data was not exposed, as a third-party provider handles payment processing. The April attack followed a March incident that exposed 15,700 accounts across The North Face and Timberland. It was the fourth credential stuffing incident against VF Corporation brands since 2020. The pattern reflects a structural problem: tens of millions of customer accounts, high password reuse rates, and authentication systems not designed to detect low-and-slow validation campaigns.

The Change Healthcare breach in February 2024 remains the most consequential recent example of credential-based initial access. The ALPHV/BlackCat ransomware group entered UnitedHealth’s Change Healthcare subsidiary through compromised Citrix credentials on a remote-access portal without MFA, as confirmed in Congressional testimony from UnitedHealth’s CEO. The attackers moved laterally through the billing network and deployed ransomware that shut down payment processing for healthcare providers across the United States for weeks. The incident produced a $22 million ransom payment and an estimated $872 million in reported disruption costs in the first quarter alone. One set of valid credentials on one unprotected endpoint caused one of the largest healthcare-sector disruptions in US history.

## Detection and Evasion Techniques

Modern credential stuffing campaigns specifically target the detection mechanisms most organisations have deployed. Attackers bypass velocity-based controls that flag high volumes of failed login attempts from a single IP by rotating through residential proxies. They distribute attempts across thousa...