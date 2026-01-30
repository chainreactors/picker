---
title: NFCShare Android Trojan: NFC card data theft via malicious APK
url: https://www.d3lab.net/nfcshare-android-trojan-nfc-card-data-theft-via-malicious-apk/
source: D3Lab
date: 2026-01-29
fetch_date: 2026-01-30T04:04:19.839207
---

# NFCShare Android Trojan: NFC card data theft via malicious APK

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

# NFCShare Android Trojan: NFC card data theft via malicious APK

[Malware](https://www.d3lab.net/category/malware/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/01/NFCShare_Cover.png?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/01/NFCShare_Cover.png?fit=1030%2C687&ssl=1 "NFCShare_Cover")

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/01/NFCShare_Cover.png?resize=1030%2C687&ssl=1)

## Executive Summary

The D3Lab team analyzed an Android application distributed through a Deutsche Bank phishing campaign. Victims are prompted to enter their phone number, then instructed to “update” their banking app by downloading a malicious APK named `deutsche.apk`. The APK presents itself as “Support Nexi” and guides the user through a fake “card verification” flow: bring the card near the phone, keep it close while “authenticating,” and enter the card PIN. Under the hood, the app reads NFC card data (ISO‑DEP) and exfiltrates it to a remote WebSocket endpoint.

Based on consistent internal artifacts (package naming, classes, messages, and UI flow), we assign this new cluster the family name **NFCShare**.

## Distribution: Deutsche Bank phishing flow

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/01/Phishing_Deutsche_Bank_APK_Download.png?resize=1030%2C625&ssl=1)
![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/01/Phishing_Deutsche_Bank_Phone.png?resize=1030%2C625&ssl=1)

The infection chain starts with a bank‑themed phishing site mimicking Italian Deutsche Bank. The victim is asked for a mobile number and then told to update the bank app. The “update” is delivered as an APK (`deutsche.apk`). After installation, the app claims to be “Support Nexi” and drives the user through a fake security verification designed to harvest NFC card data and the card PIN.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/01/NFCShare_Supporto_Nexi.png?resize=217%2C200&ssl=1)

## What the app does (user flow)

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/01/NFCShare_Screenshot_Avvicina_La_Tua_Carta.png?resize=381%2C407&ssl=1)

The UI is implemented as a local HTML/JS page loaded into a WebView:

* **Step 1:** “Bring your card close”
* **Step 2:** “Keep the card near the phone while authentication completes”
* **Step 3:** PIN collection (4 or 6 digits)

This matches a typical NFC‑relay/harvesting workflow: capture card data via NFC and request the PIN to enable fraudulent transactions.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/01/NFCShare_Screenshot_Carta_Rilevata.png?resize=380%2C448&ssl=1)
![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/01/NFCShare_Screenshot_PIN.png?resize=347%2C832&ssl=1)

## Technical analysis highlights

### 1) NFC reading and card data extraction

The app uses `android.nfc.tech.IsoDep` (ISO‑DEP/ISO 14443‑4) to communicate with payment cards and builds a `CardInfoitmanteis` object containing:

* Card number
* Card type
* Label
* Expiration date

The data is serialized into a string format:

```
number &amp; type &amp; label &amp; MM/yy
```

### 2) Network exfiltration via WebSocket

The app connects to a WebSocket endpoint and sends JSON messages containing NFC data. The connection string is obfuscated and resolved at runtime.

```
ws://38[.]47[.]213[.]197:7068/
```

### 3) String obfuscation (NPStringFog)

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/01/NFCShare_Screenshot_Code_Key.png?resize=819%2C401&ssl=1)

Strings are XOR‑encoded and decoded using a hardcoded key:

```
KEY = "itnewpag"
```

Sample decoding (from smali):

```
const-string v0, "1E07544A584359495D43405746434F565043545247465948"
invoke-static {v0}, Lobfuse/NPStringFog;->decode(Ljava/lang/String;)Ljava/lang/String;

=> "ws://38[.]47[.]213[.]197:7068/"
```

