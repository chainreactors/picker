---
title: [Phishing kit] 'Moha' kit, targeting DEWA suppliers
url: https://stalkphish.com/2022/02/04/phishing-kit-moha-kit-targeting-dewa-suppliers/
source: Over Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:12.597972
---

# [Phishing kit] 'Moha' kit, targeting DEWA suppliers

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

[← Blog](/blog/)·4 February 2022·4 min read

# [Phishing kit] 'Moha' kit, targeting DEWA suppliers

[phishing](/category/phishing/)[phishing kit](/category/phishing-kit/)[PhishingKit-Yara-Rules](/category/phishingkit-yara-rules/)

![](/_astro/phishing_kit_analysis-moha.BGztfM5g_Z1ted8O.webp)

At StalkPhish we like dissecting Phishing kits, first because we create [Yara rules](/products/phishingkit-yara-rules/) for detection, secondly because we must continually keep up to date with new developments in terms of phishing kits, finally because we like to pass on to the general public knowledge about this type of threat.

The phishing kit we go to analyze this time is a kit targeting Dubai Electricity and Water Authority suppliers:

![](/_astro/moha1.CYyMolDv_BhHBQ.webp)

*Moha kit targeting DEWA suppliers*

The kit Zip archive was left on the server by the scammer. We named this kit ‘**Moha**’ from the name of his potential developer (*Moha404*), even if some pages are taken from other kits:

![](/_astro/moha3.CJ7lmcoA_ZM5IF9.webp)

## First observations

The code is pretty big for a phishing kit with 1.2MB size.
What we can observe first it is the fact that all the files necessary for the good functioning of the kit are embedded in the kit.
This excludes any detection by the target’s infrastructure using HTTP referers for example.
All files are embedded in the kit, but this kit uses Google analytics to retrieve data about connections, after verification, it seems the Google analytics tracker ID is the same than the legitimate one, from the real DEWA website.

![](/_astro/moha2.DJu89z02_Z2v6aDk.webp)

*Google analytics HTTP POST*

We can observe that all connections to the phishing site are also logged into a HTML file (*visit.html)* with a little bit of enrichment as the IP address of the visitor device and its geographic location:

![](/_astro/moha4.BaDyvghQ_Z2oARJS.webp)

*visits logged into visit.html*

Then the scammer can easily retrieve data through his browser (note that API keys are not configured, so it does not work as expected in this case, particularly the geographical data):

![](/_astro/moha5.CTHhZ0fw_1wFSDq.webp)

*visits logs*

As many times, the purpose of this kit is to… steal credit cards data…

![](/_astro/moha6.Q1hr4m7s_1D631V.webp)

*Credit card data gathering*

… as the victim’s email address and password, twice, to be sure it is not fake data:

![](/_astro/moha7.hw7wqb0O_26EDWn.webp)

*Email data gathering*

Then it will politely thank you before redirecting the victim on the legitimate DEWA website:

![](/_astro/moha8.CubXIOdn_Z24dV3d.webp)

## **Bots and crawlers filtering tricks**

As many phishing kits, this one embed filtering functions to prevent crawlers and bots to gather data, this kit contains a bunch of functions and files dedicated to this purpose.

The “locker” directory contains all files needed to filter some access:

![](/_astro/moha9.CwGI9243_2u2hTL.webp)

*Files dedicated to access filtering*

Several tricks are used there:

* a *.htaccess* file containing *RewriteRule*s and deny filters
* a *robots.txt* file which disallow search engines indexing
* several files filtering strings contained in HTTP User-Agent
* several files filtering IP addresses
* calls to online IP address whois platforms
* implementation of an OSS crawler detection tool (<https://github.com/JayBizzle/Crawler-Detect>)

Once detected, the connection considered as a bot connection is write into a *bots.txt* file and a HTTP 404 Not Found error message is sent to this bot:

![](/_astro/moha10.B1QoguQQ_Z1ACgPY.webp)

*HTTP 404 error message*

Then the crawler is prompt for a redirect to a random site appearing in a list (*sites.txt*):

![](/_astro/moha11.Ce7lyHOY_15I6u4.webp)

*a small part of sites.txt file*

## **Phishing kit configuration**

Phishing kits often present several vectors for exfiltrating stolen data and configuration files are there in order to indicate where to send the stolen data.

This kit uses 2 ways for exfiltration, first by e-mail and the second one uses Telegram (you can check our [dedicated blog post](/2020/12/14/how-phishing-kits-use-telegram/) about Telegram use by phishing kits):

![](/_astro/moha12-1.CNfHqd7__Z1YYLTC.webp)

*hamza.php*

Configured variables are then used for exfiltration:

![](/_astro/moha16.BCjuRroQ_hNV80.webp)

*E-mail and Telegram exfiltration code*

There is also a specific configuration file allowing to store, even to exfiltrate, the data in an obfuscated way, but again this functionality is badly implemented and it does not work:

![](/_astro/moha14-1.CtYs8raI_Z1OyLHX.webp)

*proxy.ini file*

![](/_astro/moha13-1.DOjKyfj6_ItC8i.webp)

*data obfuscation code*

## **Affiliated kits**

By observing the source code of this kit, we see several strings appearing which do not relate to the rest of the code, this means that, as in many other phishing kits, pieces have been extracted from other already existing kits.

![](/_astro/moha15.bdX31C0-_O0k8E.webp)

*From proxyblock.php*

We can find this string (‘*scampage by devilscream*’) in others kit’s source code, as a Apple 16shop kit:

![](/_astro/moha17.B5aic6mE_2gHoVO.webp)

## **Detection**

As seen before, the Google analytics tracker ID was left into the index page by the phishing kit creator, this should be a good start for investigating where this kit was deployed.

There is also several online tools you can use for detection, we use [StalkPhish.io](https://www.stalkphish.io) API to monitor particular strings and brand names that may appear in domain names or URIs used by phishing kits:

![](/_astro/moha18-1.CgHFeXdj_1OERsk.webp)

*Stalkphish.io API extraction*

For the phishing kit zip file detection and triage you can use our dedicated Yara rule we published on our GitHub repository: <https://github.com/t4d/PhishingKit-Yara-Rules/blob/master/PK_DEWA_moha.yar>

![](/_astro/moha19.xU5B32WF_Z1wWI6J.webp)

*Phishing kit Yara rule*

## **IOCs**

Kit’s zip file hash {SHA256}:
f15264cc66c82fcc71642cc3cf7b9347072ad6617352e1937f6a174d8681c744

Exfiltration e-mail:
‘pegasiss8\\@yandex[.]com’

## Thank you

Of course we contacted the company to provide them with all the information we have ...