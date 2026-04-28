---
title: Osservatorio Nessuno
url: https://osservatorionessuno.org/blog/2026/04/morpheus-a-new-spyware-linked-to-ips-intelligence/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-27
fetch_date: 2026-04-28T05:28:29.562704
---

# Osservatorio Nessuno

[Skip to main content](#main-content)
[ ]

[![logo-osservatorio-nessuno](/imgs/logo.svg)
Osservatorio Nessuno](/)

* About us
  About us
  + [Organization](/association "Organization")
  + [Announcements](/categories/organization "Announcements")
  + [Contacts](/contacts "Contacts")
  + [Donate](/donate "Donate")
* Anonymity
  Anonymity
  + [The Tor Network](/tor "The Tor Network")
  + [Infrastructure](/categories/infrastructure "Infrastructure")
  + [Our Exit Nodes](/nodes "Our Exit Nodes")
* Surveillance
  Surveillance
  + [Digital Surveillance](/surveillance "Digital Surveillance")
  + [Research](/categories/research "Research")
  + [Nascondino](/nascondino "Nascondino")
* Activism
  Activism
  + [Advocacy](/categories/advocacy "Advocacy")
* [News](/blog)
* en
  en
  + [it](/it/blog/2026/04/morpheus-un-nuovo-spyware-collegato-a-ips-intelligence/ "it")

Menu

# Morpheus: A new Spyware linked to IPS Intelligence.

*23 April 2026* -
[Research](/categories/research)

*If you are an activist or journalist concerned about the security of your devices, or if your device has been seized and you need technical assistance, [contact us](/contacts/).*

We have analyzed a sample of a previously unknown Android spyware, likely developed in Italy. It is named “**Morpheus**”, version **2025.3.0**, and we describe its capabilities, including abusing accessibility features, automatically enabling ADB and issuing commands, disabling microphone and camera indicators, pairing additional WhatsApp devices, taking screenshots, recording audio and video, and more. We link part of the infrastructure to [IPS Intelligence](/nascondino/ips/), and discover some potentially related companies, Rever Servicenet and Iris Telecomunicazioni.

## The Spyware [#](#the-spyware)

### Infection [#](#infection)

As reported many times both [by us](https://osservatorionessuno.org/blog/2026/04/italian-spyware-maker-sio-still-developing-and-distributing-spyrtacus/) and [other well-documented cases by activists and other sources](https://arachidi.noblogs.org/), the infection mechanism is the usual for low cost spyware: deny a service to the target and then social engineer them to install an app in order to restore or obtain such service. This is often applied to mobile data, but not necessarily restricted to it. In this case, the person under attack received an SMS pointing to `assistenza-sim.it`. The app impersonated the Fastweb ISP.

### First Stage: The Dropper [#](#first-stage-the-dropper)

The dropper uses the `com.android.cored` package name, with `versionCode="1"` and `versionName="0.9.23"`.

The dropper application is a fork of [solrudev’s SimpleInstaller](https://github.com/solrudev/SimpleInstaller), an open-source rudimentary Android package installer wrapper that makes it easy to install third-party apps.

The code of the installer’s `io.github.solrudev.simpleinstaller.sampleapp.ui.MainActivity` was edited to automate the installation of the second stage of the spyware. The second stage is directly embedded inside the APK at `/assets/mobile-config.apk`.

Once the person under surveillance executes the dropper:

1. It checks if the second stage is already installed querying for the `com.android.core` package name
2. If it is not the case, it copies the `mobile-config.apk` from the `assets` folder of the APK to the device storage
3. If an external intent with action `action_gustavo` is received, the dropper installs the second stage
4. If the user has granted `REQUEST_INSTALL_PACKAGES` and `READ_EXTERNAL_STORAGE` permissions to the dropper, it installs the second stage

![Infection first stage: informing of an update](/blog/2026-04-22-morpheus-spyware-3_hu_eaaacb416e9524ee.webp)

Infection first stage: informing of an update

![Infection first stage: second stage successfully installed](/blog/2026-04-22-morpheus-spyware-4_hu_f26b984c9b8c9124.webp)

Infection first stage: second stage successfully installed

### Second Stage: The Agent [#](#second-stage-the-agent)

The agent uses the `com.android.core` package name, with `versionCode="1"` and `versionName="2025.3.0"`.

Inside of the `AndroidManifest.xml` the application defines multiple activities, receivers and services.
The most interesting are:

* `com.android.main.SplashScreenActivity` with label `Mobile Config`
* `com.android.main.FakeServiceActivity` with label `Impostazioni microG` alias of `SplashScreenActivity`, posing as a fake [microG](https://github.com/microg) Settings icon.
* `com.android.main.Launcher2Activity` with label `PlayProtect` alias of `SplashScreenActivity`, posing as a fake [Google Play Protect](https://support.google.com/googleplay/answer/2812853) icon.
* `com.android.main.LauncherActivity` with label `Mobile Config` alias of `SplashScreenActivity`
* `com.android.main.MainActivity`
* `com.android.main.AboutAppActivity`, showing a generic about UI.
* `com.android.main.EmptyActivity`
* `com.android.main.ForcePermissionsActivity`, forcing the user to enable the required permissions.
* `com.android.broadcast.CoreBroadcastReceiver`, a receiver with `RECEIVE_BOOT_COMPLETED` permission.
* `com.android.admin.DeviceAdminSampleReceiver`, a receiver with `BIND_DEVICE_ADMIN` permission.
* `com.android.core.CoreService`, a service with `BIND_ACCESSIBILITY_SERVICE` permission.

The `CoreService` handles all the [Accessibility](https://support.google.com/googleplay/android-developer/answer/10964491) actions. **Accessibility Services** are designed to help users with disabilities access their devices. Such applications can read the whole screen, click on graphical elements, interact with other applications. Unfortunately, this powerful capability is often exploited by malware, prompting Google to roll out a [series of mitigations](https://www.malwarebytes.com/blog/mobile/2026/03/google-cracks-down-on-android-apps-abusing-accessibility).

The sample declares [`isAccessibilityTool="true"`](https://developer.android.com/reference/android/R.styleable#AccessibilityService_isAccessibilityTool) in the manifest to pose itself as a legitimate accessibility tool and to obtain the full Accessibility permission set.
Starting with Android 13, apps that are sideloaded (installed outside of Google Play) are blocked from obtaining Accessibility privileges due to the [Restricted Settings](https://techwiser.com/how-to-bypass-restricted-accessibility-settings-on-android-13-14/) feature.
The dropperâinstallation technique circumvents this restriction, allowing the malicious app to gain the needed permissions despite the intended protection.

The `CoreBroadcastReceiver` listens for the systemâs bootâcompleted broadcast, enabling the app to reâlaunch automatically after a device reboot and thereby maintain **persistence**. The `DeviceAdminSampleReceiver` is the component that receives Deviceâadmin callbacks, allowing the application to acquire and manage **Deviceâadmin privileges**.

When the person under attack launches the app, they see a screen that offers to *scan* for problems with either the **SIM** or the **network connection**, a phishing pretext designed to coerce them into cooperation.

Once the scan finishes, the **Update configurations** button becomes enabled; tapping it opens the Settings page where the app requests **Accessibility** privileges.

![The second stage (agent) welcome screen](/blog/2026-04-22-morpheus-spyware-5_hu_bd4367ad1f632a83.webp)

The second stage (agent) welcome screen

## Techniques [#](#techniques)

### Abusing Overlay & Accessibility to Bypass Biometric Authentication [#](#abusing-overlay--accessibility-to-bypass-biometric-authentication)

If the preceding *shenanigans* weren’t alarming enough, the sheer number of permissions the app requests further confirms its malicious intent.

![Permissions request from the second stage](/blog/2026-04-22-morpheus-spyware-6_hu_c09c499d7bdf5240.webp)

Permissions request from the second stage

The [`SYSTEM_ALERT_WINDOW`](https://developer.android.com/referen...