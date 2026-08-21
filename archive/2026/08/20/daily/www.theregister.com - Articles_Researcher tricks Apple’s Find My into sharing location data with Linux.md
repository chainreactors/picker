---
title: Researcher tricks Apple’s Find My into sharing location data with Linux
url: https://www.theregister.com/security/2026/08/20/researcher-tricks-apples-find-my-into-sharing-location-data-with-linux/5290496
source: www.theregister.com - Articles
date: 2026-08-20
fetch_date: 2026-08-21T03:05:14.088964
---

# Researcher tricks Apple’s Find My into sharing location data with Linux

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
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

Security

# Researcher tricks Apple’s Find My into sharing location data with Linux

Clever protocol wrangling gets iBiz-only people tracking working on a non-iGadget

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
thu 20 Aug 2026 // 17:10 UTC

A young security researcher figured out a way to enroll a Linux device into Apple’s Find My network and read live location data from it.

Find My is Apple’s app for, you guessed it, finding things – whether [AirTags](https://www.theregister.com/on-prem/2022/02/11/apple-tweaks-airtags-to-make-them-less-useful-for-stalkers/688709), iPads, or other supported devices and items. It also works for people. Families can track each other's whereabouts for safety reasons, and friends can tell when others are hanging out without them.

In typical Apple fashion, though, the full Find My experience is limited to Apple hardware, like an iPhone or Mac. iBiz also offers Find Devices via the [iCloud](https://www.theregister.com/security/2025/02/24/apple-ends-icloud-advanced-data-protection-for-uk-customers/588745) website, although it lacks Find My’s people-tracking feature for viewing locations others have shared with you.

REG AD

However, the 22-year-old researcher, who goes by “Zerotistic,” [devised a way](https://zerotistic.blog/posts/find-my-people-linux/#fetching-and-decrypting-the-location) to enroll a Linux-based machine into the iNetwork, tricking Apple into sending the people-location data it exclusively reserves for Apple devices.

REG AD

It’s important to note, at this point, that this is not an exploit that allows anyone to arbitrarily retrieve any Apple user's location. It refers to registering a non-Apple device to the Find My network and retrieving the location data of people who had already chosen to share their locations with the Apple account owner.

Retrieving people-location data requires Apple to trust that the machine you’re using belongs to its network and is capable of receiving the data, which is sent over Apple’s Push Notification service (APNs).

The first step was tying the Linux machine to the researcher’s Apple account. Zerotistic obtained an identity delegate by going through Apple’s standard GrandSlam authentication protocol. In pursuit of an Apple Identity Services (IDS) device certificate, which links the intended device to an Apple Account, they then used that delegate to build a custom certificate signing request (CSR).

Lots of trial and error later, Zerotistic discovered that the CSR had to use the PKCS#10 format and a 2048-bit RSA key signed using SHA-1, linking the Linux machine to their Apple account. They bundled this up into a compressed XML file and sent it to Apple’s authenticateDS profile-enrollment endpoint.

The SHA-1 signature requirement and XML encoding were surprises. The researcher’s “best guess” is that the CSR had to conform to older standards because authenticateDS is a legacy endpoint.

Apple signed the CSR, handing the [Linux](https://www.theregister.com/os-platforms/2026/08/17/linux-72-debuts-linus-torvalds-says-new-normal-means-he-had-to-do-it-now-or-never/5288250) device the IDS certificate needed to register its public key to the researcher’s Apple account.

The Linux device was registered at this point, but further work was needed to convince Apple that it was capable of running Find My.

## MORE CONTEXT

* [### Rather than add a backdoor, Apple decides to kill iCloud encryption for UK peeps](/security/2025/02/24/apple-ends-icloud-advanced-data-protection-for-uk-customers/588745)
* [### Apple's Find My network can be abused to leak secrets to the outside world via passing devices](/security/2021/05/12/apples-find-my-network-can-be-abused-to-leak-secrets-to-the-outside-world-via-passing-devices/1310399)
* [### Apple tweaks AirTags to be less useful for stalkers, thieves](/on-prem/2022/02/11/apple-tweaks-airtags-to-make-them-less-useful-for-stalkers/688709)
* [### North Korean spies turn Google's Find Hub into remote-wipe weapon](/security/2025/11/11/north-korean-spies-used-google-find-hub-as-remote-wipe-tool/1161970)

Zerotistic found that a Find My registration request required the device to subscribe to six different subservices, define the types of encryption it suppo...