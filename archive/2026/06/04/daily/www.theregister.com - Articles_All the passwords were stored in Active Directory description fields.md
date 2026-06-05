---
title: All the passwords were stored in Active Directory description fields
url: https://www.theregister.com/security/2026/06/04/all-the-passwords-were-stored-in-active-directory-description-fields/5250820
source: www.theregister.com - Articles
date: 2026-06-04
fetch_date: 2026-06-05T06:14:28.972221
---

# All the passwords were stored in Active Directory description fields

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
  + [All Special Features](/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
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

* [Computex 2026](/special_features/computex)
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

SECURITY

# All the passwords were stored in Active Directory description fields

It was far too easy for a hacker to get the information

Avram Piltch
[Avram
Piltch](https://www.theregister.com/author/avram-piltch)
US editor

Published
thu 4 Jun 2026 // 06:00 UTC

PWNED Welcome back to [PWNED](https://theregister.com/tag/pwned), the weekly column where we talk about weak security policies and how to avoid them. Hopefully, we can learn from others’ mistakes – or at least have a good laugh at them.

Have a story about someone leaving a gaping hole in their network? Share it with us at pwned@sitpub.com. Anonymity is available upon request.

This week, we have a tale of password passivity involving Active Directory. It comes to us courtesy of Rob Anderson, head of reactive consulting services at [Reliance Cyber](https://www.reliancecyber.com/google-mssp-cybersecurity-services/), a UK-based security firm.

REG AD

Anderson recalls in the past working with a firm that was creating service accounts that developers needed to use, but the org didn’t have a proper password vault for storing the associated credentials. Instead, to make it easy for team members to find what they needed, they put the passwords into the description field for Active Directory.

REG AD

“People don't realize that as soon as you've got an Active Directory user — just an ordinary user — you can read the comments field or the description field across the whole of Active Directory,” Anderson told The Register. “It's such an amazing lapse of security.”

Soon enough, an Initial Access Broker (IAB), someone who specializes in gaining access to protected networks and then selling it to other threat actors, used a phishing campaign and executed offensive hacking tool Sliver on the endpoint. At that point, they captured a victim’s credentials, which led them to query Active Directory.

## MORE CONTEXT

* [### Company CEO flooded file share with smut, called for help after he deleted it](/security/2026/05/28/company-ceo-flooded-file-share-with-smut-called-for-help-after-he-deleted-it/5247502)
* [### Zombie user account let hackers control the city’s water](/security/2026/05/21/zombie-user-account-let-hackers-control-the-citys-water/5243724)
* [### To gain root access at this company, all an intruder had to do was ask nicely](/security/2026/05/14/to-gain-root-access-intruder-just-had-to-ask/5239853)
* [### Finance company stores DB credentials in helpfully labeled spreadsheet](/security/2026/04/30/finance-company-stored-their-db-credentials-in-spreadsheet/5224248)

Once in AD, the hackers found plenty of passwords, which came with full domain access. They used this access to delete all the backups and execute ransomware. In total, the crimes put 2000+ users out of action by encrypting Hyper-V hypervisors and their hosts. The company was taken offline for months.

What we can learn from this sad story is that you can’t put passwords in cleartext anywhere that's easy to access, unless you want an enormous attack surface. Even without a phish, an untrustworthy colleague could have sold the passwords to a threat actor. After all, [a recent survey](https://www.theregister.com/security/2026/05/06/1-in-8-workers-say-selling-company-logins-is-justifiable/5231104) found one in eight workers think selling company logins can be justified.

“I've seen it where configuration details are kept in application servers that are running, and threat actors are using fuzzing — trying likely file and directory names — which again exposes configuration and credentials to the threat actors,” Anderson said.

He noted that developers are a bit more savvy these days about where they put their credentials, but security naivete sinks ships. Trust no one. ®

[active directory](/tag/active%20directory)
[pwned](/tag/pwned)
[passwords](/tag/passwords)
[ransomware](/tag/ransomware)
[security](/tag/security)

REG AD

**SPONSORED LINKS**

[Building the New Trust Architecture for AI - Watch Now](http://pubads.g.doubleclick.net/gampad/clk?id=7330361192&iu=/6978)

[![](https://image.theregister.com/257058.jpg?imageId=257058&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

AI AND ML

## 'It would be good for the world' to slow down AI sprints, Anthropic says

The plea for caution comes the same week it beat AI archrival OpenAI to filing for an IPO](https://www.theregister.com/ai-and-ml/2026/06/05/it-would-be-good-for-the-world-to-slow-down-ai-sprints-anthropic-says/5251460)

[CYBER-CRIME

## Pink is the latest goon squad to use fake helpdesk calls to steal creds

A familiar tactic popularized by chaotic crime crew Lapsus$](https://www.there...