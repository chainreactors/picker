---
title: Shai-Hulud copycat worm infects yet another npm package
url: https://www.theregister.com/cyber-crime/2026/05/18/shai-hulud-copycat-hits-another-npm-package/5242180
source: www.theregister.com - Articles
date: 2026-05-18
fetch_date: 2026-05-19T06:05:15.486865
---

# Shai-Hulud copycat worm infects yet another npm package

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

Cyber-Crime

# Shai-Hulud copycat worm infects yet another npm package

Plus three other stealers in three other packages, all from the same scumbag

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
mon 18 May 2026 // 23:07 UTC

A Shai-Hulud copycat has turned up in yet another npm package just five days after [TeamPCP open sourced the worm](https://www.theregister.com/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319) and announced a supply-chain attack competition on BreachForums.

The poisoned package, chalk-tempalte, masquerades as an extension for the popular JavaScript terminal string styling library Chalk. It now contains a clone of Shai-Hulud, which [TeamPCP](https://www.theregister.com/security/2026/04/11/two-different-attackers-poisoned-popular-open-source-tools/5221008) published last week on GitHub after [poisoning more than 170 npm package](https://research.jfrog.com/post/shai-hulud-here-we-go-again/)s with the credential-stealing malware as part of the [ongoing](https://www.theregister.com/cyber-crime/2026/05/12/cache-poisoning-caper-turns-tanstack-npm-packages-toxic/5238650) [supply chain attacks](https://www.theregister.com/security/2026/05/01/ongoing-supply-chain-attacks-worm-into-sap-npm-packages/5228837) targeting [open source dev tools](https://www.theregister.com/devops/2026/05/11/checkmarx-tackles-another-teampcp-intrusion-as-jenkins-plugin-sabotaged/5237780).

Plus, the same scumbag that uploaded the worm to chalk-tempalte also published three other malicious npm packages - @deadcode09284814/axios-util, axois-utils, and color-style-utils - containing infostealer code, according to Ox security researchers, which detected and reported the malware over the weekend.

REG AD

## MORE CONTEXT

* [### TanStack weighs invitation-only pull requests after supply chain attack](/security/2026/05/18/tanstack-weighs-invitation-only-pull-requests-after-supply-chain-attack/5241899)
* [### OpenAI caught in TanStack npm supply chain chaos after employee devices compromised](/security/2026/05/15/openai-caught-in-tanstack-npm-supply-chain-chaos-after-employee-devices-compromised/5241019)
* [### Malware crew TeamPCP open-sources its Shai-Hulud worm on GitHub](/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319)
* [### Checkmarx tackles another TeamPCP intrusion as Jenkins plugin sabotaged](/devops/2026/05/11/checkmarx-tackles-another-teampcp-intrusion-as-jenkins-plugin-sabotaged/5237780)

“The four malwares are inherently different, as the collected data varies between them, including exfiltrated IP addresses, cloud configurations, crypto wallets, environment variables, and even one malware turning the victim’s machine into a DDoS botnet – all from the same npm user,” researcher Moshe Siman Tov Bustan [wrote](https://www.ox.security/blog/new-actors-deploy-shai-hulud-clones-teampcp-copycats-are-here/) on Sunday.

REG AD

Anyone installing any version of the packages is affected, he added, noting the total number of weekly downloads is 2,678.

On Monday, the researchers told The Register that the npm user behind all four new stealer infections ran the supply-chain campaign from a home computer or local server farm. "The use of lhr.life is a clear indicator of a reverse proxy used to expose an internal network to the internet," they wrote in an email, adding that the miscreant(s) seem to be financially motivated as the code targets victims' cryptocurrency wallets and accounts.

Plus, the DDoS botnet component "could indicate affiliation with anarchy groups looking to take down infrastructure and services, or intent to sell it as DDoS-as-a-service," they added.

If you are running any of the four, immediately uninstall the malicious package and delete any related malicious configuration from IDEs and Claude Code or other coding agents. You should also rotate your keys on any affected machines, and check for GitHub repositories containing the string “A Mini Sha1-Hulud has Appeared,” the application security shop cautions.

The Shai-Hulud copycat, like the original worm, steals secrets, credentials, crypto wallets, accounts, and other sensitive data, and sends all of this to a remote command-and-control server: 87e0bbc636999b[.]lhr[.]life. It also uploaded the stolen credentials to a new GitHub repository.

The @deadcode09284814/axios-util malware collects and exfiltrates SSH keys, environment variables, and cloud credentials to 80[.]200[.]28[.]28:2222, and the color-style-utils stealer hoovers up IP addresses, IP geo-locations, and crypto wallets and sends them to edcf8b03c84634[.]lhr[.]life.

The fourth malicious npm package (axois-utils) calls its payload a “phantom bot.” The code is written in Go, an...