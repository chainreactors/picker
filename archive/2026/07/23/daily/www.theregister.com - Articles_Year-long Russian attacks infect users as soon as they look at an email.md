---
title: Year-long Russian attacks infect users as soon as they look at an email
url: https://www.theregister.com/patches/2026/07/23/year-long-russian-attacks-infect-users-as-soon-as-they-look-at-an-email/5277358
source: www.theregister.com - Articles
date: 2026-07-23
fetch_date: 2026-07-24T05:05:47.662125
---

# Year-long Russian attacks infect users as soon as they look at an email

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
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
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

PATCHES

# Year-long Russian attacks infect users as soon as they look at an email

Phishing for dummies

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
thu 23 Jul 2026 // 17:47 UTC

Kremlin cyber goons have been breaking into government and commercial networks for at least a year by exploiting a Zimbra bug with a novel twist on Russia’s usual phishing expeditions: this attack occurs as soon as the victim looks at an email, with no need to even click on a link or open a file.

These attacks have been ongoing since July 2025, according to a whopping 27 US, UK, and other international government agencies, which attribute the intrusions to a group they track as [Laundry Bear](https://www.theregister.com/security/2025/05/27/new-russian-cyber-spy-crew-laundry-bear-joins-the-pack/974394), aka Void Blizzard.

“Laundry Bear’s targeting is almost certainly to gather sensitive information for the Russian Federation, with these actors primarily focusing on the covert acquisition of email data,” according to the [joint security alert](https://www.ic3.gov/CSA/2026/260723.pdf).

REG AD

The Russians’ latest campaign targets [CVE-2025-66376](https://nvd.nist.gov/vuln/detail/CVE-2025-66376), a cross-site scripting (XSS) vulnerability in the Zimbra web-based email and collaboration suite that was patched in November 2025 – but Moscow's attackers began exploiting it long before then. This type of vulnerability allows attackers to inject malicious JavaScript into web pages viewed by the victim.

REG AD

In this case, the phishing bears abused the security hole in the Zimbra Collaboration Suite by sending malware-laden HTML email messages to target Western organizations. Targeted orgs include those in the defense industrial base, federal and local governments, education, energy, law enforcement, media, non-governmental organizations, and technology sectors.

Some of the email addresses used in this campaign include ivanka.zurabishvili@proton[.]me, zmul1@buildandconsulting[.]com, garrysmithme@pinmx[.]net, and hostingclient@pinmx[.]net, we’re told.

The attack doesn’t require any user interaction other than viewing the malicious email, and once that happens, the attackers get to work exfiltrating a ton of data. This includes the victims’ last 90 days of email communications, email addresses and passwords, the organizations’ email directories such as global address lists, two-factor authentication tokens, and newly created application passcodes.

Then the attackers use these stolen credentials to maintain access to the victims’ email, modifying account preferences and collecting authentication information.

Laundry Bear stores the stolen goods on an unattributable virtual private server (VPS) running its custom “Flowerbed” collection framework. Flowerbed is a Python project that uses Docker for containerization. “The simplistic Flowerbed codebase has indications that artificial intelligence (AI) played a role in its development,” the government agencies noted.

The 31-page security alert includes an extensive i[ndicators of compromise (IOC) section](https://www.ic3.gov/CSA/2026/260723.pdf), which organizations should review to identify individuals compromised by the campaign.

## MORE CONTEXT

* [### New Russian cyber-spy crew Laundry Bear joins the email-stealing pack](/security/2025/05/27/new-russian-cyber-spy-crew-laundry-bear-joins-the-pack/974394)
* [### Russia-linked threat group put ChatGPT to work from lure to payload](/research/2026/05/29/russia-linked-threat-group-put-chatgpt-to-work-from-lure-to-payload/5248368)
* [### Russians are posing as Signal support to launch phishing attacks](/security/2026/03/22/russians-posing-as-signal-support-to-launch-phishing-raids/5221189)
* [### Russia-linked APT28 attackers already abusing new Microsoft Office zero-day](/security/2026/02/02/russia-linked-attackers-abuse-new-microsoft-office-zero-day/4775596)

Also, the agencies recommend minimizing employees’ use of the ZCS webmail client until their organizations update to a patched version that is not vulnerable to CVE-2025-66376. ®

[russia](/tag/russia)
[patches](/tag/patches)
[security](/tag/security)
[xss](/tag/xss)

REG AD

[![](https://image.theregister.com/257741.jpg?imageId=257741&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

off-prem

## Microsoft fiber foul-up cut off Azure California for almost five hours

Maintenance mistake caused immedia...