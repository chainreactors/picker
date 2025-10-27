---
title: Intercepting traffic on Android with Mainline and Conscrypt
url: https://blog.nviso.eu/2025/06/05/intercepting-traffic-on-android-with-mainline-and-conscrypt/
source: NVISO Labs
date: 2025-06-06
fetch_date: 2025-10-06T22:52:04.182494
---

# Intercepting traffic on Android with Mainline and Conscrypt

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Intercepting traffic on Android with Mainline and Conscrypt

[Jeroen Beckers](https://blog.nviso.eu/author/jbeckers/ "Posts by Jeroen Beckers")

[Mobile Security](https://blog.nviso.eu/category/mobile-security/), [Android](https://blog.nviso.eu/category/mobile-security/android/)

June 5, 2025June 3, 2025
20 Minutes

**TL;DR:** The [AlwaysTrustUserCerts module](https://github.com/NVISOsecurity/AlwaysTrustUserCerts) now supports Android 7 until Android 16 Beta. If you want to learn more about Mainline, Conscrypt and how everything works together, keep reading!

## Intro

To properly test the backend of any mobile application, we need to intercept (and modify) the API traffic. We could use Swagger or Postman files if they are available, but it’s a lot easier to intercept real traffic so we don’t have to worry about providing correct values, sequencing, etc.

Sometimes intercepting traffic is very straightforward: You configure a device proxy, install your proxy certificate on the device and you’re good to go. This was even the default behavior [until Android stopped trusting user certificates by default](https://blog.nviso.eu/2017/12/22/intercepting-https-traffic-from-apps-on-android-7-using-magisk-burp/). On recent versions of Android, this will only work if the network security config has been modified to include user certificates, [or if the user certificate has been moved into the system certificate repository](https://github.com/NVISOsecurity/MagiskTrustUserCerts).

Android 14 (A14) made interception a bit more difficult by moving all root certificates to a Mainline module, as I’ll explain below. Recently though, one of our devices was showing the same behavior, even on A13. While I was surprised initially, it actually makes a lot of sense. Let’s dive in!

## Android’s Conscrypt module and Mainline

The [Conscrypt module](https://source.android.com/docs/core/ota/modular-system/conscrypt), which was introduced in Android 9, is used by the Android OS to verify the TLS certificates of HTTPS connections. It contains Conscrypt itself in the form of a Java security provider, and the BoringSSL library, Google’s Fork of OpenSSL. Conscrypt is still the default security provider on Android 15 (A15).

In Android 10, Google introduced [Mainline](https://source.android.com/docs/core/ota/modular-system), which is a way for Google to update certain parts of the Android OS without requiring an over-the-air (OTA) update. These updates are installed via the Google Play Services app and require an onboarded Google Play app. Since these Mainline updates are completely separated from system updates, even devices that no longer receive official OS updates can still receive security updates for selected components. Since the introduction in Android 10, many modules have been merged into Mainline, currently bringing the total to [33 modules](https://source.android.com/docs/core/ota/modular-system/wifi) for A15.

As a result, devices typically have two update levels:

* Android Security Update (ASU): Delivered as OTA updates by the OEM
* Google Play System Update (GPSU): Delivered by Google via Google Play

![](https://blog.nviso.eu/wp-content/uploads/2025/05/image-13.png)

An Android 13 (A13) device with two patch levels: The Android Security Update (ASU) level and the Google Play System Update (GPSU) level

Internally, Mainline modules are located in the `/apex/` folder and can be viewed with root permissions. On a fresh Android 13 (A13) installation (`UP1A.231005.007`), the `/apex/` folder might look as follows:

$ ls -lh /apex
total 256K
-rw-r–r– 1 root system 11K 2025-05-12 17:20 apex-info-list.xml
drwxr-xr-x 7 system system 4.0K 1970-01-01 01:00 com.android.adbd
drwxr-xr-x 7 system system 4.0K 1970-01-01 01:00 com.android.adbd@331314022
drwxr-xr-x 8 system system 4.0K 1970-01-01 01:00 com.android.adservices
drwxr-xr-x 8 system system 4.0K 1970-01-01 01:00 com.android.adservices@331418080
drwxr-xr-x 6 system system 4.0K 1970-01-01 01:00 com.android.apex.cts.shim
drwxr-xr-x 6 system system 4.0K 1970-01-01 01:00 com.android.apex.cts.shim@1
drwxr-xr-x 6 system system 4.0K 1970-01-01 01:00 com.android.appsearch
drwxr-xr-x 6 system system 4.0K 1970-01-01 01:00 com.android.appsearch@331311000
drwxr-xr-x 8 system system 4.0K 1970-01-01 01:00 com.android.art
drwxr-xr-x 8 system system 4.0K 1970-01-01 01:00 com.android.art@331413030
drwxr-xr-x 7 system system 4.0K 1970-01-01 01:00 com.android.btservices
drwxr-xr-x 7 system system 4.0K 1970-01-01 01:00 com.android.btservices@331716000
drwxr-xr-x 5 system system 4.0K 1970-01-01 01:00 com.android.cellbroadcast
drwxr-xr-x 5 system system 4.0K 1970-01-01 01:00 com.android.cellbroadcast@331411000
drwxr-xr-x 8 system system 4.0K 1970-01-01 01:00 com.android.compos
drwxr-xr-x 8 system system 4.0K 1970-01-01 01:00 com.android.compos@1
drwxr-xr-x 8 system system 4.0K 1970-01-01 01:00 com.android.conscrypt
drwxr-xr-x 8 system system 4.0K 1970-01-01 01:00 com.android.conscrypt@331411000

```
$ ls -lh /apex
total 256K
-rw-r--r--  1 root   system  11K 2025-05-12 17:20 apex-info-list.xml
drwxr-xr-x  7 system system 4.0K 1970-01-01 01:00 com.android.adbd
drwxr-xr-x  7 system system 4.0K 1970-01-01 01:00 com.android.adbd@331314022
drwxr-xr-x  8 system system 4.0K 1970-01-01 01:00 com.android.adservices
drwxr-xr-x  8 system system 4.0K 1970-01-01 01:00 com.android.adservices@331418080
drwxr-xr-x  6 system system 4.0K 1970-01-01 01:00 com.android.apex.cts.shim
drwxr-xr-x  6 system system 4.0K 1970-01-01 01:00 com.android.apex.cts.shim@1
drwxr-xr-x  6 system system 4.0K 1970-01-01 01:00 com.android.appsearch
drwxr-xr-x  6 system system 4.0K 1970-01-01 01:00 com.android.appsearch@331311000
drwxr-xr-x  8 system system 4.0K 1970-01-01 01:00 com.android.art
drwxr-xr-x  8 system system 4.0K 1970-01-01 01:00 com.android.art@331413030
drwxr-xr-x  7 system system 4.0K 1970-01-01 01:00 com.android.btservices
drwxr-xr-x  7 system system 4.0K 1970-01-01 01:00 com.android.btservices@331716000
drwxr-xr-x  5 system system 4.0K 1970-01-01 01:00 com.android.cellbroadcast
drwxr-xr-x  5 system system 4.0K 1970-01-01 01:00 com.android.cellbroadcast@331411000
drwxr-xr-x  8 system system 4.0K 1970-01-01 01:00 com.android.compos
drwxr-xr-x  8 system system 4.0K 1970-01-01 01:00 com.android.compos@1
drwxr-xr-x  8 system system 4.0K 1970-01-01 01:00 com.android.conscrypt
drwxr-xr-x  8 system syst...