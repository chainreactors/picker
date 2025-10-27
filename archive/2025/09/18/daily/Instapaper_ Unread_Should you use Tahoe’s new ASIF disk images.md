---
title: Should you use Tahoe’s new ASIF disk images
url: https://eclecticlight.co/2025/09/17/should-you-use-tahoes-new-asif-disk-images/
source: Instapaper: Unread
date: 2025-09-18
fetch_date: 2025-10-02T20:20:28.070883
---

# Should you use Tahoe’s new ASIF disk images

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
[September 17, 2025](https://eclecticlight.co/2025/09/17/should-you-use-tahoes-new-asif-disk-images/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# Should you use Tahoe’s new **ASIF** disk images?

Among the many new features [Apple lists](https://www.apple.com/os/pdf/All_New_Features_macOS_Tahoe_Sept_2025.pdf) for macOS 26 Tahoe is a new disk image format, Apple Sparse Image Format or ASIF. In that list it appears as a feature for virtualisation, and is explained as: “Create virtualized disk images with a virtualized file format that can be formatted to any kind of file system.”

Yet in the [help pages](https://support.apple.com/et-ee/guide/disk-utility/dskutl11888/mac) for Disk Utility, the claim goes further: “A modern sparse read/write image. The space it uses on your disk is proportional to the data it contains, making it efficient and general-purpose.” In Apple’s [developer documentation](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment/) for virtualisation, there’s more detail still:
“Apple Sparse Image Format (ASIF) files transfer more efficiently between hosts or disks because their intrinsic structure doesn’t depend on the host file system’s capabilities. The size the ASIF file takes on the file system is proportional to the actual data stored in the disk image.”

This article considers whether this new ASIF disk image format, as implemented in macOS 26.0, is more suitable for general purposes than the other two leading contenders. Should you use ASIF instead of sparse bundle or read-write (UDRW) disk images?

#### Testing

To assess the performance of these disk images, read and write speeds were measured in macOS 26.0 Tahoe running on a Mac mini M4 Pro with a 2 TB internal SSD. Each disk image was created using Disk Utility, with a single APFS volume in a disk of maximum size 100 GB stored on the internal SSD, with FileVault enabled. Each format was tested using plain APFS, and separately using APFS Encrypted with 256-bit AES.

When each disk image was created and mounted, a single folder was created in it, and the image unmounted. The disk image was mounted again, and a standard write test performed into the folder using [Stibium](https://eclecticlight.co/dintch/). That writes in random order a total of 160 files ranging in size from 2 MB to 2 GB, totalling 53 GB. Once the write speed had been measured the image was unmounted again and Stibium closed. For the read test the image was mounted again and all 160 files in the test folder were read in random order using Stibium to measure their speed.

#### Results

Read and write performance for each of the tests are shown in the table, where results are ranked by read speed.

[![](https://eclecticlight.co/wp-content/uploads/2025/09/tahoediskimages.png)](https://eclecticlight.co/wp-content/uploads/2025/09/tahoediskimages.png)

All three disk image formats achieve similar read and write speeds with unencrypted images. There were substantial differences in performance, though, when encryption was used. With encryption, the sparse bundle was faster than both RAW (Read-Write, UDRW) and ASIF. The new format read at exactly half the speed of a sparse bundle, and at 57% of write speed. ASIF with APFS Encrypted was the slowest of the seven tests in both read and write.

Differences in the size on disk of images were small. Empty disks were smallest for sparse bundles and ASIF, and following deletion of all test files, ASIF returned to the smallest size, indicating that it’s the most space-efficient.

#### Why use ASIF?

If ASIF doesn’t perform any better than existing formats, and any gains in space on disk are small, when and why should you use the new format? To appreciate its strengths, you need to consider how the other two formats work in terms of the file system they’re hosted on, and the file system they run internally.

A sparse bundle stores its contents on many band files inside its bundle. When its internal file system is able to compact free space, used space can be compacted into a minimum number of bundles, and those containing just free space can be deleted. Thus the total size of its bundle will vary according to the space required to store its contents. Coupled with efficient read and write support this results in good space efficiency and performance.

When a Raw Read-Write disk image has an internal file system that is capable of Trimming free space, as APFS and HFS+ can, that process will compact free space within the image. When the image is stored on a host file system that supports sparse file format, as APFS does, the space in the image that is free can be skipped, resulting in a space-efficient sparse file. However, a host file system like HFS+ that doesn’t offer a sparse file format is unable to take advantage of that.

ASIF is claimed to be able to accomplish similar economy of storage space without relying on the host file system’s special file formats, making it more suitable when the conditions required by sparse bundles and Raw Read-Write disk images aren’t available.

Although this new feature has been announced for virtualisation, it’s most probably only going to be useful for those running VMs stored on file systems other than APFS. Prior to the introduction of ASIF, VMs hosted on APFS have used Raw Read-Write style storage which has benefited from sparse file format, whether they’re macOS or Linux. Where ASIF may be of greatest benefit is for VMs run from network shares or cloud services, whose host file system won’t be APFS.

#### Recommendations

* ASIF should be the disk image format of choice when neither sparse bundles nor Raw Read-Write images can achieve similar economy in host storage space.
* In other circumstances, where sparse bundles or Raw Read-Write images can provide space-efficient storage and full performance, they are still to be preferred.
* At present, ASIF isn’t generally a better replacement for sparse bundles or Raw Read-Write images, particularly when their internal and host file systems are APFS.
* ASIF is likely to be of greatest benefit to those running macOS or Linux virtual machines from network shares or cloud services, where the VM can’t be hosted on APFS.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://eclecticlight.co/2025/09/17/should-you-use-tahoes-new-asif-disk-images/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2025/09/17/should-you-use-tahoes-new-asif-disk-images/?share=facebook)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2025/09/17/should-you-use-tahoes-new-asif-disk-images/?share=reddit)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2025/09/17/should-you-use-tahoes-new-asif-disk-images/?share=pinterest)
* [Click to share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2025/09/17/should-you-use-tahoes-new-asif-disk-images/?share=threads)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2025/09/17/should-you-use-tahoes-new-asif-disk-images/?share=mastodon)
* [Click to...