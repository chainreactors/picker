---
title: How to Install LineageOS on Your Android Device
url: https://www.blackhillsinfosec.com/how-to-install-lineageos-on-your-android-device/
source: Black Hills Information Security
date: 2024-07-12
fetch_date: 2025-10-06T17:43:58.991049
---

# How to Install LineageOS on Your Android Device

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

11
Jul
2024

[Connor Costigan](https://www.blackhillsinfosec.com/category/author/connor-costigan/), [Hardware Hacking](https://www.blackhillsinfosec.com/category/how-to/hardware-hacking/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Mobile](https://www.blackhillsinfosec.com/category/red-team/mobile/)
[Android](https://www.blackhillsinfosec.com/tag/android/), [LineageOS](https://www.blackhillsinfosec.com/tag/lineageos/), [ROM Flashing](https://www.blackhillsinfosec.com/tag/rom-flashing/)

# [How to Install LineageOS on Your Android Device](https://www.blackhillsinfosec.com/how-to-install-lineageos-on-your-android-device/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/07/CCostigan-150x150.png)

| [Connor Costigan](https://www.blackhillsinfosec.com/team/connor-costigan/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/07/BLOG_chalkboard_000678-1024x576.png)

Hey guys, my name is Connor. I am a web developer here at BHIS who also loves hacking phones. Particularly, Android phones! Today, I am going to show you the basics on installing LineageOS onto your Android device while providing extra detail and background on the installation process as a whole. Although this tutorial is aimed at installing LineageOS specifically, the lessons taught here can be applied to installing other ROMs for your device.

### **What is Lineage? Why Lineage?**

To understand Lineage, it would be good to first go over a little bit of history regarding Android. Android’s Operating System is an open-source Linux operating system that is maintained by [Google](https://source.android.com/). This does not mean that someone can access the OS code for flagship phones such as the Samsung Galaxy, Google Pixel, OnePlus, etc. as they have added closed source code on top of the open-source base Android OS code. This baseline Android OS is exactly what LineageOS takes advantage of. It is a distribution of the open-source baseline Android code that is distributed for a massive number of smartphones. These distributions allow older phones to upgrade to newer Android OS versions without getting a factory update, extending the life of these phones greatly. This open-source version of Android also allows users to root their phones, giving them extra permissions as well as the removal of the Google API from the OS entirely (which is impossible with the built-in OS of most smartphones).

A WORD OF CAUTION BEFORE CONTINUING

Before continuing, it is worth noting that installing a new OS onto any Android device is risky. Data will be formatted during the installation process, which means you should make sure to **BACK UP ALL IMPORTANT FILES** before continuing! There is also the risk of “bricking” your smartphone. This is when the bootloader is no longer functional and cannot load either LineageOS or the original operating system, leaving the phone in an unusable state. During the installation, the option to not install GApps (Google apps, such as play store, Google Maps, Gmail, etc) will be available If you choose to not install GApps, just know that there will be apps that will not work properly and many that may not run entirely. Due to these potential dangers listed above, it is best to install LineageOS on a smartphone that is sitting on your shelf or in your drawer, and not the current phone you have in use. If you do wish to install LineageOS on your most current smartphone, proceed with caution!

#### What you need to get started

* An Android smartphone (preferably an older phone that is supported by LineageOS (see the supported devices [here](https://wiki.lineageos.org/devices/)) with developer mode enabled.

* A computer/laptop with Android ADB platform tools installed to an accessible directory (should include fastboot as well). We will go over downloading this in the tutorial, so do not worry if you do not have these yet.

* A wire capable of connecting and transferring data between your Android phone and computer. This usually can be a charging wire that is USB to Micro USB.

* A copy of the LineageOS ROM file for your specific device (we will go over getting this in the tutorial)

* A recovery ROM for fastboot. LineageOS offers their own recovery software that we will use, but TWRP is a common recovery ROM that people use as well. If you are already comfortable with TWRP, then feel free to use it!

* .APK files for installing any specific apps that require pre-boot installation (see recommendations below). These are not required to install the OS, but often are wanted by users and must be installed into the system before the first bootup of the OS.

* A can-do attitude!

Recommended (but optional) packages to install:
...