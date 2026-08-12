---
title: Mozilla revokes Firefox signing key after unencrypted copy lands in GitHub
url: https://www.theregister.com/security/2026/08/11/mozilla-revokes-firefox-signing-key-after-unencrypted-copy-lands-in-github/5285908
source: www.theregister.com - Articles
date: 2026-08-11
fetch_date: 2026-08-12T04:02:53.424270
---

# Mozilla revokes Firefox signing key after unencrypted copy lands in GitHub

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

SECURITY

# Mozilla revokes Firefox signing key after unencrypted copy lands in GitHub

Audit logs found no unexpected visitors, but release verification still needs an update

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
tue 11 Aug 2026 // 12:36 UTC

Mozilla has revoked a cryptographic key used to sign Firefox and Thunderbird releases after discovering someone had accidentally committed an unencrypted copy of the private key to a GitHub repository.

The browser maker [disclosed the mishap on Monday](https://blog.mozilla.org/security/2026/08/10/updated-gpg-key-for-signing-firefox-and-thunderbird-releases/), saying the GPG private subkey was checked into a private GitHub repository accessible only to a small number of Mozilla employees. All of them were already authorized to access the key through other means.

Still, leaving an unencrypted private signing key sitting in source control isn't exactly ideal, so Mozilla revoked the exposed subkey and replaced it.

REG AD

The affected subkey was used to sign Linux tarballs, RPM packages, and checksum files for Firefox and Thunderbird releases. Signing keys allow users and package managers to verify that software really came from Mozilla and hasn't been tampered with along the way.

REG AD

Mozilla said its review of available audit records "found no evidence that the key was accessed by an unauthorized party while it was present in the repository." It has introduced additional safeguards to prevent a repeat, but did not explain how the unencrypted key ended up in GitHub or how long it remained there.

For most Firefox and Thunderbird users, the key swap shouldn't require any action. Anyone manually verifying Mozilla's GPG signatures, however, will need to import the new signing key and the revocation for the old one.

## MORE CONTEXT

* [### Tech leaders issue letter to train Uncle Sam about value of open weight AI](/ai-and-ml/2026/07/24/tech-leaders-issue-letter-to-train-uncle-sam-about-value-of-open-weight-ai/5278533)
* [### Firefox 153 contains itself while Thunderbird 153 fixes almost everything](/software/2026/07/23/firefox-153-contains-itself-while-thunderbird-153-fixes-almost-everything/5276390)
* [### Mozilla speeds Firefox release schedule to biweekly](/software/2026/07/17/mozilla-speeds-firefox-release-schedule-to-biweekly/5274423)
* [### Dark patterns in Windows are steering users to Edge: Mozilla-commissioned report](/os-platforms/2026/07/15/dark-patterns-in-windows-are-steering-users-to-edge-mozilla-commissioned-report/5271792)

The change is a little more involved for users who installed Firefox through Mozilla's RPM repository. On Fedora 43 and later, DNF should download the updated key during the next Firefox update, although users will be asked to approve its import. Mozilla says users running Fedora 42 or earlier, RHEL, Rocky Linux, AlmaLinux, openSUSE, or SUSE will need to remove the old key and manually import its replacement.

There's another wrinkle for anyone checking older releases: after importing the revocation, normal signature verification will reject releases signed with the revoked subkey.

Thunderbird users don't have to worry about RPM-specific shenanigans, as Mozilla doesn't provide official RPM packages for the email client.

The Register asked Mozilla how long the private key was sitting in GitHub, how it got there, and whether its audit logs cover the entire period it was exposed, but did not receive a response. ®

[mozilla](/tag/mozilla)
[firefox](/tag/firefox)
[web browser](/tag/web%20browser)
[security](/tag/security)

REG AD

[![](https://image.theregister.com/5286595.jpg?imageId=5286595&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

AI AND ML

## India’s central bank wants AI to approve loans that humans would reject

Regulator hopes for greater financial inclusion, without extra risk or blaming models for bad decisions](https://www.theregister.com/ai-and-ml/2026/08/12/indias-central-bank-wants-ai-to-approve-loans-that-humans-would-reject/5286572)

[AI and ML

## Modular's Mojo programming language hits 1.0 milestone

Developers await open source compiler release to dispel uncertainty following Qu...