---
title: When the attacker becomes the user: Rethinking account takeover
url: https://www.theregister.com/security/2026/10/22/sponsored-when-the-attacker-becomes-the-user-rethinking-account-takeover/5303913
source: www.theregister.com - Articles
date: 2026-10-22
fetch_date: 2026-10-23T06:46:57.379080
---

# When the attacker becomes the user: Rethinking account takeover

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
  + [Edge and IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS and IaaS](/tag/paas-iaas)
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
  + [AI and ML](/tag/ai%20and%20ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OS Platforms](/tag/os%20platforms)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [Nvidia GTC Berlin 2026](/special_features/nvidia_gtc_berlin_2026)
  + [Cybersecurity Month 2026](/special_features/cybersecurity_month_2026)
  + [VMware Explore 2026](/special_features/vmware_explore_2026)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [RSA Conference](/special_features/rsa)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Modernizing Financial Services with FIS and AWS](https://vendorvoice.theregister.com/aws_fis_capital_markets/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
  + [Digicert](https://vendorvoice.theregister.com/digicert)
  + [Netscout](https://vendorvoice.theregister.com/netscout)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [Software](/software)
* [Microsoft](/tag/microsoft)
* [Developer](/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [GTC Berlin](/special_features/nvidia_gtc_berlin_2026)

security

# When the attacker becomes the user: Rethinking account takeover

SPONSORED FEATURE: AI makes phishing easier than ever

Guy Matthews
[Guy
Matthews](https://www.theregister.com/author/guy-matthews)

Published
thu 22 Oct 2026 // 16:00 UTC

[Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)

In a world full of cyber risk, account takeover has emerged as one of the most insidious of all threats. If an attacker can successfully compromise a legitimate email account, they are then able to pose as a trusted individual or organization without triggering any warnings. Traditional email security will see nothing wrong. From there the threat actor can pick their moment to cause havoc with objectives that range from stealing money, expropriating sensitive data and propagating catastrophic malware. Serious financial loss and a damaged corporate reputation are commonplace outcomes.

The typical account takeover lifecycle starts with the bad guys obtaining credentials, usually through the medium of phishing. Generative AI (GenAI) has made it easy for an attacker to trick an unwary individual into giving away login data, perhaps by posing as a colleague or other trusted party or by encouraging them to enter confidential information on a fake login page.

You might expect, once a legitimate identity has been successfully compromised, that all hell would immediately break loose. These days the typical account takeover artist is more stealthy and sinister than that, in no rush to act at this early stage since no alarm bells have been triggered. Most will take their time to test out and verify their stolen login data, and see where it might take them.

“Conventionally attackers would take over an account and immediately start firing off spam and phishing,” says Dave Baggett, SVP Cybersecurity with software developer Kaseya. “Now they are starting to get clever. They’ll get access to an account and sit tight, watching all the email traffic passing and waiting for an opportune moment to inject themselves into the conversation.”

### **From the inside out**

Once they’ve figured out an organisation’s weak points and come up with a plan of attack, the bad guys will start to weaponize the compromised email account to target other employees and internal systems. Assuming their motivation is financial, they might be on the hunt for a way into payroll or invoicing databases. But their ultimate aim might lie further afield in the form of the organisation’s customers and suppliers, and that’s when the real nightmare can start. So called outbound phishing offers the criminal a way to assert control over a whole new range of sensitive end points.

Victims of outbound phishing are highly vulnerable in the face of what seem to be messages from a trusted partner and ally. It is one thing for an organisation to protect its own email accounts with robust controls like multifactor authentication (MFA), but no one has control over the authentication practices of other parties: “Let’s say we have a customer who we’re protecting,” explains Baggett. “They’re safe, but imagine that they start getting suspicious emails from a third party. Our customer has no idea what is or isn’t protecting that third party. Emails coming from that source might appear to be from a real account, but it could be a hacker typing them.”

Given that you can’t run checks on third party organisations, something more sophisticated than regular email security is required. Ideally this would be a GenAI-powered solution that can bring language understanding to bear, able to examine conversation histories in depth to see if something anomalous can be spotted.

It makes life even harder for defenders when the bad actor has successfully assumed the identity of somebody senior. If they are impersonating a top-tier manager with an extensive and trusted reputation then they have a powerful asset on their hands. All the trust and goodwill of that senior individual is now inherited by the criminal.

Conventional email fi...