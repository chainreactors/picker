---
title: Data theft extortion rises, while healthcare is still most-targeted vertical in Talos IR engagements
url: https://blog.talosintelligence.com/talos-ir-q2-2023-quarterly-recap/
source: Over Security - Cybersecurity news aggregator
date: 2023-07-27
fetch_date: 2025-10-04T11:56:25.705628
---

# Data theft extortion rises, while healthcare is still most-targeted vertical in Talos IR engagements

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

# Incident Response trends Q2 2023: Data theft extortion rises, while healthcare is still most-targeted vertical

By
[Nicole Hoffman](https://blog.talosintelligence.com/author/nicole/)

Wednesday, July 26, 2023 08:00

[Talos IR trends](https://blog.talosintelligence.com/category/ctir-trends/)
[Cisco Talos Incident Response](https://blog.talosintelligence.com/category/cisco-talos-incident-response/)

Cisco Talos Incident Response (Talos IR) responded to a growing number of data theft extortion incidents that did not involve encrypting files or deploying ransomware, a 25 percent increase since last quarter and the most-observed threat in the second quarter of 2023.

In this type of attack, threat actors steal victim data and threaten to leak or sell it unless the victim pays varying sums of money, eliminating the need to deploy ransomware or encrypt data. This differs from the double-extortion ransomware method, whereby adversaries exfiltrate and encrypt files and demand payment for victims to receive a decryption key.

[Cisco Talos Incident Response Quarterly Report (Q2 2023)

One-page overview of the top threats observed in the field last quarter.

071823 IR Q223 TAR.pdf

172 KB

download-circle](https://blog.talosintelligence.com/content/files/2023/07/071823-IR-Q223-TAR.pdf "Download")

Ransomware was the second most-observed threat this quarter, accounting for 17 percent of engagements, a slight increase from last quarter’s 10 percent. This quarter featured the LockBit and Royal ransomware families, which Talos IR has observed in previous quarters. Talos IR also observed several ransomware families for the first time, including 8Base and MoneyMessage.

Compromised credentials or valid accounts were the top observed means of gaining initial access this quarter, accounting for nearly 40 percent of total engagements. It was challenging to identify how the credentials were compromised considering they were obtained from devices outside the company’s visibility, such as saved credentials on an employee’s personal device.

![](https://blog.talosintelligence.com/content/images/2023/07/Q2-TopThreats-dark.jpg)

Continuing the trend from last [quarter](https://blog.talosintelligence.com/quarterly-report-incident-response-trends-in-q1-2023/), healthcare was the most targeted vertical this quarter, making up 22 percent of the total number of incident response engagements, closely followed by financial services.

![](https://blog.talosintelligence.com/content/images/2023/07/Q2-Targets-dark.jpg)

## Data theft extortion on the rise, featuring Clop, Karakurt and RansomHouse

Data theft extortion was the top observed threat this quarter, accounting for 30 percent of threats Talos IR responded to, a 25 percent increase in data theft extortion incidents compared to last quarter. The rise in data theft extortion incidents compared to previous quarters is consistent with public reporting on a growing number of ransomware groups stealing data and extorting victims without encrypting files and deploying ransomware.

Data theft extortion is not a new phenomenon, but the number of incidents this quarter suggests that financially motivated threat actors are increasingly seeing this as a viable means of receiving a final payout. Carrying out ransomware attacks is likely becoming more challenging due to global law enforcement and industry disruption efforts, as well as the implementation of defenses such as increased behavioral detection capabilities and endpoint detection and response (EDR) solutions.

This quarter featured activity from the RansomHouse and Karakurt extortion groups for the first time in Talos IR engagements. Active since 2021, [Karakurt](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-152a) typically gains access to environments via valid accounts, phishing, or exploiting vulnerabilities. In one observed Karakurt data theft extortion engagement, the attackers hijacked a remote desktop protocol (RDP) account, enumerated domain trusts using the network administration command-line tool nltest, executed PowerShell scripts to recover passwords, and modified domain policies.

RansomHouse has been active since late 2021 and is known for gaining access to corporate environments by exploiting vulnerabilities. In a RansomHouse engagement, the adversaries used non-interactive sessions to bypass multi-factor authentication (MFA), carried out a DCSync attack to collect credentials from a domain controller, and abused remote services such as secure shell (SSH) and RDP to move laterally. A DCSync attack occurs when attackers use various commands in Microsoft Directory Replication Service (DRS) Remote Protocol to masquerade as a domain controller to acquire user credentials from another domain controller. An attacker first needs to compromise a user account with domain replication privileges, which are typically domain admins.

Some ransomware groups, such as BianLian and Clop, are reportedly shifting away from using encryption, favoring data theft extortion in recent attacks, according to public reporting. Although Talos IR did not respond to any BianLian incidents this quarter, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) published a joint [advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a) on May 16 with the FBI and the Australian Cyber Security Centre (ACSC) confirming that as of January, the BianLian group stopped conducting ransomware operations in favor of performing exfiltration-based data theft extortion. BianLian group’s shift from deploying ransomware may also be due to the release of a free decrypter for BianLian ransomware in January 2023, possibly prompting them to pursue alternate methods. It is possible BianLian determined they could be successful without the use of data encrypti...