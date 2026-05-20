---
title: America's top cyber-defense agency left a GitHub repo open with with passwords, keys, tokens – and incredibly obvious filenames
url: https://www.theregister.com/security/2026/05/19/americas-top-cyber-defense-agency-left-a-github-repo-open-with-with-passwords-keys-tokens-and-incredibly-obvious-filenames/5242915
source: www.theregister.com - Articles
date: 2026-05-19
fetch_date: 2026-05-20T06:05:24.690636
---

# America's top cyber-defense agency left a GitHub repo open with with passwords, keys, tokens – and incredibly obvious filenames

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge + IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS + IaaS](/paas_iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI + ML](/ai_ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OSes](/oses)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Bootnotes](/bootnotes)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/tag/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [Datacenter](/tag/datacenter)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [IT Careers](/tag/tech%20jobs)
* [Columnists](/tag/columnists)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Security

# America's top cyber-defense agency left a GitHub repo open with with passwords, keys, tokens – and incredibly obvious filenames

I wonder what's in 'external-secret-repo-creds.yaml' and 'AWS-Workspace-Firefox-Passwords.csv'?

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
tue 19 May 2026 // 18:49 UTC

The US Cybersecurity and Infrastructure Security Agency (CISA) left open a GitHub repository named “Private-CISA” containing plain-text passwords, private keys, tokens, and secrets – with obvious file names like “external-secret-repo-creds.yaml” and “AWS-Workspace-Firefox-Passwords.csv” – for six months.

GitGuardian researcher Guillaume Valadon, fresh off a recent talk on Kubernetes secret leaks, found the public repository on May 14, and told The Register that he “quickly understood that the leak was bad and that time was running out. A national agency having 844 MB of production infrastructure material in a public GitHub repository for six months is as serious as a secrets leak gets.”

Valadon, who previously spent nine years at France’s CISA equivalent, ANSSI, told us the leak included tokens for CISA's internal JFrog Artifactory, Azure registry keys, AWS credentials, Kubernetes manifests, ArgoCD application files, Terraform infrastructure code, GitHub personal access tokens, and Entra ID SAML certificates.

REG AD

## MORE CONTEXT

* [### Trump wants to take a battle axe to CISA again and slash $707M from budget](/security/2026/04/03/trump-wants-to-slash-707m-from-cisas-budget/5226686)
* [### CISA flags data-theft bug in NSA-built OT networking tool](/security/2026/04/29/cisa-flags-data-theft-bug-in-nsa-built-ot-networking-tool/5225947)
* [### Nobody believes the 'criminals and scumbags' who hacked Canvas really deleted stolen student data](/cyber-crime/2026/05/14/security-pros-doubt-canvas-attackers-really-deleted-stolen-student-data/5240799)
* [### Murder, she wrote: Ex-FBI chief wants some ransomware crims charged with homicide](/security/2026/04/21/ex-fbi-lead-urges-homicide-charges-against-ransomware-scum/5225420)

GitGuardian reported the leaky repository to CISA on May 14, and the agency took it down a day later.

REG AD

A CISA spokesperson told The Register that it was aware of the report and is investigating. "Currently, there is no indication that any sensitive data was compromised as a result of this incident.”

It’s not a good look for the nation’s infosec agency, which [hasn’t had a permanent boss](https://www.theregister.com/on-prem/2025/05/28/ex-cisa-employee-describes-culture-of-fear-at-the-agency/495296) since Trump took office,  is facing [hundreds of millions of dollars in budgets cuts](https://www.theregister.com/security/2026/04/03/trump-wants-to-slash-707m-from-cisas-budget/5226686) on top of [deep cuts to staff and funding](https://www.theregister.com/on-prem/2025/10/14/trump-admin-slashes-cisa-staff-again-amid-shutdown/545651) last year, and has suffered its share of [embarrassing security snafus](https://www.theregister.com/security/2026/01/29/cisa-insider-threat-warning-comes-with-an-ironic-twist/4639815) in the interim.

In a Tuesday blog, Valadon [said](https://blog.gitguardian.com/how-we-got-a-cisa-github-leak-taken-down-in-26-hours/) he initially thought the repo “was a hoax, given how suspicious the directory names (Backup-April-2026/, All Backups/, LZ-Artifactory/, Kubernetes-Important-Yaml-Files/, ENTRA ID - SAML Certificates/ ...), file names (external-secret-repo-creds.yaml, CAWS GitHub Token.txt, Important AWS Tokens.txt, AWS-Workspace-Firefox-Passwords.csv, Kube-Config.txt ...), and their contents (private keys, personal and professional GitHub tokens, AWS secrets, ...) seemed too good to be true,” Valadon wrote.

It wasn’t a hoax  – “The Cybersecurity and Infrastructure Security Agency is aware of the reported exposure and is continuing to investigate the situation,”  but it was a “catalogue of unsafe practices,” he added, containing passwords stored in plain text, backups committed to Git, and an “explicit” how-to guide for disabling GitHub's secret scanning.

After initially reporting the leak through the CERT/CC portal, and only receiving an auto-acknowledgement as of the morning of May 15  – a Friday  – Valadon [alerted](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/) security journalist Brian Krebs about the publicly exposed secrets, which seemed to speed up CISA’s processes. By 6 pm EST that night, the feds took down the repository.

Valadon told The Reg he gives CISA credit for quickly deleting the repository. “Most of our responsible disclosures take much longer, and many are never fixed,” he said. “Managing to take the repository offline in a day is impressive work.”

He doesn’t know...