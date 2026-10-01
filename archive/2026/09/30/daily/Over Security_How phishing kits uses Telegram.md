---
title: How phishing kits uses Telegram
url: https://stalkphish.com/2020/12/14/how-phishing-kits-use-telegram/
source: Over Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:08.797576
---

# How phishing kits uses Telegram

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

[← Blog](/blog/)·14 December 2020(updated 29 March 2021)·3 min read

# How phishing kits uses Telegram

[phishing](/category/phishing/)[phishing kit](/category/phishing-kit/)

![](/_astro/bot1.QE2YtVjx_20Ngzg.webp)

Last days I found several kits using Telegram to exfiltrate stolen data. One of this kit is from *z0n51* and targets Crédit Agricole (a french bank) customers. Actors uses Telegram chat groups to harvest data instead (or combined with) of using the soooo typical email vector, and, as with email, we can collect informations about actors (maybe more than with email actually). Let’s have a dive into one of this kits.

### Find a PhishingKit source from a collection

As a great fan of [StalkPhish](https://github.com/t4d/StalkPhish) (well I code it, so…) I collect a certain number of phishing kit sources everyday, for phishing kits collection triage I use the project PhishingKit-Yara-Rules (<https://github.com/t4d/PhishingKit-Yara-Rules>) and for this case I use the PhishingKit Zip YARA rule “*PK\_CA\_z0n51.yar*” (<https://github.com/t4d/PhishingKit-Yara-Rules/blob/master/PK_CA_z0n51.yar>).
Using this dedicated YARA rule, and the open source tool PhishingKit-Yara-Search (<https://github.com/t4d/PhishingKit-Yara-Search>) I can pick some kits I’m looking for:
![](/_astro/857e4-1opbvk848k_ubnahc6fkmgq.B9EiuBb0_4Tmuu.webp)
We can observe the first 2 files have the same SHA1 hash, this is exactly the same file deployed on 2 different URLs:
![](/_astro/3dfae-1u-1ivxu3n8leck863rn-dw.BWI5VH-E_Z1i9G9s.webp)

### The Phishing Kit

Lucky me, I can still connect to, at least, one of this URL list to present you screenshots. This kit do what this sort of phishing kits do, harvesting users bank account credentials, personal and credit card informations:
![](/_astro/fe12d-1-1ffq9ee-gvefd-pvlaybw.BPtAZl3E_J0dtC.webp)
![](/_astro/37dc9-1mng8bzuye0svlrdbmyc2iw.BOaz3EIw_Z22TOzG.webp)
![](/_astro/f0eab-1ou6gm7gtt9gfb09tx07d5w.CEEch-gN_17eAG9.webp)
![](/_astro/432d9-13bxdy-dk1yxwmrb64-6efa.DJhjFtdW_Zcv5NO.webp)
![](/_astro/64e0c-1ymqrgbbhcqnyigpnq9teig.tXSdrGhn_Z1cz7C8.webp)
Sometimes you can get the phishing kit sources, presented as an archive (.zip for the most) still hosted on the webserver. StalkPhish is code to retrieve this files for further analysis. This is how this archive looks like:
![](/_astro/e409e-16z5wlq7eccjo3zpw0f6kjq.DrxWV46I_vyMCl.webp)
At first glance, we can observe the existence of the **“*z0n51”*** directory which give informations about this kit. You can see the typical, for this kit, presence of files like **“*vu.txt”*** and **“*resulttt987.txt”*** which will store informations about victims (or crawlers ;p ) visiting phishing pages.
What interests us in this kit is the use of Telegram. This *z0n51* phishing kit load a Telegram configuration from the file ***inc/functions.php:***
![bot1](/_astro/bot1.QE2YtVjx_20Ngzg.webp)
As you can see, this PHP function use 2 variables ***$api\_key*** which correspond to the Telegram’s Bot authentication token and the Telegram’s chat ***$chat\_id*** to create a PHP Curl command which will use the ***sendMessage*** Telegram’s API command to exfiltrate data into the chat.
Since we have the Telegram’s chat and bot ids, we can play with it our turn :)

### Playing with Telegram’s bot API

You can find documentation here: <https://core.telegram.org/bots/api>
Interesting bot API commands are: *getMe*, *getChat*, *getChatAdministrators*, *getUserProfilePhotos.*
I go to use *torify* (using Tor network) to anonymize my location. First I check informations about the bot, with the *getMe* command:
![CA-getme](/_astro/ca-getme-1.Chnjb5Ua_1qBGgQ.webp)
We can observe that we are declared as a bot with a *username* and *first\_name*, as well as rights given to this bot.
Then we can ask more informations about the chat channel using *getChat* command:
![CA-getchat](/_astro/ca-getchat.CESCOvst_1v4OlH.webp)

The title is rather explicit: “CREDIT RZLT” (RZLT=result)
But who is behind this channel? Let’s ask using the *getChatAdministrators* command:
![CA-chatadmin](/_astro/ca-chatadmin-1.C1p5NuSS_ZTfHb5.webp)

Well, except our bot informations, there’s other interesting informations there, like those of the creator:
![](/_astro/dda65-1iy4jztnfqjhj1uw934vqew.BqrZVD2I_Z2qMesq.webp)
From there we can have more informations about the actor behind the phishing kit, we know he/she is not a bot and we can retrieve interesting strings for further investigations, as the rather explicit *username*, useful when you make some search about this actor (you can find some toolboxes, some defacement material, and so on…).

### More

Sometimes creators add photos to their user account, photos you can consult, and download, using commands *getUserProfilePhotos* and *getFile* (even if this is not the case here). Also, it could be useful for threat hunters to retrieve informations about the stolen data, by using WebHooks (check *setWebhook* and *getWebhookInfo*).

### In conclusion

The phishing kits which use Telegram bots can bring more material to an investigator to perform a further investigation about an actor behind data theft, and I advise you to perform those operations to retrieve additional informations.

[#Cybersecurity](/tag/cybersecurity/)[#Infosec](/tag/infosec/)[#Stalkphish](/tag/stalkphish/)

## Keep reading

![](/_astro/israel3.CujJiqJP_Z2lca5m.webp)

6 December 2019· phishing

### [[Phishing Kit] 'Israel' Outlook Web App credentials stealer](/2019/12/06/israel-outlook-credentials-harvester/)

An analysis of a phishing kit found with StalkPhish tool. This phishing kit impersonating a professional Outlook login pattern and exfiltrate credentials on an online portal (FormBuddy)... with no success.

![](/_astro/fb_viet.C8V718uo_Z1cDClk.webp)

9 April 2021· phishing

### [Phishing kit using Google sheet to exfiltrate stolen data](/2021/04/09/phishing-kit-using-google-sheet-to-exfiltrate-stolen-data/)

Analysis of a Facebook phishing kit which exfiltrate stolen data to an online Google Sheet using ajax POST method.

## Phishing campaigns move fast. So should you.

Start with a free search, or talk to us about API access and custom intelligence for your brand.

[Try W...