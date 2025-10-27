---
title: Squarephish - An advanced phishing tool that uses a technique combining the OAuth Device code authentication flow and QR codes
url: https://buaq.net/go-140924.html
source: unSafe.sh - 不安全
date: 2022-12-22
fetch_date: 2025-10-04T02:11:33.812909
---

# Squarephish - An advanced phishing tool that uses a technique combining the OAuth Device code authentication flow and QR codes

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/24982cb46e7fb40451246867ce5b84f5.jpg)

Squarephish - An advanced phishing tool that uses a technique combining the OAuth Device code authentication flow and QR codes

SquarePhish is an advanced phishing tool that uses a technique combining the OAuth Device co
*2022-12-21 21:30:0
Author: [www.kitploit.com(查看原文)](/jump-140924.htm)
阅读量:42
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgttmELdITUTzXbOUGIkSlkLHY5zCtzi0UdrK9qCGGwrZUTAQYLFja6hoNtdwohNEiATcE62WZIcsP1_VbUEWT26Zn0yU5nRyPWPMGgDoDohnjWFs8fUcdlbuGuCkJstV18YEzPexF4XV62xaZAs3qkI2yY9DiyMgDAaZIcq0JJcfuxjFX2BnLRt8RRtw=w516-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEgttmELdITUTzXbOUGIkSlkLHY5zCtzi0UdrK9qCGGwrZUTAQYLFja6hoNtdwohNEiATcE62WZIcsP1_VbUEWT26Zn0yU5nRyPWPMGgDoDohnjWFs8fUcdlbuGuCkJstV18YEzPexF4XV62xaZAs3qkI2yY9DiyMgDAaZIcq0JJcfuxjFX2BnLRt8RRtw)

