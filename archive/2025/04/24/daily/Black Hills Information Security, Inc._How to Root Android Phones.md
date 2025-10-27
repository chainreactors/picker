---
title: How to Root Android Phones
url: https://www.blackhillsinfosec.com/how-to-root-android-phones/
source: Black Hills Information Security, Inc.
date: 2025-04-24
fetch_date: 2025-10-06T22:06:26.208637
---

# How to Root Android Phones

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

23
Apr
2025

[Dave Blandford](https://www.blackhillsinfosec.com/category/author/dave-blandford/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Mobile](https://www.blackhillsinfosec.com/category/red-team/mobile/)
[Android](https://www.blackhillsinfosec.com/tag/android/), [root](https://www.blackhillsinfosec.com/tag/root/), [root user](https://www.blackhillsinfosec.com/tag/root-user/), [Rooting](https://www.blackhillsinfosec.com/tag/rooting/), [superuser](https://www.blackhillsinfosec.com/tag/superuser/)

# [How to Root Android Phones](https://www.blackhillsinfosec.com/how-to-root-android-phones/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/10/DBlandford-150x150.png)

| [Dave Blandford](https://www.blackhillsinfosec.com/team/david-blandford/)

*Penetration Tester. Developer. Pure GNU/Linux Phone Enthusiast*.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/RootAndroid_header.png)

This blog will cover how to root an AVD emulator and a physical Pixel 6. But before we cover those topics, let’s cover what it is we will be doing and some of the pro/cons of rooting an Android phone.

#### First – What is rooting?

Rooting an Android device is a term used for bypassing device restrictions and becoming *superuser* — often called the “root user,” or just “root.” As superuser, user will have access to system level resources and have greater access on the device.

#### Second – Why would I want to root a device?

Testing mobile applications for Android usually requires a rooted device. As mentioned above, rooting will give us superuser access on the phone, which allows us to perform actions that make testing easier (e.g. installing proxy CA certificate in system).

The Android operating system is based on the Android Open Source Project (AOSP) (<https://source.android.com/>), which is the official open-source initiative maintained by Google for the development of the Android operating system. Its purpose is to provide the source code and tools necessary to allow developers, hardware manufacturers, and anyone else to build their own custom versions of Android.

A quick note about the AOSP. The device manufacturer (e.g. Samsung) and the carrier (e.g. T-Mobile) will add to their own updates and changes to their version of Android, so their version of Android on each is based off the AOSP but not a 1:1 match. Updates to Android go through the carrier and device manufacturer before they reach the device. Testing with Google devices bought directly from Google (and not through a carrier) is my recommendation because it is closest to the AOSP.

There are also custom ROMs that a user can flash on an Android device that are different than the AOSP.

##### What is a ROM?

A ROM is custom firmware that can be flashed on the device. The name is a legacy namesake that is still used. ROM stands for Read Only Memory, which is where the firmware was on older Android devices. The firmware on modern phones is stored in the internal flash memory. ROM is a name that stuck to mean custom firmware.

Examples of custom ROMS:

* GrapheneOS – <https://grapheneos.org/>
  + The team does great work! A privacy focused ROM
* CalyxOS – <https://calyxos.org/>
  + Privacy-based custom ROM
  + Fun fact about the Calyx Institute (the team that supports CalyxOS) – They have an unlimited mobile internet solution — (<https://calyxinstitute.org/membership/internet>). Sharing because I think it is cool 🙂

#### Third – Bypass security controls (That sounds bad…)

It is. Be careful when rooting a personal phone. (I am not endorsing that you do that and would strongly advise against rooting a personal phone.) If you do decide to root your personal phone, be sure to lock the bootloader after you do what you intended (e.g. installing a custom ROM).

Running sensitive applications (e.g. banking, email client for work) is not recommended on a rooted phone for several reasons. The application is running on a phone where other applications may have access to everything, including the app’s data directory. A couple rules of thumb — always assume the app is not secure, keep protections in place to prevent data loss (e.g. session tokens stored in application’s data directory that another application can access). I could write an entirely new blog/book on this topic but always assume that an application running on your phone wants access to all the data from other apps on your phone (https://techcrunch.com/2024/03/26/facebook-secret-project-snooped-snapchat-user-traffic/). Rooting the phone makes it easier for apps (and attackers) to access information that should not be made available to that app or perform unwarranted actions against another ...