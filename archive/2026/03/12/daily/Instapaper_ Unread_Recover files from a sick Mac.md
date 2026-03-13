---
title: Recover files from a sick Mac
url: https://eclecticlight.co/2026/03/10/recover-files-from-a-sick-mac/
source: Instapaper: Unread
date: 2026-03-12
fetch_date: 2026-03-13T04:07:58.735659
---

# Recover files from a sick Mac

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
[March 10, 2026](https://eclecticlight.co/2026/03/10/recover-files-from-a-sick-mac/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# Recover files from a sick Mac

Gone are the days when you could pop the hard drive out of a sick Mac and connect it to another to recover its contents. This article explains how you may be able to transfer some or all of the contents of a modern Mac’s internal SSD to another Mac.

#### Any Mac: Thunderbolt

As long as you can get your Mac up and running, the fastest way to transfer files from its internal storage is back-to-back Thunderbolt networking, easily set up in Network settings. All you need is another Mac with a free Thunderbolt port and a suitable cable to connect them directly.

#### Apple silicon: Share Disk

If you can get an Apple silicon Mac to start up in Recovery mode, or Fallback Recovery, then you’ve got a good chance of salvaging whatever you need from its internal SSD.

Connect it back-to-back with another Mac using a Thunderbolt 4 (or 3) cable. Start the sick Mac up in Recovery, pass through to Options and authenticate as necessary. In the **Utilities** menu there select the **Share Disk** command.

[![](https://eclecticlight.co/wp-content/uploads/2026/03/target1.png)](https://eclecticlight.co/wp-content/uploads/2026/03/target1.png)

Select the volume you want to share, and when necessary unlock it with the password required for its encryption.

On the other Mac, that shared volume should appear as a networked device, connected as Guest, or on the Desktop. Despite that, you should have full access to its contents. This connection uses SMB, so listing large folders in the Finder will be surprisingly slow.

[![](https://eclecticlight.co/wp-content/uploads/2026/03/target2.jpg)](https://eclecticlight.co/wp-content/uploads/2026/03/target2.jpg)

Now you can copy across all the files you want to your other Mac. That’s impressively quick, and can read them at about 3 GB/s, as you’d expect from a fast locally attached SSD. However, because of the SMB overhead, copying many small files is noticeably slower.

This can also get a bit kludgy when you’ve finished and want to disconnect. Trying to eject the shared volume may not work, and even when you stop sharing on the Mac in Recovery, and disconnect the cable, you may find the other Mac just won’t let go of it.

This only works with a single volume at a time. If you have added volumes to your Mac’s internal SSD, then you’ll have to repeat the process to access files on a different volume. But it does allow you to choose which volume to share.

#### Apple silicon: DFU mode

If you’re unable to put your sick Mac into Recovery, or Fallback Recovery, it’s still possible it has entered DFU mode, or could do so when started up to engage that mode. This is explored in more detail in [this article](https://eclecticlight.co/2026/02/04/is-your-mac-dead-in-dfu-mode-or-alive/), but doesn’t give you access to the contents of the Mac’s internal storage. You could try reviving it rather than performing a full Restore, though, as that isn’t destructive of its contents.

#### Intel T2: Target Disk

There are now two ways to enter Target Disk Mode on an Intel Mac with a T2 chip: if the Mac is already up and running (and not near-dead at all), you can opt for this in System Settings > General > Startup Disk, although I’m not sure why you would want to. If the Target really is sick, the only way you’re likely to engage this mode is to hold the T key during startup until the Thunderbolt symbol appears on its display.

The Target and Host must now be connected using a Thunderbolt 3 or 4 cable, although between Macs that are *both* running Catalina or earlier, a USB or USB-C cable could be used instead.

Shortly after they’re connected and ready, the Target’s internal Data volume should mount in the Host’s Finder. You should then be prompted for its FileVault password, and gain access to its contents. As with Apple silicon Macs, you can also copy files from the Host to the Target. To disconnect the Host and Target, eject the Target’s volume from the Host, then press and hold the Power button on the Target to shut it down.

Note that Target Disk Mode doesn’t offer a choice of volume.

#### Any Mac: External Boot Disk

If an Intel Mac with a T2 chip already has its boot security set (using Startup Security Utility) to allow it boot from an external disk, you may be able to get that to work, then mount the internal SSD to allow you to recover its contents to that or another external disk.

This is unlikely to work with an Apple silicon Mac, though, as it must always start the boot process from its internal SSD before it can continue booting from a system installed on an external bootable disk.

#### Summary

* Cable: Thunderbolt 4 (or 3) connecting the two Macs back-to-back.
* Apple silicon Mac: Recovery mode, Utilities menu, Share Disk.
* Intel T2 Mac: T key held during startup.
* Eject the Target’s disk on completion.
* Apple silicon Mac: disconnect button, then shut down.
* Intel T2 Mac: hold the Power button to shut down.

### Share this:

* [Share on X (Opens in new window)
  X](https://eclecticlight.co/2026/03/10/recover-files-from-a-sick-mac/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2026/03/10/recover-files-from-a-sick-mac/?share=facebook)
* [Share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2026/03/10/recover-files-from-a-sick-mac/?share=reddit)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2026/03/10/recover-files-from-a-sick-mac/?share=pinterest)
* [Share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2026/03/10/recover-files-from-a-sick-mac/?share=threads)
* [Share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2026/03/10/recover-files-from-a-sick-mac/?share=mastodon)
* [Share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2026/03/10/recover-files-from-a-sick-mac/?share=bluesky)
* Email a link to a friend (Opens in new window)
  Email
* [Print (Opens in new window)
  Print](https://eclecticlight.co/2026/03/10/recover-files-from-a-sick-mac/#print?share=print)

Like Loading...

### *Related*

Posted in [Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/) and tagged [Apple silicon](https://eclecticlight.co/tag/apple-silicon/), [Intel](https://eclecticlight.co/tag/intel/), [recovery](https://eclecticlight.co/tag/recovery/), [recovery mode](https://eclecticlight.co/tag/recovery-mode/), [SMB](https://eclecticlight.co/tag/smb/), [T2](https://eclecticlight.co/tag/t2/), [Target mode](https://eclecticlight.co/tag/target-mode/), [troubleshooting](https://eclecticlight.co/tag/troubleshooting/). Bookmark the [permalink](https://eclecticlight.co/2026/03/10/recover-files-from-a-sick-mac/).

## 4Comments

[Add yours](#reply-title)

1. 1
   ![EcleX's avatar](https://1.gravatar.com/avatar/a6d54e9182f7d897e95acb5d3a80ff3e906778739160d11135eb257ea3f2a7bd?s=96&d=identicon&r=G)

   EcleX
   [on March 10, 2026 at 9:17 am](https://eclecticlight.co/2026/03/10/recover-files-from-a-...