---
title: The hits keep on coming for Cisco vulnerabilities
url: https://www.theregister.com/security/2026/06/24/the-hits-keep-on-coming-for-cisco-vulnerabilities/5261797
source: www.theregister.com - Articles
date: 2026-06-24
fetch_date: 2026-06-25T06:10:33.034422
---

# The hits keep on coming for Cisco vulnerabilities

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
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
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

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Security

# The hits keep on coming for Cisco vulnerabilities

CVE-2026-20230 under exploitation, while an earlier SD-WAN 0-day looks even worse than we thought

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
wed 24 Jun 2026 // 23:27 UTC

It’s looking like another tough week ([month](https://www.theregister.com/patches/2026/06/15/cisco-sd-wan-make-me-root-bug-under-attack/5255916)? [year](https://www.theregister.com/security/2026/05/21/cisco-serves-up-yet-another-perfect-10-bug-with-secure-workload-admin-flaw/5244012)?) for Switchzilla amid reports of new serious vulnerabilities under attack.

First up is a server-side request forgery bug in its Unified Communications Manager tracked as CVE-2026-20230.

Cisco [disclosed and patched](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW) this flaw in early June. The comms control platform doesn’t properly validate some HTTP requests, and an attacker could exploit this bug to gain root privileges on a compromised device.

REG AD

At the time, Cisco said that a proof-of-concept exploit was available – and now it seems unknown miscreants are putting that exploit code to use, with threat intel company Defused [warning](https://x.com/DefusedCyber/status/2069074520057557244) that it observed miscreants exploiting CVE-2026-20230 over the weekend.

REG AD

“The observed chain abuses the WebDialer SSRF to deploy a rogue Apache Axis service, uses that service to write a first-stage JSP file-writer, then drops a second-stage command-execution shell under /platform-services/axis2-web/,” the firm [noted](https://www.linkedin.com/posts/cve-2026-20230-cisco-cucm-webdialer-ssrf-share-7475496621158494208-LjIv/) on LinkedIn.

### Cisco Catalyst SD-WAN zero day

Then, a Mandiant advisory on Wednesday warned that a Cisco SD-WAN zero-day tracked as CVE-2026-20245 was exploited much earlier than initially disclosed, including at a communications service provider where the attacker elevated a compromised admin account to full root-level access.

While the Google-owned threat hunting biz said it can't assess the full scope of the intruders' post-compromise activity, this SD-WAN device compromise could have been dire, potentially giving the attacker total visibility across an entire corporation's internet traffic. This is what makes SD-WAN zero-days such a [hot target for government-sponsored spies](https://www.theregister.com/on-prem/2026/02/26/five-eyes-urge-action-as-cisco-zero-day-attacks-uncovered/4493149) looking to set up shop for long-term snooping activities.

It also explains the rash of [attackers battering Cisco SD-WAN devices](https://www.theregister.com/security/2026/04/21/more-cisco-sd-wan-bugs-battered-in-attacks/5229107) since the start of the year.

## MORE CONTEXT

* [### Cisco adds another SD-WAN box to max-severity bug advisory](/security/2026/06/17/cisco-adds-another-sd-wan-box-to-max-severity-bug-advisory/5257621)
* [### Yet another Cisco SD-WAN 0-day under attack, and no patch in sight](/security/2026/06/05/yet-another-cisco-sd-wan-0-day-under-attack-and-no-patch-in-sight/5251855)
* [### Cisco serves up yet another perfect 10 bug with Secure Workload admin flaw](/security/2026/05/21/cisco-serves-up-yet-another-perfect-10-bug-with-secure-workload-admin-flaw/5244012)
* [### More Cisco SD-WAN bugs battered in attacks](/security/2026/04/21/more-cisco-sd-wan-bugs-battered-in-attacks/5229107)

Cisco had [issued an advisory](https://www.theregister.com/security/2026/06/05/yet-another-cisco-sd-wan-0-day-under-attack-and-no-patch-in-sight/5251855) for CVE-2026-20245 in early June, admitting that attackers had a head start on abusing this security hole. “In June 2026, the Cisco PSIRT became aware of exploitation of this vulnerability,” the vendor [said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx) at the time.

In a Wednesday report, however, Google’s Mandiant incident response and consulting biz reported that exploitation of this bug – Cisco’s sixth SD-WAN vulnerability listed as under attack since the start of the year, and the second zero-day in two months – began much earlier.

REG AD

“In early 2026, Mandiant identified a threat actor targeting SD-WAN infrastructure at a service provider,” Mandiant threat hunters Chester Sng, Pete Boonyakarn, and Logeswaran Nadarajan [wrote](https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager). “After gaining initial access, the threat actor exploited a zero-day vulnerability ([CVE-2026-20245](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4u...