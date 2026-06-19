---
title: Explainer Disk encryption
url: https://eclecticlight.co/2026/06/13/explainer-disk-encryption/
source: Instapaper: Unread
date: 2026-06-18
fetch_date: 2026-06-19T07:09:23.225154
---

# Explainer Disk encryption

[Skip to content](#content)

[![](https://eclecticlight.co/wp-content/uploads/2015/01/eclecticlightlogo-e1421784280911.png?w=103)](https://eclecticlight.co/)

# [The Eclectic Light Company](https://eclecticlight.co/)

Macs & painting – 🦉 No AI content

##### Main navigation

Menu

* [Downloads](https://eclecticlight.co/downloads/)
* [Freeware](https://eclecticlight.co/free-software-menu/)
* [All Macs](https://eclecticlight.co/mac-problem-solving-2-2/)
* [M1-M5 Macs](https://eclecticlight.co/m1-macs-2/)
* [Troubleshooting](https://eclecticlight.co/mac-troubleshooting-summary/)
* [Painting](https://eclecticlight.co/painting-topics-2-2/)
* [Mac Front Page](https://eclecticlight.co/category/macs/)

[hoakley](https://eclecticlight.co/author/hoakley/)
[June 13, 2026](https://eclecticlight.co/2026/06/13/explainer-disk-encryption/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **Explainer:** Disk encryption

This week’s news of deprecations in macOS is dominated by CoreStorage, and the consequent loss of access to HFS+ encrypted volumes. As it might seem odd that a part of macOS responsible for Fusion Drives should also affect encryption, this article tries to explain why, and where we’ve got to since.

In the Good Old Days, our Macs seldom contained anything particularly sensitive, and the few files that might hold private information could be encrypted on their own. Then came electronic banking, credit card and ID information, and crypto wallets, and we really needed to ensure they were properly protected.

#### HFS+

With the release of Mac OS X, its native file system HFS+ had no support for encryption. When Apple introduced its first version of FileVault to encrypt just the user’s Home folder in 2003, that had to be accomplished using an encrypted disk image. That not only caused problems with Time Machine backups, but its protection was easily defeated and the whole disk image decrypted.

The first whole-volume encryption for HFS+ came in 2011, when Apple added support for a logical volume manager in CoreStorage, which implements encryption for HFS+. The second and more successful attempt at FileVault thus used HFS+ with whole-volume encryption in CoreStorage. Encrypted HFS+ has also been available for use on external storage, where it still depends on CoreStorage.

Encrypted HFS+ uses the XTS-AES mode of AES with a 256-bit key, with both encryption and decryption being performed by the CPU. Earlier Intel processors didn’t have instructions to accelerate that, and combination with hard disk storage imposed a noticeable overhead of around 3% on storage read and write. This was most apparent when encryption was first enabled on a volume, which could take many hours before its entire contents had been encrypted.

Among other features reliant on CoreStorage are Apple’s Fusion Drives, consisting of a larger hard disk with an SSD working together as a pair in tiered storage, introduced in late 2012. It appears that macOS Tahoe might have already discontinued support for Fusion Drives, although its `diskutil` command still claims to support them, and a [recent support note](https://support.apple.com/102226) doesn’t mention any limitations.

#### APFS

The next step was a file system that had encryption designed into it from the start, APFS, released in 2017. That was quickly followed by hardware support for encryption, first in T2 chips, then in Apple silicon chips from 2020.

What has been encrypted has also changed over time. The first FileVault only encrypted the contents of a user’s Home folder, but CoreStorage encrypts whole HFS+ volumes. Until macOS Catalina divided the startup volume into System and Data volumes in a boot volume group, FileVault encrypted both system and user files. From Catalina onwards it was thought that all volumes on the internal SSD were encrypted, but more recently it has become clear that has been limited to the Data volume, possibly since Big Sur.

The hardware that performs FileVault’s encryption and decryption is part of the controller for the internal SSD, and is outside the Secure Enclave, which is responsible for generating and protecting the keys used.

[![](https://eclecticlight.co/wp-content/uploads/2025/10/filevaultpasswords1a.jpg)](https://eclecticlight.co/wp-content/uploads/2025/10/filevaultpasswords1a.jpg)

When you enter your FileVault password, that’s passed to the Secure Enclave, where it’s combined with the hardware key to generate the Key Encryption Key (KEK), and that’s then used together with hardware and xART keys to decrypt or unwrap the Volume Encryption Key (VEK) used for decryption/encryption.

![apfsencryption1](https://eclecticlight.co/wp-content/uploads/2024/04/apfsencryption1.png?w=940)

APFS encryption more generally also uses separate VEKs and KEKs which are stored in and accessed from Keybags associated with both containers and volumes. The Container Keybag contains wrapped VEKs for each encrypted volume within that container, together with the location of each encrypted volume’s keybag. The Volume Keybag contains one or more wrapped KEKs for that volume, and an optional passphrase hint. However, because those Keybags are stored in the file system on the encrypted disk and not protected by a Secure Enclave, they’re inherently more vulnerable.

#### Future

Most recent is the threat posed by anticipated advances in quantum cryptography, which promise to break some classical encryption methods. At present, Apple considers that FileVault should remain robust because of its multiple layers of protection. However, it may be that doubling the key size from 256 to 512 bits is an appropriate defence for APFS encryption that doesn’t enjoy the protection of the Secure Enclave.

#### Further reading

[A Brief History of FileVault](https://eclecticlight.co/2024/10/19/a-brief-history-of-filevault/)
[How keys are used in FileVault and encryption](https://eclecticlight.co/2025/06/25/how-keys-are-used-in-filevault-and-encryption/)
[macOS Tahoe extends quantum-secure encryption](https://eclecticlight.co/2025/07/07/macos-tahoe-extends-quantum-secure-encryption/)
[Quantum-secure cryptography in Apple operating systems](https://support.apple.com/guide/security/secc7c82e533/web)

### Share this:

* [Share on X (Opens in new window)
  X](https://eclecticlight.co/2026/06/13/explainer-disk-encryption/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2026/06/13/explainer-disk-encryption/?share=facebook)
* [Share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2026/06/13/explainer-disk-encryption/?share=reddit)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2026/06/13/explainer-disk-encryption/?share=pinterest)
* [Share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2026/06/13/explainer-disk-encryption/?share=threads)
* [Share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2026/06/13/explainer-disk-encryption/?share=mastodon)
* [Share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2026/06/13/explainer-disk-encryption/?share=bluesky)
* Email a link to a friend (Opens in new window)
  Email
* [Print (Opens in new window)
  Print](https://eclecticlight.co/2026/06/13/explainer-disk-encryption/#print?share=print)

Like Loading...

### *Related*

Posted in [Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/) and tagged [APFS](https://eclecticlight.co/tag/apfs/), [CoreStorage](https://eclecticlight.co/tag/corestorage/), [encryption](https://eclecticlight.co/tag/encryption/), [FileVault](https://eclecticlight.co/tag/filevault/), [HFS+](https://eclecticlight.co/tag/hfs/), [Secure Enclave](https://eclecticlight.co/tag/secure-enclave/). Bookmark the [permalink](https://eclecticlight.co/2026/06/13/explainer-disk-encryption/).

## 18Comments

[Add ...