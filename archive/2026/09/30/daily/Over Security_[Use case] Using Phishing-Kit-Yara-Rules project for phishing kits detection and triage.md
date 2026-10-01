---
title: [Use case] Using Phishing-Kit-Yara-Rules project for phishing kits detection and triage
url: https://stalkphish.com/2021/08/17/using-phishing-kit-yara-rules-project-for-phishing-kits-detection-and-triage/
source: Over Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:10.990012
---

# [Use case] Using Phishing-Kit-Yara-Rules project for phishing kits detection and triage

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

[← Blog](/blog/)·17 August 2021(updated 7 April 2025)·2 min read

# [Use case] Using Phishing-Kit-Yara-Rules project for phishing kits detection and triage

[phishing](/category/phishing/)[phishing kit](/category/phishing-kit/)[PhishingKit-Yara-Rules](/category/phishingkit-yara-rules/)

![](/_astro/pkyara.CVbexl8o_Z16Wmpc.webp)

Since some months now, we maintain specific Yara rules to detect phishing kit sources (.zip files). Phishing kits sources are sometimes left on the host serving phishing pages.

Using the StalkPhish project (see <https://stalkphish.com/products/stalkphish/>) we used to collect phishing kits in order to extract e-mails addresses, Telegram channels (see <https://stalkphish.com/2020/12/14/how-phishing-kits-use-telegram/>), and so on.

In order to sort our zip files collection we use our phishing kit Yara rules (see <https://stalkphish.com/products/phishingkit-yara-rules/>).

## **About these Yara rules**

Today the repository count 211 Yara rules for several threats and brands, all these rules are free of use and are published under the GNU GPLv3 licence.

You can find these rules on GitHub: <https://github.com/t4d/PhishingKit-Yara-Rules>

For rule analysis we use the VirusTotal YARA-CI plugin on the GitHub repository, this permit to control if rules are correct and don’t contain mistakes before being used.

These rules are created using phishing kit sources we grab every day and are named with the brand name and a actor/team name we can obtain from the sources:

![](/_astro/pkrule.oCkcI545_Z2apQfj.webp)

*A phishing kit Yara rules*

These rules go to parse the Zip file to find specific names of files and directories, in the example above, all specified files and directories must exist for the file to be considered as matching the Yara rule.

Of course you can participate to the project, creating your own Yara rule and making a pull request on the repository. Please try to respect the contribution rules, you can find here: <https://github.com/t4d/PhishingKit-Yara-Rules/blob/master/CONTRIBUTING.md>

## **Using phishing kit Yara rules**

Using official yara binary (apt install yara, for example), you can use each phishing kit Yara rule on your file/directory, like this:

$ yara PK\_impots\_gouv\_fr\_azubi.yar /data/dl
`PK_impots_gouv_fr_azubi /data/dl/http__pqok.justns.ru_information.zip PK_impots_gouv_fr_azubi /data/dl/https__adorid.com_hih_Impots20.zip PK_impots_gouv_fr_azubi /data/dl/http__hosting2078368.online.pro_Impots.zip [...]`

You can create a unique .yar file with all phishing kit Yara rules inside and use it in the same command. By default Yara can’t use a directory containing .yar files as an argument.

Also you can use the python tool we called *PhishingKit-Yara-Search* made to use a directory containing all the rules as a argument: <https://github.com/t4d/PhishingKit-Yara-Search>

You can use it to scan 1 file with all yourYara rules:

`$ /data/tools/yara-phishing/PhishingKit-Yara-Search-0.3.py -f /tmp/http__eeomsomdinbf.com__amaz.zip -r /data/tools/yara-phishing/rules/`

![](/_astro/yarav3.Dxi-2HMd_ZC6eoW.webp)

*Scan 1 file with all your Yara rules*

Or use all your Yara rules to fully scan a directory:

`$ /data/tools/yara-phishing/PhishingKit-Yara-Search-0.3.py -D /tmp/ -r /data/tools/yara-phishing/rules/`

![](/_astro/yarav32.BqXvHi_8_2hKrM4.webp)

*Scan all files of a directory with all your Yara rules*

## **VirusTotal**

Since some months now these Yara rules from our project are implemented in [VirusTotal](https://www.virustotal.com)’s analysis. Dropping a file to VT for analysis will, if a PhishingKit Yara rule exists, give you this information as *crowdsourced YARA Rules* into the *detection* section (you have to be logged in to see this part):

![](/_astro/vtyara.x1bH_OfS_Ohas9.webp)

*VirusTotal using Phishing-Kit-Yara-Rules project for analysis*

You can check the matching rule for further details:

![](/_astro/vtyara2.EJpBJLew_4EVBb.webp)

*Yara rule details*

## Keep in touch

For all our news about these rules our other projects you can follow us on [Twitter](https://twitter.com/Stalkphish_io) or our [blog](/blog-feed/)! As we told you above: don’t hesitate to particpate to this open source project, you know, to make Internet a safer place :)

![](/_astro/yaranews.Dp6dkOlO_1nPYdQ.webp)

[#PhishingKit-Yara-Search](/tag/phishingkit-yara-search/)[#python](/tag/python/)[#Stalkphish](/tag/stalkphish/)[#tool](/tag/tool/)[#virustotal](/tag/virustotal/)[#yara](/tag/yara/)

## Keep reading

![](/_astro/stalkphishio-front-1946811513-e1708424431522.BUtRPza2_ZujiCE.webp)

30 June 2021· phishing

### [How-to use StalkPhish.io](/2021/06/30/howto-stalkphish-io/)

StalkPhish.io is a SaaS application which provides enriched data about potential phishing URL or brand impersonation use, with a REST API.

![](/_astro/dhl_blog.Lih-WVZd_Z2nR4CP.webp)

14 November 2021· phishing

### [Several domain names, one protected redirector, one phishing campaign](/2021/11/14/several-domain-names-one-protected-redirector-one-phishing-campaign/)

Sometimes phishing campaigns are not conduced with phishing kits only, actors behind those phishing campaigns can use different tricks to prevent their work…

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
* [Legal n...