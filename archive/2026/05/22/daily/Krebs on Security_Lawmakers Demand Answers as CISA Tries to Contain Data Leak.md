---
title: Lawmakers Demand Answers as CISA Tries to Contain Data Leak
url: https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/
source: Krebs on Security
date: 2026-05-22
fetch_date: 2026-05-23T05:43:02.843606
---

# Lawmakers Demand Answers as CISA Tries to Contain Data Leak

Advertisement

[![](/b-doppel/9.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=imitation)

Advertisement

[![](/b-doppel/14.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=deepfake)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Lawmakers Demand Answers as CISA Tries to Contain Data Leak

May 22, 2026

[12 Comments](https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/#comments)

Lawmakers in both houses of Congress are demanding answers from the **U.S. Cybersecurity & Infrastructure Security Agency** (CISA) after KrebsOnSecurity reported this week that a CISA contractor intentionally published AWS GovCloud keys and a vast trove of other agency secrets on a public **GitHub** account. The inquiry comes as CISA is still struggling to contain the breach and invalidate the leaked credentials.

![](https://krebsonsecurity.com/wp-content/uploads/2026/05/CISA-logo.png)

On May 18, KrebsOnSecurity reported that a CISA contractor with administrative access to the agency’s code development platform had [created a public GitHub profile](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/) called “**Private-CISA**” that included plaintext credentials to dozens of internal CISA systems. Experts who reviewed the exposed secrets said the commit logs for the code repository showed the CISA contractor disabled GitHub’s built-in protection against publishing sensitive credentials in public repos.

CISA acknowledged the leak but has not responded to questions about the duration of the data exposure. However, experts who reviewed the now-defunct Private-CISA archive said it was originally created in November 2025, and that it exhibits a pattern consistent with an individual operator using the repository as a working scratchpad or synchronization mechanism rather than a curated project repository.

In a written statement, CISA said “there is no indication that any sensitive data was compromised as a result of the incident.” But in a [May 19 a letter](https://www.hassan.senate.gov/imo/media/doc/letter_to_cisa_re_data_security.pdf) (PDF) to CISA’s Acting Director **Nick Andersen**, **Sen. Maggie Hassan** (D-NH) said the credential leak raises serious questions about how such a security lapse could occur at the very agency charged with helping to prevent cyber breaches.

“This reporting raises serious concerns regarding CISA’s internal policies and procedures at a time of significant cybersecurity threats against U.S. critical infrastructure,” Sen. Hassan wrote.

![](https://krebsonsecurity.com/wp-content/uploads/2026/05/HassanCISAletter.png)

Sen. Hassan noted that the incident occurred against the backdrop of major disruptions internally at CISA, which [lost more than a third of it workforce](https://www.cybersecuritydive.com/news/cisa-cybersecurity-division-reorganization/812155/) and almost all of its senior leaders after the Trump administration forced a series of early retirements, buyouts, and resignations across the agency’s various divisions.

**Rep. Bennie Thompson** (D-MS), the ranking member on the House Homeland Security Committee, echoed the senator’s concerns.

“We are concerned that this incident reflects a diminished security culture and/or an inability for CISA to adequately manage its contract support,” Thompson wrote in [a May 19 letter](https://federalnewsnetwork.com/wp-content/uploads/2026/05/2026.05.19-T_Andrersen_F_BGT_DR_CISA-AWS-Credentials-Final.pdf) to the acting CISA chief that was co-signed by **Rep. Delia Ramirez** (D-Ill), the ranking member of the panel’s Subcommittee on Cybersecurity and Infrastructure Protection. “It’s no secret that our adversaries — like China, Russia, and Iran — seek to gain access to and persistence on federal networks. The files contained in the ‘Private-CISA’ repository provided the information, access, and roadmap to do just that.”

KrebsOnSecurity has learned that more a week after CISA was first notified of the data leak by the security firm **GitGuardian**, the agency is still working to invalidate and replace many of the exposed keys and secrets.

On May 20, KrebsOnSecurity heard from **Dylan Ayrey**, the creator of **TruffleHog**, an open-source tool for discovering private keys and other secrets buried in code hosted at GitHub and other public platforms. Ayrey said CISA still hadn’t invalidated an RSA private key exposed in the Private-CISA repo that granted access to a GitHub app which is owned by the CISA enterprise account and installed on the CISA-IT GitHub organization with full access to all code repositories.

“An attacker with this key can read source code from every repository in the CISA-IT organization, including private repos, register rogue self-hosted runners to hijack CI/CD pipelines and access repository secrets, and modify repository admin settings including branch protection rules, webhooks, and deploy keys,” Ayrey told KrebsOnSecurity. CI/CD stands for Continuous Integration and Continuous Delivery, and it refers to a set of practices used to automate the building, testing and deployment of software.

KrebsOnSecurity notified CISA about [Ayrey’s findings](https://trufflesecurity.com/blog/cisa-leaked-admin-github-token-remained-live-2-days) on May 20. Ayrey said CISA appears to have invalidated the exposed RSA private key sometime after that notification. But he noted that CISA still hasn’t rotated leaked credentials tied to other critical security technologies that are deployed across the agency’s technology portfolio (KrebsOnSecurity is not naming those technologies publicly for the time being).

CISA responded with a brief written statement in response to questions about Ayrey’s findings, saying “CISA is actively responding and coordinating with the appropriate parties and vendors to ensure any identified leaked credentials are rotated and rendered invalid and will continue to take appropriate steps to protect the security of our systems.”

Ayrey said his company Truffle Security monitors GitHub and a number of other code platforms for exposed keys, and attempts to alert affected accounts to the sensitive data exposure(s). They can do this easily on GitHub because the platform publishes a live feed which includes a record of all commits and changes to public code repositories. But he said cybercriminal actors also monitor these public feeds, and are often quick to pounce on API or SSH keys that get inadvertently published in code commits.

![The Private CISA GitHub repo exposed dozens of plaintext credentials to important CISA GovCloud resources. The filenames include AWS-Workspace-Bookmarks-April-6-2026.html, AWS-Workspace-Firefox-Passwords.csv, Important AWS Tokens.txt, kube-config.txt, etc.](https://krebsonsecurity.com/wp-content/uploads/2026/05/privatecisa-filelist.png)

In practical terms, it is likely that cybercrime groups or foreign adversaries also noticed the publication of these CISA secrets, the most egregious of which appears to have happened in late April 2026, Ayrey said.

“We monitor that firehose of data for keys, and we have tools to try to figure out whose they are,” he said. “We have evidence attackers monitor that firehose as well. Anyone monitoring GitHub events could be sitting on this information.”

**James Wilson**, the enterprise technology editor for the *Risky Business* security podcast, said organizations using GitHub to manage code projects can set top-down policies that prevent employees from disabling GitHub’s protections against publishing ...