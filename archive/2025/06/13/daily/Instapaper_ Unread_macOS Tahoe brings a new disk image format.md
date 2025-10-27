---
title: macOS Tahoe brings a new disk image format
url: https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/
source: Instapaper: Unread
date: 2025-06-13
fetch_date: 2025-10-06T22:55:28.914272
---

# macOS Tahoe brings a new disk image format

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
[June 12, 2025](https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# macOS Tahoe brings a new disk image format

Disk images have been valuable tools marred by poor performance. In the wrong circumstances, an encrypted sparse image (UDSP) stored on the blazingly fast internal SSD of an Apple silicon Mac may write files no faster than 100 MB/s, typical for a cheap hard drive. One of the important new features introduced in macOS 26 Tahoe is a new disk image format that can achieve near-native speeds: ASIF, [documented here](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment/).

This has been detailed as a major improvement in lightweight virtualisation, where it promises to overcome the most significant performance limitation of VMs running on Apple silicon Macs. However, ASIF disk images are available for general use, and even work in macOS Sequoia. This article shows what they can do.

Apple provides few technical details, other than stating that the intrinsic structure of ASIF disk images doesn’t depend on the host file system’s capabilities, and their size on the host depends on the size of the data stored in the disk. In other words, they’re a sparse file in APFS, and are flagged as such.

#### Make an ASIF disk image

Currently, there are only two ways to create one of these new disk images, either in Tahoe’s Disk Utility, or using its `diskutil` command tool, as in
`diskutil image create blank --format ASIF --size 100G --volumeName myVolume imagePath`
to create an ASIF image with a maximum capacity of 100 GB with a single APFS volume named `myVolume` with the path and name `imagePath`. You can also use a `from` option to convert an existing disk image to ASIF format.

These are only good for Tahoe, as there’s no support for their creation in Sequoia 15.5 or earlier. Neither is there any access documented for the `hdiutil` command tool, more normally used to work with disk images, although its general commands should work fine with ASIFs.

Resulting disk images have a UTI type of `com.apple.disk-image-sparse`, in contrast to RAW (UDIF read-write) images of type `com.apple.disk-image-udif`, which can be used to distinguish them.

#### Economy

When first created, a 100 GB ASIF disk image took less than 1 GB disk space, but after extensive use and adding a second volume, its size on disk when empty again ranged between 1.9-3.2 GB. No attempt was made to compact the disk image using `hdiutil`, and its man page doesn’t make clear whether that’s supported or effective with this type of disk image.

#### Performance

Read and write performance were measured using [Stibium](https://eclecticlight.co/dintch/) over a total of more than 50 GB in 160 files ranging in size from 2 MB to 2 GB in randomised order. When performed using a 100 GB ASIF image on the 2 TB internal SSD of a MacBook Pro M3 Pro running macOS 26 beta, transfer speeds for unencrypted APFS were 5.8 and 6.6 GB/s read and write. Those fell to 4.8 and 4.6 GB/s when using an APFS encrypted volume in the disk image.

Although there’s currently no way to create an ASIF disk image on a Mac running Sequoia, I compressed the disk image using Apple Archive (aar) to preserve its format and copied it to a Mac mini M4 Pro running macOS 15.5, and repeated the performance tests on its 2 TB internal SSD. Unencrypted APFS there attained 5.5 and 8.3 GB/s read and write.

#### Use

Apple recommends switching from the previous RAW (UDIF read-write) disk images used for the backing store of VMs to ASIF for their greater efficiency in file transfer between hosts or disks. As the disk image in a VM is created when the VM is first made and installed, this awaits implementation in virtualisers. Because the only access provided at present is the `diskutil` command tool, apps will need to consider creating an ASIF image where that’s available, in macOS 26 Tahoe.

Although ASIF appears to be supported by Sequoia 15.5, the danger with a VM based on an ASIF image is that it may not be compatible with older versions of macOS. Apple hasn’t yet revealed which of those can mount and use this new format.

[Previous tests](https://eclecticlight.co/2024/10/16/disk-images-performance/) on different types of disk image demonstrated that, prior to ASIF, the best performance was achieved by sparse bundles. The following table compares those with ASIF.

[![](https://eclecticlight.co/wp-content/uploads/2025/06/diskimages25.png)](https://eclecticlight.co/wp-content/uploads/2025/06/diskimages25.png)

Allowing for the differences in chips, ASIF is clearly faster than both UDRW read-write and UDSP sparse images, whether plain or encrypted. It’s also likely to be significantly faster than sparse bundles, and has the advantage that it uses a single file for its backing store.

#### Conclusions

* Where possible, in macOS 26 Tahoe in particular, VMs should use ASIF disk images rather than RAW/UDRW.
* Unless a sparse bundle is required (for example when it’s hosted on a different file system such as that in a NAS), ASIF should be first choice for general purpose disk images in Tahoe.
* It would be preferable for virtualisers to be able to call a proper API rather than a command tool.
* Keep an eye on [C-Command’s DropDMG](https://c-command.com/dropdmg/). I’m sure it will support ASIF disk images soon.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/?share=facebook)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/?share=reddit)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/?share=pinterest)
* [Click to share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/?share=threads)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/?share=mastodon)
* [Click to share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/?share=bluesky)
* Click to email a link to a friend (Opens in new window)
  Email
* [Click to print (Opens in new window)
  Print](https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/#print?share=print)

Like Loading...

### *Related*

Posted in [Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/) and tagged [ASIF](https://eclecticlight.co/tag/asif/), [disk image](https://eclecticlight.co/tag/disk-image/), [Disk Utility](https://eclecticlight.co/tag/disk-utility/), [diskutil](https://eclecticlight.co/tag/diskutil/), [macOS 26](https://eclecticlight.co/tag/macos-26/), [sparse image](ht...