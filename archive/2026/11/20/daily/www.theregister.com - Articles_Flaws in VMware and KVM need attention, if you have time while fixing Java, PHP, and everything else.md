---
title: Flaws in VMware and KVM need attention, if you have time while fixing Java, PHP, and everything else
url: https://www.theregister.com/security/2026/11/20/flaws-in-vmware-and-kvm-need-attention-if-you-have-time-while-fixing-java-php-and-everything-else/5311193
source: www.theregister.com - Articles
date: 2026-11-20
fetch_date: 2026-11-21T09:02:41.087417
---

# Flaws in VMware and KVM need attention, if you have time while fixing Java, PHP, and everything else

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
* [Outages](/tag/outage)

REG AD

[security](/tag/security)

# Flaws in VMware and KVM need attention, if you have time while fixing Java, PHP, and everything else

Critical Virtzilla bugs allow authentication bypass, as a nested virtualization issue got Digital Ocean ducking

![Simon Sharwood, Reg APAC editor](https://image.theregister.com/5299461.webp?imageId=5299461&x=0.00&y=6.18&cropw=100.00&croph=66.89&width=360&height=360)

Simon Sharwood
[Simon
Sharwood](https://www.theregister.com/author/simon-sharwood)
APAC Editor

Published
fri 20 Nov 2026 // 00:57 UTC

[Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)

### READ MORE

* [#### XXRI-OS explores the lowest end of the Linux desktop

  1 day ago](/os-platforms/2026/11/19/xxri-os-explores-the-lowest-end-of-the-linux-desktop/5311036)
* [#### NoisyTCP bug gives Linux servers a remote crash problem 11 years in the making

  4 days ago](/security/2026/11/16/noisytcp-bug-gives-linux-servers-a-remote-crash-problem-11-years-in-the-making/5310144)
* [#### Omaxian takes the Omarchy look down a different Linux backstreet

  4 days ago](/os-platforms/2026/11/16/omaxian-takes-the-omarchy-look-down-a-different-linux-backstreet/5309750)
* [#### Microsoft’s Azure Linux dons Fedora to dress itself up for mainstream workloads

  5 days ago](/os-platforms/2026/11/16/microsofts-azure-linux-dons-fedora-to-dress-itself-up-for-mainstream-workloads/5310016)
* [#### Another Linux kernel developer steps back from some duties due to overload

  7 days ago](/ai-and-ml/2026/11/13/another-linux-kernel-developer-steps-back-from-some-duties-due-to-overload/5309628)

If you’ve got a moment to spare in between sorting out emergency patches for [PHP](https://www.theregister.com/patches/2026/11/18/another-critical-php-security-release-has-dropped/5310911), [Java](https://www.theregister.com/security/2026/11/18/oracle-reveals-fix-this-asap-grade-java4shell-bug-that-allows-attacks-on-many-third-party-apps/5310661), and [PostgreSQL](https://www.theregister.com/databases/2026/11/17/postgresql-patches-52-security-holes-sends-version-14-into-retirement/5310108), VMware has just bid for any remaining space on your schedule by publishing two critical-rated security advisories.

[VMSA-2026-0009](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39495) addresses [CVE-2026-123890](https://www.tenable.com/cve/CVE-2026-123890), a 9.8-rated flaw that VMware says means a malicious actor with network access to vCenter may exploit this issue to bypass authentication and gain unauthorized access to the system. vCenter is the tool admins use to manage fleets of virtual machines. The flaw is present in VMware’s flagship Cloud Foundation suite.

VMware also wants its users to address CVE-2026-123891, which allows attackers to read and write the database used by SDDC Manager, the tool for managing entire software-defined datacenters. Attackers can execute arbitrary commands and elevate privileges to root.

REG AD

The prospect of an unknown party getting access to vCenter or SDDC manager is not pleasant. At least VMware has fixed its software.

REG AD

The virty giant hasn't done the same to address a second advisory, [VMSA-2026-0010](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39625), which warns that Cloud Foundation, Aria Operations, and VCF Operations HCX products all use Apache – which has a 9.8-rated remote code execution vulnerability (CVE-2026-119618).

VMware plans to ship new versions of its products with a patched version of Apache, but for now only has workarounds that disable the http2 protocol.

### A KVM curiosity

Admins who oversee virtual infrastructure also need to pay attention to Linux KVM, the subject of a curious incident over the last 24 hours.

This mess started with the November 18 disclosure of [CVE-2026-99312](https://nvd.nist.gov/vuln/detail/cve-2026-99312), a bug which allows an attacker to use a guest virtual machine to inflict Denial of Se...