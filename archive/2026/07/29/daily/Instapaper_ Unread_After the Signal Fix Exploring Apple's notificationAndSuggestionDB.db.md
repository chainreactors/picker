---
title: After the Signal Fix Exploring Apple's notificationAndSuggestionDB.db
url: https://blog.digital-forensics.it/2026/07/after-signal-fix-exploring-apples.html
source: Instapaper: Unread
date: 2026-07-29
fetch_date: 2026-07-30T04:52:33.878788
---

# After the Signal Fix Exploring Apple's notificationAndSuggestionDB.db

[Skip to main content](#main)

### Search This Blog

# [ZENA FORENSICS](https://blog.digital-forensics.it/)

something about digital forensics and something not

### After the Signal Fix: Exploring Apple's notificationAndSuggestionDB.db

By

[Mattia Epifani](https://www.blogger.com/profile/05734345790174061166 "author profile")

-
[July 28, 2026](https://blog.digital-forensics.it/2026/07/after-signal-fix-exploring-apples.html "permanent link")

Following my recent research into Apple's Biome ecosystem, I continued examining additional artifacts located within the DuetExpertCenter framework.

Although much of the recent forensic attention has focused on the SEGB file format and, in particular, on the notification-related streams located within:

/private/var/mobile/Library/DuetExpertCenter/streams/

it seemed reasonable to assume that additional notification-related artifacts might exist elsewhere within the same framework. This assumption proved correct.

During the analysis of several iOS full filesystem acquisitions, I identified an SQLite database named:

/private/var/mobile/Library/DuetExpertCenter/streams/notificationAndSuggestionDB.db

At first glance, the database appeared relatively small and unremarkable. A closer inspection, however, revealed a valuable artifact for forensic investigations.

## The "notifications" Table

Among the various tables present in the database, the most interesting is undoubtedly "notifications".

The table contains 36 columns, several of which appear highly relevant from a forensic perspective.

The most useful fields identified during testing are:

* Received Timestamp (MAC Absolute)
* BundleID
* ThreadID
* ContactID
* rawIdentifier
* isMessage (0/1)
* isGroupMessage (0/1)
* notificationBodyLength
* Delivery Method (seen values 0 and 1)
* Urgency (seen values 1 and 2)
* deliveryReason (seen values 0 and 1)
* latestOutcome
* latestOutcomeTimestamp (MAC Absolute)
* isProminent (0/1)
* isActive (0/1)
* receivedMode

## No Notification Content, But Plenty of Metadata

One particularly interesting aspect of this artifact is what it does not contain.

Unlike the previously documented stream "userNotificationEvents" that attracted widespread attention in 2026, **the database does not appear to store notification content**. No message previews were observed during testing.

However, in multiple test devices and real-world forensic images, the database contained notification records dating back **as far as approximately 60 days**.

This is particularly noteworthy because the observed retention period appears to exceed the retention commonly observed in the Biome notification-related streams, where active records are typically retained for approximately 28 days.

From a forensic perspective, this longer retention period significantly increases the value of the artifact. Even when the originating application has been removed from the device, or when the message that generated the notification has subsequently been deleted, investigators may still be able to demonstrate that a notification associated with a specific application was received on a given day.

Although the database may not preserve the content of the notification itself, it can still provide valuable evidence regarding application usage, communication activity, and the timing of user interactions.

In many investigations, establishing that a notification from WhatsApp, Signal, Messages, Mail, or another application was received at a particular point in time may be just as valuable as recovering the original content.

## Application-Specific Findings

### WhatsApp

For WhatsApp notifications, the field "ThreadID" typically contains the chat identifier.

Examples include values such as:

393331234567@s.whatsapp.net

which can be directly associated with individual WhatsApp conversations.

In addition, the field "rawIdentifier" often contains the corresponding telephone number.

### Signal

Signal notification records exhibit similar behavior.

The field "rawIdentifier" frequently contains the telephone number associated with the remote sending party.

This is particularly noteworthy given the recent public attention surrounding Signal notification artifacts on iOS.

### Calls

Records related to incoming calls also appear to preserve useful identifiers associated with the remote party in the "rawIdentifier" column.

### SMS Messages

For traditional SMS notifications, the phone number is often recoverable from the "ThreadID" column, rather than from the "rawIdentifier" column.

## Why BundleID Matters

One field deserving particular attention is "BundleID". Even when no user content is available, BundleID provides investigators with a clear indication of which application generated the notification. This allows investigators to establish application usage patterns and create timelines of device activity even when the underlying application data is no longer available.

## Beyond Notification Content

The timing of this discovery is particularly interesting.

Recent iOS updates introduced changes that prevent notification content from being retained in the manner previously documented by forensic researchers.

The existence of notificationAndSuggestionDB.db demonstrates that, while notification content may no longer be preserved, Apple still maintains a substantial amount of notification metadata.

Whether this is intentional system telemetry, internal intelligence data, or simply operational metadata remains to be fully understood.

Regardless of its original purpose, the artifact clearly provides valuable information for forensic investigations.

## Tested Versions

During testing, the database was consistently identified on devices running iOS 15 through iOS 26.

The artifact was observed both in laboratory devices and in real-world forensic images.

At this time, I have not yet determined the earliest iOS version in which the database first appeared, even though it was not found in some iOS 14 images.

## Support in iLEAPP

After validating the artifact and reviewing multiple datasets, I shared the findings with Alexis Brignoni.

As has happened on more than one occasion, Alexis implemented support incredibly quickly.

A dedicated parser for notificationAndSuggestionDB.db has now been added to the iLEAPP project and is available through the public repository.

Investigators using the latest version of [iLEAPP](https://github.com/abrignoni/iLEAPP) can therefore immediately begin evaluating the artifact within their own datasets.

## Final Thoughts

The history of iOS forensics repeatedly demonstrates that valuable evidence often survives in unexpected locations.

The recent attention given to notification content led many researchers to focus on SEGB files and notification streams stored within DuetExpertCenter.

Yet only a few folders away sits another artifact capable of documenting notification activity across dozens of applications and potentially preserving evidence for several months.

The content may be gone. The metadata, however, remains.

And as every forensic examiner knows, metadata often tells an important story of its own. Sometimes, it tells enough of the story.

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Comments

#### Post a Comment

### Popular posts from this blog

### [WhatsApp Forensics](https://blog.digital-forensics.it/2012/05/whatsapp-forensics.html)

By

[fabio sangiacomo](https://www.blogger.com/profile/14231069176415049661 "author profile")

-
[May 15, 2012](https://blog.digital-forensics.it/2012/05/whatsapp-forensics.html "permanent link")

Those who follow this blog may have noticed few months ago a post that introduced WhatsApp Xtract: this script was able to display in an HTML document all the WhatsApp messages extracted from an iPhone. A nd those who follow the xda developers forum may have recently noticed a thread on it. This last month, thanks to Martina Weidner (aka ztedd) who has decided to take contro...