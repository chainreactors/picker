---
title: Where The Wild Tags Are & Other AirTag Stories.
url: https://thebinaryhick.blog/2024/09/02/where-the-wild-tags-are-other-airtag-stories/
source: Instapaper: Unread
date: 2024-09-05
fetch_date: 2025-10-06T18:31:13.515704
---

# Where The Wild Tags Are & Other AirTag Stories.

[Skip to content](#content)

[![](https://secure.gravatar.com/avatar/30a89971088a09252b6d39339ea487072e9352a20f7a711253ed149206bc4794?s=80&d=identicon&r=g)](https://thebinaryhick.blog/)

[The Binary Hick](https://thebinaryhick.blog/)

Thoughts From a Digital Forensic Practitioner

Menu

* [Public Images](https://thebinaryhick.blog/public_images/)
* [Contact](https://thebinaryhick.blog/contact/)
* [Bluesky](https://bsky.app/profile/thebinaryhick.blog)
* [Mastodon](https://infosec.exchange/%40joshua_hickman1)
* [X (Twitter)](https://x.com/josh_hickman1)

# Where The Wild Tags Are & Other AirTag Stories.

[Binary Hick](https://thebinaryhick.blog/author/binaryhick/ "Posts by Binary Hick")

[Android](https://thebinaryhick.blog/category/android/), [Apple](https://thebinaryhick.blog/category/apple/), [iOS](https://thebinaryhick.blog/category/ios/), [Locations](https://thebinaryhick.blog/category/locations/), [Mobile](https://thebinaryhick.blog/category/mobile/), [Trackers](https://thebinaryhick.blog/category/trackers/)

2024-09-022025-08-19
15 Minutes

![](https://i0.wp.com/i.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2I5ZGY3d2UyZG14aTU0aTUzb2dhNmZnenNlM3E1M2p0bzBvaTA0MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/F8nD8ql8CcbeM/giphy.gif?w=1100&ssl=1)

Accurate depiction of my test phones.

*Note: this post is a quasi-continuation of my previous post about Bluetooth trackers on the Google Find My Device network. Also, there is a second part to this post which you can find [here](https://thebinaryhick.blog/2025/08/19/further-observations-more-on-ios-search-party/).*

While I typically write about Team Green on this blog, I will occasionally tiptoe into iOS/iPadOS land. I recently gave a presentation and wrote a blog post that, among other things, discussed unwanted Google Find My Device (FMD) trackers and how they were detected by Android and iOS devices. While I was finalizing my slide deck for that presentation I stumbled across something interesting in the iOS Unified Logs: information about unwanted trackers was being written to disk. After some digging, Googling, and some yelling at my keyboard, I discovered that examiners do have a way to obtain location data about where an iPhone was when it saw an unwanted tracker, AirTag or otherwise. This discovery lead to a few other things contained within iOS that could be helpful to examiners *and* investigators, which resulted in this post.

AirTags have been around for three years now and need no introduction. If you need a primer on Google Find My Device trackers, [I wrote a post about them](https://thebinaryhick.blog/2024/08/23/not-all-androids-who-wonder-are-lost-a-look-at-androids-find-my-device-network/) recently that should help.

## Wild Tags

As a recap, this batch of research started in the iOS Unified Logs. I summarized Unified Logs in my previous post:

> “Up until this point the thought process was that examiners would need the Unified Logs from an iOS device in order to determine where an iPhone was when it first saw a tracker, which could help investigators retrace the steps of a victim in the hopes that they could find some physical evidence or a potential crime scene. The problem, however, arises in the fact that any useful information such as locations and associated timestamps are redacted in the Unified Logs, thus rendering them useless. There is always the AirTag developer profile that Apple offers to developers, but there are two problems with this approach:
>
> 1. Applying the profile does not retroactively un-redact previously redacted data.
> 2. The profile expires automatically after five days and is removed from the device.”

Additionally, there is the issue of Bluetooth MAC address randomization, which is used by both AirTags and FMD trackers. This is done for privacy reasons, but it plays havoc when trying to find *the absolute first time* a phone saw an unwanted tracker. Knowing exactly *when* a tracker was placed on an individual could yield a new crime scene or evidence sources (e.g., surveillance footage), but interviewing the victim (if available) is crucial in making the final determination. The specification Apple and Google jointly wrote specifies that Bluetooth MAC addresses should rotate every 24 hours, so if a tracker has been following a user for more than a day, it is likely the address has rotated at least once. Further, the UUID assigned to an unwanted tracker by a victim iPhone is not the same UUID assigned by the tracker’s owner’s device. All of this makes it almost impossible to connect a physical tracker back to the owner without help from Apple or Google.

Part of my research into Google FMD trackers involved their interactions with iOS devices. As of iOS 17.5 devices now have the ability to detect unwanted trackers on that operate on the Google FMD network. For testing, I was using an iPhone 14 running iOS 17.5.1 and working with full file system extractions; the files discussed in this post are not present in logical extractions. When inspecting the Unified Logs after I received an alert for an unwanted Pebblebee tracker, I found that information about the unwanted tracker was being written to **/private/var/mobile/Library/com.apple.icloud.searchpartyd/WildModeAssociationRecord/**. See Figure 1.

[![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/08/Figure-1.png?resize=1024%2C559&ssl=1)](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/08/Figure-1.png?ssl=1)

Figure 1. A .record file being written to disc.

For reference, the log entry for the notification is highlighted in the blue box. The log entry highlighted in the red box is of interest. A file, **6EA4278F-DD8D-4541-8C9A-17364A17CDA5.record**, was being written to in the previously mentioned directory path. The file name was the same as the UUID that was referencing the Pebblebee Clip. When I went to that location in the file system, there was the lone file. See Figure 2.

[![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/08/Figure-2.png?resize=1024%2C479&ssl=1)](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/08/Figure-2.png?ssl=1)

Figure 2. The .record file.

Inspecting this file finds that it is a binary plist file. Figure 3 shows how it appears in [Mushy](https://www.doubleblak.com/app.php?id=Mushy), a free tool written by [Ian Whiffin](https://doubleblak.com).

[![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/08/Figure-3.png?resize=1024%2C880&ssl=1)](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/08/Figure-3.png?ssl=1)

Figure 3. The .record file is actually a bplist.

At first glance there does not seem to be much going on here. However, **searchpartyd** (the iOS process responsible for handling AirTag and beacon tracking) was writing to this file, so there *must* be something important here. The two values highlighted in green and blue are 16-byte values, but the value in the red box at the bottom looks like gibberish. Apple uses AES-GCM in Apple CryptoKit, which typically means a key, a nonce (or IV), and a GCM tag. The 16-byte values would certainly pass for a nonce or GCM tag, which leaves the key. For that, we head to the Keychain.

In order to proceed from this point your extraction method has to pull the keychain contents and you will need a tool to view them. For that I turned to another freely available tool written by Ian: [ArtEx](https://www.doubleblak.com/app.php?id=ArtEx2). ArtEx is able to, among other things, parse keychain content. Parsing it and filtering the content by “**searchpartyd**” (the process that was writing to the file) yielded a handful of results. See Figure 4.

[![](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/08/Figure-4.png?resize=1024%2C371&ssl=1)](https://i0.wp.com/thebinaryhick.blog/wp-content/uploads/2024/08/Figure-4.png?ssl=1)

Figure 4. The key.

Highlighted in Figure 4 is the entry for the **BeaconStore** service, which is in the **searchpartyd** Access Group. On th...