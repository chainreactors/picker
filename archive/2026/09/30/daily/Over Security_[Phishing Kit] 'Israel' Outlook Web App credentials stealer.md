---
title: [Phishing Kit] 'Israel' Outlook Web App credentials stealer
url: https://stalkphish.com/2019/12/06/israel-outlook-credentials-harvester/
source: Over Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:08.216109
---

# [Phishing Kit] 'Israel' Outlook Web App credentials stealer

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

[← Blog](/blog/)·6 December 2019(updated 24 March 2021)·2 min read

# [Phishing Kit] 'Israel' Outlook Web App credentials stealer

[phishing](/category/phishing/)[phishing kit](/category/phishing-kit/)

![](/_astro/israel3.CujJiqJP_Z2lca5m.webp)

***This morning my StalkPhish instance downloaded a new kit I never seen before. First look, it seems to be a phishing kit impersonating a professional Outlook login pattern which ( try to ) exfiltrate credentials on an online portal.***

The source kit, harvested by [StalkPhi](https://github.com/t4d/StalkPhish)[sh](https://github.com/t4d/StalkPhish), once unzipped, just contains 2 files:

`$ ls -Ggh Israel/ -rw-r--r-- 1 3,9K déc. 3 03:29 ss.html -rw-r--r-- 1 2,2K déc. 3 03:25 success.html`

![](/_astro/israel3.CujJiqJP_Z2lca5m.webp)

*DirListing-like on 000webhostapp*

![](/_astro/israel4.DM-wfn53_Zz1v4R.webp)

*Package creation date seems to be *Nov 08 2019**

The package seems to have been created on ***November 08 2019 10:01:09 am*** and deployed on ***December 03 2019 02:30 am*** (local server timezone).

Deployed, the phishing kit looks like this:

![](/_astro/israel.ByFhzMka_IRXsz.webp)

*Israel/ss.html*

The message talk about a ‘webmail database’ and en join the user to validate her/his e-mail if she/he don’t want to be deleted from a ‘database’. As you can see, the form Domain/Username looks like a Microsoft/AD field.

Once credentials confirmed, they are POST on [Formbuddy.com](http://www.formbuddy.com/) which propose to store data exfiltrated from your website forms.

![](/_astro/israel5.Bf8BghVq_ZHA5NF.webp)

*credentials HTTP POST on Formbuddy.com*

Unfortunatly for the scammer (!!!), Formbuddy seems to have tagged the referer as a phishing site:

![](/_astro/israel2.DyEEwwWf_Z1ACVJY.webp)

*Result of exfiltration try*

But, seen the HTTP POST request, in fact the request is not conform to the script use manual, and this exfiltration can not work!

![](/_astro/israel6.CUbC8U8t_1wBEIr.webp)

*Form configuration - <http://www.formbuddy.com/ins.html>*

By the way you can observe the field ‘USERNAME’, that you can find filled in the source code with the value: ‘**tony222b**’. Rationally it should be the scammer’s Formbuddy.com login account.

As seen in the source code extract, the redirection URL is: **hxxp://custom1.starkwebsolutions[.]com/image/field/success.html**One more time, this is a mistake, and logically
the **success.html** file to use should be the one in the same local directory of the server. This redirection URL was used in another phishing campaign at start of 2018, relatives to a ‘**Outlook Web App**’ and the domain name is now parked.

![](/_astro/israel7.D-dsNAaQ_Z18gwIa.webp)

*Phishing campaign at start of 2018 - <https://blogs.k-state.edu/scams/2018/01/30/phishing-scam-01302018-help-desk-team/>*

The string ‘**Outlook Web App**’ can be found in the phishing kit source retrieved, in the ‘success.html’ file:

![](/_astro/israel8.C_m_cp6N_1a4jqI.webp)

*Israel/success.html (extract)*

**Conclusion**:
As we can see, this deployed phishing kit can not be operational, and does not work as is. That’s pretty usual to find development kits deployed here and there when you harvest kits from here and there. It’s the first time I see the use of Formbuddy portal to exfiltrate data collected, that’s what I would like to share, this and a pretty interesting fail…
One more thing, I don’t understand the use of term ‘Israel’ in this kit, does it is supposed to target Israelian people?

***Artefacts:***
{SHA1} e06701797f002bb19c359644879db5f7a69c6596
hxxp://postauth.000webhostapp[.]com/
hxxp://custom1.starkwebsolutions[.]com/image/field/success.html
‘tony222b’
‘Outlook Web App’

[#formbuddy](/tag/formbuddy/)[#outlook](/tag/outlook/)[#perl](/tag/perl/)

## Keep reading

![](/_astro/bot1.QE2YtVjx_20Ngzg.webp)

14 December 2020· phishing

### [How phishing kits uses Telegram](/2020/12/14/how-phishing-kits-use-telegram/)

More and more actors uses Telegram chat groups to exfiltrate harvested data, we'll show you how we can collect informations about those actors. Let’s have a dive into one of this kits.

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