## Why we call it NFCShare (family attribution)

We chose the family name **NFCShare** because of consistent internal naming and behavior:

* Namespace/strings: `nfc.share.*` appears in internal package paths and resources.
* Function: the malware’s core purpose is to “share” (exfiltrate) NFC card data to a remote server.

Supporting internal artifacts:

* Package/namespace: `nfc.share.itnamteis.*`
* Strings: `nfc.share` and other NFC‑related UI text
* Channels: `CARD_INFO_CHANNEL`, `CARD_REMOVED`, `SEND_CHANNEL` in internal enums

This naming is stable across the codebase and better reflects the malware’s core behavior than the external branding (“Support Nexi”).

## Links to known Chinese‑linked tooling and related families

We observed several indicators suggesting a Chinese‑linked operator or tooling lineage:

* The app embeds Chinese text such as `发送端` (“sender”).
* String obfuscation and naming patterns are consistent with Chinese Android malware tooling.

We also note the following contextual overlap reported by defenders:

* The C2 IP was associated with [**SuperCardX**](https://www.cleafy.com/cleafy-labs/supercardx-exposing-chinese-speaker-maas-for-nfc-relay-fraud-operation) activity in November 2025.
* The flow is conceptually similar to **RelayNFC** as analyzed by [Cyble](https://cyble.com/blog/relaynfc-nfc-relay-malware-targeting-brazil/) (Brazil‑targeting NFC relay malware).

## IOCs

### Hashes

* SHA‑256: `afbe6751d339fbc5b7bddd29429a11740e82fef935a61acaf2fe5487444dbed4`

### Package / App

* `com.modol.nap`
* App label: Support Nexi

### Network

* ws://38[.]47[.]213[.]197:7068/
* portale-deut[.]com

29 Gennaio 2026/da [Andrea Draghetti](https://www.d3lab.net/author/andrea-d/ "Articoli scritti da Andrea Draghetti")

##### Condividi questo articolo

* [Condividi su Facebook](https://www.facebook.com/sharer.php?u=https://www.d3lab.net/nfcshare-android-trojan-nfc-card-data-theft-via-malicious-apk/&t=NFCShare%20Android%20Trojan%3A%20NFC%20card%20data%20theft%20via%20malicious%20APK)
* [Condividi su X](https://twitter.com/share?text=NFCShare%20Android%20Trojan%3A%20NFC%20card%20data%20theft%20via%20malicious%20APK&url=https://wp.me/p7upL6-1y7)
* [Condividi su WhatsApp](https://api.whatsapp.com/send?text=https://www.d3lab.net/nfcshare-android-trojan-nfc-card-data-theft-via-malicious-apk/)
* [Condividi su Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.d3lab.net%2Fnfcshare-android-trojan-nfc-card-data-theft-via-malicious-apk%2F&description=NFCShare%20Android%20Trojan%3A%20NFC%20card%20data%20theft%20via%20malicious%20APK&media=https%3A%2F%2Fi0.wp.com%2Fwww.d3lab.net%2Fwp-content%2Fuploads%2F2026%2F01%2FNFCShare_Cover.png%3Ffit%3D705%252C470%26ssl%3D1)
* [Condividi su LinkedIn](https://linkedin.com/shareArticle?mini=true&title=NFCShare%20Android%20Trojan%3A%20NFC%20card%20data%20theft%20via%20malicious%20APK&url=https://www.d3lab.net/nfcshare-android-trojan-nfc-card-data-theft-via-malicious-apk/)
* [Condividi su Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.d3lab.net%2Fnfcshare-android-trojan-nfc-card-data-theft-via-malicious-apk%2F&name=NFCShare%20Android%20Trojan%3A%20NFC%20card%20data%20theft%20via%20malicious%20APK&description=An%20Android%20trojan%20distributed%20via%20a%20Deutsche%20Bank%20phishing%20camp...