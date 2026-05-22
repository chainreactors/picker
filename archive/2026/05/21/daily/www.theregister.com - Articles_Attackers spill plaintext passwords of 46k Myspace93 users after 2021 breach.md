---
title: Attackers spill plaintext passwords of 46k Myspace93 users after 2021 breach
url: https://www.theregister.com/security/2026/05/21/46k-plaintext-passwords-pwned-in-myspace93-breach/5244024
source: www.theregister.com - Articles
date: 2026-05-21
fetch_date: 2026-05-22T06:08:45.819291
---

# Attackers spill plaintext passwords of 46k Myspace93 users after 2021 breach

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
  + [PaaS + IaaS](/tag/paas-iaas)
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
  + [AI + ML](/tag/ai-ml)
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

[Security](https://www.theregister.com/security)

# Attackers spill plaintext passwords of 46k Myspace93 users after 2021 breach

Leakage blamed on treacherous friends exposed unencrypted credentials, email addresses

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
thu 21 May 2026 // 13:20 UTC

Users of the Myspace93 parody web art site be warned: the dataset spilled after a reported breach in 2021 included the plaintext usernames and passwords of more than 46,000 registered users.

The site's co-creator has blamed "trusted members" of a Windows93 [Discord](https://www.theregister.com/special-features/2025/10/09/discord-attackers-accessed-about-70000-user-photo-ids/1348487) channel for the leakage.

The figure of 46,000+ users is a recent estimate from [HaveIBeenPwned](https://haveibeenpwned.com/Breach/Windows93) (HIBP) - the web's go-to breach aggregator - which ingested the related data this week, more than five years after the January 2021 attack.

In addition to the clear-as-day passwords and usernames, HIBP said email addresses and IP addresses were also among the exposed data.

REG AD

![Myspace93's homepage](https://image.theregister.com/5244035.webp?imageId=5244035&width=960&height=394&format=jpg)

Myspace93's homepage

Myspace93 is an offshoot of the [Windows93 project](https://windows93.net/). They’re both websites that spoof the old social media network and operating system respectively, allowing users to experience them now that they’re long gone.

REG AD

Its co-creator, who only goes by the alias jankenpopp, or Janken, [penned a note](https://web.archive.org/web/20210704163048/https%3A//www.windows93.net/dearCommunity.txt) to the website’s users following the attack. Dated July 4, 2021, Janken explained that the breach came about after they shared a beta app with trusted members of the Windows93 [Discord](https://www.theregister.com/special-features/2025/10/09/discord-attackers-accessed-about-70000-user-photo-ids/1348487) channel.

According to Janken, those members betrayed the co-creator and used their access to the beta application to steal server files and gain access to an unencrypted credential store.

## MORE CONTEXT

* [### Your AI-generated password isn't random, it just looks that way](/security/2026/02/18/llm-generated-passwords-fundamentally-weak-experts-say/4706577)
* [### From MySpace to MyFreeDiskSpace: 12 years of music – 50m songs – blackholed amid mystery server move](/on-prem/2019/03/18/from-myspace-to-myfreediskspace-12-years-of-music-50m-songs-blackholed-amid-mystery-server-move/1014794)
* [### Forgotten your Myspace password? Just a name, username, DoB will get you in – and into anyone else's, too](/security/2017/07/17/forgotten-your-myspace-password-just-a-name-username-dob-will-get-you-in-and-into-anyone-elses-too/1559971)
* [### You probably can't trust your password manager if it's compromised](/security/2026/02/16/password-managers-dont-protect-secrets-if-pwned/4306575)

“None of them alerted me immediately to what was going on,” Janken wrote. “On the contrary, they created a program to download our entire server, and it was only a week later that another honest user alerted me to the fact that these people were bragging about having the Myspace [passwords](https://www.theregister.com/security/2026/02/18/llm-generated-passwords-fundamentally-weak-experts-say/4706577).

“They didn't want to tell me the truth, and it took me two days to get a confession from them: not only had they downloaded all the source files of Windows93 behind my back, but also the unencrypted file containing the passwords of more than 45k Myspace users.

The group had also shared a download tool - along with instructions for using it - in their chat, and had posted numerous stolen files (unrelated to Myspace) across multiple platforms, said Janken.

“I removed the .smash app from the server and called them to order. They whimpered and promised me on their honor to delete all the stuff and that things would not go any further. I believed them because at the time we were very close, we talked every day, and they regularly helped me to manage the community, to fix bugs, sometimes to code new features for Windows93 or to make the services more secure. I really trusted them back in the day and considered them part of my team. I blame myself for being so naive.”

The [MySpace93 website](https://myspace.windows93.net/) is still up and running for anyone who wants to revel in a little noughties internet nostalgia, but the ability to register an account and use the site as a social network is closed.

Affected users should make sure they watch out for any reused passwords on other sites and switch on 2FA where they can.

REG AD

Janken said they had ...