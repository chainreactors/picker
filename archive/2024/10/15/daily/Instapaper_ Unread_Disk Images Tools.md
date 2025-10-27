---
title: Disk Images Tools
url: https://eclecticlight.co/2024/10/09/disk-images-tools/
source: Instapaper: Unread
date: 2024-10-15
fetch_date: 2025-10-06T18:55:26.527963
---

# Disk Images Tools

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
[October 9, 2024](https://eclecticlight.co/2024/10/09/disk-images-tools/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **Disk Images:** Tools

If you’re going to use disk images of any type, then getting the right tool for the job is essential. This article considers the leading candidates:

* Disk Utility, bundled with macOS
* DropDMG, $24.99 [from C-Command](https://c-command.com/dropdmg/), or from the App Store
* Spundle, free from its [Product Page here](https://eclecticlight.co/dintch/)
* `hdiutil`, the command tool bundled with macOS.

Although I’m sure there are a great many others, IMHO those should be at the top of your list.

#### Disk Utility

Create a new disk image using the **New Image** command in its **File** menu and there’s a basic range of choices on offer.

![dmgdiskutil](https://eclecticlight.co/wp-content/uploads/2024/10/dmgdiskutil.jpg)

This dialog has a longstanding bug, where it can reset the size you’ve entered if you change another setting, which can help you make mistakes. Otherwise, it gives limited access to some of the many options available, sufficient for the occasional and not too demanding user. Further options are available in its **Images** menu, including verification, adding checksums, conversions between types, and resizing. Notable by its absence is the ability to change the password of an encrypted disk image, which is unhelpfully deferred to the command line.

Documentation in Disk Utility’s Help book is also scant, and insufficient to serve as a reference. As Apple doesn’t provide any further technical information, apart from that in man hdiutil, you may find yourself searching websites such as this.

#### DropDMG

Since its release over 22 years ago, this has been the first choice for many who need to work with disk images, and is without doubt the best for those who distribute software in disk images. It has grown into the most comprehensive and capable utility for working with any type of disk image, and is backed up by a superb 123-page manual that goes a long way to filling the gap left by Apple. That manual is well-maintained, and contains links to recent technical articles and further information.

![dmgdropdmg](https://eclecticlight.co/wp-content/uploads/2024/10/dmgdropdmg.jpg)

DropDMG’s options for creating a new disk image far exceed those in Disk Utility. Particularly helpful are the compatible version hints shown on various options, to remind you of which file systems are available in different macOS versions, and which types of disk image container are supported. DropDMG will even convert old NDIF disk images last used in Mac OS 9 to more modern formats. It will also change the password of an encrypted disk image from a menu command.

For those who need to work with standard configurations, perhaps for software distribution, it lets you save and reuse them with ease. Those can include signing with developer certificates, product licences, background images, custom volume icons, and more. Whichever type of disk image you want to create or maintain, DropDMG should be your first choice.

#### Spundle

There are a few options for sparse bundles that even DropDMG doesn’t expose, such as control over band size, the ability to resize a sparse bundle, and to change its band size. If you want access to those, Spundle is a useful adjunct.

![dmgspundle](https://eclecticlight.co/wp-content/uploads/2024/10/dmgspundle.jpg)

Note that, unlike DropDMG, Spundle only works with sparse bundles.

#### `hdiutil`

Although this remains the definitive command tool that offers types of disk image and features you didn’t even know existed, it’s fiendishly complex to use, with a sprawling and overloaded grammar. Its man page runs to more than 11,000 words, but appears never to have been rewritten into any cohesive account of disk images, or command options. For example, change information is given in two sections, Compatibility and What’s New. Changes made in Catalina and later appear at the end of the Compatibility section, then the final What’s New section reverses time order and goes back from Catalina to Mac OS X 10.5.

I only recommend `hdiutil` for those who need to work with disk images in shell scripts, or for those few features that aren’t available in DropDMG or, for sparse bundles, in Spundle. It’s a command tool of last resort.

#### Previous article

[Introduction](https://eclecticlight.co/2024/10/07/disk-images-introduction/)

### Share this:

* [Click to share on X (Opens in new window)
  X](https://eclecticlight.co/2024/10/09/disk-images-tools/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2024/10/09/disk-images-tools/?share=facebook)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2024/10/09/disk-images-tools/?share=reddit)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2024/10/09/disk-images-tools/?share=pinterest)
* [Click to share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2024/10/09/disk-images-tools/?share=threads)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2024/10/09/disk-images-tools/?share=mastodon)
* [Click to share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2024/10/09/disk-images-tools/?share=bluesky)
* Click to email a link to a friend (Opens in new window)
  Email
* [Click to print (Opens in new window)
  Print](https://eclecticlight.co/2024/10/09/disk-images-tools/#print?share=print)

Like Loading...

### *Related*

Posted in [Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/) and tagged [disk image](https://eclecticlight.co/tag/disk-image/), [Disk Utility](https://eclecticlight.co/tag/disk-utility/), [DropDMG](https://eclecticlight.co/tag/dropdmg/), [hdiutil](https://eclecticlight.co/tag/hdiutil/), [sparse bundle](https://eclecticlight.co/tag/sparse-bundle/), [Spundle](https://eclecticlight.co/tag/spundle/). Bookmark the [permalink](https://eclecticlight.co/2024/10/09/disk-images-tools/).

## 6Comments

[Add yours](#reply-title)

1. 1
   ![Christian's avatar](https://1.gravatar.com/avatar/1367ad9df22149f70d7880ec8bdfca638822d920cd754b48009fb411d80716c8?s=96&d=identicon&r=G)

   Christian
   [on October 9, 2024 at 12:23 pm](https://eclecticlight.co/2024/10/09/disk-images-tools/#comment-100778)

   Hi Howard!

   Although Spundle and DropDMG include this feature, I like to use this script offered by Bombich Software when I just need to compact a sparsebundle:

   <https://bombich.com/software/files/tools/Compact_Sparse_Image.app.zip>

   [Like](https://eclecticlight.co/2024/10/09/disk-images-tools/?like_comment=100778&_wpnonce=70eca0d0dd)Liked by 1 person

   * 2
     ![hoakley's avatar](https://2.gravatar.com/avatar/87cc8acbb0b96b7d3b699e69cb1b0ce2bfa22c19f3737ddc73a81783fc2af50c?s=96&d=identicon&r=G)

     [hoakley](https://eclecticlightdotcom.wordpress.com)
     [on October 9, 2024 at 12:37 pm](https://eclecticlight.co/2024/10/09/disk-images-tools/#comment-100783)

     Thank you. I suspect it uses the hdiuti...