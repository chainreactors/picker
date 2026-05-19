---
title: Do fear the Reaper - stealer swipes macOS users' passwords, wallets, then backdoors them
url: https://www.theregister.com/security/2026/05/19/do-fear-the-reaper-stealer-swipes-macos-users-passwords-wallets-then-backdoors-them/5242258
source: www.theregister.com - Articles
date: 2026-05-18
fetch_date: 2026-05-19T06:05:15.062407
---

# Do fear the Reaper - stealer swipes macOS users' passwords, wallets, then backdoors them

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

# Do fear the Reaper - stealer swipes macOS users' passwords, wallets, then backdoors them

While also spoofing all the trusted domains - Apple, Microsoft, and Google - in the same attack

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
tue 19 May 2026 // 00:32 UTC

A new infostealer variant targets macOS users by spoofing Apple, Microsoft, and Google and then then gets to work searching for victims’ password managers so it can steal all of their credentials and access cryptocurrency wallets such as MetaMask and Phantom.

The updated SHub stealer variant is called Reaper, and it uses macOS Script Editor, pre-populated with the malicious payload to execute the malware, according to SentinelOne research engineer Phil Stokes, who documented the attack in a Monday blog.

But unlike [earlier SHub versions](https://www.jamf.com/blog/clickfix-macos-script-editor-atomic-stealer/) and similar [macOS stealer campaigns](https://www.theregister.com/security/2026/04/21/macos-clickfix-attacks-deliver-applescript-stealers/5226728) that rely on [ClickFix social engineering tactics](https://www.theregister.com/security/2026/03/10/crooks-compromise-wordpress-sites-spread-infostealers/5222045) to trick the user into pasting a ScriptEditor command into Apple’s Terminal command-line interface, Reaper bypasses Terminal altogether and therefore defeats defenses Apple added to [Tahoe 26.4](https://x.com/malwarezoo/status/2037305551911014760?s=20).

REG AD

## MORE CONTEXT

* [### macOS ClickFix attacks deliver AppleScript stealers to snarf credentials, wallets](/security/2026/04/21/macos-clickfix-attacks-deliver-applescript-stealers/5226728)
* [### Shai-Hulud copycat worm infects yet another npm package](/cyber-crime/2026/05/18/shai-hulud-copycat-hits-another-npm-package/5242180)
* [### Cookie thieves caught stealing dev secrets via fake Claude Code installers](/security/2026/05/11/cookie-thieves-caught-stealing-dev-secrets/5238248)
* [### Microsoft spots ClickFix campaign getting users to self-pwn on Windows Terminal](/security/2026/03/06/microsoft-spots-clickfix-scam-spreading-lumma-infostealer/5207455)

The attack starts with fake WeChat and Miro installer websites, hosted on a domain designed to instill trust in users by typo-squatting a Microsoft URL: mlcrosoft[.]co[.]com.

REG AD

When a user visits these pages, hidden JavaScript collects a ton of information about their system and browser, including IP address, location, WebGL fingerprinting data, and indicators of virtual machines or VPNs. The attack stops if the victim is located in Russia.

Assuming that the machine is located elsewhere and the user clicks on the fake tool installer, they open Apple’s Script Editor app via a sneaky link that’s heavily padded with ASCII art and fake terms to push the malicious command far below the visible portion of the window when it loads.

When the victim clicks “Run” in Script Editor, the hidden command executes the malicious AppleScript and displays a popup message purporting to be a security update for Apple’s XProtectRemediator tool. Instead of updating the security tool, however, it calls a curl command to silently download the shell script and it asks the victim to enter their login details – which are [scraped and used to decrypt various credentials](https://www.sentinelone.com/blog/how-offensive-actors-use-applescript-for-attacking-macos/)  – and then displays a fake error message.

Earlier SHub versions harvested users’ browser data, cryptocurrency wallets, developer-related configuration files, macOS Keychain and iCloud account data, and Telegram session data.

Reaper does all of this and more.

It includes a filegrabber that searches for files that contain business or financial info in the user’s Desktop and Document folders. That approach is similar to the document-theft functionality seen in [Atomic macOS Stealer](https://www.sentinelone.com/blog/from-amos-to-poseidon-a-soc-teams-guide-to-detecting-macos-atomic-stealers-2024/) (AMOS).

The script also searches for several desktop cryptocurrency tools including Exodus, Atomic Wallet, Ledger Wallet, Ledger Live, and Trezor Suite. If it finds any, it injects the wallet with malware to ensure continued funds theft.

And then, to ensure persistence, it backdoors the infected device by creating a directory structure designed to mimic Google Software Update: ~/Library/Application Support/Google/GoogleUpdate.app/Contents/MacOS/.

REG AD

“The LaunchAgent executes the target script GoogleUpdate every 60 seconds,” Stokes explains. “The script functions as a beacon, sending system details to the C2’s /api/bot/heartbeat endpoint.”

This ensures the attacker can remotely execute code on the backdoored machine. If the attacker-controlled server send...