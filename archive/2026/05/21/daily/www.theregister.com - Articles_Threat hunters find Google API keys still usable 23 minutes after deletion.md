---
title: Threat hunters find Google API keys still usable 23 minutes after deletion
url: https://www.theregister.com/devops/2026/05/21/threat-hunters-find-google-api-keys-still-usable-23-minutes-after-deletion/5244504
source: www.theregister.com - Articles
date: 2026-05-21
fetch_date: 2026-05-22T06:08:45.319686
---

# Threat hunters find Google API keys still usable 23 minutes after deletion

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

DevOps

# Threat hunters find Google API keys still usable 23 minutes after deletion

Plenty of time for bad actors to grab data or hit you with a giant bill

O'Ryan Johnson
[O'Ryan
Johnson](https://www.theregister.com/author/oryan-johnson)

Published
thu 21 May 2026 // 21:23 UTC

You know your Google API key has leaked so you rush to disable it before bad actors can start running up charges on your account. Bad news: According to [security researchers](https://www.aikido.dev/blog/google-api-keys-deletion) at Aikido, people can use the API keys for up to 23 minutes after a user deletes them, creating a window of opportunity that, when combined with Google’s automatic billing tier upgrades, can devastate victims.

“We've identified a substantial window where an attacker with access to a leaked Google API key can continue to misuse that credential, after the user believes the key is revoked,” Joseph Leon, a security researcher with Aikido, told The Register. “In that window, an attacker could run up charges, pull sensitive files uploaded to Gemini, and exfiltrate cached context.”

Aikido tested the gap during 10 trials over two days. In each trial, researchers created an API key, deleted it, and then sent three to five authenticated requests per second until no valid response came back for several minutes.

REG AD

From the time a user deletes the Google API key to when it can no longer be used propagates gradually across Google's infrastructure, he said. Some servers reject the key within seconds while others keep accepting it for 23 minutes.

REG AD

What this means is that an attacker holding a deleted key can repeatedly send requests until one reaches a server that has not caught up, Leon said. If Gemini is enabled on the project, they can dump files that were uploaded and exfiltrate cached conversations.

The paper cited a similar problem researchers disclosed in December involving [AWS keys](https://www.offensai.com/blog/aws-iam-eventual-consistency-persistence). In that case, after deletion, attackers had a four-second window to exploit, and researchers showed how they could create new credentials in that time.

“Four seconds was enough to matter on AWS,” Leon wrote in the paper. “Given recent attention to Google API keys [used to access Gemini](https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules), we set out to measure how long Google's API key revocation window remains open.”

### Flaws can hit devs with huge surprise bills

The Register has reported [numerous cases of Google](https://www.theregister.com/ai-ml/2026/05/13/google-users-fight-for-refunds-as-unauthorized-api-usage-bills-soar/5239160) API key abuse in which developers are suddenly hit with five figure bills after their credentials are compromised.

The problem was compounded in April after Google reworked its billing policy to include spending tiers for users. While developers initially thought of it as a way to limit costs, Google automatically upgrades that spending tier to the next highest level without their knowledge.

For users who have been working with Google for more than 30 days and have spent more than $1,000 over the lifetime of the account, their cap can be increased from $250 to $100,000 if their usage spikes – a windfall for crooks if the credentials fall into the wrong hands.

Developers whose Google API keys were stolen told The Register that their bills rocketed up to five figures minutes after their credentials were stolen, as bad actors loaded up on Google’s Gemini models such as Nano Banana and its video production model Veo 3.

REG AD

Google [issued refunds in the three instances](https://www.theregister.com/devops/2026/05/15/google-reimburses-register-sources-who-were-victims-of-api-fraud/5241429) that The Register brought to its attention, returning $154,000 to those developers.

The victims told The Register that, during the attack, they were frantically trying to shut down the spending and turn off access to their projects even as costs climbed by thousands of dollars. Leon said in cases where a Google developer tries to shut off access to their account, deleting the API key will still give crooks time to inflict damage.

“It's hard to put a dollar figure on it,” Leon told us. “The window averaged 16 minutes in our testing and stretched to nearly 23 at the worst. During that window, the success rate is wildly unpredictable. We saw minutes where over 90% of requests still authenticated, and others where fewer than 1% did. An attacker who knows this can send requests at high volume to maximize their odds of hitting a server that hasn't caught up. For Google API keys with Gemini access, the damage isn't just a compute bill. It's the files and cached context an attacker can exfi...