---
title: Inside an N26 Impersonation Campaign: From Vishing and Fake Control 1.0 to the Copybara Android RAT
url: https://www.d3lab.net/inside-an-n26-impersonation-campaign-from-vishing-and-fake-control-1-0-to-the-copybara-android-rat/
source: D3Lab
date: 2026-07-29
fetch_date: 2026-07-30T04:52:29.614464
---

# Inside an N26 Impersonation Campaign: From Vishing and Fake Control 1.0 to the Copybara Android RAT

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

# Inside an N26 Impersonation Campaign: From Vishing and Fake Control 1.0 to the Copybara Android RAT

[Malware](https://www.d3lab.net/category/malware/), [Phishing](https://www.d3lab.net/category/phishing/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/dropper-installer-screen-1.png?resize=860%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/dropper-installer-screen-1.png?fit=656%2C1030&ssl=1 "dropper-installer-screen")

An active fraud campaign targeting users in Italy combines voice phishing, a real-time phishing control panel, and an Android remote access trojan. The operation begins with a phone call from someone impersonating N26 support and ends with the attacker controlling financial applications on the victim’s phone.

The malicious application is presented as a device certification component. Behind that pretext is a multistage Android dropper whose embedded payload belongs to the Copybara family.

This is not simply a credential-harvesting website. It is a human-operated workflow designed to move the attacker from social engineering to on-device fraud.

## The campaign in context

The campaign was publicly highlighted by [ShadowOpCode on X](https://x.com/ShadowOpCode/status/2082128738725052781), who referenced a detailed [victim report on Reddit](https://www.reddit.com/r/ItaliaPersonalFinance/comments/1v90zgd/truffato_tramite_n26_phishing_avanzato/).

According to the report, the victim first received several calls. An automated message claimed that additional account verification was required, after which a purported N26 representative guided the victim through a device “certification” process.

The operator used trusted real messages already visible in the banking application to reinforce the story. The victim was then moved outside the bank’s trusted communication channel and instructed to contact a fraudulent support address.

The reply led to an N26-themed login page hosted on an attacker-controlled domain. After the victim entered credentials, the site offered an Android package and the operator instructed the victim to enable Accessibility, location, device-control, and other invasive permissions.

Once those permissions were granted, an N26-branded white screen and loading indicator covered the display. The victim reported that settings were changed and transactions were attempted across several financial applications while that cover remained visible.

## A phishing site operated in real time

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/Phishing_n26.png?resize=1030%2C622&ssl=1)

The phishing site is part of a web-based phishing control system identified with high confidence as **Fake Control 1.0** **or AdminLTE**. The identification is based on the structure of the victim URL, the server-side layout, the exposed primary and backup SQLite databases, and the dedicated malware-delivery channel.

The phishing site was also observed delivering the Android package analyzed in this report.

## What Fake Control 1.0 does

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/AdminLTE_Fake_Control_C2.png?resize=530%2C471&ssl=1)](https://www.d3lab.net/?attachment_id=6332)

Fake Control 1.0 uses PHP, SQLite, JavaScript, and an administrative interface based on AdminLTE. AdminLTE itself is a legitimate and widely used dashboard template; its presence alone is not a malicious family marker.

The distinctive evidence lies in the workflow implemented around it. The kit maintains victim records, updates the operator dashboard every few seconds, collects credentials and one-time codes across multiple stages, and allows the operator to control what the victim sees next.

The available commands include messages, token validation and invalidation, transaction-cancellation lures, and an APK download action. This turns the page into an interactive social-engineering console rather than a static login clone.

The kit stores operational data in SQLite and keeps a separate backup. The administrative components provide access to individual victim sessions, aggregate access logs, and export functions. Portuguese identifiers such as `senha`, `acesso`, `gerente`, and `enviarComando` indicate the development language or ecosystem of the kit, but they do not establish the nationality or location of the campaign operators.

The victim URL contains separate values for verification, session identification, and attempt tracking. Those parameters match the flow described in the Fake Control material and explain how a phone operator can follow one victim in real time while presenting different instructions or download actions.

## The Android delivery stage

The outer application calls itself `N26 Pdf` and uses the package name `io.smart.evolve`. It presents an update screen for a component named `Certificato N26`.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/07/dropper-installer-screen-1.png?resize=656%2C1030&ssl=1)

The dropper copies an embedded package, asks Android for permission to install applications from an unknown source, and invokes the standard `PackageInstaller` flow. A foreground observer checks the permission state every 800 milliseconds and continues as soon as installation is allowed.

The dropper also creates a local per-application VPN for `com.android.vending`, the Google Play Store package. It routes IPv4 and IPv6 traffic into a local TUN interface and discards the packets for 240 seconds.

Strings in the code refer to a ten-second block, but the implemented constant is 240,000 milliseconds. The most plausible purpose is to disrupt Play Store or Play Protect communication during the installation window.

## Structural anti-analysis

Both the outer dropper and the embedded payload contain deliberate ZIP inconsistencies. [apkInspector](https://github.com/erev0s/apkInspector/) identified conflicting compression methods between local headers and the central directory.

The outer APK contains random Unicode path components, large extra fields, and an asset path 2,441 bytes long. Conventional tools may reject the file or fail when creating the directory structure.

The embedded APK adds another technique. Seventy resources are placed below file-like prefixes such as `classes.dex`, `AndroidManifest.xml`, and `resources.arsc`, creating collisions between files and directories.

These anomalies are evidence of anti-static-analysis engineering, but they are not treated as malicious proof on their own. The malicious classification rests on the loader, installation behavior, command-and-control configuration, and RAT capabilities.

## Recovering the hidden stages

The outer application class, `biz.include.seat.Lbachelorcycle`, extracts a JAR hidden at the end of the extreme asset path. It processes the asset and decrypts the result using RC4.

The recovered JAR contains a DEX that implements the actual dropper logic. That loader locates `assets/base.apk`, presents its label and icon to the victim, and installs it.

The reconstructed chain is: N26 Pdf dropper > Obfuscated Application class > Encrypted WJcugJ.jar > RC4 decryption > Dynamic loader DEX ...