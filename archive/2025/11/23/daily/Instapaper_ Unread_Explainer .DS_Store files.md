---
title: Explainer .DS_Store files
url: https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/
source: Instapaper: Unread
date: 2025-11-23
fetch_date: 2025-11-24T03:22:14.755467
---

# Explainer .DS_Store files

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
[November 15, 2025](https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **Explainer:** .DS\_Store files

Here’s a bonus riddle for this weekend: what’s so invisible you can never see it in the Finder, is in many of the folders in your Home folder, and can break your backups? The answer is a .DS\_Store file, officially a *Desktop Services Store.* Although they might appear more ancient, they originated in Mac OS X when its Finder was [being rewritten from scratch](https://www.arno.org/on-the-origins-of-ds-store) in 1999.

It had been intended that Desktop Services would eventually gain a public API, but somewhere along the line Apple decided to keep it private, and their format and function have never been officially documented. Its name starts with a dot/stop/period to make it invisible in the Finder, and since macOS Sierra it has been made invisible even when the Finder reveals other invisible files. Currently the best way to see it is in Terminal, where the `-a` option to `ls` should include .DS\_Store files.

They can be confused with another annoying but more useful hidden file: shadow files whose names start with `._` that are used to carry extended attribute data as part of the AppleDouble file format used on some FAT file systems. They too are invisible in the Finder even when hidden files are supposed to be displayed, but are associated with individual files rather than folders.

#### Function

The Finder will normally create a .DS\_Store file in a folder that you have write access to, when some change is made to it in the Finder, such as creating or copying a file into that folder.

.DS\_Store files contain a folder’s custom attributes, data like icon positions, and in more recent versions of macOS custom settings for the display of file metadata.

Among the most important of their contents for some users are Finder or Spotlight Comments, which are normally displayed in the Comments section of the Get Info dialog for a file. Those comments may also be duplicated in the com.apple.metadata:kMDItemFinderComment extended attribute (xattr) of that file, but that’s a secondary copy that can fall out of sync with what’s stored in the .DS\_Store file, and the Finder ignores the xattr anyway. The reliance of Finder Comments on invisible .DS\_Store files can lead to their unreliability compared with other forms of metadata.

#### Problems

You’re more likely to come across .DS\_Store files when they make a nuisance of themselves by tripping something up. Send a folder from your Mac to a Windows or Linux system, for example, and it’s likely to confuse the recipient with that mysterious extra file that you can’t see at all. Send a folder to another Mac by AirDrop, and any .DS\_Store file inside it will also accompany its visible contents. That in turn can cause problems with some backup utilities if it results in an older .DS\_Store file being found in a folder that has already been backed up with a newer one.

Recent versions of macOS should no longer write .DS\_Store files to computers connected to them over a network. If you want to stop them from being exposed in network volumes of older systems, use the command
`defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true`
to disable that. One place .DS\_Store files can prove particularly troublesome is in Git repositories. Mikey @0xmachos has provided [a simple solution](https://0xmachos.com/2020-01-22-Eradicating-.DS_Store-From-Git/) for eradicating them.

At one stage Apple even recommended that they should be explicitly excluded from servers used for network backups or other storage. They can trip up revision control systems, baffle those who open archives created on a Mac, stop folder copying, and confound folder comparison. The simple solution to these, as with so many other problems with .DS\_Stores, is to open the folder containing that hidden file, move some of its contents about to force it to be refreshed, and move on.

In the past, .DS\_Store files have been suspected of leaking data, and were involved in at least one security vulnerability. Thankfully they now seem as puzzling and opaque to the developers of malware as they are to other users, but I’m sure that one day, someone else will try to do bad things with them again.

#### Removal

You can recursively delete .DS\_Store files from a hierarchy using the command
`find . -name .DS_Store -delete`
and Ross Tulloch’s [BlueHarvest](https://www.zeroonetwenty.com/blueharvest/) can automatically remove them.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/?share=facebook)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/?share=reddit)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/?share=pinterest)
* [Click to share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/?share=threads)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/?share=mastodon)
* [Click to share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/?share=bluesky)
* Click to email a link to a friend (Opens in new window)
  Email
* [Click to print (Opens in new window)
  Print](https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/#print?share=print)

Like Loading...

### *Related*

Posted in [Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/) and tagged [Finder](https://eclecticlight.co/tag/finder/), [metadata](https://eclecticlight.co/tag/metadata/), [comment](https://eclecticlight.co/tag/comment/), [.DS\_Store](https://eclecticlight.co/tag/ds_store/), [BlueHarvest](https://eclecticlight.co/tag/blueharvest/). Bookmark the [permalink](https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/).

## 6Comments

[Add yours](#reply-title)

1. 1
   ![Enzo Vincenzo's avatar](https://0.gravatar.com/avatar/0acf8c79121e5b8bca32292e422ca24ce2ba41449caface89ac636d113cd1d39?s=96&d=identicon&r=G)

   Enzo Vincenzo
   [on November 15, 2025 at 8:28 am](https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/#comment-109668)

   [Reply](https://eclecticlight.co/2025/11/15/explainer-ds_store-files-2/?replytocom=109668#respond)

   Thanks Howard! Great article.
   I would like to take this opportunity to suggest that with exFAT discs and various USB sticks, to delete all shadow files, I always use the Terminal command
   dot\_clean -v
   After the command and a space, I enter the path of the disc or stick, or better yet, I drag the icon directly into the Terminal window after the above command and space.
   The -v flag is very useful because it allows you to see what is happening and the fina...