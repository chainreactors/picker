---
title: [Phishing kit] Scammer vs Scammer - backdoored phishing kit
url: https://stalkphish.com/2021/04/22/scammer_vs_scammer_backdoored_phishing_kit/
source: Over Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:09.839830
---

# [Phishing kit] Scammer vs Scammer - backdoored phishing kit

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

[← Blog](/blog/)·22 April 2021(updated 14 October 2022)·2 min read

# [Phishing kit] Scammer vs Scammer - backdoored phishing kit

[phishing](/category/phishing/)[phishing kit](/category/phishing-kit/)[Stalkphish](/category/stalkphish/)

![](/_astro/api.CpHi5lTg_SBvlk.webp)

Scammer world should be a hard *thug* life. A merciless world… with no pity… Some scammers try to steal other ones! What a shameless! During our researches we found one of those ‘backdoored’ phishing kit, let’s have a fast dive into it.

As usual our [StalkPhish](https://github.com/t4d/StalkPhish) instance found some kits we check sometimes. This one is a XBalti one which target Chase. Nothing unusual - XBalti phishing kits are quite common unfortunately - until we check a little bit more into the code.

![](/_astro/chase.bQ4rp0H4_1QWzHH.webp)

*This kit was placed into a hacked server, server which is not very well secured, not secured because scammers took it and because the Apache service allow the OpenDir function, as you can see:*

![](/_astro/opendir.Bg-Nn6Xy_ZdbM7y.webp)

What we checked is ***XB4LTIV5.zip*** file (ok, there is a Spox one too, but one thing at a time), which looks like this when you uncompress the zip file:

![](/_astro/zip.WumRp7y5_ZN4vvx.webp)

This zip file contains the Chase phishing kit uncompressed into the *en/* directory, whith a XBalti v3 admin panel:

![](/_astro/admin2.ByM_TfjS_Z1KzO93.webp)

But what we found the most interesting into this kit is the use of an *obfuscated* part of the code, contained into the ***api.php*** file:

![](/_astro/api.CpHi5lTg_SBvlk.webp)

It is a very light code obfuscation as you can see, because it is base64 encoded in fact… Anyway there is no use of such encoding in other files so why is it there? Let’s check what’s inside:

![](/_astro/api_desob.CtfGNpDw_1gSTQy.webp)

Seen? Yeah, you got it! There is another exfiltration channel, using the Telegram API (check this [blog post](/2020/12/14/how-phishing-kits-use-telegram/) to know more about use of Telegram in phishing kits) to send data, as this file (***api.php***) is loaded into the ***send.php*** file to double send the stolen credentials:

![](/_astro/loaded_api2.C-dKTPnd_1NlsN.webp)

Now, how this backdoor came into this phishing kit zip file? Does the code has been re-write using webshell by another actor? Yes, because there is webshell deployed on this box (the ***hassan1.php*** we saw before on the opendir screen capture):

![](/_astro/anon_shell.BOmms5Hg_2i63Qx.webp)

But, wait, it’s password protected! No problem, another actor deployed another webshell without any protection…

![](/_astro/webshell2.DvIMF-Z6_24iekS.webp)

¯\_ (ツ)\_/¯

Anyway, because the backdoor is contained into the zip file, we can think that this kit is ‘armed’ as it is.

Well, it seems that the scammer world is a hard world as we saw, backdoored phishing kits is legion, and scammer’s world is sometimes offended with this, as we can read here and there into scammers forums:

![](/_astro/forum.CmwQHrs8_2qShPj.webp)

Hard times we are living…

[#backdoor](/tag/backdoor/)[#scammer](/tag/scammer/)[#xbalti](/tag/xbalti/)

## Keep reading

![](/_astro/fb_viet.C8V718uo_Z1cDClk.webp)

9 April 2021· phishing

### [Phishing kit using Google sheet to exfiltrate stolen data](/2021/04/09/phishing-kit-using-google-sheet-to-exfiltrate-stolen-data/)

Analysis of a Facebook phishing kit which exfiltrate stolen data to an online Google Sheet using ajax POST method.

![](/_astro/stalkphishio-front-1946811513-e1708424431522.BUtRPza2_ZujiCE.webp)

30 June 2021· phishing

### [How-to use StalkPhish.io](/2021/06/30/howto-stalkphish-io/)

StalkPhish.io is a SaaS application which provides enriched data about potential phishing URL or brand impersonation use, with a REST API.

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