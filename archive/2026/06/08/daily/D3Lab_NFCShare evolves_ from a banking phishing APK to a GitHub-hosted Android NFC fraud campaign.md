---
title: NFCShare evolves: from a banking phishing APK to a GitHub-hosted Android NFC fraud campaign
url: https://www.d3lab.net/nfcshare-evolves-from-a-banking-phishing-apk-to-a-github-hosted-android-nfc-fraud-campaign/
source: D3Lab
date: 2026-06-08
fetch_date: 2026-06-09T06:03:38.909999
---

# NFCShare evolves: from a banking phishing APK to a GitHub-hosted Android NFC fraud campaign

[![D3Lab](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2019/04/D3Lab_Logo_Enfold-300x102.png?fit=300%2C102&ssl=1 "D3Lab_Logo_Enfold-300×102")](https://www.d3lab.net/ "D3Lab_Logo_Enfold-300×102")

* [Home](https://www.d3lab.net/)
* [Services](/#services)
* [Philosophy](/#philosophy)
* [Contact](/#contact)
* [Blog](https://www.d3lab.net/blog/)
* [Fare clic per aprire il campo di ricerca
  Fare clic per aprire il campo di ricerca

  Cerca](?s= "Fare clic per aprire il campo di ricerca")
* **Menu**
  Menu

* [Collegamento a X](https://twitter.com/D3LabIT "Collegamento a X")
* [Collegamento a LinkedIn](https://www.linkedin.com/company/d3labsrl/ "Collegamento a LinkedIn")
* [Collegamento a Rss questo sito](https://www.d3lab.net/feed/ "Collegamento a Rss  questo sito")
* [Collegamento a Mail](/#contact "Collegamento a Mail")

# NFCShare evolves: from a banking phishing APK to a GitHub-hosted Android NFC fraud campaign

[Malware](https://www.d3lab.net/category/malware/), [Phishing](https://www.d3lab.net/category/phishing/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/NFCShare_Cover.png?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/NFCShare_Cover.png?fit=1030%2C687&ssl=1 "NFCShare_Cover")

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/NFCShare_Cover.png?resize=1030%2C687&ssl=1)

In January 2026, we analyzed [NFCShare](https://www.d3lab.net/nfcshare-android-trojan-nfc-card-data-theft-via-malicious-apk/), an Android banking trojan distributed as a malicious APK through a phishing flow impersonating Deutsche Bank. The malware presented a fake card-verification interface, asked the victim to place a payment card near the phone, collected the card PIN, and exfiltrated NFC-derived payment-card data to a WebSocket endpoint.

Since 14 May 2026, we have observed a newer wave of NFCShare APKs impersonating Italian and European banking brands. The campaign we investigated started from an ad hoc phishing website, `areaclienti-intesa.com`, which mimicked the look and feel of Intesa Sanpaolo. After the victim entered home-banking credentials, the phishing flow prompted the user to update the banking application. At that point, the website visually directed the victim to a shortened URL, such as `https://tinyurl[.]com/Intesa-Carte`, which then redirected toward APKs hosted in the GitHub repository `antoniocastaldo1998/app-scuola`.

The newer samples are still **NFCShare**. The core NFC and exfiltration logic remains largely unchanged. The relevant evolution is operational and anti-analysis oriented: more frequent APK rebuilds, brand rotation, a new C2 endpoint, a 10-DEX layout, and malformed ZIP paths designed to break naive APK extractors.

## Distribution: phishing site, short URLs, and GitHub hosting

The recent campaign uses bank-themed APK names such as `Intesa Carte.apk`, `Sella Carte.apk`, `Banca Sella Carte.apk`, `Klirway Carte.apk`, `BCC Roma Carte.apk`, `Fideuram Carte.apk`, `Mooney Carte.apk`, `Nexi Carte.apk`, `CaixaBank.apk`, `CaixaBankNfc.apk`, and `CaixaReactivaTarjeta.apk`.

The victim flow is consistent with mobile banking phishing. The user is first brought to the fake Intesa Sanpaolo-themed website `areaclienti-intesa[.]com`. After submitting home-banking credentials, the user is told that the banking app must be updated. The phishing page then redirects through a shortened URL and ultimately leads to the malicious APK hosted on GitHub.

We cannot exclude an additional social-engineering layer: victims may also receive an SMS or a phone call from a fake bank operator who guides them through the process, including enabling Android installation from unknown sources in order to sideload the APK.

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/Screenshot-2026-06-05-alle-14.51.27.png?resize=1030%2C577&ssl=1)](https://www.d3lab.net/?attachment_id=6140)

The GitHub repository used for hosting is named `app-scuola`, which translates roughly to “school app”. Its README is a simple decoy:

```
# app-scuola
app di scuola per compiti a casa
ciaoo!!
```

The repository also contains a small shell script, likely used locally by the operator to push new builds:

```
#!/usr/bin/env bash
set -e

BRANCH="main"
COMMIT_MSG="Aggiornato tutto"

git switch "$BRANCH"
git add -A
git commit -m "$COMMIT_MSG"
git push origin "$BRANCH"
```

The commit history supports this operational model. As of 5 June 2026, the repository contains 57 commits, starting on 10 April 2026, and the vast majority of later commits use the same message: `Aggiornato tutto` (“Updated everything”). Across the Git history, we identified 56 unique APK payloads referenced as blobs.

## Repository timeline

| Date | Observed activity |
| --- | --- |
| 10 Apr 2026 | Repository initialized. Early APKs named `Nexi Carte.apk` appear. |
| 15 Apr 2026 | Spanish-language lure appears as `Nexi Tarjetas.apk`. |
| 22-30 Apr 2026 | Brand rotation expands to `BCC Roma Carte.apk`, `Klirway Carte.apk`, `Banca Sella Carte.apk`, and `Sella NFC.apk`. |
| 11-13 May 2026 | New lures include `Mooney Carte.apk`, `Intesa Carte.apk`, and `Fideuram Carte.apk`. |
| 14 May 2026 onward | Repeated updates to `Intesa Carte.apk`, consistent with the recent wave observed in the wild. |
| 31 May-4 Jun 2026 | Additional builds include `Sella Carte.apk`, `Klirway carte.apk`, `CaixaBank.apk`, `CaixaBankNfc.apk`, and `CaixaReactivaTarjeta.apk`. A separate `120/` folder contains several test or campaign builds. |

## What changed since the first NFCShare sample?

We compared the application analyzed in January with the recent Banca Sella sample and other APKs from the GitHub-hosted wave.

| Feature | Application analyzed in January | Recent Sella / Intesa / Klirway wave |
| --- | --- | --- |
| Package | `com.modol.nap` | `com.modol.nap` |
| Main activity | `nfc.share.itnamteis.MainActivity` | `nfc.share.itnamteis.MainActivity` |
| DEX count | 8 | 10 |
| C2 | `ws://38[.]47[.]213[.]197:7068/` | `ws://nfck[.]loseyourip[.]com:8001/` |
| C2 obfuscation | Encoded through `NPStringFog` | Recovered in cleartext by JADX |
| NFC logic | `IsoDep`, EMV parsing, card data exfiltration | Same core logic |
| UI | Local HTML in WebView | Same local HTML template, with minor variants |
| Anti-analysis | Standard APK ZIP layout | Malformed/poisoned ZIP paths that break simple extractors |

The most important change is not the C2 rotation, which is expected in an active fraud operation. The most important technical evolution is the packaging: newer APKs contain malformed ZIP entries such as paths rooted under `/AndroidManifest.xml/`, `/classes.dex/`, and `/resources.arsc/`. APKs are ZIP archives, and simple extraction tools may try to write those entries as absolute paths. In our tests, this caused extraction failures such as:

```
Error extracting files: [Errno 30] Read-only file system: '/AndroidManifest.xml'
```

This does not prevent proper analysis, but it disrupts automated pipelines that assume benign ZIP paths. It also explains why some family classifiers may return a lower match score for recent samples: the family did not change, but the package structure interferes with extraction and manifest/resource parsing.

## Why this is still NFCShare

The recent samples retain the internal markers that originally motivated the NFCShare family name:

* `nfc.share.itnamteis` namespace
* `CardInfoitmanteis` model
* `MqttChannel` enum with `CARD_INFO_CHANNEL`, `CARD_REMOVED`, and `SEND_CHANNEL`
* Local WebView UI loaded from `assets/index.html`
* NFC reader code using `android.nfc.tech.IsoDep`
* `NPStringFog` with the hardcoded key `itnewpag`
* Chinese string `发送端` (“sender”) decoded at runtime

The channel enum is particularly useful for attribution and hunting:

```
package nfc.share.itnamteis.model;

public enum MqttChannel {
    FETCH_CHANNEL,
    SEND_CHANNEL,
    LOG_CHANNEL,
    CARD_INFO_CHANNEL,
    CARD_REMOVED,
    NOTIFICATION_CHANNEL,
    ANSWER_CHANNEL,
  ...