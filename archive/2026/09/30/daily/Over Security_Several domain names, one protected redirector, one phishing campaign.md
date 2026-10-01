---
title: Several domain names, one protected redirector, one phishing campaign
url: https://stalkphish.com/2021/11/14/several-domain-names-one-protected-redirector-one-phishing-campaign/
source: Over Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:11.566709
---

# Several domain names, one protected redirector, one phishing campaign

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

[← Blog](/blog/)·14 November 2021(updated 3 February 2022)·2 min read

# Several domain names, one protected redirector, one phishing campaign

[phishing](/category/phishing/)[phishing redirector](/category/phishing-redirector/)

![](/_astro/dhl_blog.Lih-WVZd_Z2nR4CP.webp)

Sometimes phishing campaigns are not conduced with phishing kits only, actors behind those phishing campaigns can use different tricks to prevent their work being takedown, as using protected web *redirectors*.

A campaign we can see this days use this redirector trick on several domain names. This campaign target DHL customers, impersonating the delivery company.

## A captcha protected redirector

More, the redirector is protected by a Google reCAPTCHA challenge:

![](/_astro/dhl_blog.Lih-WVZd_Z2nR4CP.webp)

*Google reCAPTCHA challenge*

Like this a scraper, a robot, can’t continue behind this page to get the final landing phishing page.

## **Downloading sources with StalkPhish**

With the help of [StalkPhish](https://github.com/t4d/StalkPhish), we can try to download the source code of pages if it is available somewhere, and *bingo!* we can find a zip file archive containing sources of this *tool*:

![](/_astro/zip_blog.BExLb5az_Z1K8C8j.webp)

*downloaded zip file content*

The *index.php* file call the *challenge.php* one which present the captcha challenge, once the captcha completed and validated the *zabk.php* page

![](/_astro/shot_blog.LHgGVOGz_Z1XiYVF.webp)

*index.php file calling challenge.php*

… is call which redirect the user to the landing page: hxxps://trakscloth.cc/manage/

![](/_astro/page_blog.SuRLcZB1_1fUOax.webp)

**zabk.php* file content*

…which is - surprise - the phishing kit landing page (page we can’t show you because the domain doesn’t work anymore).

## Pivoting on a string using StalkPhish

To have an idea of the *magnitude* of the campaign, you can use StalkPhish one more time to retrieve several informations about it, for that you can use the **-s** option of stalkphish with the name of the directory (*haktmcha*) the files are installed, as:

> > python3 StalkPhish.py -c conf/example.conf -s **haktmcha**

Then you can retrieve several domains and URLs where this redirector is, or was, installed:

![](/_astro/stalk_blog.B_VKUMfl_2sS35H.webp)

*StalkPhish’s database extract*

## Using online app StalkPhish.io to find threat

You can also use [StalkPhish.io](https://www.stalkphish.io) API to bust this threat. For that you just have to search for the exact same string (‘*haktmcha*’).

You need a API key for that, register for free there: <https://stalkphish.io/accounts/register/>

You can use this command to get data:

> > curl -H ‘authorization: Token *your\_API\_Token\_There*’ <https://stalkphish.io/api/v1/search/url/haktmcha>

As is you can obtain several URLs where the redirector kit has been deployed and have an idea of who and where this campaign was targeting:

![](/_astro/io_blog.DRdAl_Uz_3TmPg.webp)

*StalkPhish.io JSON data*

Thank you!

Keep in touch for a next blog post by registering on our mailing-list there: <https://stalkphish.com/contact/>

[#dhl](/tag/dhl/)[#Stalkphish](/tag/stalkphish/)

## Keep reading

![](/_astro/pkyara.CVbexl8o_Z16Wmpc.webp)

17 August 2021· phishing

### [[Use case] Using Phishing-Kit-Yara-Rules project for phishing kits detection and triage](/2021/08/17/using-phishing-kit-yara-rules-project-for-phishing-kits-detection-and-triage/)

Since some months now, we maintain specific Yara rules to detect phishing kit sources (.zip files). Phishing kits sources are sometimes left on the host…

![](/_astro/using_pk-yara-rules-with_clamav-1.Cbha9yKk_Z29CiQE.webp)

25 January 2022· PhishingKit-Yara-Rules

### [Using PhishingKit-Yara-Rules with ClamAV](/2022/01/25/using-phishingkit-yara-rules-with-clamav/)

As a reminder, the PhishingKit-Yara-Rules project is a free and open source project which provides several dozen phishing kit detection rules contained in zip…

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