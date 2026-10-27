---
title: PHP2Shell: No login, no app code, no warning. What next?
url: https://www.theregister.com/security/2026/10/26/partner-content-no-login-no-app-code-no-warning-what-next/5305336
source: www.theregister.com - Articles
date: 2026-10-26
fetch_date: 2026-10-27T07:06:05.114627
---

# PHP2Shell: No login, no app code, no warning. What next?

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
  + [PHP2Shell](/tag/php2shell)
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
* [PHP2Shell](/tag/php2shell)

security

# PHP2Shell: No login, no app code, no warning. What next?

PARTNER CONTENT: Learn what the flaws are, how far exploitation has gone, and how to get to full coverage fast with Tanium

Tanium
Tanium

Published
mon 26 Oct 2026 // 08:00 UTC

[Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)

If you run PHP anywhere in your environment, patch to PHP 8.5.12, 8.4.27, 8.3.36 or 8.2.35 now. Two critical flaws disclosed last week, CVE-2026-109618 and CVE-2026-109619 (nicknamed "PHP2Shell"), let an unauthenticated attacker run code on a server with nothing more than a crafted web request. Both carry a CVSS v4.0 score of 9.2, every earlier release is affected, and exploitation in the wild has been reported.

The patch is the easy part. The hard part is finding every copy of PHP you own, because PHP rarely shows up where you expect it. This post covers what the flaws are, how far exploitation has gone, and how to get to full coverage fast.

![Tanium alert page](https://image.theregister.com/5305339.webp?imageId=5305339&x=0.00&y=0.00&cropw=99.72&croph=100.00&width=960&height=1200&format=jpg)

Tanium alert page

C/O Tanium

### **What happened**

Details leaked before the planned embargo, so the PHP security team moved fast and shipped fixes within about a day of announcing them.

###

| When (UTC) | Event |
| --- | --- |
| Oct 21, 14:17 | NVD publishes CVE-2026-109618, marked "Undergoing Analysis" |
| Oct 21, 14:04 | CISA KEV catalog update lists neither CVE |
| Oct 21, ~14:00 | PHP publishes the official advisory and releases 8.5.12, 8.4.27, 8.3.36 and 8.2.35 |
| Oct 21, 13:47 | Fixed Windows builds appear on downloads.php.net |
| Oct-21 | watchTowr reports exploitation observed in its global honeypot network |
| Oct-20 | CERT-EU issues advisory 2026-018, advising isolation of internet-facing PHP apps |
| Oct-20 | PHP announces an emergency security release after details leak; watchTowr confirms the flaws are real |

### **The two vulnerabilities**

Both bugs live in PHP core, not in any framework or plugin, so they reach anything that runs PHP to serve web requests.

###

| CVE | What goes wrong | Validated RCE on |
| --- | --- | --- |
| CVE-2026-109618 | Memory corruption reached through out-of-memory conditions while PHP parses multipart (file upload) requests | mod\_php |
| CVE-2026-109619 | A use-after-free on the request that follows a fatal error | mod\_php, PHP-FPM |

Affected server setups include PHP-FPM, mod\_php, php-cgi, FrankenPHP and LiteSpeed. PHP rates mod\_php as the highest risk. No login is needed: the attacker only has to reach a PHP endpoint over HTTP.

Fixed versions: 8.5.12, 8.4.27, 8.3.36 and 8.2.35. Every earlier release is affected. PHP has also published minimal source backports for 7.4, 8.0 and 8.1, but there are no official releases for those branches. Treat a backport as a stopgap and plan the upgrade.

### **Is it being exploited?**

Yes, though reliable public exploits are still scarce. watchTowr reports exploitation in its honeypot network as of October 21, and Tenable relays Cloudflare's CTO saying Cloudflare is seeing early attacks. Other telemetry, such as Patchstack's, shows mostly probing so far. Neither CVE is in CISA's KEV catalog yet, and no public indicators of compromise have been released.

How hard the bug is to weaponize depends on the platform. VulnCheck reproduced both flaws and found:

* Code execution works on ARM64, and on x86 systems where address space layout randomization (ASLR) is turned off.
* Dozens of public proof-of-concepts exist, but very few work and none bypass ASLR on x86-64.
* Red Hat likewise rates RCE as hard in practice on default PHP-FPM deployments.

Don't read that as permission to wait. Exploits mature quickly once a patch diff is public, and fake PoC repositories for headline CVEs often carry malware, so treat any you find with caution. [Tanium's](https://www.tanium.com/see-a-demo/?utm_source=situationpublishing&utm_source_platform=direct&utm_asset=none&utm_medium=nativecontent&utm_campaign=thrdprty-r...