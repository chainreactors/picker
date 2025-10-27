---
title: iOS Forensic
url: https://jaybird1291.github.io/blog-cyber/en/posts/fcsc/
source: Instapaper: Unread
date: 2025-07-29
fetch_date: 2025-10-06T23:58:13.659252
---

# iOS Forensic

[↓
Skip to main content](#main-content)

[Jaybird1291
![Jaybird1291](/blog-cyber/img/avatar.png)](/blog-cyber/en/)

[Jaybird1291](/blog-cyber/en/)[Posts](/blog-cyber/en/posts/)[About me](/blog-cyber/en/posts/about-me/)[Projects](/blog-cyber/en/posts/projets/)[iOS Security resources](/blog-cyber/en/hide/resources-ios/)

EN

[EN](/blog-cyber/en/posts/fcsc/)[FR](/blog-cyber/posts/fcsc/)[JA](/blog-cyber/ja/posts/fcsc2025/)

EN

[EN](/blog-cyber/en/posts/fcsc/)[FR](/blog-cyber/posts/fcsc/)[JA](/blog-cyber/ja/posts/fcsc2025/)

* [Posts](/blog-cyber/en/posts/)
* [About me](/blog-cyber/en/posts/about-me/)
* [Projects](/blog-cyber/en/posts/projets/)
* [iOS Security resources](/blog-cyber/en/hide/resources-ios/)

# FCSC 2025 - iOS Forensic

18 May 2025·9 mins·
loading

·
loading

·

 Like
·

[FCSC](/blog-cyber/en/tags/fcsc/)[2025](/blog-cyber/en/tags/2025/)[IOS](/blog-cyber/en/tags/ios/)[Writeup](/blog-cyber/en/tags/writeup/)

![Jaybird1291](/blog-cyber/img/avatar.png)

Author

Jaybird1291

Table of Contents

* [Scenario](#scenario)
* [Setup](#setup)
* [Intro - iForensics - iCrash](#intro---iforensics---icrash)
* [⭐ - iForensics - iDevice](#---iforensics---idevice)
* [⭐ - iForensics - iWiFi](#---iforensics---iwifi)
* [⭐⭐ - iForensics - iTreasure](#---iforensics---itreasure)
* [⭐⭐ - iForensics - iNvisible](#---iforensics---invisible)
* [⭐⭐ - iForensics - iBackdoor 1/2](#---iforensics---ibackdoor-12)
* [⭐⭐ - iForensics - iBackdoor 2/2](#---iforensics---ibackdoor-22)
* [⭐⭐⭐ - iForensics - iC2](#---iforensics---ic2)

Table of Contents

* [Scenario](#scenario)
* [Setup](#setup)
* [Intro - iForensics - iCrash](#intro---iforensics---icrash)
* [⭐ - iForensics - iDevice](#---iforensics---idevice)
* [⭐ - iForensics - iWiFi](#---iforensics---iwifi)
* [⭐⭐ - iForensics - iTreasure](#---iforensics---itreasure)
* [⭐⭐ - iForensics - iNvisible](#---iforensics---invisible)
* [⭐⭐ - iForensics - iBackdoor 1/2](#---iforensics---ibackdoor-12)
* [⭐⭐ - iForensics - iBackdoor 2/2](#---iforensics---ibackdoor-22)
* [⭐⭐⭐ - iForensics - iC2](#---iforensics---ic2)

![](/blog-cyber/posts/fcsc/pictures/chall.png)

## Scenario [#](#scenario)

> As you pass through customs, the customs officer asks you to hand over your phone and its unlock code. The phone is returned to you a few hours later…
>
> Suspicious, you send your phone to ANSSI’s CERT-FR for analysis. CERT-FR analysts carry out a collection on the phone, consisting of a sysdiagnose and a backup.
>
> iForensics - iDevice
> iForensics - iWiFi
> iForensics - iTreasure
> iForensics - iNvisible
> iForensics - iBackdoor 1/2
> iForensics - iBackdoor 2/2
> iForensics - iC2
> iForensics - iCompromise

We have a logical `backup.tar.xz` (logical) **plus** a set of *sysdiagnose* and crash files!

## Setup [#](#setup)

For the whole series I relied on:

* DB Browser for SQLite
* EC-DIGIT-CSIRC/sysdiagnose
* iLEAPP
* Autopsy

Handy reference material:

* ![](/blog-cyber/posts/fcsc/pictures/FOR585-1.png)
* ![](/blog-cyber/posts/fcsc/pictures/FOR585-2.png)

Sure, you could bring in heavier artillery (Plaso etc.), but I was solving the CTF late and opted for the fast route. 🤠

## Intro - iForensics - iCrash [#](#intro---iforensics---icrash)

> It seems that a flag has hidden itself in the place where crashes are stored on the phone…

Super-easy one. We know the crashes live in `sysdiagnose_and_crashes.tar.xz`, so:

```
tar -xf sysdiagnose_and_crashes.tar.xz
```

From here you can `grep -r "FCSC{"` or simply browse the crash folders by hand.

If we go inside `sysdiagnose_and_crashes/private/var/mobile/Library/Logs/CrashReporter/` we’ll spot **fcsc\_intro.txt** — and the flag.

**Flag** : `FCSC{7a1ca2d4f17d4e1aa8936f2e906f0be8}`

## ⭐ - iForensics - iDevice [#](#---iforensics---idevice)

> To start with, find some information of interest about the phone: iOS version and phone model identifier.
> The flag is in the format FCSC{|}. For example, for an iPhone 14 Pro Max running iOS 18.4 (22E240): FCSC{iPhone15,3|22E240}.

To answer this question, you need to know what an iOS backup consists of. I spoke earlier of a “logical” backup. This is important because if you look inside the backup, all you see are weird folders:

![](/blog-cyber/posts/fcsc/pictures/backup.png)

To make sense of it we must rebuild the real paths using **Manifest.db** (introduced with iOS 10). That DB maps each fileID to its original RelativePath.

Luckily, some human-readable files survive at the root, including **Info.plist**. Apple stores key device metadata there:

* product Type (model identifier, e.g. iPhone12,3)
* product Version (iOS version, e.g. 16.0)
* build Version (e.g. 20A362)
* IMEI, serial, GUID, last-backup date, installed apps etc.

Everything we need for the flag!

![](/blog-cyber/posts/fcsc/pictures/infoplist.png)

**Flag** : `FCSC{iPhone12,3|20A362}`

If you’re interested in rebuilding the arbo, here’s a demonstration:

First, let’s take a look at what **Manifest.db** is made of:

![](/blog-cyber/posts/fcsc/pictures/manifestdb.png)

Pretty straightforward, so a tiny script can recreate the tree:

```
#!/bin/bash
BACKUP="/mnt/hgfs/backup/backup"
OUT="/mnt/hgfs/backup/reconstructed-backup"

mkdir -p "$OUT"

sqlite3 -separator '|' "$BACKUP/Manifest.db" \
"SELECT fileID, domain, COALESCE(relativePath,'') FROM Files;" \
| while IFS="|" read -r FILEID DOMAIN RELPATH; do

  [[ -z "$RELPATH" ]] && continue

  DEST_DIR="$OUT/$DOMAIN/$(dirname "$RELPATH")"
  DEST_PATH="$OUT/$DOMAIN/$RELPATH"

  mkdir -p "$DEST_DIR"
  ln -s "$BACKUP/$FILEID" "$DEST_PATH" 2>/dev/null || true
done
```

And voilà !

![](/blog-cyber/posts/fcsc/pictures/reconstructed.png)

## ⭐ - iForensics - iWiFi [#](#---iforensics---iwifi)

> To continue, find some information of interest about the phone: SSID and BSSID of the WiFi network the phone is connected to, as well as the iCloud account associated with the phone.
>
> The flag is in the format FCSC{||}. For example, if the phone is connected to the example WiFi network, which has the BSSID 00:11:22:33:44:55 and the associated iCloud account is example@example.com: FCSC{example|00:11:22:33:44:55|example@example.com}.

To speed up the extraction of Wi-Fi and iCloud information, we can use iLEAPP (iOS Logs, Events, and Protobuf Parser): it will automatically collect and organize lots of artifacts for us and make a report.

After running iLEAPP you can read SSID & BSSID straight from the Wi-Fi section:

![](/blog-cyber/posts/fcsc/pictures/wifi.png)

For the iCloud account there are many angles possible; one of the easiest is to check which Apple ID installed the apps.

![](/blog-cyber/posts/fcsc/pictures/icloud.png)

**Flag** : `FCSC{FCSC|66:20:95:6c:9b:37|robertswigert@icloud.com}`

## ⭐⭐ - iForensics - iTreasure [#](#---iforensics---itreasure)

> Before the phone was handed over to customs, its owner had time to send a treasure. Find this treasure.

There are several quick avenues here. The wording hints at something **sent**, so my first stop was plain old SMS / iMessage.

Because iLEAPP parses the `sms.db` for us, we can open the report and jump straight to the message table:

![](/blog-cyber/posts/fcsc/pictures/sms.png)

It can also be fed to Autopsy via the “Logical File Analysis” module. Autopsy scans all the files and, based on their headers (magic bytes), groups some of the media (JPEG, PNG, etc.) under the “User Content Suspected” tab, since the **Access Path** is located in `HomeDomain/Media/DCIM/...`. It therefore considers it to be user content (photo taken or imported).

**Flag** : `FCSC{511773550dca}`

## ⭐⭐ - iForensics - iNvisible [#](#---iforensics---invisible)

> It seems that a message could not be sent… Find the recipient of this message.
> The flag is in the format FCSC{}. For example, if the recipient is example@example.com: FCSC{example@example.com}.

In this case, it’s very quick: you can go straight to the DB **sms.db**. This is the database containing all conversations (iMessage and SMS), with the main tables message (headers,...