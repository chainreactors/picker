---
title: Analysis of FvncBot campaign
url: https://cert.pl/en/posts/2026/03/fvncbot-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-31
fetch_date: 2026-04-01T04:47:39.913914
---

# Analysis of FvncBot campaign

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

Analysis of FvncBot campaign

30 March 2026
| [Kacper Ratajczak](../../../../author/kacper-ratajczak/) | [#android](../../../../tag/android/), [#analysis](../../../../tag/analysis/), [#fvncbot](../../../../tag/fvncbot/)

CERT Polska has analyzed new samples associated with the FvncBot campaign targeting Polish users. This write-up is based on an SGB-branded variant.

## Basic information

The campaign samples are hosted on `ruvofech.it[.]com`, with no identified distribution source (as of the analysis date).

The app presents itself as `Token U2F Mobilna Ochrona SGB`, claims that a `Play Component` is required, and then guides the victim through the installation of a hidden second-stage application labeled `Android V.28.11`. After that, the victim is pushed into enabling an accessibility service presented as `System Update`. Once enabled, the implant registers the device with the attacker-controlled backend and begins sending telemetry.

#### How does that happen?

The flow from the perspective of the victim that was captured during dynamic analysis is as follows:

The user launches an application themed with the logo of one of the Polish banks (SGB). It is presented with a landing screen that displays `Play Component` Required and prompts the user to press `Install Component`.

![sgb1](../../../../uploads/2026/03/sgb_installed_1.png)
![sgb2](../../../../uploads/2026/03/sgb_landing_2.png)

Android opens the `Install unknown apps` screen for the app. The user is shown an installation prompt for `Android V.28.11`. After installation, the lure changes to an `Activate` button. Pressing it opens a `Setup Required` screen that instructs the user to enable an accessibility service.

![sgb3](../../../../uploads/2026/03/sgb_3.png)
![sbg4](../../../../uploads/2026/03/sgb_4.png)
![sgb5](../../../../uploads/2026/03/sgb_5.png)
![sgb6](../../../../uploads/2026/03/sgb_6.png)

After the service is enabled, the app displays `All Systems Operational`. In this campaign, all samples use different banks as disguises.

![sgb7](../../../../uploads/2026/03/sgb_ready_7.png)
![alior](../../../../uploads/2026/03/alior.png)
![paribas](../../../../uploads/2026/03/paribas.png)

This is the key social-engineering pattern in this campaign: the visible bank-themed lure does not perform the final malicious activity itself. Instead, it installs and activates a second-stage implant that hides behind Android/system default branding.

#### What did we find in the analyzed sample?

* The outer package is `com.junk.knock`, branded as `Token U2F Mobilna Ochrona SGB`.
* Then dynamically loads an installer stage from `/data/user/0/com.junk.knock/app_tell/tWyWeG.txt` using `DexClassLoader`.
* The runtime-loaded installer extracts `assets/apk/payload_grass.apk`, which is the visible second-stage implant.
* The installer uses `core://setup` to hand the victim into the second stage.
* The second stage is packaged as `com.core.town` and branded `Android V.28.11`.
* The `com.core.town` APK is itself another loader and hides an additional payload in a nested asset named `qkcCg.jpg`.
* The hidden asset is transformed with an RC4-like routine keyed by `sDjCM` and expands to the final implant dex.
* During dynamic execution, the final implant registers to `https://jeliornic.it.com/api/v1/devices/register` and receives per-device credentials.

#### How to protect yourself

* Download your bank application only from official application stores like Google Play Store or App Store.
* If you receive a phone call allegedly from your bank in which the caller warns you of a potential threat, hang up and call back using the number listed on the bankâs official website. This will help you avoid scams involving CLI spoofing.
* Treat any request to manually install a âsecurity componentâ or âruntime componentâ (Play Component) from the outside of the Google Play as highly suspicious.
* If an app asks for `Install unknown apps` and then accessibility access, treat that as a critical warning sign.

## Technical analysis

Every Android application starts with an `AndroidManifest.xml` file. In this case, the manifest already shows that the outer SGB-branded app is designed to work with another package, `com.core.town`, and its provider.

#### Manifest and lure strings

```
<queries>
    <package android:name="com.core.town"/>
    <provider android:authorities="com.core.town.provider"/>
</queries>
...
<application
    android:label="@string/app_name"
    android:name="com.erupt.defense.Scementplanet">
    <receiver android:name="com.gallery.oppose.OpposeHelper$InstallResultReceiver" ... />
    <activity android:name="com.gallery.oppose.OpposeActivity" ... >
```

The strings shown to the victim are not incidental; they are the operatorâs guided installation flow:

```
<string name="app_name">Token U2F Mobilna Ochrona SGB</string>
<string name="component_required_title">Play Component Required</string>
<string name="component_install_description">The Play Component ensures secure and stable application functionality. Installation will take just a few seconds.</string>
<string name="install_button">Install Component</string>
<string name="permission_required">Installation permission required</string>
<string name="permission_granted">Permission granted! Try again</string>
<string name="component_active_title">All Systems Operational</string>
```

#### Stage 1 loader: private path + DexClassLoader

The outer application class initializes the private directories and file name used for runtime loading:

```
public String i = "bonus";
public String j = "tell";
...
public String r = "tWyWeG.txt";
...
return context.getDir(this.j, 0);
...
return new File(str, this.r);
```

It also decodes staged content and forwards control into a reflective loader helper:

```
byte[] bArr3 = {91, 5, 10};
...
bArr2[i9] = (byte) (bArr[i9] ^ bArr3[i9 % length2]);
...
this.s.a(str, str2, stringBuffer.toString(), context);
```

The helper is explicit about the loading mechanism and specifically uses `DexClassLoader`:

```
public DexClassLoader a(String str, String str2, String str3, Field field, WeakReference weakReference) throws NoSuchMethodException {
    Constructor constructor = DexClassLoader.class.getConstructor(String.class, String.class, String.class, ClassLoader.class);
    Object[] objArr = new Object[4];
    objArr[0] = str;
    objArr[1] = str2...