---
title: One Hacked cPanel Account: Five Phishing Kits, SEO Spam, Mailers and a Zoo of Webshells
url: https://lukeleal.com/research/posts/hacked-cpanel-five-phishing-kits-and-a-shell-zoo/
source: Over Security
date: 2026-11-14
fetch_date: 2026-11-15T08:37:38.878228
---

# One Hacked cPanel Account: Five Phishing Kits, SEO Spam, Mailers and a Zoo of Webshells

[# Cybersecurity Research 🚀](/research/posts/)

* Menu ▾
* + [Backdoors](https://lukeleal.com/research/tags/backdoor/)
  + [Phishing](https://lukeleal.com/research/tags/phishing/)
  + [Skimmers](https://lukeleal.com/research/tags/skimmer/)
  + [Past Research](https://blog.sucuri.net/author/luke)
  + [PGP Key](https://lukeleal.com/research/pages/pgp/)
  + [RSS](https://lukeleal.com/research/posts/index.xml)

* [Backdoors](https://lukeleal.com/research/tags/backdoor/)
* [Phishing](https://lukeleal.com/research/tags/phishing/)
* [Skimmers](https://lukeleal.com/research/tags/skimmer/)
* + ▾
  + - [Past Research](https://blog.sucuri.net/author/luke)
    - [PGP Key](https://lukeleal.com/research/pages/pgp/)
    - [RSS](https://lukeleal.com/research/posts/index.xml)

# [One Hacked cPanel Account: Five Phishing Kits, SEO Spam, Mailers and a Zoo of Webshells](https://lukeleal.com/research/posts/hacked-cpanel-five-phishing-kits-and-a-shell-zoo/)

2026-11-07Luke

#[phishing kit](https://lukeleal.com/research/tags/phishing-kit/)
#[web shell](https://lukeleal.com/research/tags/web-shell/)
#[backdoor](https://lukeleal.com/research/tags/backdoor/)
#[cPanel](https://lukeleal.com/research/tags/cpanel/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[Telegram](https://lukeleal.com/research/tags/telegram/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
#[SEO spam](https://lukeleal.com/research/tags/seo-spam/)
#[incident response](https://lukeleal.com/research/tags/incident-response/)
#[Correos](https://lukeleal.com/research/tags/correos/)
#[USPS](https://lukeleal.com/research/tags/usps/)
#[PayPal](https://lukeleal.com/research/tags/paypal/)
#[InPost](https://lukeleal.com/research/tags/inpost/)
![One Hacked cPanel Account: Five Phishing Kits, SEO Spam, Mailers and a Zoo of Webshells](https://lukeleal.com/research/cpanel-phishing-hub-cover-q90.jpg "Cover Image")

## Table of Contents

* [The Account](#the-account)
* [The Hub: One Index, Five Kits](#the-hub-one-index-five-kits)
  + [What the visitor log says](#what-the-visitor-log-says)
* [The Kits](#the-kits)
  + [1. Spain: “Pago de sanciones” (`/Electronica/`)](#1-spain-pago-de-sanciones-electronica)
  + [2. Poland: parcel fee (`/pol/`)](#2-poland-parcel-fee-pol)
  + [3. USA: USPS tracking (`/ca/`)](#3-usa-usps-tracking-ca)
  + [4. Australia: TPG webmail and DHL (`/au/`)](#4-australia-tpg-webmail-and-dhl-au)
  + [5. PayPal and friends (`/g/`, `/en/`, `/ae/`, `/ch/`)](#5-paypal-and-friends-g-en-ae-ch)
  + [Spread across the other sites](#spread-across-the-other-sites)
* [The Support Tools](#the-support-tools)
  + [Bulk mailers](#bulk-mailers)
  + [SEO spam doorways](#seo-spam-doorways)
* [The Webshells](#the-webshells)
  + [A marker on 41 directories](#a-marker-on-41-directories)
* [The Database](#the-database)
* [How They Got In](#how-they-got-in)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)

I was handed the full backup of a cPanel account that had been flagged by Google Safe Browsing. The home directory was complete: websites, mail, logs, database dumps, the host’s own quarantine, even `.ssh`. That is rare, because normally you only get the web root.

> The account was running **five phishing kits at the same time**, all sending stolen data to Telegram bots. It also held SEO spam doorways, bulk mailers, **six webshells** and an administrator user planted in the WordPress database. Someone also tagged the account with a file called `xaryes.txt` in **41 places**.

I analysed everything statically. Nothing was executed and no C2 was contacted. The client and the account name are left out. Bot tokens and the webshell password are redacted.

## The Account[#](#the-account)

It is an ordinary shared hosting account with about ten sites on it: three WordPress installs for a small real-estate business, a demo copy, an old backup copy (WordPress 4.9.4), and two or three domains that only ever served phishing.

The two scanner logs give the scale. The cleanup scanner reported these detection classes in the live sites:

| Detection | Files |
| --- | --- |
| `php.phishing.redirect` | 10 |
| `rex.defaced.generic` | 10 |
| `js.spam-seo.redirect` | 9 |
| `filename.php_on_wp-core_images` | 8 |
| `php.phishing.script` | 7 |
| `htaccess.phishing.block_bots` | 5 |
| `php.phishing.generic`, `php.mailer.generic`, `html.phishing.paypal` | 2 each |
| `php.malware.obfuscated` / `.filesman` / `.assert` | 1 each |

Another **3,789 findings** were inside the host’s own quarantine folder (`quarantine_1751478240`, an epoch for **2025-07-02**). That folder holds 29,273 files, 14,689 of them PHP: a whole infected web root that the host moved aside and left in the account.

## The Hub: One Index, Five Kits[#](#the-hub-one-index-five-kits)

The phishing lives under one domain, plus a second parked one. The root `index.php` is a **gate** in front of everything else. The header is the seller’s advert:

```
// 𝓑𝔂 𝓤𝔂𝓼𝓷𝓧
// Telegram For Buy Anyscampage : @xuysnx
```

So this is a kit that was **bought** from a scam-page seller and not written by the operator. The gate does four things before it sends anyone to a kit:

1. `DesktopBlock.php` loads `Mobile_Detect` and returns **403 to any non-mobile browser**. Victims come from SMS, so desktop visitors are analysts and scanners.
2. A **country allow-list**: `ES` and `MA` (Spain and Morocco). Every other country is dropped.
3. An **ISP blacklist** (Cloudflare, Google, Amazon, Namecheap, OVH, Hetzner, DigitalOcean, Microsoft, Yandex, phishtank and others) and about **85 IP-prefix patterns** for Google, other crawlers and security-vendor ranges.
4. A **User-Agent bot list**.

If a visitor passes, the page redirects with JavaScript to `/Electronica/`. Failures get logged to `visitors.html`, a 130 KB table the operator reads. It survived in the backup and is a good picture of the campaign.

### What the visitor log says[#](#what-the-visitor-log-says)

990 requests between **2024-08-31 and 2025-08-12**, the day the cleanup began, so the hub was live for a full year:

| Verdict | Requests |
| --- | --- |
| Allowed (reached the kit) | 337 |
| Country not allowed | 312 |
| Detected as bot | 341 |

Top countries: Spain 304, China 264, United States 218, Morocco 36, Germany 26, South Korea 26. The allowed ISPs were mostly **Telefónica de España, Orange Espagne, Digi Spain** and **Maroc Telecom** (34 hits). The Chinese and US traffic is cloud scanners, mostly Tencent ranges, and every one of them was turned away. The Maroc Telecom hits are most likely the operator testing the page.

The gate works the way it is meant to: **a scanner that is not a Spanish mobile phone sees a 403.** That also explains why the sites were up for a year before Google flagged them.

## The Kits[#](#the-kits)

### 1. Spain: “Pago de sanciones” (`/Electronica/`)[#](#1-spain-pago-de-sanciones-electronica)

A Correos-branded page for paying a fine. It asks for a card, then shows a fake 3-D Secure page (*“Valida esta compra para continuar”*) and asks for the SMS code. Stripe checkout CSS and SVGs were copied over to look genuine. The pages are `cc.php`, `vbv.php`, `sms.php`, `pin.php`, `wait.php` and `info.php`.

`config.php` is the whole control panel, with French comments and a `#zerocution` tag:

```
$mail_send = FALSE;
$tlg_send  = true;       // Telegram
$bot_token = "<redacted>";
$rez_chat  = "<redacted>";
$vbv = true;  $timeVBV = "15";
```

`wait.php` is a holding page that auto-refreshes after 20 seconds to `sms.php`, which asks for the code sent by the bank. `captured.txt` has 919 lines but only visitor IPs (`ip : ^68.*.*.*`), no card data. Everything else went to the bot.

### 2. Poland: parcel fee (`/pol/`)[#](#2-poland-parcel-fee-pol)

An InPost-style tracking page that asks for a small redelivery fee (`$fees = "8,99 PLN"`), then the card, then an SMS code. It has its own antibot (`$antibot = "yes"`, `$block_proxy = "yes"`), a `blacklisted_ips.txt`, a `botMother` folder and a `bo...