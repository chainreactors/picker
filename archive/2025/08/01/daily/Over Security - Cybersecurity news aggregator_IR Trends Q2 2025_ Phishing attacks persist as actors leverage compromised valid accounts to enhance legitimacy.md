---
title: IR Trends Q2 2025: Phishing attacks persist as actors leverage compromised valid accounts to enhance legitimacy
url: https://blog.talosintelligence.com/ir-trends-q2-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-01
fetch_date: 2025-10-07T00:49:17.878728
---

# IR Trends Q2 2025: Phishing attacks persist as actors leverage compromised valid accounts to enhance legitimacy

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

# IR Trends Q2 2025: Phishing attacks persist as actors leverage compromised valid accounts to enhance legitimacy

By
[Lexi DiScola](https://blog.talosintelligence.com/author/lexi/)

Thursday, July 31, 2025 06:00

[Talos IR trends](https://blog.talosintelligence.com/category/ctir-trends/)

Phishing remained the top method of initial access this quarter, appearing in a third of all engagements – a decrease from 50 percent last quarter. Threat actors largely leveraged compromised internal or trusted business partner email accounts to deploy malicious emails, bypassing security controls and gaining targets’ trust. Interestingly, the objective of the majority of observed phishing attacks appeared to be credential harvesting, suggesting cybercriminals may consider brokering compromised credentials as simpler and more reliably profitable than other post-exploitation activities, such as engineering a financial payout or stealing proprietary data.

Ransomware and pre-ransomware incidents made up half of all engagements this quarter, similar to last quarter. Cisco Talos Incident Response (Talos IR) responded to Qilin ransomware for the first time, identifying previously unreported tools and tactics, techniques, and procedures (TTPs), including a new data exfiltration method. Our observations of Qilin activity indicate a potential expansion of the group and/or an increase in operational tempo in the foreseeable future, warranting this as a threat to monitor. Additionally, ransomware actors leveraged a dated version of PowerShell, PowerShell 1.0, in a third of ransomware and pre-ransomware engagements this quarter, likely to evade detection and gain more flexibility for their offensive capabilities.

This video discusses the biggest trends from the Q2 2025 Talos IR report

## Actors leverage compromised email accounts for phishing attacks aimed at credential harvesting

As mentioned above, threat actors used phishing for initial access in a third of engagements this quarter, a decrease from 50 percent last quarter when it was also the top observed initial access technique. However, last quarter featured a dominant voice phishing (vishing) campaign deploying Cactus and Black Basta ransomware that was significantly less present this quarter, potentially contributing to this decline.

Threat actors largely leveraged compromised internal or trusted business partner email accounts to send malicious emails, which appeared in 75 percent of engagements where phishing was used for initial access. Using a legitimate trusted account affords an attacker numerous advantages, such as potentially bypassing an organization’s security controls as well as appearing more trustworthy to the recipient. For example, in one phishing engagement, the targeted organization’s users were victims of a phishing campaign sent from the compromised email address of a legitimate business partner. The phishing emails leveraged malicious links directing victims to a fake Microsoft O365 login page that prompted visitors to authenticate with MFA, likely so the attacker could steal users’ credentials and session tokens.

We assess that credential harvesting was the end goal in the majority of phishing attacks this quarter, such as in the example highlighted above. Though the tactic of leveraging compromised valid email accounts is often associated with business email compromise (BEC) attacks, this observation suggests cybercriminals may consider brokering compromised credentials to be more reliably profitable than attempting to manipulate a target into making a financial payout. Further, not including a financial request in the email body likely makes an email less suspicious to a victim, potentially raising the chances of a successful attack. In one engagement, an attacker successfully compromised a user’s email account after the user clicked a link within a phishing email and provided their credentials to the phishing site. The adversary proceeded to send multiple internal spear phishing emails as the compromised user with a link to an internal SharePoint link, which then directed to a credential harvesting page that successfully tricked approximately a dozen additional users into entering their credentials.

## Ransomware trends

Ransomware and pre-ransomware incidents made up half of all engagements this quarter, similar to [last quarter](https://blog.talosintelligence.com/ir-trends-q1-2025/). Talos IR observed Qilin and Medusa ransomware for the first time, while also responding to previously seen Chaos ransomware.

### Qilin ransomware activity showcases previously unreported TTPs and suggests increased operational tempo

We responded to a Qilin ransomware incident for the first time this quarter, identifying tools and TTPs that have not been previously publicly reported. Specifically, we observed the operators leveraging a suspected custom compiled encryptor with hardcoded victim user credentials, Backblaze-hosted command and control (C2) infrastructure, and file transfer tool CyberDuck, an exfiltration method not previously associated with this threat actor or its affiliates. The threat actors likely leveraged stolen valid credentials to gain initial access, then used a combination of commercial remote monitoring and management (RMM) solutions to facilitate lateral movement and data staging, including TeamViewer, VNC, AnyDesk, Chrome Remote Desktop, Distant Desktop, QuickAssist, and ToDesk. To ensure persistent access until encryption was completed, the actors created an AutoRun entry in the Software registry Hive on each infected system to trigger the ransomware execution each time the system was rebooted and a scheduled task to silently relaunch Qilin at every new logon. These attack techniques ultimately led to a widespread infection requiring a complete rebuild of the Acti...