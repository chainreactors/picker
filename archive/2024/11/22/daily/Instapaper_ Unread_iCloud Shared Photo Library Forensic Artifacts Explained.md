---
title: iCloud Shared Photo Library Forensic Artifacts Explained
url: https://theforensicscooter.com/2024/11/17/icloud-shared-photo-library-forensic-artifacts-explained/
source: Instapaper: Unread
date: 2024-11-22
fetch_date: 2025-10-06T19:23:18.421816
---

# iCloud Shared Photo Library Forensic Artifacts Explained

[Skip to content](#content)

[The Forensic Scooter](https://theforensicscooter.com/)

[ ]

Menu +
×
expanded
collapsed

* [The Forensic Scooter](https://theforensicscooter.com/)
  + [Contact](https://theforensicscooter.com/contact/)
* [Blog](https://theforensicscooter.com/blog/)

# iCloud Shared Photo Library: Forensic Artifacts Explained

Posted by[Scott\_koenig](https://theforensicscooter.com/author/scottkoenig3347/)[November 17, 2024](https://theforensicscooter.com/2024/11/17/icloud-shared-photo-library-forensic-artifacts-explained/)Posted in[iOS Settings](https://theforensicscooter.com/category/ios-settings/), [Photo Library](https://theforensicscooter.com/category/photo-library/), [Photos.Sqlite](https://theforensicscooter.com/category/photos-sqlite/)Tags:[#DFIR](https://theforensicscooter.com/tag/dfir/), [digital-forensics](https://theforensicscooter.com/tag/digital-forensics/), [forensics](https://theforensicscooter.com/tag/forensics/), [iCloud Shared Photo Library](https://theforensicscooter.com/tag/icloud-shared-photo-library/), [iLEAPP](https://theforensicscooter.com/tag/ileapp/), [iOS Settings](https://theforensicscooter.com/tag/ios-settings/), [photodata-photos-sqlite](https://theforensicscooter.com/tag/photodata-photos-sqlite/), [Photos.Sqlite](https://theforensicscooter.com/tag/photos-sqlite/), [sqlite-query](https://theforensicscooter.com/tag/sqlite-query/)

![](https://theforensicscooter.com/wp-content/uploads/2024/11/tvxc.gif?w=500)

Hello again, this one took some time to release, but I hope it helps!

iCloud Shared Photo Library (SPL) was introduced during WWDC 2022 as a new feature within iOS 16. Since that time, there have been several articles and how-to videos regarding setting up and using iCloud Shared Photo Library, but I am not aware of any blogs or published research that discuss some of the digital forensic artifacts related to this feature. I found the following links useful during my research about the feature:

<https://support.apple.com/en-us/HT213248>

<https://support.apple.com/guide/iphone/use-icloud-shared-photo-library-iph1a6c849ab/16.0/ios/16.0>

<https://support.apple.com/guide/iphone/use-icloud-shared-photo-library-iph1a6c849ab/17.0/ios/17.0>

<https://www.macrumors.com/guide/icloud-shared-photo-library/>

One of the best videos I came across was posted to [YouTube by Joel Feld](https://youtu.be/vs9UQwKAHu8?si=xcJDNDU7_ljSN-Rw). I would strongly recommend watching it prior to reading this blog. It provides a detailed overview of the iCloud Shared Photo Library settings and details not discussed in this blog.

Since the announcement of iCloud Shared Photo Library (SPL), I have been thinking about how this feature could affect the assets saved on an iPhone and the data being stored in the Local Photo Library (LPL) \*/PhotoData/Photos.sqlite. In this blog, I hope to answer some of those questions.

**Forensic Questions:**

Can we use the Local Photos Library (LPL) \*/PhotoData/Photos.sqlite data to determine if iCloud Shared Photo Library (SPL) is active?

Can we use the LPL \*/PhotoData/Photos.sqlite data to determine the participants of a SPL?

Can we use the LPL \*/PhotoData/Photos.sqlite data to determine if an asset (media file) has been shared to a SPL?

Can we use LPL \*/PhotoData/Photos.sqlite data to determine which participant contributed an asset to a SPL?

Where is iCloud Shared Photo Library assets stored on a device?

How can the iCloud Shared Photo Library feature be used for anti-forensics?

**Test Devices:**

Bandit Scooters’ iPhone 6s Plus [iPhone8,2] A1687

* iOS 15.3.1 (19B74)
* 128 GB device storage capacity

Bandit Scooters’ iPhone 8 Plus [iPhone10,2] A1864

* iOS 15.4.1
* 256 GB device storage capacity

Dexter Scooters’ iPhone SE (1st Gen) [iPhone8,4] A1662

* iOS 15.6 (19G71)
* 32 GB device storage capacity

Dexter Scooters’ iPhone 7 [iPhone9,1] A1660

* iOS 15.1 (19B74)
* 128 GB device storage capacity

Scooter Scotts’ iPhone X [iPhone10,3] A1864

* iOS 14.7 (18G69)
* 128 GB device storage capacity

John Scooter Wick’s iPhone 12 Pro [iPhone13,3] A2341

* iOS 16.0.2 (20A380)
* 128 GB device storage capacity

John Scooter Wick’s iPhone 12 Pro [iPhone13,3] A2341

* iOS 18.0 Beta 1 (22A5282m)
* 128 GB device storage capacity

Scott Koenig’s iPhone 14 Pro [iPhone15,2]

* iOS 17.3.1 and 17.4.1
* 128 GB device storage capacity

NOTE: The iPhone SE and the iPhone 7 both belong to Dexter Scooter. Dexter’s Apple ID is being used on both devices and sharing iCloud Storage. You will see some of the impacts this had during the video documentation.

**Device Settings:**

Sometimes the most difficult task during research is locating the file(s) used to store device settings related to a device activity and feature being researched. During the research and testing for iCloud Shared Photo Library (SPL), I was able to locate some files that contained notable data related to SPL. Most of these files (property lists and databases) are ones that I have previously researched and analyzed. These plists and databases will be mentioned in this section so that they can be used for reference during your analysis. Some of them might be referenced again in further detail if additional analysis is required.

***store.cloudphotodb***

This database will contain data about the creation and existence of an iCloud Shared Photo Library. As a reminder, this database can be found at the following location:

* [\*\mobile\Media\PhotoData\CPL\storage\store.cloudphotodb](//private/var/mobile/Media/PhotoData/CPL/storage/store.cloudphotodb)

If you analyze the *scopes* table *scopeIdentifier* field, you should find a scope identifier that matches the identifier located in the *\*\PhotoData\Photos.sqlite ZSHARE* table *ZSCOPEIDENTIFIER* field. Based on my testing, a scope identifier for an iCloud Shared Photo Library will begin with “SharedSync-“ then be followed by a UUID.

This *scopeIdentifier* can be found in multiple files within a device that is the owner and / or participant of the iCloud Shared Photo Library (SPL).

If you analyze this database and an iCloud Shared Photo Library has been created, you will observe the db contains a lot of useful information about the SPL. This includes several embedded plists and other data. One thing that was discovered during the testing and research is the creation date located in *store.cloudphotodb* *scopes* table *creationDate* field and in *\*\PhotoData\Photos.sqlite ZSHARE* table *ZSCOPEIDENTIFIER* field. The creation date of the iCloud Shared Photo Library in this instance was on 2024-02-19.

Note in the top half of the figure below is from \*\PhotoData\Photos.sqlite *ZSHARE* table *ZCREATIONDATE* field matches the date the SPL was created and the date listed in \*\CPL\storage\store.cloudphotodb *scopes* table creationDate field does not. For the purpose of this research and blog, I did not take the time to detail why this occurred but, it should be noted if the creation date of the SPL is critical to the investigation, you should reference the \*\PhotoData\Photos.sqlite for a more accurate date timestamp.

![](https://theforensicscooter.com/wp-content/uploads/2024/11/spl_blog1.png?w=1024)

SPL\_Blog#1.png

**Property Lists:**

Parsers have been created within [iLEAPP](https://github.com/abrignoni/iLEAPP) to assist with parsing and reviewing the data stored within the following property lists.

Below are some other fields within the *com.apple.mobileslideshow.plist* to search that allow you gain insight into how the device is setup and used in conjunction with iCloud Shared Photo Library (SPL):

[**com.apple.mobileslideshow.plist**](https://github.com/abrignoni/iLEAPP/blob/main/scripts/artifacts/Ph80comappleMobileSlideShowPlist.py)

This is a property list (plist) I have mentioned during the [Optimized iPhone Storage](https://theforensicscooter.com/2022/12/05/do-you-have-a-full-sized-assetor-just-a-thumbnail-did-optimized-iphone-storage-process-occur/) and [Shared with You](https:...