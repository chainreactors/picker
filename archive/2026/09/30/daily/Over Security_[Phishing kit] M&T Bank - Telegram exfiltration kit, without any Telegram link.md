---
title: [Phishing kit] M&T Bank - Telegram exfiltration kit, without any Telegram link
url: https://stalkphish.com/2022/03/14/phishing-kit-mt-bank-telegram-exfiltration-kit-without-any-telegram-link/
source: Over Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:13.177953
---

# [Phishing kit] M&T Bank - Telegram exfiltration kit, without any Telegram link

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

[← Blog](/blog/)·14 March 2022(updated 15 March 2022)·3 min read

# [Phishing kit] M&T Bank - Telegram exfiltration kit, without any Telegram link

[phishing](/category/phishing/)[phishing kit](/category/phishing-kit/)[PhishingKit-Yara-Rules](/category/phishingkit-yara-rules/)[tool](/category/tool/)

![](/_astro/phishing_kit_analysis-mtbank_xx-3.vzNpu73E_1cBSR5.webp)

One of the latest kits downloaded by StalkPhish targets customers of the online bank M&T. It has a special feature that we wanted to share with you. We still [blogged about the use of Telegram by scammers](/2020/12/14/how-phishing-kits-use-telegram/), but this kit present an interesting new trick.

![](/_astro/etlgr4.CQZe0y-__Z1HKEyD.webp)

*M&T Bank ‘xx’ phishing kit front page*

## First observations

As many, the archive of this kit has been left on the server by the scammer. We named this kit ‘**xx**’ because the archive presents a *xx.php* file. This kit is only composed of 2 pages, a PHP file to process the collected data and an HTML file:

![](/_astro/etlgr5.CJn3PLTD_Z1Wr6Fl.webp)

*Phishing kit Zip archive content*

The HTML page has no specificities, the links to the original site are kept, as well as the images that are called from the original server, which makes it a particularly easy to detect phishing kit as long as the HTTP referers are monitored.

The collected data are then sent to the *xx.php* file:

![](/_astro/etlgr6.CjuhsYXi_2adFLV.webp)

*call to the *xx.php* script*

## Exfiltration script

The *xx.php* script looks similar to a lot of phishing kits, and more specifically to an existing M&T Bank NFL kit (see <https://github.com/t4d/PhishingKit-Yara-Rules/blob/master/PK_MTB_NFL.yar>):

![](/_astro/etlgr3.CenFFgrr_Z1AERfu.webp)

**xx.php file**

What is particularly interesting here is the email address.

## Using Telegram through email address

While many scammers usually use Gmail, Yandex, Yahoo, Protonmail, etc… email addresses, this actor uses an **etlgr.com** email address. This domain is used by a platform that offers to reroute data sent to an email address, to a Telegram bot:

![](/_astro/etlgr2.CveVULkS_Z1gnDiP.webp)

You just have to launch, in your Telegram app, a conversation with the proposed bot, to generate an email address:

![](/_astro/etlgr.DimCeFML_Z1r4LcP.webp)

*Screenshot from etlgr.com website*

Once the email address generated, the attacker can then declare it in the exfiltration script to send the stolen data, via email, to the Telegram bot.

## The bot, the service and the OpSec

The bot offers a help section with commands to configure the service and subscription, as you can see here:

![](/_astro/etlgr9.C6m8U5-Y_1TRzu8.webp)

*Bot help*

One of the most interesting command is the *subscription* one, command you can use to retrieve informations about your account… or the scammer one! This command generate a *subscription management* link to the subscription page which use your ID account.

![](/_astro/etlgr10.z2Ri7ch5_1Ui9S8.webp)

*Subscription command, with subscription management link*

Then you can modify the link using the *chat ID* (in email address, the ID before the @etlgr.com) to have access to scammer’s informations:

![](/_astro/etlgr11.C-1Q0lXS_4Lh4C.webp)

*Scammer’s informations on the subscription page*

We can observe several things here:

* the scammer purchased a one year subscription, which will expires on 2022-11-17
* you can pay using Bitcoin
* you can find a link to the subscriber Telegram profile page:

![](/_astro/etlgr8.Cubj2rm-_HYHGv.webp)

*Scammer’s Telegram profile*

Then you can now continue your investigations on the scammer if you want to go further, but this is not the purpose of this post.

## Search and destroy

In order to search for this type of kit you can use the StalkPhish.io API using the *URL search* and containing the string “*Hajjjerr.htm*” or “*mbankss*” (you can register on stalkphish.io for free here: [https://stalkphish.io](https://stalkphish.io/)), then you will retrieve a list of URLs where those phishing kit was installed:

> $ curl -H “authorization: Token YOUR\_STALKPHISH.IO\_API\_TOKEN” [https://api.stalkphish.io/api/v1/search/url/Hajjjjerr.htm|jq](https://api.stalkphish.io/api/v1/search/url/Hajjjjerr.htm%7Cjq)

![](/_astro/etlgr12.CxUggg17_Z1W8duh.webp)

*Stalkphish.io API extraction*

Then you can start your takeover campaign!

## **IOCs**

Kit’s zip file hash {SHA256}:
f43a06a42b87920c300929003787fc3c6a3b7f0fb7f0f97726c9f2f3f8c0dd80

Contact e-mail:
‘784320094\\@etlgr[.]com’

Associated scammer infos:
‘Don Dari’, ‘\\@dondarigh’, https[:]//t.me/dondarigh

PhishingKit Yara Rule:
[PK\_MTB\_xx.yar](https://github.com/t4d/PhishingKit-Yara-Rules/blob/master/PK_MTB_xx.yar)

[#analysis](/tag/analysis/)[#Stalkphish](/tag/stalkphish/)[#telegram](/tag/telegram/)

## Keep reading

![](/_astro/phishing_kit_analysis-moha.BGztfM5g_Z1ted8O.webp)

4 February 2022· phishing

### [[Phishing kit] 'Moha' kit, targeting DEWA suppliers](/2022/02/04/phishing-kit-moha-kit-targeting-dewa-suppliers/)

At StalkPhish we like dissecting Phishing kits, first because we create Yara rules for detection, secondly because we must continually keep up to date with new…

![](/_astro/threat_intel-stalkphish_intelowl-2.ajU93v9P_Z2qEgAV.webp)

4 April 2022· CERT

### [[Threat intelligence] Using StalkPhish.io with Intel Owl to speed up threat analysis](/2022/04/04/threat-intelligence-using-stalkphish-io-with-intelowl-to-speed-up-threat-analysis/)

Using StalkPhish.io analyzer as a threat intelligence feed for IntelOwl to speed up your threat analysis.

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
* [Docs](http...