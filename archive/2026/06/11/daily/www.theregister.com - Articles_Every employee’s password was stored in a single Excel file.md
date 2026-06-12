---
title: Every employee’s password was stored in a single Excel file
url: https://www.theregister.com/security/2026/06/11/every-employees-password-was-stored-in-a-single-excel-file/5253784
source: www.theregister.com - Articles
date: 2026-06-11
fetch_date: 2026-06-12T06:28:16.129799
---

# Every employee’s password was stored in a single Excel file

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

SECURITY

# Every employee’s password was stored in a single Excel file

The CEO thought this was the best way to deal with some email issues

Avram Piltch
[Avram
Piltch](https://www.theregister.com/author/avram-piltch)
US editor

Published
thu 11 Jun 2026 // 08:00 UTC

PWNED Welcome, once again, to PWNED, the weekly screed where we highlight those who did not do the deed of securing their systems. If someone left their passwords or their access exposed, we will be writing about them here.

Have a story about someone leaving a gaping hole in their network? Share it with us at pwned@sitpub.com. Anonymity is available upon request.

This week’s terrifying tale of poor security hygiene comes courtesy of Luke Irwin, CEO and principal consultant at [Aegis Cybersecurity](https://aegiscyber.com.au/). He’s been in the industry for more than a quarter of a century and he knows where the bits are buried.

REG AD

At one point, Irwin consulted for a company that was a large national facility services organization, a 2,000-employee firm that provided cleaning, security guards, industrial abseiling (cleaning the facade), and other things that other large businesses need to keep their physical plants running smoothly.

REG AD

The CEO had one very peculiar idea about how to keep his own house in order: he wanted to have access to every one of his employees’ login credentials.

The chief executive had an Excel spreadsheet sitting right on his desktop with a complete list of all the employee usernames and passwords. Let that sink in for a second. One person had all the keys to the castle in a single, easily accessible file.

In any decent security setup, no one in the company has access to anyone else’s password. Even the head of the IT department should not know another employee’s password. I say this as someone who used to work for a company where the IT department would ask you to DM them your password if you had computer problems.

But this company’s CEO wanted the usernames and passwords for reasons I’m sure any of his employees would appreciate: so he could go into their email accounts! He had an experience where one colleague had sent secret information to the entire company via email and he had spent the evening logging into every single account and deleting the message before anyone could see it.

Just in case other messages were sent in error in the future, the CEO wanted the ability to log into all the relevant accounts and delete them himself. Perhaps for the same reason, he would not allow MFA (multi-factor authentication), because that would have kept him out of people’s inboxes. He was adamant even though the company had been the victim of a ransomware incident previously.

“Despite repeated advice, he held that position for around four months, until we were able to demonstrate that the IT team could remove messages centrally using fairly simple administrative commands, without needing everyone’s password,” Irwin said.

Even after getting rid of the Excel sheet of shame, the boss still refused to turn on MFA and the company subsequently suffered two data breaches involving sensitive client data.

## MORE CONTEXT

* [### All the passwords were stored in Active Directory description fields](/security/2026/06/04/all-the-passwords-were-stored-in-active-directory-description-fields/5250820)
* [### Company CEO flooded file share with smut, called for help after he deleted it](/security/2026/05/28/company-ceo-flooded-file-share-with-smut-called-for-help-after-he-deleted-it/5247502)
* [### Zombie user account let hackers control the city’s water](/security/2026/05/21/zombie-user-account-let-hackers-control-the-citys-water/5243724)
* [### The network password was a key plot point in one of the most famous movies of all time](/security/2026/05/07/guessable-admin-password-exposes-sloppy-network-security/5231161)

Unfortunately, this company wasn’t the only one that Irwin worked with where the management had something against MFA. Another client, this one in the medical sector, was opposed to multi-factor authentication because it “made things just a little too hard” for the external consultants they were using to access their systems.

REG AD

During the time that Irwin worked with that company, they got lucky and no one breached them. But since then, he’s seen signs that their data was available on the dark web. No word on whether they ever switched MFA on.

There’s plenty to learn from Irwin’s two clients, but it’s all pretty obvious. First, don’t let anyone, even administrators or CEOs, have other people’s passwords. If someone has to get into another person’s email account, have IT use administrative access. Second, always enable MFA, preferably [MFA with passkeys](...