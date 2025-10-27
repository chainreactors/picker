---
title: Velociraptor Version 0.6.7 Better Offline Collection, Encryption, and an Improved NTFS Parser Dig Deeper Than Ever
url: https://www.rapid7.com/blog/post/2022/12/02/velociraptor-version-0-6-7-better-offline-collection-encryption-and-an-improved-ntfs-parser-dig-deeper-than-ever/
source: Instapaper: Unread
date: 2022-12-06
fetch_date: 2025-10-04T00:36:26.067284
---

# Velociraptor Version 0.6.7 Better Offline Collection, Encryption, and an Improved NTFS Parser Dig Deeper Than Ever

[![Rapid7](/_next/static/media/rapid7-logo.cd245920.svg)](/)

* Platform
* Services
* Resources
* Partners
* Company

##

[Request Demo](/request-demo/)

[Back to Blog](/blog/)

Detection and Response

# Velociraptor Version 0.6.7: Better Offline Collection, Encryption, and an Improved NTFS Parser Dig Deeper Than Ever

[![Mike Cohen](/default-author-image.svg)

Mike Cohen](/blog/author/mike-cohen/)

Dec 2, 2022|Last updated on Aug 25, 2023|xx min read

![Velociraptor Version 0.6.7: Better Offline Collection, Encryption, and an Improved NTFS Parser Dig Deeper Than Ever](https://www.rapid7.com/cdn/assets/blt8233f404f4edae83/683ddef93d7b5e2bb11365ba/ThinkstockPhotos-177843422.jpg)

*By Mike Cohen and Carlos Canto*

Rapid7 is excited to announce the release of version 0.6.7 of [Velociraptor](/products/velociraptor/) – an advanced, open-source [digital forensics and incident response (DFIR)](/fundamentals/digital-forensics-and-incident-response-dfir/) tool that enhances visibility into your organization’s endpoints. This release has been in development and testing for several months and features significant contributions from our community.  We are thrilled to share its powerful new features and improvements.

## NTFS Parser changes

In this release, the NTFS parser was improved significantly. The main areas of development focused on better support for NTFS compressed and sparse files as well as improved path reconstruction.

In NTFS, there is a Master File Table (MFT) containing a record for each file on the filesystem. The MFT entry describes a file by attaching several attributes to it. Some of these are $FILE\_NAME attributes representing the names of the file.

In NTFS, a file may have multiple names. Normally, files have a long file name and a short filename. Each $FILE\_NAME record also contains a reference to the parent MFT entry of its directory.

When Velociraptor parses the MFT, it attempts to reconstruct the full path of each entry by traversing the parent MFT entry, recovering its name, etc. Previously, Velociraptor used one of the $FILE\_NAME records (usually the long file name) to determine the parent MFT entry. However, this is not strictly correct, as each $FILE\_NAME record can be a **different parent directory**. This surprising property of NTFS is called **hard links**.

You can play with this property using the fsutil program. The following adds a hard link to the program at C:/users/test/downloads/X.txt into a different directory.

C:> fsutil hardlink create c:\Users\Administrator\Y.txt c:\Users\Administrator\downloads\X.txtHardlink created for c:\Users\Administrator\Y.txt <<===>> c:\Users\Administrator\downloads\X.txt

The same file in NTFS can exist in multiple directories at the same time by use of hard links. The filesystem simply adds a new $FILE\_NAME entry to the MFT entry for the file pointing at another parent directory MFT entry.

Therefore, when scanning the MFT, Velociraptor needs to report all possible directories in which each MFT entry can exist – there can be many such directories, since each directory can have its own hard links.

**As a rule, an MFT Entry can represent many files in different directories!**

![An example of the notepad MFT entry with its many hard links](https://lh6.googleusercontent.com/wCf_Gbqg2v9IMnHYJCCS_Mvq1mZcIFDis1j2Vc-8-MzA66bejCiHmbOkv491DmR_xQACcUvFR5nn-jPWfhJiXLFt_w2jmmh0RxEpfWSUZtfhhPWYICvTdB0Bg0pBtv2fb1jKpO7lTJCG-ZRnztztygtam9sZlzwjaWeH3Zlh9p6p8t-3q0c-URsnaV5Kqg)An example of the notepad MFT entry with its many hard links

## Reassembling paths from MFT entries

When Velociraptor attempts to reassemble the path from an unallocated MFT entry, it might encounter an error where the parent MFT entry indicated has already been used for some other file or directory.

In previous versions, Velociraptor simply reported these parents as potential parts of the full path, since – for unallocated entries – the path reconstruction is best effort. This led to confusion among users with often nonsensical paths reported for unallocated entries.

In the latest release, Velociraptor is more strict in reporting parents of unallocated MFT entries, also ensuring that the MFT sequence numbers match. If the parent’s MFT entry sequence number does not match, Velociraptor’s path reconstruction indicates this as an error path.

![Unallocated MFT entries may have errors reconstructing a full path](https://lh5.googleusercontent.com/6rlFCnbAsVFMzEBVUDdkMSz9-yAh-9DO48H5t0FtAN5BcpVoccrZFZjwkYOFJxJC0jXZnB3NGyxzPfd2YIodQ65ffG62vDWt3bZNp_1bcf0Qmq0L_VJ5KGpFIapaSebHsjhvrkitlyoq2xK70Kv5SKk1phf3EdasgjjhCzvLiAk51H28Oebp4HD0ZhrglQ)Unallocated MFT entries may have errors reconstructing a full path

In the above example, the parent’s MFT entry has a sequence number of 5, but we need a sequence number of 4 to match it. Therefore, the parent’s MFT entry is rejected and instead we report the error as the path.

## The offline collection and encryption

Velociraptor’s offline collector is a pre-configured Velociraptor binary, which is designed to be a single shot acquisition tool. You can build an Offline Collector by following the [documentation](https://docs.velociraptor.app/docs/offline_triage/#offline-collections). The Offline Collector does not require access to the server, instead simply collecting the specified artifacts into a zip file (which can subsequently be uploaded to the cloud or simply shared with the DFIR experts for further analysis).

Previously, Velociraptor only supported encrypting the zip archive using a password. This is problematic because the password had to be embedded inside the collector configuration and so could be viewed by anyone with access to the binary.

In the latest release, Velociraptor supports asymmetric encryption to protect the acquisition zip file. There are two asymmetric schemes: X509 encryption and PGP encryption. Having asymmetric encryption improves security greatly because only the public key needs to be included in the collector configuration. Dumping the configuration from the collection is not sufficient to be able to decrypt the collected data - the corresponding private key is also required!

This is extremely important for forensic collections since these will often contain sensitive and PII information.

Using this new feature is also extremely easy: One simply selects the X509 encryption scheme during the configuration of the offline collector in the GUI.

![Configuring the offline collector for encryption](https://lh3.googleusercontent.com/FHyuW2--kdEphFovYcR1CIM-v2JooSK_fjYfIRKI1Yi-GEDa7YQC0G9S-9DES4Qnwf_noWJeZ5F6nnmyrI1jNixD46jVnaz-Y1EZhQbDCermLhdURJ2UH49llQxa0y38mBI8EhozbyyhV0vVfDDv97oU-ovqRWPrfTxw6YO9RWdRZopQxpOuE9Y4q_cheg)Configuring the offline collector for encryption

You can specify any X509 certificate here, but if you do not specify any, Velociraptor will use the server’s X509 certificate instead.

Velociraptor will generate a random password to encrypt the zip file, and then encrypt this password using the X509 certificate.

![The resulting encrypted container](https://lh4.googleusercontent.com/75GMxNDSQhpeUynBB9X5JMT4t30q8fYBTMriMeveBW5K06_Nh_eMxCZGoe3ccBBOPaz2YgKnXh-ejwdZE-PlV0-U5Xeww1-D2pIbUTl9FEziS4zZfvRd4CUJdNHpVDu3mcNXV1eN_xMMEDaf7MxCSim1ysZ3Yco2H3FtORVZcfx6tMpvDQcM-Kh_MX4bRQ)The resulting encrypted container

Since the ZIP standard does not encrypt the file names, Velociraptor embeds a second zip called data.zip inside the container. The above illustrates the encrypted data zip file and the metadata file that describes the encrypted password.

Because the password used to encrypt the container is not known and needs to be derived from the X509 private key, we must use Velociraptor itself to decrypt the container (i.e. we can not use something like 7zip).

![Decrypting encrypted containers with the server’s private key](https://lh5.googleusercontent.com/GlJ2vWv4_74NSgZhi9SnWf0-4f7DEMtVlhmPNs9oY5piOmLHHhbqbax8aOXxsKtNj4zeUMLFFir5gC43u1T2x7FTY7mlxpcQatu_QG...