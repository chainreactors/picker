---
title: Dissecting an Android stalkerware
url: https://andpalmier.com/posts/stalkerware-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-31
fetch_date: 2025-10-04T02:48:27.928254
---

# Dissecting an Android stalkerware

[↓Skip to main content](#main-content)

[andpalmier](/)

[Home](/)
[About](/about/)

* [Home](/)
* [About](/about/)

# Dissecting an Android stalkerware

11 January 2023·13 mins

![andpalmier](/img/img_hu15764436753934245777.jpeg)

Author

andpalmier

cyber threat researcher, eternal noob, As Roma fan

Table of Contents

* [What is stalkerware?](#what-is-stalkerware)
* [The website](#the-website)
* [Features](#features)
* [Analysis of the sample](#analysis-of-the-sample)
  + [Permissions requested](#permissions-requested)
  + [Randomly generated package name](#randomly-generated-package-name)
  + [Getting the PIN](#getting-the-pin)
  + [Extracting and sending media files](#extracting-and-sending-media-files)
  + [Screen and audio recording](#screen-and-audio-recording)
  + [GPS location](#gps-location)
* [Closing remarks](#closing-remarks)
  + [Mitre ATT&CK Tactics And Techniques](#mitre-attck-tactics-and-techniques)
  + [YARA](#yara)
  + [IOCs](#iocs)

Table of Contents

* [What is stalkerware?](#what-is-stalkerware)
* [The website](#the-website)
* [Features](#features)
* [Analysis of the sample](#analysis-of-the-sample)
  + [Permissions requested](#permissions-requested)
  + [Randomly generated package name](#randomly-generated-package-name)
  + [Getting the PIN](#getting-the-pin)
  + [Extracting and sending media files](#extracting-and-sending-media-files)
  + [Screen and audio recording](#screen-and-audio-recording)
  + [GPS location](#gps-location)
* [Closing remarks](#closing-remarks)
  + [Mitre ATT&CK Tactics And Techniques](#mitre-attck-tactics-and-techniques)
  + [YARA](#yara)
  + [IOCs](#iocs)

In this technical blog post, we will examine the components of a stalkerware app designed for Android devices and marketed towards Italian customers. By analyzing the various components of this type of software, hopefully we can gain a deeper understanding of how these apps operate and develop strategies for detecting and removing it from infected devices.

## What is stalkerware?

Stalkerware is a type of malicious software that is designed to track and monitor someone’s digital activity without their knowledge or consent. This type of software is often used by individuals who want to spy on their partners or children, or by employers who want to monitor the activity of their employees. Stalkerware can be used to track a wide range of digital activity, including web searches, geolocation, text messages and chats, photos, voice calls, and more. The use of stalkerware is generally considered unethical and may also be illegal, as it violates the privacy of the targeted individual.

These apps are often distributed as paid services outside of the Google Play Store, as Google’s Developer Program Policy prohibits the distribution of apps that collect and transmit personal or sensitive data from a device without adequate notice or consent ([Developer Program Policy: September 16, 2020 announcement](https://support.google.com/googleplay/android-developer/answer/10065487)).

In this post, we will be focusing on a specific Android sample which was developed for the Italian market, as it was advertised in a website in Italian and the code of the sample contains numerous Italian expressions.

## The website

The app is described on the website as a tool for “secretly spying Android phones without being noticed by the owner of the smartphone”. The company behind the app claims to be active in 24 countries around the world, with headquarters in Europe, New Zealand, Brazil, and Canada.

The website of the app includes an End-User License Agreement (EULA) stating that the app should only be installed on devices owned by the user, and it also requires the user to notify any person using a device with the software installed, or any other person with the right to access a monitored account, of the presence of the software.

!['End-User License agreement' from the website of the app](/images/posts/stalkerware-analysis/eula.png)

‘End-User License Agreement’ from the website of the app. The highlighted section roughly translates to ‘*you also agree to notify on the presence of the software any person using a device with the software installed, or any other person with the right to access a monitored account*’.

However, according to the company’s website, the most common reason that clients use their stalkerware service is for “relationship cheating” with 40% of respondents citing this as their motivation; 32% of respondents said that they were using the service to monitor their minor children, and 11% cited “personal curiosity, no real reason”.

!['Reasons for using the spy app' from the website of the app](/images/posts/stalkerware-analysis/reasons.png)

‘Reasons for using the spy app’ from the website of the app

The licensing model for this stalkerware app includes a free trial of 3 days, during which users have access to all of the features of the app and the online panel for viewing the data captured from the device. After the free trial expires, users must pay a fee of €22 per month to continue using the service. This fee can be paid via PayPal or credit card, after registering in the admin panel of the website.

## Features

The list of features advertised include the ability to extract WhatsApp audios, pictures, and videos, access all media files on the phone, record calls and ambient audio, record the screen, report on notifications received, list installed apps, and track the phone’s location. The website of the app also claims that it is “invisible” to the user of the phone and to many antivirus solutions.

To use this stalkerware app, the user must have physical access to the victim’s phone and enable the installation of “unknown apps” from the Android settings. This process can be a bit tedious for non-experienced users, so the website provides various guides and short videos to help users download and install the app on different Android devices and access the panel to view the stolen information.

## Analysis of the sample

The apk sample can be downloaded directly from the website. At time of writing, the sample is not listed in VirusTotal, but we can use a small tool I wrote called apkingo to gather some information on the app:

[andpalmier/apkingo

extract info from apk files

Go

70

12](https://github.com/andpalmier/apkingo)

```
App name:	X Android Antivirus

* General info
PackageName:	com.vitefa.fosupevilucugo
Version:	1.0
MainActivity:	com.vitefa.fosupevilucugo.MainActivity
MinimumSdk:	22 (Android 5.1)
TargetSdk:	31 (Android 12)

* Hash values
Md5:		67f5f3b3c858453fdc0c901d3f09f985
Sha1:		86504d29d3d5a852e8e37c951c049917a9b11907
Sha256:		5ab4ff9f8028c02cbb0886922142227732cfe3aaec99af1a5af2ddb43b0fb5a8

* Permissions
android.permission.ACCESS_NETWORK_STATE
android.permission.READ_SYNC_STATS
android.permission.WRITE_SYNC_SETTINGS
android.permission.AUTHENTICATE_ACCOUNTS
android.permission.READ_SYNC_SETTINGS
android.permission.ACCESS_COARSE_LOCATION
android.permission.ACCESS_FINE_LOCATION
android.permission.ACCESS_LOCATION_EXTRA_COMMANDS
android.permission.ACCESS_NOTIFICATION_POLICY
android.permission.ACCESS_WIFI_STATE
android.permission.ACCESS_WIMAX_STATE
android.permission.ACTION_MANAGE_OVERLAY_PERMISSION
android.permission.BODY_SENSORS
android.permission.BROADCAST_STICKY
android.permission.CALL_PHONE
android.permission.CAMERA
android.permission.CHANGE_NETWORK_STATE
android.permission.CHANGE_WIFI_MULTICAST_STATE
android.permission.CHANGE_WIFI_STATE
android.permission.CHANGE_WIMAX_STATE
android.permission.DISABLE_KEYGUARD
android.permission.GET_ACCOUNTS
android.permission.INTERNET
android.permission.MANAGE_ACCOUNTS
android.permission.MODIFY_AUDIO_SETTINGS
android.permission.PERSISTENT_ACTIVITY
android.permission.PROCESS_OUTGOING_CALLS
android.permission.PACKAGE_USAGE_STATS
android.permission.READ_CELL_BROADCASTS
android.permission.READ_CONTACTS
android.permission.READ_EXTERNAL_STORAGE
android.permission.READ_PHONE_STATE
android.permission.READ_I...