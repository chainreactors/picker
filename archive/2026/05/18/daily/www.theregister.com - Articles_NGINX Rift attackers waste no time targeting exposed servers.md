---
title: NGINX Rift attackers waste no time targeting exposed servers
url: https://www.theregister.com/security/2026/05/18/nginx-rift-attackers-waste-no-time-targeting-exposed-servers/5241851
source: www.theregister.com - Articles
date: 2026-05-18
fetch_date: 2026-05-19T06:05:16.454409
---

# NGINX Rift attackers waste no time targeting exposed servers

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

# NGINX Rift attackers waste no time targeting exposed servers

Researchers say 18-year-old flaw already being probed and exploited just days after disclosure

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
mon 18 May 2026 // 14:02 UTC

Exploit attempts are already hammering a newly disclosed NGINX bug dubbed "NGINX Rift," proving once again that attackers read patch notes faster than most admins.

Researchers at [VulnCheck](https://docs.vulncheck.com/initial-access/2026-05-15#cve-2026-42945-nginx-ngx_http_rewrite_module-heap-based-buffer-overflow-queries-and-signatures-only) said they are seeing active exploitation tied to CVE-2026-42945, a heap buffer overflow flaw affecting both NGINX Open Source and NGINX Plus that was disclosed last week after apparently sitting unnoticed for 18 years.

VulnCheck's Patrick Garrity [said](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7461369932883152896/) the company observed exploitation activity on its canary systems "just days after the CVE was published."

REG AD

"An unauthenticated attacker can crash the NGINX worker process by sending crafted HTTP requests," he said. "On servers with ASLR disabled – which, of course, is extremely unlikely – code execution is possible."

REG AD

Researchers at [Depthfirst](https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability) disclosed the bug last week, saying the flaw had been sitting in NGINX's rewrite module since 2008. The vulnerability, nicknamed "NGINX Rift," was assigned a CVSS score of 9.2.

According to F5, [which acquired NGINX in 2019](https://www.theregister.com/on-prem/2019/03/12/f5-networks-buys-into-open-source-hands-over-670m-for-nginx-double-nginx-infinity-nginx/1332869), the flaw can be triggered by specially crafted HTTP requests under certain server configurations. In most cases, the result is a crashed worker process and a forced restart, though systems running without standard Linux memory protections could potentially face code execution.

## MORE CONTEXT

* [### Grafana Labs admits all its codebase are belong to someone who popped its GitHub account](/cyber-crime/2026/05/18/grafana-labs-admits-attackers-downloaded-its-codebase-from-github/5241686)
* [### Linus Torvalds says AI-powered bug hunters have made Linux security mailing list ‘almost entirely unmanageable’](/security/2026/05/18/linus-torvalds-says-ai-powered-bug-hunters-have-made-linux-security-mailing-list-almost-entirely-unmanageable/5241633)
* [### Patch time for Cisco SD-WAN admins as vendor drops yet another make-me-admin zero-day](/patches/2026/05/15/cisco-discloses-yet-another-sd-wan-make-me-admin-0-day/5241071)
* [### OpenAI caught in TanStack npm supply chain chaos after employee devices compromised](/security/2026/05/15/openai-caught-in-tanstack-npm-supply-chain-chaos-after-employee-devices-compromised/5241019)

A public proof-of-concept exploit appeared the same day patches dropped, which helps explain why researchers started seeing exploitation attempts almost immediately.

In practice, turning this into reliable remote code execution takes a pretty specific setup. The target server must be running a specific rewrite configuration, attackers need enough knowledge of that setup to exploit it correctly, and ASLR must also be disabled on the host system.

Security researcher Kevin Beaumont noted that while the bug is real, modern Linux defaults significantly reduce the likelihood of successful real-world RCE.

"Regarding CVE-2026-42945 in nginx – no modern (or even old) Linux distribution runs nginx without ASLR," Beaumont said. "So, cool, sweet technical vuln – it's valid – but the RCE apocalypse ain't coming."

Even so, VulnCheck said Censys scans surfaced roughly 5.7 million internet-exposed NGINX servers running potentially vulnerable versions, which means patching teams everywhere just inherited another very long week. ®

[cve-2026-42945](/tag/cve-2026-42945)
[nginx](/tag/nginx)
[exploitation](/tag/exploitation)
[security](/tag/security)
[f5](/tag/f5)
[vulnerability](/tag/vulnerability)

REG AD

[![](https://image.theregister.com/4094156.jpg?imageId=4094156&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

Networks

## Iran hints it could interfere with submarine cables in the Strait of Hormuz

Threatens unspecified ‘fees’ and warns of economic consequences – yet only major kinetic action could stop data flows entirely](https://www.theregister.com/networks/2026/05/19/iran-hints-it-could-interfere-with-submarine-cables-in-the-strait-of-hormuz/5242319)

[VIrtualization

## VMware quietly debuts Arm hypervisor tech preview

Supports Nvidia Grace and Ampere...