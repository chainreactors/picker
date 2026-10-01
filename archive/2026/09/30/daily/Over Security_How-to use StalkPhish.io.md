---
title: How-to use StalkPhish.io
url: https://stalkphish.com/2021/06/30/howto-stalkphish-io/
source: Over Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:10.411231
---

# How-to use StalkPhish.io

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

[← Blog](/blog/)·30 June 2021(updated 29 November 2021)·2 min read

# How-to use StalkPhish.io

[phishing](/category/phishing/)[phishing kit](/category/phishing-kit/)[tool](/category/tool/)

![](/_astro/stalkphishio-front-1946811513-e1708424431522.BUtRPza2_ZujiCE.webp)

## What is the purpose of StalkPhish.io?

[StalkPhish.io](https://www.stalkphish.io) is a SaaS application which provides enriched data about potential phishing URL or brand impersonation use, with a REST API.
StalkPhish.io is based on an open source software (OSS), called [StalkPhish](/products/stalkphish/), created by the founder of StalkPhish. This version of StalkPhish is an augmented one (more enrichment, more data sources), you don’t need to deploy and maintain a StalkPhish OSS tenant, we do it for you. Then you can easily use the StalkPhish.io REST API to retrieve data you need.

---

## Register on StalkPhish.io

As we deliver an API key, you need to register - for free - on StalkPhish.io, as is you can manage your informations and API key.
To register on StalkPhish.io click on the ‘Register’ button on the top right of your window:

![](/_astro/sp-doc-reg-button.lDW_mPfp_1e9MEs.webp)

Then Fill in the requested informations before fill up the captcha. Use a **valid e-mail address** because you will have to validate your registering request:

![](/_astro/register-infos.B5biAo_Z_ZOor13.webp)

Once it is done, you will receive the validation link on the e-mail address you use to register, click on it, your account is now created and ready to use. You can now use the login form to log-in and have access to your account informations:

![](/_astro/user_account.DMTI4p69_10usQM.webp)

You now have access to your API key, key you need to use the StalkPhish.io’s REST API (Note that you can renew this key for a reason or another).

![](/_astro/account_infos.BUBtb2i8_1WbaoM.webp)

Once you registered, you can now start using our plateform… Welcome! :)

---

## Using StalkPhish.io REST API

A Free subscribed plan (the default plan) let you access those REST API functions:
**/api/v1/me** : Return informations about account linked to API key.
**/api/v1/last** : Return n last results, with n depending on your subscription.
\*\*/api/v1/search/\*\****url*** : Return results of string search appearing in a URL
\*\*/api/v1/search/\*\****title*** : Return results of string search appearing in a website title.
\*\*/api/v1/search/\*\****ipv4*** : Return results of IPv4 search.

You can use this REST API with the tool of your choice, like:

**cURL**: curl *-H “authorization:Token 96880783bf1ca220b2991be15252bbaeb026fbcf”* [https://api.stalkphish.io​/api/v1/\*me](https://api.stalkphish.io%E2%80%8B/api/v1/%2Ame)\*

**Wget**: *wget -qO- –header “authorization:Token 96880783bf1ca220b2991be15252bbaeb026fbcf”* [https://api.stalkphish.io​/api/v1/\*me](https://api.stalkphish.io%E2%80%8B/api/v1/%2Ame)\*

**Python requests**: my\_headers = {“Authorization” : “Token 96880783bf1ca220b2991be15252bbaeb026fbcf”}
response = requests.get(“[https://api.stalkphish.io​/api/v1/me](https://api.stalkphish.io%E2%80%8B/api/v1/me)”, headers=my\_headers)

You can first test your access using **/api/v1/me** to retrieve your account informations:

![](/_astro/api_me.bdAnh8Jp_1Lrodp.webp)

Then you can start grabbing informations you need from StalkPhish.io’s data.
We advise you to be as specific as possible on the string you look for, for example, if you look for a specific phishing kit, you can use a URL search with a specific name or directory file appearing into the phishing kit:

![](/_astro/api_url.D-Sg2l37_Z1dMxCR.webp)

And so on…

Enjoy! :)

[#Cybersecurity](/tag/cybersecurity/)[#Stalkphish](/tag/stalkphish/)

## Keep reading

![](/_astro/api.CpHi5lTg_SBvlk.webp)

22 April 2021· phishing

### [[Phishing kit] Scammer vs Scammer - backdoored phishing kit](/2021/04/22/scammer_vs_scammer_backdoored_phishing_kit/)

Scammer world should be a hard thug life. A merciless world... with no pity... Some scammers try to steal other ones! What a shameless! During our researches we found one of those 'backdoored' phishing kit, let's have a fast dive into it.

![](/_astro/pkyara.CVbexl8o_Z16Wmpc.webp)

17 August 2021· phishing

### [[Use case] Using Phishing-Kit-Yara-Rules project for phishing kits detection and triage](/2021/08/17/using-phishing-kit-yara-rules-project-for-phishing-kits-detection-and-triage/)

Since some months now, we maintain specific Yara rules to detect phishing kit sources (.zip files). Phishing kits sources are sometimes left on the host…

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