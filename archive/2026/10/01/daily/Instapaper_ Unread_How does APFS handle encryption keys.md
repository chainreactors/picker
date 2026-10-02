---
title: How does APFS handle encryption keys
url: https://eclecticlight.co/2026/09/30/how-does-apfs-handle-encryption-keys/
source: Instapaper: Unread
date: 2026-10-01
fetch_date: 2026-10-02T07:49:36.539626
---

# How does APFS handle encryption keys

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
[September 30, 2026](https://eclecticlight.co/2026/09/30/how-does-apfs-handle-encryption-keys/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# How does **APFS** handle encryption keys?

APFS volumes can be protected by encryption in several different ways, which can lead to confusion. While Apple provides a clear account of hardware encryption in FileVault, information about software encryption is harder to come by, and the focus of this article.

#### Hardware encryption

Apple’s [Platform Security Guide](https://support.apple.com/guide/security/sec4c6dc1b6e/web) gives extensive details of how this is implemented for internal SSDs in Intel T2 and Apple silicon Macs. Each volume in the internal SSD is thus in one of three states:

* unencrypted, including Recovery, Preboot and VM volumes in boot volume groups;
* encrypted, FileVault turned off, where the Volume Encryption Key (VEK) is protected only by the hardware UID in the Secure Enclave;
* encrypted, FileVault turned on, where the VEK is protected by a Key Encryption Key (KEK) incorporating the user’s password, and additional keys including a Recovery Key can be provided.

I have also written [an explanation](https://eclecticlight.co/2025/10/18/explainer-filevault-2/) of how this works in practice.

That guide doesn’t provide any details of software encryption, though, merely stating that “Encryption of removable storage devices doesn’t utilise the security capabilities of the Secure Enclave and instead is performed in the same manner as an Intel-based Mac without the T2 chip.”

#### Software encryption by APFS

APFS encryption also uses separate VEKs and KEKs stored in and accessed from Keybags associated with both containers and volumes. The Container Keybag contains wrapped VEKs for each encrypted volume within that container, together with the location of each encrypted volume’s keybag. The Volume Keybag contains one or more wrapped KEKs for that volume, and an optional passphrase hint. However, because those Keybags are stored in the file system on the encrypted disk and not protected by a Secure Enclave, they’re inherently more vulnerable than those used for hardware encryption.

![apfsencryption1](https://eclecticlight.co/wp-content/uploads/2024/04/apfsencryption1.png?w=940)

Perhaps the best way to see how these are set up in APFS is to view its log entries when creating a new volume. The following sections show those for three cases, creation of an unencrypted volume, an encrypted volume, and conversion between them. Log excerpts are from APFS version 3288.1.3 in macOS 27.0.

#### Create an unencrypted APFS volume

The opening log entry in this sequence recording unencrypted volume creation establishes the volume’s protection status, following which the newly created volume is mounted, its block size is set to the standard 4 KiB, any special role is established, and the mount is reported as complete. There are no entries referring to keybags or keys.

`01.290870 apfs_newfs:31842: disk5s2 FS will NOT be encrypted.
01.374157 apfs_log_op_with_proc:3279: disk5s2 mounting volume Volume2, requested by: mount_apfs (pid 21246); parent: mount (pid 21245)
01.374217 handle_mount:893: disk5s2 vol-uuid: 46F64E35-AEE7-44D2-ABFA-DEA28A817EAF block size: 4096 block count: 488327436 (unencrypted; flags: 0x1; features: 1.0.2)
01.374237 handle_mount:906: disk5s2 setting dev block size to 4096 from 512
01.374239 nx_volume_group_update:706: disk5s2 Volume Volume2 role 0x0 is not a System or Data volume
01.374249 apfs_log_op_with_proc:3279: disk5s2 mount-complete volume Volume2, requested by: mount_apfs (pid 21246); parent: mount (pid 21245)`

#### Create an encrypted APFS volume

Before anything else, four keybag entries are written to set up encryption keys. This involves an ambiguous entry about effaceable storage, and is followed by an entry reporting the VEK and KEK have been created for the new volume. A key is then cached and copied.

`01.273143 keybag_operation:530: wrote APFS/container keybag (v2, 3 keys, 272 bytes)
01.520459 effaceable_is_disabled:12448: ================ no-effaceable-storage is ON ================
01.521011 keybag_operation:530: wrote APFS/container keybag (v2, 1 keys, 192 bytes)
01.521939 keybag_operation:530: wrote APFS/container keybag (v2, 3 keys, 272 bytes)
01.522878 keybag_operation:530: wrote APFS/container keybag (v2, 4 keys, 432 bytes)
01.522898 apfs_meta_crypto_state_init:1575: disk5s3 created apfs volume KEK/VEK
01.696719 apfs_keycache_operation:13490: cached key for uuid 8DE84272-7D3E-4CAE-BAE7-343F122D0D00 and type 1
01.765139 apfs_keycache_operation:13500: copied key for uuid 8DE84272-7D3E-4CAE-BAE7-343F122D0D00 and type 1`

Once those are complete, entries reporting the mounting of the new volume are similar to those of an unencrypted volume. One significant addition is the explicit destruction of the cached key.

`01.765583 apfs_log_op_with_proc:3279: disk5s3 mounting volume Volume3, requested by: mount_apfs (pid 21287); parent: mount (pid 21286)
01.765676 handle_mount:893: disk5s3 vol-uuid: 8DE84272-7D3E-4CAE-BAE7-343F122D0D00 block size: 4096 block count: 488327436 (encrypted; flags: 0x8; features: 1.0.2)
01.765714 handle_mount:906: disk5s3 setting dev block size to 4096 from 512
01.765718 nx_volume_group_update:706: disk5s3 Volume Volume3 role 0x0 is not a System or Data volume
01.765729 apfs_keycache_operation:13507: destroyed key for uuid 8DE84272-7D3E-4CAE-BAE7-343F122D0D00 and type 1
01.765737 apfs_log_op_with_proc:3279: disk5s3 mount-complete volume Volume3, requested by: mount_apfs (pid 21287); parent: mount (pid 21286)`

#### Encrypt an existing unencrypted APFS volume

A first attempt to initialise the volume keybag to contain wrapped KEKs fails, presumably because the keybag hasn’t been created yet. A slightly different sequence of entries about effaceable storage and writing keys follows, then an entry reporting adding unlock records or hints to the volume keybag.

00.691061 apfs\_keybag\_init:2877: failed to initialize volume keybag, err = 2
00.696244 effaceable\_is\_disabled:12448: ================ no-effaceable-storage is ON ================
00.696465 keybag\_operation:530: wrote APFS/container keybag (v2, 1 keys, 64 bytes)
00.941992 effaceable\_is\_disabled:12448: ================ no-effaceable-storage is ON ================
00.942402 keybag\_operation:530: wrote APFS/container keybag (v2, 1 keys, 192 bytes)
00.942856 keybag\_operation:530: wrote APFS/container keybag (v2, 1 keys, 64 bytes)
00.943390 keybag\_operation:530: wrote APFS/container keybag (v2, 2 keys, 224 bytes)

00.987730 keybag\_operation:530: wrote APFS/container keybag (v2, 2 keys, 240 bytes)
00.988128 keybag\_operation:530: wrote APFS/container keybag (v2, 2 keys, 224 bytes)
00.996258 \_APFSVolumeAddUnlockRecordsOrHints:1745: UR\_ADD\_UPDATE\_SET [ OP = 4, UUID = [private], VOLUME = [private], ret = 0 ]

#### Conclusions

* Unencrypted APFS volumes don’t appear to have volume keybags, and certainly don’t have keys there or in the container keybag.
* Keys are created early and added to keybags when a volume is to be encrypted.
* Creation of volume KEK/VEK is explicitly recorde...