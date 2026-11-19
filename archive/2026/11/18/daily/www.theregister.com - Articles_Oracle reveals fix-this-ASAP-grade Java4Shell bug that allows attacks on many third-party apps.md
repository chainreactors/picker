---
title: Oracle reveals fix-this-ASAP-grade Java4Shell bug that allows attacks on many third-party apps
url: https://www.theregister.com/security/2026/11/18/oracle-reveals-fix-this-asap-grade-java4shell-bug-that-allows-attacks-on-many-third-party-apps/5310661
source: www.theregister.com - Articles
date: 2026-11-18
fetch_date: 2026-11-19T09:47:49.707184
---

# Oracle reveals fix-this-ASAP-grade Java4Shell bug that allows attacks on many third-party apps

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
  + [Supercomputing](/special_features/supercomputing_month_2026)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [SC 26](/special_features/sc26)
  + [Supercomputing Month 2026](/special_features/supercomputing_month_2026)
  + [Nvidia GTC Berlin 2026](/special_features/nvidia_gtc_berlin_2026)
  + [Cybersecurity Month 2026](/special_features/cybersecurity_month_2026)
  + [VMware Explore 2026](/special_features/vmware_explore_2026)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
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
* [Security](/tag/security)
* [Software](/tag/software)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Supercomputing](/special_features/supercomputing_month_2026)

REG AD

[security](/tag/security)

# Oracle reveals fix-this-ASAP-grade Java4Shell bug that allows attacks on many third-party apps

Attackers can crash the JVM or achieve unauthenticated RCE

![Simon Sharwood, Reg APAC editor](https://image.theregister.com/5299461.webp?imageId=5299461&x=0.00&y=6.18&cropw=100.00&croph=66.89&width=360&height=360)

Simon Sharwood
[Simon
Sharwood](https://www.theregister.com/author/simon-sharwood)
APAC Editor

Published
wed 18 Nov 2026 // 04:33 UTC

[Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)

### READ MORE

* [#### Chrome zero-day whack-a-mole continues as 2026 tally hits 8

  8 days ago](/security/2026/11/10/chrome-zero-day-whack-a-mole-continues-as-2026-tally-hits-8/5308732)
* [#### Oracle gobbles $20 billion borrowing limit a week after setting it

  16 days ago](/paas-and-iaas/2026/11/02/oracle-gobbles-20-billion-borrowing-limit-a-week-after-setting-it/5307014)
* [#### Oracle wants to bill you for every AI task, not just every seat

  20 days ago](/applications/2026/10/29/oracle-wants-to-bill-you-for-every-ai-task-not-just-every-seat/5306403)
* [#### Oracle celebrates end of Cybersecurity Awareness Month with quadruple trouble

  21 days ago](/security/2026/10/28/oracle-celebrates-end-of-cybersecurity-awareness-month-with-quadruple-trouble/5306121)
* [#### Big Red gets cozy with Google to offer TPUs to AI customers

  22 days ago](/ai-and-ml/2026/10/27/big-red-gets-cozy-with-google-to-offer-tpus-to-ai-customers/5305846)

The United States Cybersecurity and Infrastructure Security Agency (CISA) has urged Java users to immediately patch a high-severity flaw in the software, which attackers can use to crash the Java virtual machine or achieve unauthenticated remote code execution (RCE).

Oracle revealed the flaw in its [monthly patch dump for November](https://www.oracle.com/security-alerts/cspunov2026.html), which offers 655 patches, 62 of them rated critical, affecting 62 products.

Several of the flaws are rated more dangerous than the Java problem, [CVE-2026-114938](https://nvd.nist.gov/vuln/detail/cve-2026-114938), which Big Red didn’t single out as worthy of special attention despite [CISA’s warning](https://www.cisa.gov/news-events/alerts/2026/11/17/critical-java-vulnerability-requires-immediate-patching).

REG AD

The cyber-agency’s decision seems apt because vulnerability research and red teaming outfit Calif.io, which discovered the flaw, [used its X account](https://x.com/calif_io/status/2122724367654334810) to claim news of the problem had leaked before public disclosure and the release of Oracle's fixes.

REG AD

By then, Calif had already tested the flaw, which it [named “Java4Shell,”](https://calif.io/java4shell) and found applications including Keycloak, Atlassian’s Jira and Confluence, Jenkins, Apache Kafka Broker, and Elasticsearch are susceptible to RCE.

Calif, which also helped to find the [PHP2Shell flaw](https://www.theregister.com/security/2026/10/22/php-blames-supply-chain-security-biz-chainguard-for-putting-huge-chunks-of-the-web-at-risk/5304611), says the flaw is a memory-corruption vulnerability in OpenJDK's Base64 decoder.

“Base64 is a very common way of representing binary data as text. It is used in authentication protocols, to encode file uploads, and to deliver network messages,” the company explained. “To decode Base64 faster, OpenJDK uses specialized x86-64 CPU instructions to process many bytes at once.”

“We discovered a bug in that optimized machine-level code that lets malformed input overwrite neighboring memory. With careful exploitation, the corruption can reveal sensitive memory, as [Heartbleed](https://www.heartbleed.com/) did, or lead to remote code execution. The corruption itself can be triggered by just 64 A characters followed by a single =:”

Calif applied the CVSS 4.0 bug-rating scheme and gave the flaw a critical-rated score of 9.2/10.

Infosec outfit SentinelOne’s ...