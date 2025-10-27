---
title: From party trick to file protection sparse files have their uses
url: https://eclecticlight.co/2023/06/28/from-party-trick-to-file-protection-sparse-files-have-their-uses/
source: Instapaper: Unread
date: 2023-06-29
fetch_date: 2025-10-04T11:50:52.504793
---

# From party trick to file protection sparse files have their uses

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
[June 28, 2023](https://eclecticlight.co/2023/06/28/from-party-trick-to-file-protection-sparse-files-have-their-uses/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **From party trick to file protection:** sparse files have their uses

APFS may not seem the right tool for performing party tricks on your Mac, but the combination of clone and sparse files can make for some nerdy fun. This article looks at how those tricks can turn into something more useful, and secure sensitive data more efficiently.

#### Sparse file trick

For the basic trick, you’ll need my little app [Sparsity](https://eclecticlight.co/taccy-signet-precize-alifix-utiutility-alisma/), which creates (otherwise useless) sparse files, and a small partition/container of around 100 GB with a single APFS volume inside it. In that volume, make yourself a 10 GB sparse file, and duplicate it many times until it appears to overflow the size of the container. This works because the sparse files don’t occupy the space expected by their 10 GB size, and their clones occupy even less space on disk.

#### Disk image trick

Delete those, and try something a little more sophisticated. This time, create an empty 10 GB UDIF Read/Write disk image in that container using [DropDMG](https://c-command.com/dropdmg/) or Disk Utility, then unmount that disk image. At this stage it still takes 10 GB of disk space. Double-click it to mount it, confirm that it’s empty, and unmount it again. Use the Finder’s Get Info to confirm that it now takes just a few MB of disk space, although its size remains nominally 10 GB. That’s because APFS has changed it into a sparse file, so all its empty space has vanished. You can now duplicate that disk image many times without losing much free space in the container, just as you did with the previous sparse file.

#### Encrypted disk images

![multidmg1](https://eclecticlight.co/wp-content/uploads/2023/06/multidmg1.jpg?w=940)

Now let’s turn that trick into something useful, something we were promised over six years ago, when studying Apple’s [initial documentation](https://eclecticlight.co/2017/01/27/apple-file-system-what-it-means-what-it-brings/) for APFS. I wrote then that APFS “has encryption designed into it from the outset. It therefore allows you to choose from several options for each volume within an APFS container. These range from no encryption at all, to multi-key encryption with different files/folders protected by different keys, even a separate key for metadata.”

Unless I have somehow missed it, we still seem to be waiting for this multi-key encryption with different files/folders protected by different keys. In the meantime, I here suggest an alternative that’s just as flexible and efficient, using disk images.

Empty that APFS volume again, and this time create an encrypted 50 GB UDIF Read/Write disk image in it, using a password you can remember, or later add to your keychain if you prefer. Perform the same unmount-mount-unmount sequence to shrink it down to a small sparse file. Then create another two of those, each with a different memorable password. You’ll now have three encrypted disk images taking next to no space in that one volume.

![multidmg2](https://eclecticlight.co/wp-content/uploads/2023/06/multidmg2.jpg?w=940)

In the absence of the promised “multi-key encryption with different files/folders protected by different keys” in APFS, the only obvious option is to add an APFS encrypted volume for each collection of files you want encrypted separately. That’s clumsy in two respects:

* Default behaviour at startup, or when that disk is connected, is to mount all volumes, thus prompting for each password whether or not you want that encrypted volume mounted.
* Although encrypted volumes can be backed up by Time Machine, their backups won’t then be protected by separate passwords, only the password for the whole encrypted backup.

Your three encrypted disk images now behave almost like encrypted APFS volumes, except that:

* you only need mount them when you want to access that particular set of encrypted files;
* each can grow to the maximum size set for that disk image, provided that their total size remains within that of the container;
* when each is mounted, it is trimmed, and free space eliminated from the disk space required to store the files in that image;
* each can be backed up by Time Machine to unencrypted backup storage, while retaining their individual password protection;
* each can be backed up using third-party utilities to unencrypted APFS or networked storage, while retaining their individual password protection.

Note that this only applies to disk images using HFS+ or APFS format internally, as other file systems won’t be trimmed on mounting.

Of course, you could also do this using encrypted sparse bundles if you prefer. To maintain their size efficiency, though, you need to periodically compact them manually, as APFS neither trims them during mounting, nor does it save them in sparse format. Now that plain disk images are stored as sparse files, as of macOS Monterey, most of the advantages of sparse bundles have been lost. Finally, it’s worth noting that at present you can’t change the password on an encrypted sparse bundle, but you can on an encrypted disk image, although Apple will hopefully get round to fixing that bug in the near future.

#### Summary

* To protect collections of files using encryption, your first choice now should be an APFS or HFS+ format encrypted read/write disk image.
* As they’re stored as sparse files, set their size to the maximum you’re likely to want, as they will grow and shrink as needed.
* To compact a read/write disk image, mount and unmount it, so that its free space will be trimmed.
* You can safely back up an encrypted disk image to unencrypted storage, as it will retain its individual password.
* Some party tricks can be useful after all.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://eclecticlight.co/2023/06/28/from-party-trick-to-file-protection-sparse-files-have-their-uses/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2023/06/28/from-party-trick-to-file-protection-sparse-files-have-their-uses/?share=facebook)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2023/06/28/from-party-trick-to-file-protection-sparse-files-have-their-uses/?share=reddit)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2023/06/28/from-party-trick-to-file-protection-sparse-files-have-their-uses/?share=pinterest)
* [Click to share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2023/06/28/from-party-trick-to-file-protection-sparse-files-have-their-uses/?share=threads)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2023/06/28/from-party-trick-to-file-protection-sparse-files-have-their-uses/?share=mastodon)
* [Click to share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2023/06/28/from-party-trick-to-file-protection-sparse-files-have-their-uses/?share=bluesky)
* Click to email a li...