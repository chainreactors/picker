---
title: Grafana Labs admits all its codebase are belong to someone who popped its GitHub account
url: https://www.theregister.com/cyber-crime/2026/05/18/grafana-labs-admits-attackers-downloaded-its-codebase-from-github/5241686
source: www.theregister.com - Articles
date: 2026-05-18
fetch_date: 2026-05-19T06:05:17.771288
---

# Grafana Labs admits all its codebase are belong to someone who popped its GitHub account

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

Cyber-Crime

# Grafana Labs admits all its codebase are belong to someone who popped its GitHub account

No customer info stolen, no impact to operations, and no blackmail payment

Simon Sharwood
[Simon
Sharwood](https://www.theregister.com/author/simon-sharwood)
APAC Editor

Published
mon 18 May 2026 // 06:46 UTC

Observability outfit Grafana Labs has revealed that an attacker accessed its GitHub repository and stole its codebase.

In social media posts the company [blamed](https://www.linkedin.com/posts/we-recently-discovered-that-an-unauthorized-share-7461591117050855424-QQvO) the situation on an “unauthorized party” who was somehow able to obtain a token that offered access to its GitHub environment.

The company thinks it has identified the source of the credential leak, and therefore “invalidated the compromised credentials and implemented additional security measures to further secure our environment against unauthorized access.”

REG AD

But that didn’t stop the attacker from threatening to release the company’s code unless Grafana paid a ransom.

REG AD

Grafana says it won’t pay.

## MORE CONTEXT

* [### OpenTelemetry co-founder tools up for project graduation party](/software/2026/04/24/opentelemetry-co-founder-tools-up-to-push-project-to-10/5228112)
* [### Datadog digs down into GPU efficiency as AI costs soar](/software/2026/04/23/datadog-digs-down-into-gpu-efficiency-as-ai-costs-soar/5224634)
* [### Grafana offers AI assistant for free, warns users not to go mad](/software/2026/04/22/grafana-free-ai-for-all-please-dont-bankrupt-us/5220384)
* [### Yahoo! Japan’s owner consolidating 164 OpenStack clusters into one](/off-prem/2026/04/07/yahoo-japans-consolidating-164-openstack-clusters-into-one/5229172)

“Based on our operational experience and the published stance of the Federal Bureau of Investigation, which notes that ‘paying a ransom doesn't guarantee you or your organization will get any data back’ and only ‘offers an incentive for others to get involved in this type of illegal activity,’ we have determined the appropriate path forward is to not pay the ransom,” the company wrote.

It’s not clear if that stance is entirely principled, because plenty of Grafana’s products are already open source. The company’s posts suggest that the attacker accessed code that is not freely available.

The Register has sought clarification about just what the attacker accessed, because if they lifted code that’s mostly already open source there’s little reason for Grafana to pay a ransom!

Grafana’s decision not to pay may also be easier than it is for other victims of cybercrime because the company says it “determined that no customer data or personal information was accessed during this incident, and we have found no evidence of impact to customer systems or operations.”

The company therefore appears confident that whatever code the attackers downloaded won’t make a material different to its business, or harm customers.

The same couldn’t be said for educationware giant Canvas, which last week [paid extortionists](https://www.theregister.com/cyber-crime/2026/05/14/security-pros-doubt-canvas-attackers-really-deleted-stolen-student-data/5240799) after they claimed to have stolen data describing over 275 million students and faculty.

The Register will update this story if we receive additional information from Grafana Labs. ®

[ransomware](/tag/ransomware)
[grafana](/tag/grafana)
[cyber-crime](/tag/cyber-crime)
[security](/tag/security)
[observability](/tag/observability)

REG AD

[![](https://image.theregister.com/4094156.jpg?imageId=4094156&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

Networks

## Iran hints it could interfere with submarine cables in the Strait of Hormuz

Threatens unspecified ‘fees’ and warns of economic consequences – yet only major kinetic action could stop data flows entirely](https://www.theregister.com/networks/2026/05/19/iran-hints-it-could-interfere-with-submarine-cables-in-the-strait-of-hormuz/5242319)

[VIrtualization

## VMware quietly debuts Arm hypervisor tech preview

Supports Nvidia Grace and Ampere processors](https://www.theregister.com/virtualization/2026/05/19/vmware-quietly-debuts-arm-hypervisor-tech-preview/5242293)

[## ZTE showcases at GSMA M360 LATAM 2026, driving future business model restructuring - AI & network two-way integration

AI-integrated networks can cut costs, boost 5G efficiency, and help regional telcos shift beyond basic connectivity](https://www.theregister.com/networks/2026/05/15/zte-showcases-at-gsma-m360-latam-2026-driving-future-business-model-restructuring-ai-network-two-way-integration/5240254)

[Security

## Do fear the Reaper - stealer swipes macOS users...