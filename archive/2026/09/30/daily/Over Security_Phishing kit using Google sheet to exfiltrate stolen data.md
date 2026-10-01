---
title: Phishing kit using Google sheet to exfiltrate stolen data
url: https://stalkphish.com/2021/04/09/phishing-kit-using-google-sheet-to-exfiltrate-stolen-data/
source: Over Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:09.245814
---

# Phishing kit using Google sheet to exfiltrate stolen data

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

[← Blog](/blog/)·9 April 2021·1 min read

# Phishing kit using Google sheet to exfiltrate stolen data

[phishing](/category/phishing/)[phishing kit](/category/phishing-kit/)[PhishingKit-Yara-Rules](/category/phishingkit-yara-rules/)[Stalkphish](/category/stalkphish/)

![](/_astro/fb_viet.C8V718uo_Z1cDClk.webp)

As we operate a [StalkPhish](https://github.com/t4d/StalkPhish) instance which scan thousands suspicious links a day, we often find, let’s say *originals*, phishing kits to analyse. Today we found a phishing kit targeting vietnamese Facebook users:

![](/_astro/fb_viet.C8V718uo_Z1cDClk.webp)

**vietnamese Facebook phishing page**

We retrieved the source code as the zip file was still on the server. The phishing kit sources zip file contains only a page, some images and CSS, and a javascript function:

![Phishing kit zip file sources](/_astro/fb_viet-kit_zip.lUVv-2Zo_ZH6uhe.webp)

There is no e-mail exfiltration vector as we can see commonly: this kit uses Google sheet form ajax post function to exfiltrate stolen credentials!

Reading the HTML file source code, we can see the page grab the victim’s IP address, Domain, date:

![](/_astro/fb_viet-source_ip.BgznrD_A_ZJj5zN.webp)

As well as the identifiers entered by users:

![](/_astro/fb_viet-src_index.Cv6OOT3D_ZwnGcj.webp)

Then the *validation-function.js* is called. This Javascript function, after data validation and serialization, go to send stolen data to a Google sheet, via a POST method, using it as a database:

![](/_astro/fb_viet-post.DYJyj_e1_Z1FfouX.webp)

![kit JS function](/_astro/fb_viet-kit_fct.Ce7i017n_ZQ2Mqf.webp)

This function uses [Google Apps Script](https://developers.google.com/apps-script/reference/spreadsheet) function which permit to write into Google sheet using the API!

## **Take aways**

index.html (SHA256): *3cfd92bdd9a801382199a52624ecaa8b78a32dc80893f0a6186cce4128c6552b*

phishing kit archive (SHA256): *34ee59548f8ba626568d91393acb76791a559f958c1f61bf5dabeb425e396640*

Phishing Kit Yara Rule: <https://github.com/t4d/PhishingKit-Yara-Rules/blob/master/PK_Facebook_GSheet.yar>

[#facebook](/tag/facebook/)

## Keep reading

![](/_astro/bot1.QE2YtVjx_20Ngzg.webp)

14 December 2020· phishing

### [How phishing kits uses Telegram](/2020/12/14/how-phishing-kits-use-telegram/)

More and more actors uses Telegram chat groups to exfiltrate harvested data, we'll show you how we can collect informations about those actors. Let’s have a dive into one of this kits.

![](/_astro/api.CpHi5lTg_SBvlk.webp)

22 April 2021· phishing

### [[Phishing kit] Scammer vs Scammer - backdoored phishing kit](/2021/04/22/scammer_vs_scammer_backdoored_phishing_kit/)

Scammer world should be a hard thug life. A merciless world... with no pity... Some scammers try to steal other ones! What a shameless! During our researches we found one of those 'backdoored' phishing kit, let's have a fast dive into it.

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