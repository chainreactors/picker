---
title: Using PhishingKit-Yara-Rules with ClamAV
url: https://stalkphish.com/2022/01/25/using-phishingkit-yara-rules-with-clamav/
source: Over Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:12.017254
---

# Using PhishingKit-Yara-Rules with ClamAV

[Skip to content](#main)

[![StalkPhish](/_astro/logo-black.CenBZhy0_18YWso.webp)](/)

[Platform](/products/)

* [StalkPhish.io platformDaily phishing & brand impersonation feed](/products/stalkphish-io/)
* [REST APIPlug our intelligence into your tools](/2025/11/05/stalkphish-io-advanced-phishing-detection-with-one-api/)
* [Web SearchFree lookup, no account required](https://www.stalkphish.io)

[Open Source](/community/)

* [PhishingKit-Yara-RulesYARA rules to identify phishing kits](/products/phishingkit-yara-rules/)
* [StalkPhish-OSSThe phishing kits stalker](/products/stalkphish/)
* [PhishingKitHunterFind kits using your own website files](/products/phishingkithunter/)
* [All projects on GitHub](https://github.com/t4d)

[Blog](/blog/)[Pricing](https://www.stalkphish.io/pricing/)[Docs](https://www.stalkphish.io/documentation/fullapi/)

[Company](/about/)

* [About](/about/)
* [In the News](/press-media/)
* [Contact](/contact/)
* [Legal notice](/legal-notice/)

[fr](/fr/?lang=fr "Version française") [Get API Access](https://www.stalkphish.io/accounts/register/)

[Platform](/products/)[StalkPhish.io platform](/products/stalkphish-io/)[REST API](/2025/11/05/stalkphish-io-advanced-phishing-detection-with-one-api/)[Web Search](https://www.stalkphish.io)

[Open Source](/community/)[PhishingKit-Yara-Rules](/products/phishingkit-yara-rules/)[StalkPhish-OSS](/products/stalkphish/)[PhishingKitHunter](/products/phishingkithunter/)[All projects on GitHub](https://github.com/t4d)

[Blog](/blog/)

[Pricing](https://www.stalkphish.io/pricing/)

[Docs](https://www.stalkphish.io/documentation/fullapi/)

[Company](/about/)[About](/about/)[In the News](/press-media/)[Contact](/contact/)[Legal notice](/legal-notice/)

[Get API Access →](https://www.stalkphish.io/accounts/register/)

[← Blog](/blog/)·25 January 2022·1 min read

# Using PhishingKit-Yara-Rules with ClamAV

[PhishingKit-Yara-Rules](/category/phishingkit-yara-rules/)[tool](/category/tool/)

![](/_astro/using_pk-yara-rules-with_clamav-1.Cbha9yKk_Z29CiQE.webp)

As a reminder, the PhishingKit-Yara-Rules project is a free and open source project which provides several dozen phishing kit detection rules contained in zip archives. You can find these rules on GitHub: <https://github.com/t4d/PhishingKit-Yara-Rules>

We have already covered the creation and use of Phishing Kit Yara rules in a previous post (see: <https://stalkphish.com/2021/08/17/using-phishing-kit-yara-rules-project-for-phishing-kits-detection-and-triage/>).

Specifically, these are rules intended for the detection and sorting of archives of phishing kits.

[![](/_astro/pkyara.CVbexl8o_Z16Wmpc.webp)](https://github.com/t4d/PhishingKit-Yara-Rules)

*PhishingKit-Yara-Rules project GitHub page*

We covered how to use the [PhishingKit-Yara-Search](https://github.com/t4d/PhishingKit-Yara-Search) project to use these rules, as well as VirusTotal’s use of these rules.

But do you know you can use these rules with ClamAV too?

---

Using PhishingKit-Yara-Rules with ClamAV

As many threat analysts, we often embed the free antivirus engine [ClamAV](https://www.clamav.net/) in our analysis stacks. First, because it’s always good to check files you are manipulating during a threat analysis, and because this antivirus is free (big thanks to the dev community!).

[![](https://www.clamav.net/assets/clamav-trademark.png)](https://www.clamav.net/assets/clamav-trademark.png)

Since the 0.99b (yes… it was 2015) you can use Yara rules to scan files in a directory, using the *`clamscan`* binary with ***`-d`*** argument, you force to use Yara rules as database.

First, you need to clone the rules repository:

***`$ git clone https://github.com/t4d/PhishingKit-Yara-Rules`***

Then you ‘just’ have to declare the directory of your Yara rules following the -d argument, then follow the directory you have to scan:

`$ clamscan -d /data/tools/yara-phishing/rules/ /tmp/Stalkphish_phishing-kits/`

The ***`clamscan`*** binary do what it have to do, and you just have to catch the report for the result:

![](/_astro/blog-yara-clamav-scan.CoXHALiI_Z1b4KHS.webp)

*ClamAV scan result with PhishingKit-Yara-Rules*

Yes, two lines of code, no more :)

---

Some last words, you can join the StalkPhish community on Keybase: <https://keybase.io/team/stalkphish> or our page on LinkedIn: <https://www.linkedin.com/company/stalkphish>

Enjoy!

[#phishing](/tag/phishing/)[#phishing kit](/tag/phishing-kit/)[#Stalkphish](/tag/stalkphish/)[#yara](/tag/yara/)

## Keep reading

![](/_astro/dhl_blog.Lih-WVZd_Z2nR4CP.webp)

14 November 2021· phishing

### [Several domain names, one protected redirector, one phishing campaign](/2021/11/14/several-domain-names-one-protected-redirector-one-phishing-campaign/)

Sometimes phishing campaigns are not conduced with phishing kits only, actors behind those phishing campaigns can use different tricks to prevent their work…

![](/_astro/phishing_kit_analysis-moha.BGztfM5g_Z1ted8O.webp)

4 February 2022· phishing

### [[Phishing kit] 'Moha' kit, targeting DEWA suppliers](/2022/02/04/phishing-kit-moha-kit-targeting-dewa-suppliers/)

At StalkPhish we like dissecting Phishing kits, first because we create Yara rules for detection, secondly because we must continually keep up to date with new…

## Phishing campaigns move fast. So should you.

Start with a free search, or talk to us about API access and custom intelligence for your brand.

[Try Web Search](https://www.stalkphish.io) [Contact us](/contact/)

![StalkPhish](/_astro/logo-white.Sf2bjwIL_c2FW8.webp)

Phishing, scam and brand impersonation detection, with the threat-actor intelligence behind it.

## Platform

* [StalkPhish.io platform](/products/stalkphish-io/)
* [REST API](/2025/11/05/stalkphish-io-advanced-phishing-detection-with-one-api/)
* [Web Search](https://www.stalkphish.io)
* [Pricing](https://www.stalkphish.io/pricing/)
* [Docs](https://www.stalkphish.io/documentation/fullapi/)

## Open Source

* [PhishingKit-Yara-Rules](/products/phishingkit-yara-rules/)
* [StalkPhish-OSS](/products/stalkphish/)
* [PhishingKitHunter](/products/phishingkithunter/)
* [All projects on GitHub](https://github.com/t4d)

## Company

* [About](/about/)
* [In the News](/press-media/)
* [Contact](/contact/)
* [Legal notice](/legal-notice/)
* [Blog](/blog/)
* [RSS feed](/rss.xml)

© 2026 StalkPhish. All rights reserved.

No tracking cookies.[Legal notice](/legal-notice/)