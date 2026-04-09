---
title: Analysis of cifrat: could this be an evolution of a mobile RAT?
url: https://cert.pl/en/posts/2026/04/cifrat-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-08
fetch_date: 2026-04-09T04:32:10.065062
---

# Analysis of cifrat: could this be an evolution of a mobile RAT?

[Report an incident](https://incydent.cert.pl/#!/lang=en)

Back

* You're in the menu
* About us
  + About us
  + [About our team](../../../../about-us/)
  + [Contact](../../../../contact/)
* For experts
  + For experts
  + [News](../../../../news/)
  + [Publications](../../../../publications/)
  + [The Warning List](../../../../warning-list/)
  + Projects
  + [n6](../../../../n6/)
  + [Artemis](/en/posts/2024/01/artemis-security-scanner/)
  + [MWDB](https://mwdb.cert.pl/)
  + CVD program
  + [CVD policy](../../../../cvd)
  + [Advisories](../../../../cve)

* About us
* For experts

[Report an incident](https://incydent.cert.pl/#!/lang=en)

About us

[About our team](../../../../about-us/)
[Contact](../../../../contact/)

Baza wiedzy

[FaÅszywe inwestycje](/falszywe-inwestycje)
[UwaÅ¼aj na faÅszywe sklepy online](/falszywe-sklepy)
[(Nie)bezpieczne pÅatnoÅci](/baza-wiedzy/niebezpieczne-platnosci)
[FaÅszywi konsultanci](/baza-wiedzy/falszywi-konsultanci)
[Zadbaj o bezpieczne hasÅa i logowanie](/bezpieczne-hasla)
[FaÅszywe zaÅÄczniki w mailach](/falszywe-zalaczniki)
[FaÅszywe proÅby o szybki przelew](/szybkie-przelewy)
[FaÅszywe SMSy - plaga ostatnich miesiÄcy](/baza-wiedzy/falszywe-smsy)
[Bezpieczny telefon](/bezpieczny-telefon)

Biuletyn OUCH!

[Porady bezpieczeÅstwa OUCH!](/ouch)

For experts

[Publications](../../../../publications/)
[The Warning List](../../../../warning-list/)

Projects

[n6](../../../../n6/)
[Artemis](/en/posts/2024/01/artemis-security-scanner/)
[MWDB](https://mwdb.cert.pl/)

CVD program

[CVD policy](../../../../cvd)
[Advisories](../../../../cve)

Analysis of cifrat: could this be an evolution of a mobile RAT?

03 April 2026
| [Kacper Ratajczak](../../../../author/kacper-ratajczak/) | [#android](../../../../tag/android/), [#analysis](../../../../tag/analysis/), [#booking](../../../../tag/booking/), [#banker](../../../../tag/banker/), [#rat](../../../../tag/rat/)

CERT Polska has analyzed an android malware sample distributed through infrastructure impersonating *Booking.com*. We refer to it as `cifrat` (a name derived from the the `io.cifnzm.utility67pu` package name and its RAT functionality) for this analysis purpose because, we could not confidently map it to a known family name (as of the analysis date).

The analyzed sample was delivered through a phishing chain that ended with a fake Booking Pulse application update page and a malicious APK download. The visible app was only the beginning of the infection path. Static and dynamic reverse engineering showed that the downloaded APK was a multi stage dropper that unpacked a second APK, then a hidden final payload, and ultimately deployed an accessibility controlled RAT communicating over WebSockets.

## Basic information

The infection chain starts with a phishing email. The victim is encouraged to click a link, which first leads them to:

`https://share.google/Yc9fcYQCgnKxNfRmH`

and then redirects them to:

`https://booking.interaction.lat/starting/`

That final page presents itself as a *Booking.com* branded security/update prompt and offers a malicious APK download:

* `com.pulsebookmanager.helper.apk` - `d408588683b4e66bfe0b5bb557999844fe52d1bfbda6836a48e15290082a5d42`

The downloaded app is the outer dropper. After installation, it loads a native library, decrypts another embedded APK disguised as `Google Play Services`, and that second APK decrypts one more hidden stage. The final recovered payload is a full Android RAT that abuses accessibility features and has support for overlay injection, SMS access, screen streaming, camera capture, remote gestures, and SOCKS5 tunneling.

#### How does that happen?

The infection flow observed from the victim side is as follows.

The victim first receives a phishing email. The message uses social engineering to persuade the recipient to click a link embedded in the body.

![email](../../../../uploads/2026/04/email.jpeg)
![booking](../../../../uploads/2026/04/fake_booking.png)

Clicking the phishing link redirects the victim through `share.google/Yc9fcYQCgnKxNfRmH` and then to `booking.interaction.lat/starting/`. On that page, the user sees a fake *Booking.com* branded update message claiming that a security update is required. Pressing `Aktualizuj teraz` button leads to the download of `com.pulsebookmanager.helper.apk`. Downloaded application is impersonating *Booking.com* pulse app:

![pulse](../../../../uploads/2026/04/pulse.png)

Once installed, the app does not immediately expose its final malicious behavior. Instead, it acts as a delivery shell. It loads a native decoder, decrypts an embedded second stage APK, and installs that second stage under the package `io.cifnzm.utility67pu`, labeled `Google Play Services`.

That second stage APK is still not the final payload. Its `Application` class extracts another hidden asset named `FH.svg`, decrypts it, treats the result as a ZIP archive, loads hidden dex files from it, and then transfers execution into the actual malware module.

At that point the malware becomes a fully functional RAT. The recovered final stage contains screen streaming support, keylogging, HTML injection, SMS collection, camera support, remote gestures, device manipulation, and a dual WebSocket control plane connected to `otptrade.world` C2 server.

#### What did we find in the analyzed sample?

* The downloaded package of the APK is `com.pulsebookmanager.helper`, labeled `Pulse`.
* The outer APK drops and loads a native library `l0a0cac5c.so`.
* That native library decodes hidden strings and gates the rest of the installation flow.
* The outer APK decrypts `res/raw/init_bundle_uzge.bin` with a 32-byte XOR key and installs the result as `io.cifnzm.utility67pu`.
* The installed second stage APK is labeled `Google Play Services`.
* The second stage APK extracts a hidden asset named `FH.svg`.
* `FH.svg` is decrypted with an RC4-like routine keyed by `mLYQ`.
* The decrypted blob contains the final dex files.
* The final malware module communicates with `otptrade.world` over split control/data WebSocket channels.

#### How to protect yourself

* Download your applications only from official application stores like Google Play Store or App Store.
* Treat any app update delivered from a browser page as suspicious, especially when it asks you to sideload an APK.
* If an app asks for accessibility access, screen capture permissions, notification access, or overlay privileges after sideload installation, treat that as a critical warning sign.

## Technical analysis

Every Android application starts with an `AndroidManifest.xml` file. In this sample, the manifest already shows that the downloaded *Booking.com* themed APK is not a normal standalone application. Before any code is decompiled, the manifest reveals a staged installer design: the app requests sideload permissions, explicitly expects another package to exist, uses a custom `Application` class for early bootstrap, and monitors package installation events.

#### AndroidManifest.xml analysis

The first useful indicator is the manifest of the outer APK. Even without decompiling Java code, it already shows a sideloading oriented application that expects a second package to appear and monitors installation events.

```
<uses-permission android:name="android.permission.REQUEST_INSTALL_PACKAGES"/>
<uses-permission android:name="android.permission.INTERNET"/>
<queries>
    <intent>
        <action android:name="android.intent.action.MAIN"/>
    </intent>
    <package android:name="io.cifnzm.utility67pu"/>
</queries>
```

```
<application android:allowBackup="true" android:dataExtractionRules="@xml/data_extraction_rules" android:extractNativeLibs="true" android:fullBackupContent="@xml/backup_rules" android:hardwareAccelerated="true" android:icon="@mipmap/ic_launcher" android:label="Pulse" android:largeHeap="true" android:name="v0a0cac5c.l0a0cac5c" android:networkSecurityConfig="@xml/network_security_config" android:requestLegacyExternalStorage="true" andr...