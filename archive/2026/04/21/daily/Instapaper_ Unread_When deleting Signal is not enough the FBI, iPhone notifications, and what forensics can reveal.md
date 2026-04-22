---
title: When deleting Signal is not enough the FBI, iPhone notifications, and what forensics can reveal
url: https://andreafortuna.org/2026/04/11/signal-fbi-iphone-notifications-forensics/
source: Instapaper: Unread
date: 2026-04-21
fetch_date: 2026-04-22T04:45:09.319516
---

# When deleting Signal is not enough the FBI, iPhone notifications, and what forensics can reveal

[Andrea Fortuna](/)
[ ]

[About](/about/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# When deleting Signal is not enough: the FBI, iPhone notifications, and what forensics can reveal

Apr 11, 2026

by [Andrea Fortuna](/about/)

A few days ago, [404 Media published a detailed report](https://www.404media.co/fbi-extracts-suspects-deleted-signal-messages-saved-in-iphone-notification-database-2/) that made a lot of people uncomfortable: the FBI managed to recover Signal messages from a suspect’s iPhone, even though the app had already been uninstalled. No encryption was broken. No Signal server was compromised. The messages were sitting in the phone’s own notification database, waiting to be found.

![cover](/assets/2026/signal-fbi-cover.jpg)

The case itself involves a relatively minor charge, vandalism in the United States, but the forensic technique that emerged from the related court proceedings is genuinely interesting and worth unpacking in some detail. This case is not about Signal’s cryptography. It is about iOS data persistence and the false assumption that uninstalling an app deletes all evidence.

## What actually happened in court

According to the 404 Media reconstruction, an FBI agent testified during the trial that some incoming Signal messages had been recovered from the defendant’s iPhone through what was described as Apple’s internal notification storage. Signal was no longer installed on the device, but the text of previously received notifications was still present in the system’s notification database.

There is an important detail to keep in mind here: only incoming messages were recovered, not outgoing ones. This is entirely consistent with how push notifications work. When someone sends you a message on Signal, the app server pushes a notification to Apple’s infrastructure, which then delivers it to your device. If the notification content was not stripped before delivery, the text lands in the operating system’s notification database. Outgoing messages, which originate directly from your device to the server, never go through this pathway and therefore leave no equivalent trace.

The defendant apparently had Signal’s notification preview setting enabled, meaning the content of incoming messages was included in the notification payload and saved by iOS as part of its normal operation. That single configuration choice turned a security-conscious application into a source of recoverable evidence.

## Inside Apple’s push notification system

![ios push](/assets/2026/ios-push-info.jpg)

To understand why this data persists, first look at how Apple Push Notification service (APNs) operates. APNs is the central, cloud-based gateway through which all remote notifications must pass before reaching an Apple device. It acts as an intelligent broker: receiving notification requests from app provider servers, validating them, and routing them to the correct destination over a secure connection.

Before any notification can be delivered, an initial registration sequence must take place. When you first install a messaging app and allow notifications, iOS asks the user for permission. Once granted, the system communicates with APNs and receives a unique device token. The app then forwards this token to its backend server.

When someone sends you a message, the app’s server constructs a JSON payload (up to 4 KB) containing the notification instructions and sends it to APNs, which encrypted device token in hand, routes it to your specific device. The payload contains an `aps` dictionary where developers specify elements like the alert title and body, sound, badge counts, and specific flags.

A critical flag is `mutable-content: 1`. If present, it wakes the app via a Notification Service Extension before the alert is shown to the user. This is exactly what end-to-end encrypted messaging apps like Signal use: the incoming notification itself does not contain the readable message, but once the extension kicks in, it decrypts the payload and modifies the notification content locally before it hits the screen.

Forensic examiners focus on this detail: iOS does not discard notification data immediately after display. The system keeps a notification database on the device, and uninstalling an app does not automatically delete it. The push notification token associated with an app is also not immediately invalidated upon removal, so servers can technically continue sending notifications even after the app is gone, though the operating system will ultimately handle them without a corresponding app to receive them.

Apple recently updated its APNs token authentication system, as [announced on the developer portal in early 2025](https://developer.apple.com/news/?id=wy4tb0uo), introducing team-scoped and topic-specific keys to improve security and traceability. Whether this change has any bearing on the notification persistence issue is unclear, but the timing is at minimum worth noting.

## The notification database as a forensic artifact

The relevant database on iOS lives within the system’s BulletinBoard framework. Analysts familiar with full filesystem acquisitions will recognize the path `/private/var/mobile/Library/BulletinBoard/`, which contains structured data about notifications, including their content, timestamps, and associated bundle identifiers.

This is not new from a forensic standpoint. In my [BFU acquisition post using checkra1n](https://andreafortuna.org/2020/01/10/ios-forensics-bfu-before-first-unlock-acquisition-using-checkra1n/) I documented `/Library/BulletinBoard/ClearedSections.plist` as a log of cleared notifications. The data was always there; this case simply brought it into public awareness.

This artifact matters because of its relationship to device security states. iOS operates with two primary encryption modes: BFU, or Before First Unlock, and AFU, After First Unlock. In BFU state, the device has been powered on but the passcode has not yet been entered, and most user data is protected under a more restrictive encryption class. In AFU state, following the first unlock, a broader set of data becomes accessible, and this is the state in which most forensic acquisitions yield useful results. The notification database, depending on the protection class assigned to it, may be accessible in AFU state even without a jailbreak, particularly through backup-based extraction methods.

It is useful to consider how iOS handles data caching and persistence more broadly. The system preserves data so it can redisplay notifications, reconstruct notification center state after a restart, and maintain continuity between sessions. That behavior is intentional, but it creates a forensic surface that is easy to miss.

## How investigators likely extracted the data

The 404 Media report does not confirm the exact method used by the FBI, and no official statement has been made about the specific technique or the state of the device at the time of examination. However, based on what is publicly known about iOS forensic methods, a few scenarios are plausible.

![infographic](/assets/2026/signal-fbi-info.jpg)

The most likely path, especially if the device had been unlocked at some point after seizure, is a logical acquisition combined with an analysis of the extracted backup. As I have covered in detail in my [guide to iOS forensics without jailbreak](https://andreafortuna.org/2026/02/04/ios-forensics-without-jailbreak-a-practical-guide-to-modern-mobile-evidence-acquisition/), encrypted iTunes backups contain significantly more data than their unencrypted counterparts, and they can include system databases and app artifacts that reveal quite a lot about device state and user activity. Backup extraction using `idevicebackup2` is forensically sound and requires no modification of the device itself.

If investigators had access to the device in AFU state, they may also have ...