SquarePhish is an advanced [phishing](https://www.kitploit.com/search/label/Phishing "phishing") tool that uses a technique combining the OAuth Device code [authentication](https://www.kitploit.com/search/label/Authentication "authentication") flow and QR codes.

> See [PhishInSuits](https://github.com/secureworks/PhishInSuits "PhishInSuits") for more details on using OAuth Device Code flow for phishing attacks.

```

```

## Attack Steps

An attacker can use the `email` module of SquarePhish to send a malicious QR code email to a victim. The default pretext is that the victim is required to update their [Microsoft](https://www.kitploit.com/search/label/Microsoft "Microsoft") MFA authentication to continue using mobile email. The current client ID in use is the Microsoft Authenticator App.

> By sending a QR code first, the attacker can avoid prematurely starting the OAuth Device Code flow that lasts only 15 minutes.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgttmELdITUTzXbOUGIkSlkLHY5zCtzi0UdrK9qCGGwrZUTAQYLFja6hoNtdwohNEiATcE62WZIcsP1_VbUEWT26Zn0yU5nRyPWPMGgDoDohnjWFs8fUcdlbuGuCkJstV18YEzPexF4XV62xaZAs3qkI2yY9DiyMgDAaZIcq0JJcfuxjFX2BnLRt8RRtw=w516-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEgttmELdITUTzXbOUGIkSlkLHY5zCtzi0UdrK9qCGGwrZUTAQYLFja6hoNtdwohNEiATcE62WZIcsP1_VbUEWT26Zn0yU5nRyPWPMGgDoDohnjWFs8fUcdlbuGuCkJstV18YEzPexF4XV62xaZAs3qkI2yY9DiyMgDAaZIcq0JJcfuxjFX2BnLRt8RRtw)

The victim will then scan the QR code found in the email body with their mobile device. The QR code will direct the victim to the attacker controlled server (running the `server` module of SquarePhish), with a URL paramater set to their email address.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEisc9z0jSx7X-P7u1J6BSB44M2ROK52tXgag6ApLECHeg4BowT1rhMCZX2KtsYvHbiZq_P2yLChO_W1RLYFiDe-IVlnmfgtLBkMwVc4kSWkuNzyyrq20AUMQrt1Mp7yqO6uGbzjsDJGuplbddJOAWab3oNm6C_gCQOhCG4_DIl2XmCGBNv0xnsyzmdfuw=w370-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEisc9z0jSx7X-P7u1J6BSB44M2ROK52tXgag6ApLECHeg4BowT1rhMCZX2KtsYvHbiZq_P2yLChO_W1RLYFiDe-IVlnmfgtLBkMwVc4kSWkuNzyyrq20AUMQrt1Mp7yqO6uGbzjsDJGuplbddJOAWab3oNm6C_gCQOhCG4_DIl2XmCGBNv0xnsyzmdfuw)

When the victim visits the malicious SquarePhish server, a background process is triggered that will start the OAuth Device Code authentication flow and email the victim a generated Device Code they are then required to enter into the legitimate Microsoft Device Code website (this will start the OAuth Device Code flow 15 minute timer).

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiH2Wm69-7ZH1OPOV8UAvFFQ7a1GoVc42kRpE1U9qG1L002JDjijFmfURPEMAPGVJnXG1FRxjLQu9TkvwG-HPNcRdtwY5R4mR3ecyhiPHgn5I50IbZYzZwNhetxwO-RSnXaAp3uj_7lIRbdYUN2Vs09peLqO9TDkF1snvhUS8ssU4b970kWW3-E6keHkg=w640-h412)](https://blogger.googleusercontent.com/img/a/AVvXsEiH2Wm69-7ZH1OPOV8UAvFFQ7a1GoVc42kRpE1U9qG1L002JDjijFmfURPEMAPGVJnXG1FRxjLQu9TkvwG-HPNcRdtwY5R4mR3ecyhiPHgn5I50IbZYzZwNhetxwO-RSnXaAp3uj_7lIRbdYUN2Vs09peLqO9TDkF1snvhUS8ssU4b970kWW3-E6keHkg)

The SquarePhish server will then continue to poll for authentication in the background.

```
[2022-04-08 14:31:51,962] [info] [[email protected]] Polling for user authentication...
[2022-04-08 14:31:57,185] [info] [[email protected]] Polling for user authentication...
[2022-04-08 14:32:02,372] [info] [[email protected]] Polling for user authentication...
[2022-04-08 14:32:07,516] [info] [[email protected]] Polling for user authentication...
[2022-04-08 14:32:12,847] [info] [[email protected]] Polling for user authentication...
[2022-04-08 14:32:17,993] [info] [[email protected]] Polling for user authentication...
[2022-04-08 14:32:23,169] [info] [[email protected]] Polling for user authentication...
[2022-04-08 14:32:28,492] [info] [[email protected]] Polling for user authentication...
```

The victim will then visit the Microsoft Device Code authentication site from either the link provided in the email or via a redirect from visiting the SquarePhish URL on their mobile device.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh1KvJizK-OueapfwFqmFEf2vbmB2wM0Y_hP0MdB9xPLFWZiAe6uyhrUG5cD-U-zWN-6Aqt8-K57f0yzkWaV3OZQmbQt7zPiXv6z6m74SOX1lt_LJG9OYzaQyrdAJVTUSxGMaVxjZtSFiinUimP-T6dvFfuGyTGbLAddW-llc_Iqe0NFpIN8aoXRBUemg=w640-h506)](https://blogger.googleusercontent.com/img/a/AVvXsEh1KvJizK-OueapfwFqmFEf2vbmB2wM0Y_hP0MdB9xPLFWZiAe6uyhrUG5cD-U-zWN-6Aqt8-K57f0yzkWaV3OZQmbQt7zPiXv6z6m74SOX1lt_LJG9OYzaQyrdAJVTUSxGMaVxjZtSFiinUimP-T6dvFfuGyTGbLAddW-llc_Iqe0NFpIN8aoXRBUemg)

The victim will then enter the provided Device Code and will be prompted for consent.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj4sds3-J8eqoDw3YrbtTWx5TzHxkKfAkChXSDTKCqmndk5xlWmX1Q5UOAdZ5oDHjZ0kPX5M07daccDCtcZcTJlDA_0BQhg9yzwECm52Qe12t0LEK34us9vaxt1E5u4iSOF8po9e-8MNkphnEq8K6TpUeBEJ79iOww4NY3ak4EfPqbYKFn7N15iutzFXg=w640-h500)](https://blogger.googleusercontent.com/img/a/AVvXsEj4sds3-J8eqoDw3YrbtTWx5TzHxkKfAkChXSDTKCqmndk5xlWmX1Q5UOAdZ5oDHjZ0kPX5M07daccDCtcZcTJlDA_0BQhg9yzwECm52Qe12t0LEK34us9vaxt1E5u4iSOF8po9e-8MNkphnEq8K6TpUeBEJ79iOww4NY3ak4EfPqbYKFn7N15iutzFXg)

After the victim authenticates and consents, an authentication token is saved locally and will provide the attacker access via the defined scope of the requesting application.

The current scope definition:

```
"scope": ".default offline_access profile openid"
```

> !IMPORTANT: Before using either module, update the required information in the [settings.config](https://github.com/secureworks/squarephish/blob/main/settings.config "settings.config") file noted with `Required`.

## Email Module

Send the target victim a generated QR code that will trigger the OAuth Device Code flow.

```
usage: squish.py email [-h] [-c CONFIG] [--debug] [-e EMAIL]

optional arguments:
  -h, --help            show this help message and exit

-c CONFIG, --config CONFIG
                        squarephish config file [Default: settings.config]

--debug               enable server debugging

-e EMAIL, --email EMAIL
                        victim email address to send initial QR code email to
```

## Server Module

Host a server that a generated QR code will be pointed to and when requested will trigger the OAuth Device Code flow.

```
usage: squish.py server [-h] [-c CONFIG] [--debug]

optional arguments:
  -h, --help            show this help message and exit

-c CONFIG, --config CONFIG
                        squarephish config file [Default: settings.config]

--debug               enable server debugging
```

## Configuration

All of the applicable settings for execution can be found and modified via the [settings.config](https://github.com/secureworks/squarephish/blob/main/settings.config "settings.config") file. There are several pieces of required information that d...