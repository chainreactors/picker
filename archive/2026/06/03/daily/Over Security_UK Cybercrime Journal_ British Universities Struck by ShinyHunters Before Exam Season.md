---
title: UK Cybercrime Journal: British Universities Struck by ShinyHunters Before Exam Season
url: https://blog.bushidotoken.net/2026/05/uk-cybercrime-journal-british.html
source: Over Security
date: 2026-06-03
fetch_date: 2026-06-04T06:32:00.860113
---

# UK Cybercrime Journal: British Universities Struck by ShinyHunters Before Exam Season

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### UK Cybercrime Journal: British Universities Struck by ShinyHunters Before Exam Season

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[June 03, 2026](https://blog.bushidotoken.net/2026/05/uk-cybercrime-journal-british.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlSq7QAKiZ_udFZ4N4PltYnNvxvHGZ9DH-WnTHSOewFrT1jbYgoD947PFM3M7qipR7q15XVZ11E4-AqCH5KVfTwV65bUXelDzODbwLMPxFh4e_GviuOa7Pkj6h7oYp2L17SC3BhgTp1jrtlU7gjSebXCcZ2JKstimfUCJoJ5LCDDSZXdt4NVmTep0kdmXm/w400-h278/IMG_4929.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlSq7QAKiZ_udFZ4N4PltYnNvxvHGZ9DH-WnTHSOewFrT1jbYgoD947PFM3M7qipR7q15XVZ11E4-AqCH5KVfTwV65bUXelDzODbwLMPxFh4e_GviuOa7Pkj6h7oYp2L17SC3BhgTp1jrtlU7gjSebXCcZ2JKstimfUCJoJ5LCDDSZXdt4NVmTep0kdmXm/s816/IMG_4929.jpeg)

What Happened:

* On 3 May 2026, ShinyHunters, the English-speaking adolescent cybercrime collective, claimed they breached Instructure by listing them on their Tor data leak site.
* Instructure is a US-based software provider behind the widely adopted Canvas Learning Management System (LMS).
* ShinyHunters reportedly exfiltrated 3.65 terabytes of data, spanning 275 million global records from up to 9,000 institutions, before posting extortion messages across university login portals demanding Bitcoin.
* The outage forced prominent UK higher education institutions, including the University of Liverpool, Queen’s University Belfast, and the University of Manchester, to take systems offline and hastily rewrite their end-of-year exam submission schedules.
* Instructure confirmed the affected data includes names, student ID numbers, email addresses, and private student-instructor messages. Instructure also confirmed no passwords, financial data, or government IDs were pilfered.
* When the initial negotiation deadline passed, ShinyHunters then escalated by defacing Canvas login portals at roughly 330 institutions and pivoting to direct school-by-school extortion.
* Following the initial investigation into the breach, Instructure confirmed that ShinyHunters had exploited a vulnerability in its “Free-for-Teacher” account creation system.
* To prevent the data from being leaked, Instructure announced it had “reached an agreement with the unauthorised actor” behind the data extortion attack.
* According to an expert interviewed by ABC News, while a ransom amount hadn't yet been verified or publicly confirmed, people claiming to have knowledge of the situation estimated the amount was $10 million USD.

Analyst Comment:

Canvas is reportedly the UK’s primary digital learning platform, whose usage grew significantly during the pandemic. The timing of the attack also couldn’t come at a worse time for UK universities. In May, thousands of undergraduate students will be uploading their dissertations and trying to access their course content to prepare for their exams.

Active since 2019, ShinyHunters is a financially motivated data-theft-extortion collective that first emerged publicly in January 2020. Notably, ShinyHunters does not currently deploy ransomware as part of their intrusions. Instead, they exfiltrate data from cloud platforms, software environments, and third-party integrators, then demand a ransom to avoid its public release. SaaS Platforms such as Salesforce, Snowflake, GainSight, SalesLoft Drift and their customers have been targeted by ShinyHunters and adjacent groups in the last couple years.

Instructure is one of the few victims who have likely paid ShinyHunters. Most victims refuse due to not being able to trust that the cybercriminals will stick to their word and delete the stolen data. The consensus across the industry is paying the ransom is never the appropriate option for multiple reasons, such as fuelling future attacks, making your company look like an easy target, and possibly violating sanctions and local ransom payment ban laws. The most likely scenario is that Instructure felt they should pay the ransom to prevent further harm from the release of personal information of millions of students in their system.

**Defensive Takeaways:**

* Enhance Platform Security: ShinyHunters reportedly exploited a vulnerability in Instructure’s Free-for-Teacher system, which highlights the importance of identity security audits alongside standard application penetration testing.
* Enhance Logging and Round-the-Clock Monitoring: ShinyHunters reportedly exfiltrated 3.65 terabytes of data from Instructure. Enhanced activity logs and a certified 24/7 SOC monitoring service could have detected these actions by identifying anomalous login events and data exfiltration events to unknown IP addresses.
* Create and Test Backup Processes: While Canvas was down, the universities shifted to alternative methods like email and printed paper. This case highlights the importance of business continuity plans (BCPs) along with making sure they are updated and tested.
* Be Wary of Second-Order Effects: After a breach of this size, its key to warn users and SOC teams to be vigilant for new waves of phishing emails, brute forcing attacks, and other account takeover methods leveraging the stolen data.
* Never Trust a Cybercriminal: In Instructure’s case, the company says it received “digital confirmation of data destruction (shred logs).” However, as Allison Nixon says, it’s completely unprovable because such shred logs or videos can be easily faked.

Relevant Sources:

1. <https://www.instructure.com/incident_update>
2. <https://www.bbc.com/news/articles/ce3pq0136eqo>
3. <https://www.academicjobs.com/uk/higher-education-news/canvas-cyber-attack-hits-uk-universities-or-academicjobs-uk-18738>
4. <https://www.theguardian.com/technology/2026/may/17/canvas-hack-cyber-criminals-data-ransom-paid>
5. <https://www.abc.net.au/news/2026-05-14/instructure-dealing-with-canvas-cyberhackers-dangerous-tactic/106674686>

Relevant CTI Resources:

1. <https://www.ransomware.live/id/SW5zdHJ1Y3R1cmUgSG9sZGluZ3MsIEluYy4gKENhbnZhIExNUywgaW5zdHJ1Y3R1cmUuY29tKUBzaGlueWh1bnRlcnM>
2. <https://www.ransomware.live/group/shinyhunters>
3. <https://www.halcyon.ai/ransomware-alerts/education-sector-in-the-crosshairs-shinyhunters-extortion-campaign-against-instructure>
4. <https://www.halcyon.ai/threat-group/shinyhunters>
5. <https://blog.unit221b.com/dont-read-this-blog/harassment-scare-tactics-why-victims-should-never-pay-shinyhunters>
6. <https://www.sans.org/blog/hunting-saas-threats-insights-for589-course-cybercriminal-campaigns>

[Canvas](https://blog.bushidotoken.net/search/label/Canvas)
[Cybercrime](https://blog.bushidotoken.net/search/label/Cybercrime)
[Instructure](https://blog.bushidotoken.net/search/label/Instructure)
[ShinyHunters](https://blog.bushidotoken.net/search/label/ShinyHunters)
[TheCom](https://blog.bushidotoken.net/search/label/TheCom)
[UK](https://blog.bushidotoken.net/search/label/UK)
[UK Cybercrime Journal](https://blog.bushidotoken.net/search/label/UK%20Cybercrime%20Journal)
[university](https://blog.bushidotoken.net/search/label/university)

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

Introduction This blog is a summary and analysis of recent additions to the Ransomware Tool Matrix (RTM) as well as the Ransomw...