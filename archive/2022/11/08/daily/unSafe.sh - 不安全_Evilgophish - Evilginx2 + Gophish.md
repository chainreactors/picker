---
title: Evilgophish - Evilginx2 + Gophish
url: https://buaq.net/go-134598.html
source: unSafe.sh - 不安全
date: 2022-11-08
fetch_date: 2025-10-03T21:54:20.846993
---

# Evilgophish - Evilginx2 + Gophish

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

![](https://8aqnet.cdn.bcebos.com/11d7905bc08b97c572770a27df21768f.jpg)

Evilgophish - Evilginx2 + Gophish

Combination of evilginx2 and GoPhish. Credits Before I begin, I would like to say that I a
*2022-11-7 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-134598.htm)
阅读量:132
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg4W8DUvoZAz5gpA-NmxLHaP3iAIo_Yu8Z0By3oagKW8eix8CL46E8GUexK7gfFah68qJrOr8w5CaF_KhYcgtGborKR3MEybAV5dl02pllRXmJjjJThJ2gn3RaSgcfDiyBgnbDAZ8YXUI9E5z_KMDQS_eTM3XnteBar6a6E6vBCrk3faDGaxd45SjlOTg=w640-h456)](https://blogger.googleusercontent.com/img/a/AVvXsEg4W8DUvoZAz5gpA-NmxLHaP3iAIo_Yu8Z0By3oagKW8eix8CL46E8GUexK7gfFah68qJrOr8w5CaF_KhYcgtGborKR3MEybAV5dl02pllRXmJjjJThJ2gn3RaSgcfDiyBgnbDAZ8YXUI9E5z_KMDQS_eTM3XnteBar6a6E6vBCrk3faDGaxd45SjlOTg)

Combination of [evilginx2](https://github.com/kgretzky/evilginx2 "evilginx2") and [GoPhish](https://github.com/gophish/gophish "GoPhish").

## Credits

Before I begin, I would like to say that I am in no way bashing [Kuba Gretzky](https://github.com/kgretzky "Kuba Gretzky") and his work. I thank him personally for releasing [evilginx2](https://github.com/kgretzky/evilginx2 "evilginx2") to the public. In fact, without his work this work would not exist. I must also thank [Jordan Wright](https://github.com/jordan-wright "Jordan Wright") for developing/maintaining the incredible [GoPhish](https://github.com/gophish/gophish "GoPhish") toolkit.

## Prerequisites

You should have a fundamental understanding of how to use `GoPhish`, `evilginx2`, and `Apache2`.

## Disclaimer

I shall not be responsible or liable for any misuse or illegitimate use of this software. This software is only to be used in authorized [penetration testing](https://www.kitploit.com/search/label/Penetration%20Testing "penetration testing") or red team engagements where the operator(s) has(ve) been given explicit written permission to carry out social engineering.

## Why?

As a penetration tester or red teamer, you may have heard of `evilginx2` as a proxy [man-in-the-middle](https://www.kitploit.com/search/label/Man-in-the-Middle "man-in-the-middle") framework capable of bypassing `two-factor/multi-factor authentication`. This is enticing to us to say the least, but when trying to use it for [social engineering](https://www.kitploit.com/search/label/Social%20Engineering "social engineering") engagements, there are some issues off the bat. I will highlight the two main problems that have been addressed with this project, although some other bugs have been fixed in this version which I will highlight later.

1. Lack of tracking - `evilginx2` does not provide unique tracking statistics per victim (e.g. opened email, clicked link, etc.), this is problematic for clients who want/need/pay for these statistics when signing up for a social engineering engagement.
2. Session overwriting with NAT and proxying - `evilginx2` bases a lot of logic off of remote IP address and will whitelist an IP for 10 minutes after the victim triggers a lure path. `evilginx2` will then skip creating a new session for the IP address if it triggers the lure path again (if still in the 10 minute window). This presents issues for us if our victims are behind a firewall all sharing the same public IP address, as the same session within `evilginx2` will continue to overwrite with multiple victim's data, leading to missed and lost data. This also presents an issue for our proxy setup, since `localhost` is the only IP address requesting `evilginx2`.

## Background

In this setup, `GoPhish` is used to send emails and provide a dashboard for `evilginx2` campaign statistics, but it is not used for any landing pages. Your phishing links sent from `GoPhish` will point to an `evilginx2` lure path and `evilginx2` will be used for landing pages. This provides the ability to still bypass `2FA/MFA` with `evilginx2`, without losing those precious stats. `Apache2` is simply used as a proxy to the local `evilginx2` server and an additional hardening layer for your phishing infrastructure. Realtime campaign event notifications have been provided with a local websocket/http server I have developed and full usable `JSON` strings containing tokens/cookies from `evilginx2` are displayed directly in the `GoPhish` GUI (and feed):

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi_DVBD0tjq0D9oSxBWtrGmYGobd_bdpxIwNIi0A34WkS6Y2y8n2wu-O8tjxDZSmJKTN6PJh_F-YGUigP4Ccq4sB9IQuAWNvJVY5ul2CrGAfTf1kDbZeq3O_Wi7Co0pE8YZAe2MYHgWODW78o-_fMR5nPkFudwYzIJW2d8PycloQSB5Ra6zqMkrwmppCQ=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEi_DVBD0tjq0D9oSxBWtrGmYGobd_bdpxIwNIi0A34WkS6Y2y8n2wu-O8tjxDZSmJKTN6PJh_F-YGUigP4Ccq4sB9IQuAWNvJVY5ul2CrGAfTf1kDbZeq3O_Wi7Co0pE8YZAe2MYHgWODW78o-_fMR5nPkFudwYzIJW2d8PycloQSB5Ra6zqMkrwmppCQ)

## Infrastructure Layout

* `evilginx2` will listen locally on port `8443`
* `GoPhish` will listen locally on port `8080` and `3333`
* `Apache2` will listen on port `443` externally and proxy to local `evilginx2` server
  + Requests will be filtered at `Apache2` layer based on redirect rules and IP blacklist configuration
    - Redirect functionality for unauthorized requests is still baked into `evilginx2` if a request hits the `evilginx2` server

## setup.sh

`setup.sh` has been provided to automate the needed configurations for you. Once this script is run and you've fed it the right values, you should be ready to get started. Below is the setup help (note that certificate setup is based on `letsencrypt` filenames):

Redirect rules have been included to keep unwanted visitors from visiting the phishing server as well as an IP blacklist. The blacklist contains IP addresses/blocks owned by ProofPoint, Microsoft, TrendMicro, etc. Redirect rules will redirect known *"bad"* remote hostnames as well as User-Agent strings.

## replace\_rid.sh

In case you ran `setup.sh` once and already replaced the default `RId` value throughout the project, `replace_rid.sh` was created to replace the `RId` value again.

```
Usage:
```

## Email Campaign Setup

Once `setup.sh` is run, the next steps are:

1. Start `GoPhish` and configure email template, email sending profile, and groups
2. Start `evilginx2` and configure phishlet and lure (must specify full path to `GoPhish` `sqlite3` database with `-g` flag)
3. Ensure `Apache2` server is started
4. Launch campaign from `GoPhish` and make the landing URL your lure path for `evilginx2` phishlet
5. **PROFIT**

## SMS Campaign Setup

An entire reworking of `GoPhish` was performed in order to provide `SMS` campaign support with `Twilio`. Your new `evilgophish` dashboard will look like below:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg4W8DUvoZAz5gpA-NmxLHaP3iAIo_Yu8Z0By3oagKW8eix8CL46E8GUexK7gfFah68qJrOr8w5CaF_KhYcgtGborKR3MEybAV5dl02pllRXmJjjJThJ2gn3RaSgcfDiyBgnbDAZ8YXUI9E5z_KMDQS_eTM3XnteBar6a6E6vBCrk3faDGaxd45SjlOTg=w640-h456)](https://blogger.googleusercontent.com/img/a/AVvXsEg4W8DUvoZAz5gpA-NmxLHaP3iAIo_Yu8Z0By3oagKW8eix8CL46E8GUexK7gfFah68qJrOr8w5CaF_KhYcgtGborKR3MEybAV5dl02pllRXmJjjJThJ2gn3RaSgcfDiyBgnbDAZ8YXUI9E5z_KMDQS_eTM3XnteBar6a6E6vBCrk3faDGaxd45SjlOTg)

Once you have run `setup.sh`, the next steps are:

1. Configure `SMS` message template. You will use `Text` only when creating a `SMS` message template, and you should not include a tracking link as it will appear in the `SMS` message. Leave `Envelope Sender` and `Subject` blank like below:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhOOWyWmPQxQG-3SaOy9pOymY7Ot9oOzgmxRmc-QvVnsW5cFZg0TNKKbvBrGeP7vXmtz0D9307kkvbHVH4E_TUEX0GUCCZ7Om5m3zE5rBc8ld6qMebRtOOUQPJ5VctPQhPQAgGKCZ3JYYG-wx6t1psrqGfNRv2EAYcX38yJJX...