---
title: IR Trends Q1 2025: Phishing soars as identity-based attacks persist
url: https://blog.talosintelligence.com/ir-trends-q1-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-29
fetch_date: 2025-10-06T22:08:35.914005
---

# IR Trends Q1 2025: Phishing soars as identity-based attacks persist

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# IR Trends Q1 2025: Phishing soars as identity-based attacks persist

By
[Lexi DiScola](https://blog.talosintelligence.com/author/lexi/)

Monday, April 28, 2025 06:00

[Talos IR trends](https://blog.talosintelligence.com/category/ctir-trends/)
[Cisco Talos Incident Response](https://blog.talosintelligence.com/category/cisco-talos-incident-response/)

Phishing attacks spiked this quarter as threat actors leveraged this method of initial access in half of all engagements, a vast increase from previous quarters. Conversely, the use of valid accounts for initial access was rarely seen this quarter, despite being the top observed method in 2024, according to our [Year in Review report](https://blog.talosintelligence.com/2024yearinreview/). Nevertheless, valid accounts played a prominent role in the attack chains Cisco Talos Incident Response (Talos IR) observed as actors predominately used phishing to gain access to a user account, then leveraged this access to establish persistence in targeted networks.

Ransomware and pre-ransomware incidents made up a slightly larger portion of threats observed this quarter, with most incidents falling into the latter category. Talos IR’s investigations into pre-ransomware events provided unique insight into defensive measures that successfully stopped these attacks before a ransomware executable could be deployed, including early engagement with the incident response team and robust monitoring of certain threat actor tactics, techniques and procedures (TTPs).

Watch a discussion on the biggest trends on this latest report

## Actors leverage access to valid accounts via phishing to establish persistence

Threat actors used phishing to achieve initial access in 50 percent of engagements, a notable increase from less than 10 percent last quarter. Vishing was the most common type of phishing attack seen, accounting for over 60 percent of all phishing engagements, though we also observed malicious attachment, malicious link and business email compromise (BEC) attacks.

Adversaries predominately leveraged phishing to gain access to a valid account, pivot deeper into the targeted network, and expand their foothold, contrasting other phishing objectives we have seen in the past such as eliciting sensitive information or monetary transfers. For example, in an observed vishing campaign — described in further detail in the ransomware section below — adversaries deceived users over the phone into establishing remote access sessions to the user’s workstation, then used this access to load tooling, establish persistence mechanisms and disable endpoint protections.

In some engagements, actors leveraged phishing attacks to steal users’ legitimate access tokens, enabling them to maintain persistent access to the targeted networks. In one engagement, adversaries deployed a phishing email with a malicious link to successfully steal a user’s multi-factor authentication (MFA) session token along with their credentials. From there, the actors gained unauthorized access to the target’s Microsoft Office 365 environment and deployed enterprise applications with the likely goal of gaining further access into additional accounts. In another phishing engagement, upon gaining access to a user’s valid account, the actors cloned their active access token and specified new credentials for outbound connections. They then sought to expand their access by running commands to gather system information and creating a scheduled task to execute a malicious JavaScript file upon user login.

## Ransomware trends

### Vishing campaign leveraging BlackBasta and Cactus TTPs hits manufacturing and construction organizations

Ransomware and pre-ransomware incidents made up over 50 percent of engagements this quarter, an increase from nearly 30 last quarter. A robust campaign leveraging BlackBasta and Cactus TTPs that targeted manufacturing and construction organizations accounted for over 60 percent of pre-ransomware and ransomware engagements and was consistent with public reporting on likely related incidents.

The attack chain we observed begins with the threat actors flooding users’ mailboxes at targeted organizations with a large volume of benign spam emails. After a few days, the actors call the victim, usually via Microsoft Teams, and direct them to initiate a Microsoft Quick Assist remote access session, helping them with installation of the program if not already present on the user’s system. Once a Quick Assist session is established, the adversary loads tooling to collect information about the target system and establish persistence. The actors create the TitanPlus registry key and embed IP addresses to enable command and control (C2) communication, using character substitution to obfuscate the infrastructure. After completing the TitanPlus registry key persistence process, the adversary then performs subsequent privilege escalation and lateral movement, seemingly with the ultimate goal of deploying ransomware. We initially observed the threat actors leveraging BlackBasta ransomware and pivoting to Cactus ransomware after public reporting on their use of the former was released. Our analysis of engagements involving Cactus led us to identify a previously undocumented variant of the ransomware, which builds upon previous functionality with new command-line arguments that provide the threat actors with greater control over the binary's function, likely to prioritize efficiency and maximum impact.

![](https://blog.talosintelligence.com/content/images/2025/04/2025Q1_Q1BlackBasta-1.jpg)

**Looking forward:** The threat actors responsible for this campaign have proven to be agile, modifying their TTPs as more public reporting on this campaign emerges, which leads us to assess they will continue to adjust their TTPs and/or incorporate a dif...