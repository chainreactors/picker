---
title: UK Cybercrime Journal: ACRO Breach Report
url: https://blog.bushidotoken.net/2026/08/uk-cybercrime-journal-acro-breach-report.html
source: Over Security
date: 2026-08-28
fetch_date: 2026-08-29T08:32:54.387766
---

# UK Cybercrime Journal: ACRO Breach Report

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### UK Cybercrime Journal: ACRO Breach Report

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[August 26, 2026](https://blog.bushidotoken.net/2026/08/uk-cybercrime-journal-acro-breach-report.html "permanent link")

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiy2q7B6PoRTxd5IvDfgsCa2Qdhjg8Bu1tKWpTZUuG7Bov4NdTC5ShSl4EPsqbcnXL3LDNYgMppM7mje9H2koeMvC7yxmeomLNFfPpi2KVAbzyNpHaF3fRrovK31Qpg_M0SlXAG8lTkBbzga3jDR0rlDov5lzXd2msehROZHj2Vns-YqLyj_oBDQWIoAAGq=w400-h400)](https://blogger.googleusercontent.com/img/a/AVvXsEiy2q7B6PoRTxd5IvDfgsCa2Qdhjg8Bu1tKWpTZUuG7Bov4NdTC5ShSl4EPsqbcnXL3LDNYgMppM7mje9H2koeMvC7yxmeomLNFfPpi2KVAbzyNpHaF3fRrovK31Qpg_M0SlXAG8lTkBbzga3jDR0rlDov5lzXd2msehROZHj2Vns-YqLyj_oBDQWIoAAGq)

**What Happened**

* On 7 August 2026, the UK Information Commissioner's Office (ICO) [disclosed](https://ico.org.uk/media2/njrjayzm/acro-reprimand-202608.pdf) that between July 2021 and June 2023, the ACRO Criminal Records Office suffered three separate compromises involving its customer portal website (acro.police.uk).
* ACRO is a national police unit providing public services such as issuing Police Certificates, International Child Protection Certificates, and processing Subject Access Requests.
* In March 2023, ACRO was notified about an SQL injection attack that reportedly exposed 15 sets of credentials, the majority of which belonged to its employees.
* A subsequent forensic investigation uncovered long-term threat actor activity within the website's environment, spanning from 9 July 2021 to 22 June 2023.
* The website was built on the Kentico CMS and was running version 12.0.0 between September 2019 and March 2023. This version had multiple known vulnerabilities at the time of the incident, but suffered from ambiguity around who was accountable for patching led to missed hotfixes and updates.
* Between 15 and 16 February 2023, an unknown threat actor staged personal data for exfiltration, which included Police Certificate Applications, Subject Access Request (SAR) forms, and International Child Protection Certificate forms.
* Due to insufficient log retention, ACRO could not definitively determine if the data was successfully exfiltrated. A maximum of 10,920 data subjects had their data staged, but ACRO ultimately notified 84,048 data subjects on a precautionary basis in April 2023.
* Notably, on 23 February 2023, the ICO learned that ACRO's Trend Micro antivirus software detected and quarantined four attempts to install the well-known credential harvesting tool Mimikatz. However, because ACRO operated without a documented patching policy and lacked a structured process for analyzing security alerts, these warnings were never reviewed or acted upon.

**Analyst Comment**

The Information Commissioner's Office (ICO) reprimand against the ACRO underscores the persistent issue within many organisations of a breakdown in basic IT governance and accountability. The fact that a threat actor was able to operate within the environment for nearly two years highlights systemic failures in both vulnerability management and security monitoring. Running an outdated content management system with known vulnerabilities for several years is a critical oversight. The ambiguity surrounding patching responsibilities created a dangerous blind spot that adversaries successfully exploited.

Further, the failure to act on critical security alerts is also a classic breakdown in the incident response chain. While the deployed Trend Micro antivirus successfully detected and quarantined a known threat, the alerts were ultimately ignored. Security tools are only as effective as the teams monitoring and responding to them. Without a structured review process, even the most sophisticated detection capabilities fall flat.

It is important to note, however, that while private sector organisations will receive a hefty fine for data protection offences, public sector organisations like ACRO receive a public reprimand from the ICO rather than receive a fine that confiscates public funds.

At the time of writing, the data has not yet appeared on any cybercrime forums or underground chat channels. The use of an open source tool like Mimikatz combined with SQL injection attacks indicates a likely opportunistic adversary rather than a stealthy cyber-espionage operation. However, both cybercriminal and nation state groups are known for opportunistic attacks. Current attribution for who or what was responsible this breach remains uncertain from an open source intelligence (OSINT) perspective.

On a positive note, the ICO highlighted that ACRO’s network segmentation effectively prevented the threat actor from pivoting from the compromised web environment into core policing systems. This containment significantly reduced the scale of harm and demonstrates the immense value of architectural defense-in-depth strategies. Following the breach, ACRO has migrated its portal to the Salesforce Experience Cloud for automated patching and hotfixes and implemented a Security Information and Event Management (SIEM) system to improve visibility.

**Defensive Takeaways**

* **Establish Clear Accountability for Patching:** Organisations must have a documented patching policy with clearly defined ownership, especially for public-facing web applications and Content Management Systems (CMS). Ambiguity in IT governance directly leads to unpatched vulnerabilities which then get exploited.
* **Implement Structured Alert Monitoring:** Deploying antivirus or Endpoint Detection and Response (EDR) solutions alone is insufficient if alerts are not actively monitored and investigated. It is recommended to establish either structured internal processes or an outsourced 24/7 Managed Detection and Response (MDR) or SOC service to review and respond to critical security alerts promptly.
* **Maintain Robust Network Segmentation:** Ensure that public-facing web infrastructure is strictly segmented from internal corporate networks and core operational systems. As demonstrated in this incident, strict segmentation is a crucial control for stopping an attacker's lateral movement.
* **Ensure Adequate Log Retention:** Insufficient logging severely hinders incident response and forensic investigations. Implement comprehensive logging policies and utilise a SIEM to aggregate logs, ensuring they are retained long enough to accurately determine the scope of data exfiltration during a compromise.

**Relevant Sources**

1. <https://ico.org.uk/media2/njrjayzm/acro-reprimand-202608.pdf>
2. <https://www.theregister.com/security/2026/08/12/exposed-woeful-security-at-uk-criminal-records-office-that-led-to-sensitive-data-leak/5286736>

[ACRO](https://blog.bushidotoken.net/search/label/ACRO)
[breachcybercrime](https://blog.bushidotoken.net/search/label/breachcybercrime)
[Mimikatz](https://blog.bushidotoken.net/search/label/Mimikatz)
[UK](https://blog.bushidotoken.net/search/label/UK)
[UK Cybercrime Journal](https://blog.bushidotoken.net/search/label/UK%20Cybercrime%20Journal)
[UK Police](https://blog.bushidotoken.net/search/label/UK%20Police)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Popular posts from this blog

### [Ransomware Tool Matrix Project Updates: May 2025](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html)

-
[May 05, 2025](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_BpTZksj9aZ67Y0MoiVTbyhuF2ZNK6mjoCeIlkF5MIjc7DlouoqPLYd-7XXsHgxT6Vytvvo-gY5b8JO3Ujab_8XLnSo1LbYrBUW78GrP2U8wx3ZT-B2ZwMGLO2aVCovVuIX3qZWYIN3X-GCw470E7tr2aiI0CPIgi9bkXbvDldhDL1hNZEc48rVTPyvxY/s320/OIG2.jpg)](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html)

Introduction This blog is a summary and analysis of recent addi...