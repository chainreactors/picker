---
title: Russian snoops add OAuth abuse to targeted phishing campaigns
url: https://www.theregister.com/security/2026/08/21/russian-snoops-add-oauth-abuse-to-targeted-phishing-campaigns/5290706
source: www.theregister.com - Articles
date: 2026-08-21
fetch_date: 2026-08-22T02:52:48.471762
---

# Russian snoops add OAuth abuse to targeted phishing campaigns

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
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

Security

# Russian snoops add OAuth abuse to targeted phishing campaigns

Don't click on that State Department meeting invite

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
fri 21 Aug 2026 // 01:19 UTC

Google is tracking three distinct suspected Russian cyber-spy groups that are targeting individuals in academia, aerospace, defense, government agencies, and think tanks across Europe and the US.

The UNC (unclassified) groups, as Google calls them, have been orchestrating these highly targeted campaigns since at least last year, and they remain ongoing. Some of the phishing and OAuth-abuse operations used in the attack took place this month.

Each campaign had fewer than 100 targets, and under 10 victims, the threat-intel team told The Register.

REG AD

Despite the small numbers, if you work in government, NGOs, academia, or aerospace, you may be a target, and over the past few months the Russian snoops have adapted their attacks to abuse legitimate authentication flows. This makes these types of social engineering tactics appear more legitimate – and allows the cyber operatives to compromise personal accounts across multiple platforms, Google warns.

REG AD

It also means that potential victims may not recognize these as phishing attempts.

Google says it [wants to raise awareness](https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia) about these campaigns “so that targets can more readily recognize malicious outreach.”

In other words: don’t blindly trust that calendar invite that purports to come from the US State Department.

### UNC6293

The security analysts have been tracking one of the three, UNC6293, for almost two years. UNC6293 is a suspected APT29 ([aka Cozy Bear](https://www.theregister.com/security/2025/06/03/microsoft-et-al-pledge-clarity-on-cybercrew-names-hmph/379496), which [Google now tracks as Ice Relic](https://www.theregister.com/security/2026/07/27/google-goes-it-alone-with-a-new-cybercrime-crew-taxonomy/5278749) – insert eyeroll) phishing squad that poses as US State Department employees to lure victims into giving the snoops long-term access to their email correspondence.

[APT29](https://www.theregister.com/security/2025/08/29/aws-nails-russias-cozy-bear-trying-to-nick-microsoft-creds/766083) is probably best known for the [2020 SolarWinds hack](https://www.theregister.com/2021/04/15/solarwinds_hack_russia_apt29_positive_technologies_sanctions), and infosec analysts from the UK and US governments, and the private sector, often link it to Russia's Foreign Intelligence Service (SVR).

On Thursday, Google’s Threat Intelligence Group (GTIG) said it's now tracking two other suspected Russian groups, UNC7005 and UNC5976, which also conduct phishing, abuse OAuth flows, and/or deploy malware to these same types of targeted individuals.

Last summer, GTIG documented UNC6293 phishing for app passwords belonging to people who are critical of Russia. In this campaign, they impersonated State Department personnel, and they’ve continued using that lure while also adding OAuth phishing into their toolkit.

REG AD

“In June 2026, GTIG observed OAuth phishing where UNC6293 requested targets share either the full URL or ‘verification code’ after performing a legitimate login to an external provider,” Google threat analysts Gabby Roncone and Wesley Shields said in the Thursday report. “By providing the requested verification code the target would grant UNC6293 access to the account.”

### UNC7005

GTIG also asserts, with “moderate confidence,” that UNC7005 is another initial access group connected to APT29/Cozy Bear/Ice Relic – and the SVR. This crew, first identified in February, usually targets academia, diplomatic, and nonprofit personnel across Ukraine, Western Europe, and the US. While it shares similarities with UNC6293, Google tracks it separately “due to its lower sophistication and poor operational security, infrastructure with divergent characteristics, and incorporation of malware.”

Reliaquest and Microsoft first [sounded the alarm](https://www.theregister.com/security/2026/08/03/russias-svr-borks-public-wi-fis-for-digital-surveillance/5282399) on this group - Redmond track...