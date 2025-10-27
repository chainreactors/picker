---
title: iOS 17- The “Forever” Setting That Isn’t… Or Is It
url: https://smarterforensics.com/2024/08/ios-17-the-forever-setting-that-isnt-or-is-it/
source: Instapaper: Unread
date: 2024-08-21
fetch_date: 2025-10-06T18:05:26.740520
---

# iOS 17- The “Forever” Setting That Isn’t… Or Is It

[Skip to content](#content)

# [Smarter Forensics](https://smarterforensics.com/)

[Search](#search-container)

Primary Menu

* [About Us](https://smarterforensics.com/)
* [Blog](https://smarterforensics.com/blog/)
* [Contact Us](https://smarterforensics.com/contact-us/)
* [Papers, Scripts and More](https://smarterforensics.com/reading-room/)
* [Presentations](https://smarterforensics.com/presentations/)
* [SANS FOR585](https://smarterforensics.com/for585/)

Search for:

[iOS](https://smarterforensics.com/category/ios/), [Uncategorized](https://smarterforensics.com/category/uncategorized/)

# iOS 17- The “Forever” Setting That Isn’t… Or Is It?

[August 7, 2024](https://smarterforensics.com/2024/08/ios-17-the-forever-setting-that-isnt-or-is-it/) [Heather Barnhart](https://smarterforensics.com/author/heather/) [1 Comment](https://smarterforensics.com/2024/08/ios-17-the-forever-setting-that-isnt-or-is-it/#comments)

[![](https://smarterforensics.com/wp-content/uploads/2024/08/DALL·E-2024-08-07-21.28.49-A-sleek-iPhone-screen-displaying-the-iOS-17-home-screen.-In-the-foreground-the-word-Forever-appears-in-bold-letters-but-it-is-breaking-into-pieces.webp)](https://smarterforensics.com/wp-content/uploads/2024/08/DALL%C2%B7E-2024-08-07-21.28.49-A-sleek-iPhone-screen-displaying-the-iOS-17-home-screen.-In-the-foreground-the-word-Forever-appears-in-bold-letters-but-it-is-breaking-into-pieces.webp)

When I teach SANS FOR585 Smartphone Forensic Analysis In-Depth, we really dive into iOS artifacts to validate the truth of what happened, what tools are reporting, and what they are missing. Message retention is often needed to help examiners understand why data no longer exists on the iOS device if the user didn’t delete it. When hunting for deleted messages, I suggest students validate the current message retention settings in **com.apple.MobileSMS.plist**, then examine the messages that are parsed in the tools and compare that to the **message** table of **sms.db**. If message retention is set to 30 days and you are looking for older messages, chances are good they no longer exist on the device. If this isn’t the case and message retention is set to forever, get ready to dig and hope for the best because your job just got harder. Bottom line, understanding the values in com.apple.MobileSMS.plist when it comes to message retention can be a time saver.

Apple always likes to change things up and it’s impossible to see everything that has changed right away, even with all the amazing DFIR researchers out there. Sometimes it takes a customer to email with a question on how the tool is behaving. This is why I decided to write this blog. I want to thank that customer and anyone reading this for validating! This is key to our craft in DFIR. I also want to thank Ian Whiffin for hearing me out and sharing screenshots from test devices.

It’s a known fact that I work at Cellebrite with a group of brilliant examiners. Part of our job is helping customers make sense of data. A question came in about message retention and why PA 10 was reporting one thing and the phone showed another. Same day, different question, new bug? Or new method of tracking settings on the device? For this matter, it was a bit of everything. Apple changed the way message retention is tracked in com.apple.MobileSMS.plist. This plist can be located here: /private/var/mobile/Library/Preferences/com.apple.MobileSMS.plist.

The good news is that this file is accessible with an encrypted iTunes backup, advanced logical, and full file system extractions. I didn’t bother testing unencrypted backups because so much data is missed. ALWAYS encrypt the backup.

For as long as I can remember, we have been reading the values from the com.apple.MobileSMS.plist under **KeepMessageForDays**. The values may be:

* KeepMessageForDays = 0 = Forever
* KeepMessageForDays = 365 = 1 Year
* KeepMessageForDays = 30 = 30 Days

\*\*Note – for iOS 13 and earlier if **KeepMessageForDays** is missing from the plist, the message retention was set to **Forever** on that device. According to Ian Whiffin, if the default message retention of **Forever** is ***never*** changed (regardless of iOS version), the **KeepMessageForDays** may also be missing from the plist. We plan to validate this further as we will soon have access to devices where that setting has never been modified and will also look for the new values.

[![](https://smarterforensics.com/wp-content/uploads/2024/08/memere-1.jpg)](https://smarterforensics.com/wp-content/uploads/2024/08/memere-1.jpg)

So just when we are comfy with the values in this plist, iOS 17 came along and changed how the values are stored. While the **KeepMessageForDays** may exist in the com.apple.MobileSMS.plist, it is no longer in use by Apple for tracking message retention in devices that are running iOS 17. The values here seem to reflect old settings of message retention, and ***not*** what the device settings currently reflect. Don’t you love when old remnants are left behind that cause confusion?

For iOS 17, we need to rely upon the value stored under **SSKeepMessages.** The values will be the same as before.

* SSKeepMessages = 0 = Forever
* SSKeepMessages = 365 = 1 Year
* SSKeepMessages = 30 = 30 Days

**Testing and Validation:**

Ian provided me with 4 examples from test devices and I used 3 of my own test devices and my personal phone. Here are some examples you may come across that I think makes the point of the blog.

**iPhone 15 Pro running 17.4.1** – Message Retention is set to Forever and was previously set to Forever in iOS 16.

[![](https://smarterforensics.com/wp-content/uploads/2024/08/Heather_iPhone.jpg)](https://smarterforensics.com/wp-content/uploads/2024/08/Heather_iPhone.jpg)

**iPhone 10 running iOS 16.\*** – was set to forever on iOS 16.1.2. Changed it to 1 year and updated to 16.7.10. Here is what the settings looked like.

[![](https://smarterforensics.com/wp-content/uploads/2024/08/phone-settings-473x1024.jpg)](https://smarterforensics.com/wp-content/uploads/2024/08/phone-settings.jpg)

[![](https://smarterforensics.com/wp-content/uploads/2024/08/1year-settings-473x1024.jpg)](https://smarterforensics.com/wp-content/uploads/2024/08/1year-settings.jpg)

The device was acquired using iTunes and the encrypted backup was parsed in [ArtEx](https://www.doubleblak.com/app.php?id=ArtEx2). Note that only the current setting is shown. The modified date of com.apple.MobileSMS.plist reflects when I made the changes, but other factors could impact the timestamp.

[![](https://smarterforensics.com/wp-content/uploads/2024/08/iOS16.jpg)](https://smarterforensics.com/wp-content/uploads/2024/08/iOS16.jpg)

Note that **SSKeepMessages** does not exist. It’s because this is iOS 16 and this key was added in iOS 17.

**iPhone 11 running iOS 17.0** – message retention was set to forever and not changed when updated from iOS 16 to iOS 17. This extraction was parsed in Cellebrite Physical Analyzer 10.3.

[![](https://smarterforensics.com/wp-content/uploads/2024/08/ios17_forever-forever-949x1024.jpg)](https://smarterforensics.com/wp-content/uploads/2024/08/ios17_forever-forever.jpg)

The following examples are from iOS 17 devices. Note the lack of **KeepMessageForDays**. I am providing several screenshots to show the different settings as captured by Ian Whiffin.

**iOS 17+** – The default setting is Forever. I am examining the com.apple.MobileSMS.plist in [Mushy](https://doubleblak.com/app.php?id=Mushy), a free tool developed by Ian Whiffin.

[![](https://smarterforensics.com/wp-content/uploads/2024/08/default.jpg)](https://smarterforensics.com/wp-content/uploads/2024/08/default.jpg)

**iOS 17+** – Message retention was changed from the default of forever to 1 year. Again, I reviewed this in Mushy.

[![](https://smarterforensics.com/wp-content/uploads/2024/08/1year_mushy.jpg)](https://smarterforensics.com/wp-content/uploads/2024/08/1year_mushy.jpg)

**iOS 17+** -Message retention was changed from...