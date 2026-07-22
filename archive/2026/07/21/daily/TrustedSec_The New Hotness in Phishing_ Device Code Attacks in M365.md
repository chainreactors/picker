---
title: The New Hotness in Phishing: Device Code Attacks in M365
url: https://trustedsec.com/blog/the-new-hotness-in-phishing-device-code-attacks-in-m365
source: TrustedSec
date: 2026-07-21
fetch_date: 2026-07-22T05:04:14.042954
---

# The New Hotness in Phishing: Device Code Attacks in M365

[Skip to Main Content](#main)

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [The New Hotness in Phishing: Device Code Attacks in M365](https://trustedsec.com/blog/the-new-hotness-in-phishing-device-code-attacks-in-m365)

July 21, 2026

# The New Hotness in Phishing: Device Code Attacks in M365

Written by
Lumi Taiwo and
Danny Dubree

Threat Hunting
Incident Response
Social Engineering

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/HotnessInPhishing_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1784292695&s=6a941ef4470363f5e5f025ea42bb832d)

Table of contents

* [1. The Attack, Step by Step](#Attack)
* [2. What the Tokens Unlock](#Unlock)
* [3. What It Looks Like in Your Logs](#Logs)
* [4. Stopping It: Prevention and Containment](#Stopping)
* [5. The Bottom Line](#Bottom)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#89b6fafcebe3eceafdb4cae1eceae2acbbb9e6fcfdacbbb9fde1e0faacbbb9e8fbfde0eae5ecacbbb9effbe6e4acbbb9ddfbfcfafdeceddaeceaacbbb8afe8e4f9b2ebe6edf0b4dde1ecacbbb9c7ecfeacbbb9c1e6fde7ecfafaacbbb9e0e7acbbb9d9e1e0fae1e0e7eeacbac8acbbb9cdecffe0eaecacbbb9cae6edecacbbb9c8fdfde8eae2faacbbb9e0e7acbbb9c4babfbcacbac8acbbb9e1fdfdf9faacbac8acbbcfacbbcffdfbfcfafdecedfaeceaa7eae6e4acbbcfebe5e6eeacbbcffde1eca4e7ecfea4e1e6fde7ecfafaa4e0e7a4f9e1e0fae1e0e7eea4edecffe0eaeca4eae6edeca4e8fdfde8eae2faa4e0e7a4e4babfbc "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-new-hotness-in-phishing-device-code-attacks-in-m365 "Share on Facebook")
* [Share on X](https://twitter.com/share?text=The%20New%20Hotness%20in%20Phishing%3A%20Device%20Code%20Attacks%20in%20M365%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-new-hotness-in-phishing-device-code-attacks-in-m365 "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-new-hotness-in-phishing-device-code-attacks-in-m365&mini=true "Share on LinkedIn")

Device code phishing has a quality that makes it unusually effective: it does not follow the pattern of traditional phishing attacks. The victim ends up granting access to the attacker by completing a genuine sign-in on a Microsoft URL, `Microsoft[.]com/devicelogin`. The MFA prompts the user approves are legitimate. This method also frequently bypasses Conditional Access policies, because as far as the sign-in pipeline is concerned, the authentication originates from a legitimate Microsoft endpoint. From the user’s perspective, nothing is wrong. From the responder’s perspective, the only artifact left behind is an OAuth token issued to a session the attacker controls.

Across the business email compromise (BEC) and Microsoft 365 (M365) incident response engagements TrustedSec responds to, device code flow abuse continues to surface as an initial access technique that sidesteps both user suspicion and several of the Conditional Access patterns organizations rely on. This post unpacks how the attack works, what it looks like in the logs, and what actually stops it.

## **How the Device Code Flow is Supposed to Work**

Modern authentication is designed around the assumption that the device you are logging in to is also the device you are logging in from. You open a browser, navigate to a login page, enter your credentials, complete your MFA prompt, and access is granted. Simple.

However, what happens when the device you are trying to authenticate to does not have a browser? The OAuth 2.0 device authorization grant, defined in RFC 8628 and commonly known as the device code flow, exists for this reason. Some devices cannot reasonably host a browser-based login. Examples of such devices include smart TVs, command-line tools, IoT hardware, and printers that all need a way to authenticate a user without a keyboard or full web view. Microsoft implements the grant in Entra ID for exactly these scenarios, and it is used by tooling such as the Azure CLI, the ***kubectl*** Entra plugin, and various device enrollment flows.

The flow runs in six (6) steps:

1. The client (the “device”) asks Entra ID for a device code, naming the resource and scopes it wants.
2. Entra returns a `device_code`, a short human-readable `user_code`, a verification URL (`Microsoft[.]com/devicelogin`), and a time-to-live of approximately 15 minutes.
3. The client displays the `user_code` and the URL to the user.
4. The user opens the URL on a second device, enters the code, signs in, and consents.
5. The client polls the token endpoint, presenting the `device_code`.
6. Once the user finishes, Entra returns an `access_token` and a `refresh_token` to the polling client.

The flow assumes that whoever displays the code and whoever enters it are the same person, but nothing in the protocol binds the two together. If an attacker initiates the flow and persuades a victim to enter the att...