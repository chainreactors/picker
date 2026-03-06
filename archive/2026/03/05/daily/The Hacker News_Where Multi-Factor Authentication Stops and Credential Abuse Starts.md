---
title: Where Multi-Factor Authentication Stops and Credential Abuse Starts
url: https://thehackernews.com/2026/03/where-multi-factor-authentication-stops.html
source: The Hacker News
date: 2026-03-05
fetch_date: 2026-03-06T04:04:48.339872
---

# Where Multi-Factor Authentication Stops and Credential Abuse Starts

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

# [Where Multi-Factor Authentication Stops and Credential Abuse Starts](https://thehackernews.com/2026/03/where-multi-factor-authentication-stops.html)

**The Hacker News**Mar 05, 2026Windows Security / Active Directory

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh573fCRL7EMT-Piz1QEJizjMNdQH5G4eMHpLbuCGvm-PNF6-osRuSQF09DHGIuYS1EXDgZXUmWzVf1p3kHDH0_jE7_XDKuG0J7R9Yc3kP4XbaW3UoF3gLYCQ6ba63S0iYQf3Ftf7s0UkDD9QBbnzUcBPRDQXI401TzAVjET05OjgS38tiYgfWA79kS-8g/s1700-e365/outpost.jpg)

Organizations typically roll out multi-factor authentication (MFA) and assume stolen passwords are no longer enough to access systems. In Windows environments, that assumption is often wrong. Attackers still compromise networks every day using valid credentials. The issue is not MFA itself, but coverage.

Enforced through an identity provider (IdP) such as Microsoft Entra ID, Okta, or Google Workspace, [MFA works well](https://specopssoft.com/blog/mfa-alone-not-enough-protect-passwords-and-logon/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article) for cloud apps and federated sign-ins. But many Windows logons rely solely on Active Directory (AD) authentication paths that never trigger MFA prompts. To reduce credential-based compromise, security teams need to understand where Windows authentication happens outside their identity stack.

## Seven Windows authentication paths that attackers rely on

### **1. Interactive Windows logon (local or domain joined)**

When a user signs in directly to a Windows workstation or server, authentication is typically handled by AD (via Kerberos or NTLM), not by a cloud IdP.

In [hybrid environments](https://specopssoft.com/blog/cloud-password-security-best-practices/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article), even if Entra ID enforces MFA for cloud apps, traditional Windows logons to domain-joined systems are validated by on-prem domain controllers. Unless Windows Hello for Business, smart cards, or another integrated MFA mechanism is implemented, there’s no additional factor in that flow.

If an attacker obtains a user’s password (or NTLM hash), they can authenticate to a domain-joined machine without triggering the MFA policies that protect software-as-a-service apps or federated single sign-on. From the domain controller’s perspective, this is a standard authentication request.

Tools like [Specops Secure Access](https://specopssoft.com/product/specops-secure-access/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article) are key to limiting the risk of credential abuse in these scenarios. By enforcing MFA for Windows logon, as well as for VPN and Remote Desktop Protocol (RDP) connections, this tool makes it harder for attackers to gain unauthorized access to your network. This even extends to offline logins, which are secured with one-time passcode authentication.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGX7k2ju2aZMEUd3HsI9SRDuPBy33RAcESzXSfj0w6SFovh1d4ExVdFdXlgxoof9Vo4RfieLhBIbHWeMwS7s5X_bopbTcP18G8ei4Zla5KZkcoEnEq7h23w95b4gneae8OEfLGLgsr2xv1rBYIVCcKqW7HXRJg91xEIpVMIZLIZr7RG2i5oNZWo633zos/s1700-e365/MFA-SSA.gif) |
| Specops Secure Access |

### **2. Direct RDP access that bypasses conditional access**

RDP is one of the most targeted access methods in Windows environments. Even when RDP is not exposed to the internet, attackers often reach it through [lateral movement](https://specopssoft.com/blog/corporate-account-takeover-attacks-and-prevention/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article) after initial compromise. A direct RDP session to a server doesn’t automatically pass through cloud-based MFA controls, which means the logon may rely solely on the underlying AD credential.

### **3. NTLM authentication**

NTLM is a legacy authentication protocol that, [despite being deprecated](https://specopssoft.com/blog/microsoft-phases-out-ntlm-with-kerberos/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article) in favor of the more secure Kerberos protocol, still exists for compatibility reasons. It is also a common attack vector because it supports techniques like pass-the-hash.

In pass-the-hash attacks, the attacker does not need the plaintext password; instead, they use the NTLM hash to authenticate. [MFA](https://specopssoft.com/blog/mfa-phishing-fatigue-resistant/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article) does not help if the system accepts the hash as proof of identity.

NTLM can also appear in internal authentication flows that organizations may not actively monitor; only an incident or an audit will surface it to security teams.

### **4. Kerberos ticket abuse**

Kerberos is the primary authentication protocol for AD. Instead of stealing passwords directly, [attackers steal Kerberos tickets](https://specopssoft.com/blog/kerberoasting-attacks-in-active-directory/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article) from memory or generate forged tickets after compromising privileged accounts. This enables techniques such as:

* Pass-the-ticket
* Golden Ticket
* Silver Ticket

These attacks allow long-term access and lateral movement and also reduce the need for repeated logons, which lowers the chance of detection. These attacks can persist even after password resets if the underlying compromise is not fully addressed.

### **5. Local administrator accounts and credential reuse**

Organizations still rely on local administrator accounts for support tasks and system recovery. If local admin passwords are reused across endpoints, [attackers can escalate](https://specopssoft...