---
title: Aegis v3.4.3
url: https://kitploit.com/en/posts/github-beemdevelopment-aegis-v343
source: Kitploit
date: 2026-09-07
fetch_date: 2026-09-08T06:41:02.398013
---

# Aegis v3.4.3

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/41532/4a2ed989d1d30ab15e61004ee0de37a62d3dce83ce48969bee8643bc6fe51668.png)

New releaseSep 7, 2026

# Aegis v3.4.3

A free, secure and open source app for Android to manage your 2-step verification tokens.

Share

![App icon](https://assets.kitploit.com/production/public/readmes/41532/dfad7e07b0a596480eaf29969383b41033535bc2e61770ac2cb5baa65392b411.png)

# Aegis Authenticator

[![Build](https://github.com/beemdevelopment/Aegis/actions/workflows/build-app-workflow.yaml/badge.svg)](https://github.com/beemdevelopment/Aegis/actions/workflows/build-app-workflow.yaml?query=branch%3Amaster) [![Crowdin](https://badges.crowdin.net/aegis-authenticator/localized.svg)](https://crowdin.com/project/aegis-authenticator) [![Donate](https://img.shields.io/badge/donate-buy%20us%20a%20beer-%23FF813F)](https://www.buymeacoffee.com/beemdevelopment) [![Matrix](https://img.shields.io/matrix/aegis:matrix.org?color=blue)](https://matrix.to/#/#aegis:matrix.org)

**Aegis Authenticator** is a free, secure and open source 2FA app for Android.
It aims to provide a secure authenticator for your online services, while also
including some features missing in existing authenticator apps, like proper
encryption and backups. Aegis supports HOTP and TOTP, making it compatible with
thousands of services.

For a list of frequently asked questions, please check out [the FAQ](https://github.com/beemdevelopment/aegis/blob/master/FAQ.md).

The security design of the app and the vault format is described in detail in
[this document](https://github.com/beemdevelopment/aegis/blob/master/docs/vault.md).

## Features

* Free and open source
* Secure
  + The vault is encrypted (AES-256-GCM), and can be unlocked with:
    - Password (scrypt)
    - Biometrics (Android Keystore)
  + Screen capture prevention
  + Tap to reveal
* Compatible with Google Authenticator
* Supports industry standard algorithms:
  [HOTP](https://tools.ietf.org/html/rfc4226) and
  [TOTP](https://tools.ietf.org/html/rfc6238)
* Lots of ways to add new entries
  + Scan a QR code or an image of one
  + Enter details manually
  + Import from other authenticator apps: 2FAS Authenticator, Authenticator
    Plus, Authy, andOTP, FreeOTP, FreeOTP+, Google Authenticator, Microsoft
    Authenticator, Plain text, Steam, TOTP Authenticator and WinAuth (root
    access is required for some of these)
* Organization
  + Alphabetic/custom sorting
  + Custom or automatically generated icons
  + Group entries together
  + Advanced entry editing
  + Search by name/issuer
* Material design with multiple themes: Light, Dark, AMOLED
* Export (plaintext or encrypted)
* Automatic backups of the vault to a location of your choosing

## Screenshots

[![Screenshot 1](https://assets.kitploit.com/production/public/readmes/41532/4a2ed989d1d30ab15e61004ee0de37a62d3dce83ce48969bee8643bc6fe51668.png)](https://github.com/beemdevelopment/aegis/blob/master/metadata/en-US/images/phoneScreenshots/screenshot1.png?raw=true)
[![Screenshot 2](https://assets.kitploit.com/production/public/readmes/41532/63db562421b1a2b5545ff131d32fc01340295399054fbe55acc4d02b6789af2c.png)](https://github.com/beemdevelopment/aegis/blob/master/metadata/en-US/images/phoneScreenshots/screenshot2.png?raw=true)
[![Screenshot 3](https://assets.kitploit.com/production/public/readmes/41532/90bd4058542f1ebf0c01ead96026eb28e325c84735b5ffcf48fa1fb6471203cf.png)](https://github.com/beemdevelopment/aegis/blob/master/metadata/en-US/images/phoneScreenshots/screenshot3.png?raw=true)
[![Screenshot 4](https://assets.kitploit.com/production/public/readmes/41532/a5ef9f8f980c373c66245cb6f98b8b066222b753a5ef39ef6436522c9c0dfb56.png)](https://github.com/beemdevelopment/aegis/blob/master/metadata/en-US/images/phoneScreenshots/screenshot4.png?raw=true)

[![Screenshot 5](https://assets.kitploit.com/production/public/readmes/41532/3b5d0ac72d2e4893de8fe0a29a92ea2c38b1c1fe5d80e89c9be27de5edf2be27.png)](https://github.com/beemdevelopment/aegis/blob/master/metadata/en-US/images/phoneScreenshots/screenshot5.png?raw=true)
[![Screenshot 6](https://assets.kitploit.com/production/public/readmes/41532/838b8a217b6061e1107994d6bde531c455d253a60dc5732265033c0371e87e21.png)](https://github.com/beemdevelopment/aegis/blob/master/metadata/en-US/images/phoneScreenshots/screenshot6.png?raw=true)
[![Screenshot 7](https://assets.kitploit.com/production/public/readmes/41532/620691bdeb956f52d509c237184dcca83e22e7306a1b49c2e0127b21273fc7e7.png)](https://github.com/beemdevelopment/aegis/blob/master/metadata/en-US/images/phoneScreenshots/screenshot7.png?raw=true)
[![Screenshot 8](https://assets.kitploit.com/production/public/readmes/41532/9c978917ea4ba36532e2756ebc44d86b46345ef6be8bdc6ec9b80e811ab3eeb9.png)](https://github.com/beemdevelopment/aegis/blob/master/metadata/en-US/images/phoneScreenshots/screenshot8.png?raw=true)

## Downloads

Aegis is available on the Google Play Store and on F-Droid.

[![Get it on Google Play](https://assets.kitploit.com/production/public/readmes/41532/f72611e2df8e88204009fd896d05d5e8e83c77009c63943bbffa169559934849.png)](https://play.google.com/store/apps/details?id=com.beemdevelopment.aegis)
[![Get it on F-Droid](https://assets.kitploit.com/production/public/readmes/41532/174f9e0e2098b799a6ab5211c1578410b7cac81ae42ed73003ac6fb12f572b0c.png)](https://f-droid.org/app/com.beemdevelopment.aegis)

### Verification

APK releases on Google Play and GitHub are signed using the same key. They can
be verified using
[apksigner](https://developer.android.com/studio/command-line/apksigner.html#options-verify):

root@kitploit:~

```
apksigner verify --print-certs --verbose aegis.apk
```

The output should look like:

root@kitploit:~

```
Verifies
Verified using v1 scheme (JAR signing): true
Verified using v2 scheme (APK Signature Scheme v2): true
```

The certificate fingerprints should correspond to the ones listed below:

root@kitploit:~

```
Owner: CN=Beem Development
Issuer: CN=Beem Development
Serial number: 172380c
Valid from: Sat Feb 09 14:05:49 CET 2019 until: Wed Feb 03 14:05:49 CET 2044
Certificate fingerprints:
   MD5:  AA:EE:86:DB:C7:B8:88:9F:1F:C9:D0:7A:EC:37:36:32
   SHA1: 59:FB:63:B7:1F:CE:95:74:6C:EB:1E:1A:CB:2C:2E:45:E5:FF:13:50
   SHA256: C6:DB:80:A8:E1:4E:52:30:C1:DE:84:15:EF:82:0D:13:DC:90:1D:8F:E3:3C:F3:AC:B5:7B:68:62:D8:58:A8:23
```

### Icon packs

Aegis supports icon packs to make it easier to assign icons to the entries in
your vault. There are no official icon packs, but the community maintains a
number of third-party icon packs you may want to check out. To learn how to
create your own Aegis-compatible icon pack, see [the
documentation](https://github.com/beemdevelopment/aegis/blob/master/docs/iconpacks.md).

* [aegis-icons](https://github.com/aegis-icons/aegis-icons)

  Unofficial monochrome-styled 2FA icons.

  [![aegis-icons preview](https://assets.kitploit.com/production/public/readmes/41532/5adf37c0f0b0a94dddd08af22640a8695a72f0265db13a4163acf1241f05653a.png)](https://github.com/aegis-icons/aegis-icons)
* [delta-aegis-icons](https://github.com/Delta-Icons/aegis-icons)

  Delta version of the unofficial monochrome-styled 2FA icon pack aegis-icons.

  [![delta-icons preview](https://assets.kitploit.com/production/public/readmes/41532/6a0e473aa14a18f372b70bf9c51d3f69e2405ddc91998ae18ae12e2ff5a5c582.png)](https://github.com/Delta-Icons/aegis-icons)
* [aegis-simple-icons](https://github.com/alexbakker/aegis-simple-icons) \*

  This project periodically generates an icon pack for Aegis based on [Simple
  Icons](https://simpleicons.org/).

  [![aegis-simple-icons preview](https://assets.kitploit.com/p...