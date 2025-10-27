---
title: FileVault and volume encryption explained
url: https://eclecticlight.co/2025/01/10/filevault-and-volume-encryption-explained/
source: Instapaper: Unread
date: 2025-01-15
fetch_date: 2025-10-06T20:20:19.137292
---

# FileVault and volume encryption explained

[Skip to content](#content)

[![](https://eclecticlight.co/wp-content/uploads/2015/01/eclecticlightlogo-e1421784280911.png?w=103)](https://eclecticlight.co/)

# [The Eclectic Light Company](https://eclecticlight.co/)

Macs & painting – 🦉 No AI content

##### Main navigation

Menu

* [Downloads](https://eclecticlight.co/downloads/)
* [Freeware](https://eclecticlight.co/free-software-menu/)
* [M-series Macs](https://eclecticlight.co/m1-macs/)
* [Mac Problems](https://eclecticlight.co/mac-troubleshooting-summary/)
* [Mac articles](https://eclecticlight.co/mac-problem-solving/)
* [Macs](https://eclecticlight.co/category/macs/)
* [Art](https://eclecticlight.co/painting-topics/)

[hoakley](https://eclecticlight.co/author/hoakley/)
[January 10, 2025](https://eclecticlight.co/2025/01/10/filevault-and-volume-encryption-explained/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# FileVault and volume encryption explained

Macs use two main features to safeguard your data when it’s stored locally: encryption using FileVault, and APFS encrypted volumes. Although they might appear to be the same, this article explains how they differ, particularly on Macs with T2 or Apple silicon chips.

#### Definitions

FileVault is a form of encryption applied to the whole contents of the Data volume in a macOS boot volume group, controlled through the FileVault entry in Privacy & Security settings, and its predecessors.

An APFS encrypted volume is any volume (outside the Data volume) that is formatted using APFS Encrypted, either when first created or subsequently using the Finder’s contextual menu command, or an equivalent.

#### Enabling FileVault

FileVault is enabled and disabled using its entry in Privacy & Security settings, and applies only to the Data volume in the currently active boot volume group.

![filevault3](https://eclecticlight.co/wp-content/uploads/2023/03/filevault3.jpg?w=940)

When you enable it, you’ll be offered either a Recovery Key or iCloud recovery, to unlock it if you forget the password. When FileVault is enabled on a Data volume on the internal SSD of a Mac with a T2 or Apple silicon chip, the process is almost instant, as the Data volume is already encrypted, and your password is used to protect the key used to unlock the volume, as explained below. Thus no new encryption takes place.

That works differently for Intel Macs without a T2 chip, and for any Data volume on external storage, whose contents still have to be encrypted or decrypted, a process that can take many hours. In those cases, it’s best to enable FileVault when the Data volume has been freshly created, before filling it with more files, as encryption will then be quickest.

#### Enabling APFS encryption

The quickest and simplest way to encrypt an APFS volume is to do so when that volume is created, opting for APFS Encrypted format in Disk Utility. As the volume is empty to start with, encryption is instant, and everything added to that volume is encrypted as it goes along.

You can also opt for an existing APFS volume to be changed from unencrypted to encrypted. Select the volume in the Finder, open the contextual menu using Control-click, and there select the **Encrypt** command. Unless that volume is empty, macOS will then have to encrypt its current contents, which can take many hours if there are many files already in that volume.

#### How FileVault works

On Macs with T2 or Apple silicon chips, FileVault uses two features built into those chips: the Secure Enclave to protect and handle encryption keys, and a hardware encryption engine to perform encryption and decryption at blistering speed.

The Secure Enclave incorporates the storage controller for the internal SSD, so all data transferred between CPU and SSD passes through an encryption stage in the enclave. When FileVault is disabled, data on protected volumes is still encrypted using a volume encryption key (VEK), in turn protected by a hardware key and a xART key used to protect against replay attacks.

![filevaultpasswords1](https://eclecticlight.co/wp-content/uploads/2024/03/filevaultpasswords1.jpg?w=940)

When FileVault is enabled, the same VEK is used, but it’s protected by a key encryption key (KEK), and the user password is required to unwrap that KEK, so protecting the VEK used to perform encryption/decryption. This means that the user can change their password without the volume having to be re-encrypted, and allows the use of special recovery keys in case the user password is lost or forgotten. Keys are only handled in the Secure Enclave.

#### How APFS encryption works

Encryption keys are protected at all times by encrypting and encapsulating them using a process known as *wrapping.* APFS uses the AES Key Wrap Specification in RFC 3394, using a secret such as a password to maintain confidentiality of every key.

APFS also uses separate volume and key encryption keys (VEK and KEK), so enabling the use of multiple KEKs for a single VEK, and the potential to change a KEK without having to decrypt and re-encrypt the whole volume, as used in FileVault. In APFS, VEKs and KEKs are stored in and accessed from Keybags associated with both containers and volumes.

The Container Keybag contains wrapped VEKs for each encrypted volume within that container, together with the location of each encrypted volume’s keybag. The Volume Keybag contains one or more wrapped KEKs for that volume, and an optional passphrase hint. These are shown in the diagram below.

![apfsencryption1](https://eclecticlight.co/wp-content/uploads/2024/04/apfsencryption1.png?w=940)

Apple’s documentation refers to several secrets that can be used to wrap a KEK, including a user password, an individual recovery key, an institutional recovery key, and an unspecified mechanism implemented through iCloud. Currently, for normal software encryption in APFS, only two of those appear accessible: a user password is supported in both Disk Utility and `diskutil`‘s `apfs` verb, while `diskutil` also supports use of an institutional recovery key through its `-recoverykeychain` options. Individual and iCloud recovery keys only appear available when using FileVault, in this case implemented in software, either on Intel Macs without a T2 chip, or on all Macs when encrypting an external volume.

Because keybags are stored on the disk containing the encrypted volume, if the disk is connected to another Mac, when macOS tries to mount that volume, the user will be prompted to enter its password, and can then gain access to its contents. When FileVault is used to protect a Data volume on the internal SSD of a T2 or Apple silicon Mac, that volume can only be unlocked through the Secure Enclave of that Mac, and it isn’t possible to unlock it from another Mac (that’s also true when FileVault hasn’t been enabled on that volume).

#### Common example

The most common combination of encryption systems for a modern Mac (with a T2 or Apple silicon chip) is:

* FileVault encryption of the Data volume in the boot volume group forming the active system on the internal SSD, handled within the Secure Enclave, and managed using Privacy & Security settings.
* APFS Encrypted format of the Time Machine backup storage volume, handled using keys stored in the keybags on an external disk, and managed in the Finder.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://eclecticlight.co/2025/01/10/filevault-and-volume-encryption-explained/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2025/01/10/filevault-and-volume-encryption-explained/?share=facebook)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2025/01/10/filevault-and-volume-encryption-explained/?share=reddit)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2025/01/10/filevault-and-volume-encryption-explained/?sha...