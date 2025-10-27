---
title: Digital Detectives vs. Android 14 overcoming new forensic challenges
url: https://andreafortuna.org/2024/08/15/digital-detectives-vs-android-14-overcoming-new-forensic-challenges.html
source: Instapaper: Unread
date: 2024-08-22
fetch_date: 2025-10-06T18:06:03.379160
---

# Digital Detectives vs. Android 14 overcoming new forensic challenges

[Andrea Fortuna](/)
[ ]

[About](/about/)[Rss](/feed.xml)

# Digital Detectives vs. Android 14: overcoming new forensic challenges

Aug 15, 2024

As smartphones continue to be an integral part of our daily lives, they also become increasingly valuable sources of digital evidence in investigations. Android, being one of the most widely used mobile operating systems, is often at the forefront of these investigations. With the release of Android 14, forensic analysts must adapt their techniques and tools to effectively extract and analyze data from devices running this latest version.

![image](https://github.com/user-attachments/assets/b50bb288-5631-469b-a34f-d42463cc5fce)

## Key Changes in Android 14

Before diving into the specific challenges, it’s crucial to understand some of the key changes introduced in Android 14:

1. Enhanced privacy features
2. Improved file system encryption
3. New permission model for certain APIs
4. Changes in app data storage and access
5. Updates to the Android Runtime (ART)

These changes, while beneficial for user privacy and security, can complicate the forensic analysis process.

## New Challenges for DFIR Analysts

### 1. Enhanced Privacy Features

Android 14 has introduced several privacy enhancements that can impact forensic investigations:

#### a) Scoped Storage Enforcement

Android 14 fully enforces scoped storage, which limits an app’s access to device storage. This change affects how forensic tools can access and extract data from different app directories.

**Challenge:** Forensic tools may need to be updated to work with the new storage access model, potentially requiring root access or specialized techniques to bypass scoped storage restrictions.

#### b) Photo Picker API

The new Photo Picker API allows users to select specific photos and videos to share with apps, rather than granting full access to the media library.

**Challenge:** This feature may limit the ability of forensic tools to access the entire media library, requiring new methods to extract all media files.

### 2. Improved File System Encryption

Android 14 continues to enhance file system encryption, making it more challenging to access data without the device passcode or encryption key.

**Challenge:** Forensic analysts may need to develop new techniques or rely on specialized hardware to bypass or crack the enhanced encryption.

### 3. New Permission Model for Certain APIs

Android 14 introduces a new permission model for certain APIs, requiring more granular user consent for access to sensitive data.

**Challenge:** This change may affect the ability of forensic tools to access certain types of data, requiring updates to permission handling and potentially limiting the scope of data extraction without user interaction.

### 4. Changes in App Data Storage and Access

With updates to how apps store and access data, forensic analysts need to adapt their techniques for extracting and analyzing app-specific information.

#### a) App-specific directories

Android 14 enforces stricter rules on app-specific directories, making it more challenging to access data from third-party apps.

**Challenge:** Forensic tools may need to be updated to navigate the new directory structure and access restrictions for each app.

#### b) Shared storage changes

Changes to shared storage access can impact how forensic tools extract and analyze data stored in shared locations.

**Challenge:** Analysts may need to develop new methods to access and interpret data stored in shared locations, especially for apps that have adapted to the new storage model.

### 5. Updates to the Android Runtime (ART)

Android 14 includes updates to the Android Runtime, which can affect how apps are executed and how data is stored in memory.

**Challenge:** Forensic memory analysis techniques may need to be adapted to account for changes in memory management and app execution.

## Artifact Analysis in Android 14

Despite these challenges, Android 14 still provides a wealth of artifacts that can be valuable in forensic investigations. Let’s explore some key artifacts and the challenges associated with extracting and analyzing them in Android 14.

### Device Information and General Settings

Several files contain crucial device information and settings:

* build.prop
* global\_settings.xml
* system\_settings.xml
* secure\_settings.xml
* googlesettings.db
* gservices.db

**Challenge:** While these files still exist in Android 14, the enhanced privacy features may limit access to some of this information without proper authentication or root access.

### User Accounts

User account information can be found in files such as:

* accounts\_ce.db
* accounts\_de.db
* accounts.xml

**Challenge:** The new permission model in Android 14 may restrict access to account information, requiring forensic tools to adapt their extraction methods.

### Cellular, Wi-Fi, and Bluetooth Configuration

Key files for network configuration include:

* telephony.db
* WifiConfigStore.xml
* bt\_config.conf

**Challenge:** Enhanced encryption and privacy features may make it more difficult to access these files without proper authentication.

### Installed Applications and Permissions

Several files track installed applications and their permissions:

* packages.list
* packages.xml
* runtime-permissions.xml

**Challenge:** The new permission model in Android 14 may change how this information is stored and accessed, requiring updates to forensic tools and analysis techniques.

### Native and Third-Party Application Usage Analysis

Android 14 continues to provide valuable artifacts for analyzing app usage:

* recent\_tasks folder
* usagestats folder
* batterystats files
* Digital Wellbeing database

**Challenge:** Changes in app data storage and access may require new methods to extract and interpret this usage data accurately.

## Extracting and Analyzing Key Artifacts

Let’s dive deeper into some specific artifacts and the challenges associated with extracting and analyzing them in Android 14.

### 1. Calendar Data (calendar.db)

The calendar.db file, stored in `/data/com.android.providers.calendar/databases/`, contains valuable information about a user’s schedule and events.

**Challenge:** In Android 14, accessing this database may require bypassing scoped storage restrictions and potentially dealing with enhanced encryption.

**Extraction Technique:** Forensic tools may need to emulate the Calendar app’s permissions or use root access to extract this database.

**Analysis Tip:** Pay attention to the “deleted” flag in event entries, as it may reveal information about events that the user attempted to remove.

### 2. Contacts (contacts2.db)

The contacts2.db file, located in `/data/com.android.providers.contacts/databases/`, stores contact information.

**Challenge:** Android 14’s privacy features may limit access to this database without proper authentication.

**Extraction Technique:** Advanced forensic tools may need to leverage system-level access or exploit vulnerabilities to extract this database.

**Analysis Tip:** Cross-reference contact data with communication logs from various apps to build a comprehensive picture of the user’s interactions.

### 3. SMS/MMS (mmssms.db)

The mmssms.db file, found in `/data/com.android.providers.telephony/databases/`, contains text and multimedia messages.

**Challenge:** Enhanced encryption in Android 14 may make it more difficult to access this database without the device passcode.

**Extraction Technique:** Physical extraction methods or advanced logical extraction tools may be necessary to bypass encryption and access this database.

**Analysis Tip:** Look for patterns in message timestamps and content to identify key conversations or periods of interest.

### 4. Google Maps Artifacts

Google Maps artifacts are stored in various files under `/data/com.google.android.apps.maps/databases/`.

**Challenge:** Android 14’s new permission model may restrict access to locati...