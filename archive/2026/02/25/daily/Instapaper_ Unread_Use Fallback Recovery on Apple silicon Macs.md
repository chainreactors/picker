---
title: Use Fallback Recovery on Apple silicon Macs
url: https://eclecticlight.co/2026/02/24/use-fallback-recovery-on-apple-silicon-macs/
source: Instapaper: Unread
date: 2026-02-25
fetch_date: 2026-02-26T04:12:16.907180
---

# Use Fallback Recovery on Apple silicon Macs

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
[February 24, 2026](https://eclecticlight.co/2026/02/24/use-fallback-recovery-on-apple-silicon-macs/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# Use Fallback Recovery on Apple silicon Macs

If you need features in Recovery, but can’t get an Intel Mac to enter that mode, your next step is to start it up with the Command, Option and R keys held for Remote or Internet Recovery. But you can’t do that with an Apple silicon Mac. Instead you should try Fallback Recovery, the subject of this article.

When Apple silicon Macs first came out and ran Big Sur, they only had one Recovery system, installed in a dedicated container named Apple\_APFS\_Recovery. If that didn’t work, the best you could hope for was that Refreshing or Reviving in DFU mode might fix it. That changed in Big Sur 11.6.1 and Monterey. Since then, most Apple silicon Macs have had two Recovery systems:

* **Primary** or **Paired Recovery** is stored in the Recovery volume associated with each macOS boot volume group, and inside the same container.
* **Fallback Recovery** is an older version of the Recovery system that has been moved from a paired Recovery volume and is now stored in the hidden Apple\_APFS\_Recovery container in the internal SSD.

[![](https://eclecticlight.co/wp-content/uploads/2025/06/bootdiskstructuremacosseq.png)](https://eclecticlight.co/wp-content/uploads/2025/06/bootdiskstructuremacosseq.png)

In the diagram above, Paired Recovery is the green volume disk3s3, and Fallback Recovery is disk2s1 in the yellow Apple\_APFS\_Recovery container.

#### Start up in Fallback Recovery

Where Fallback Recovery has been installed by macOS, a Mac may start up automatically in Fallback Recovery if you try to start up in Paired Recovery using a long press on the Power button, but that fails. You can also elect to start up in Fallback Recovery by pressing the Power button once, immediately pressing it again and holding that until the display informs you that options are loading. The cadence of the presses is like the Morse ‘di-da’, with a pause of no more than a second between them.

#### What’s missing from Fallback

From its outset, one standard feature of Recovery doesn’t work in Fallback: Startup Security Utility. You can’t therefore use it to change your Mac’s security settings or disable loading of third-party kernel extensions. For those you must use Paired Recovery. Apple also warns that Device Recovery Assistant may not be available in Fallback Recovery either.

Most importantly, though, Fallback Recovery can only offer the features that come with Recovery in that version of macOS. For example, at present it’s likely that Macs running Tahoe will have Fallback Recovery systems from Sequoia. Where they do, the new Repair Assistant isn’t available in Fallback Recovery, as that will still run Apple Diagnostics from Sequoia.

#### How it works

Since macOS installers and updaters for Big Sur 11.6.1 and Monterey, when the Paired Recovery system is updated, the installer may opt to copy the contents of the old Paired Recovery volume to the Fallback Recovery volume. This is presumably pre-determined in each updater and installer, and intended to ensure the fallback is as reliable as possible, even though its features are a little out of date. The user is given no option.

This may mean that a brand new Apple silicon Mac doesn’t come with Fallback Recovery, and that isn’t installed until the Mac has undergone its first macOS update.

Apple provides a bare minimum of documentation. Indeed, it’s most detailed account in its Platform Security Guide hasn’t been updated since May 2022, and [contains an error](https://support.apple.com/guide/security/sec10869885b/web) in which it claims that Fallback Recovery starts the Mac up using Paired Recovery, exactly the same as for Paired Recovery.

#### Check Fallback Recovery

If you have never started your Mac up in Fallback Recovery, it’s a good learning exercise to do so when you have a few moments. You can then tackle the question of how to tell whether the Recovery mode your Mac is in is Paired or Fallback. There are three simple signs to look for:

* If Fallback is an older version of macOS, then the Reinstall macOS feature will offer that older version.
* Startup Security Utility will warn you that you can’t make any changes if you open it in Fallback mode.
* Opening Terminal and typing the `sw_vers` command will tell you the version of macOS running.

You can also check whether Fallback Recovery is available, and its version, in my free utility [Mints](https://eclecticlight.co/mints-a-multifunction-utility/). In its main window click on the **Software Update** button to view a list of software update settings. Within those:

* `sfrProductVersion` is the version of Paired Recovery available,
* `recoveryOSProductVersion` is the version of Fallback Recovery available.

In both my active Apple silicon Macs running macOS 26.3 Tahoe, Fallback Recovery is currently macOS 15.6 Sequoia, although both have been through 26.0 and every release update since. This could of course indicate that Tahoe’s updates haven’t yet installed a new version of Recovery since that supplied with 26.0.

#### Recovery isn’t available

If neither Paired nor Fallback Recovery are available, you can try reinstalling macOS in normal user mode. As you have no option to try that in Recovery, if that fails you’ll have to put that Mac into DFU mode, connect it to another recent Mac using a USB-C cable, then [Revive its firmware](https://support.apple.com/108900). Reviving firmware isn’t destructive, and should leave both macOS System and your Data volumes intact. If that too doesn’t work, the only remaining option is to perform a full Restore, which will wipe absolutely everything on the internal SSD.

### Share this:

* [Share on X (Opens in new window)
  X](https://eclecticlight.co/2026/02/24/use-fallback-recovery-on-apple-silicon-macs/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2026/02/24/use-fallback-recovery-on-apple-silicon-macs/?share=facebook)
* [Share on Reddit (Opens in new window)
  Reddit](https://eclecticlight.co/2026/02/24/use-fallback-recovery-on-apple-silicon-macs/?share=reddit)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://eclecticlight.co/2026/02/24/use-fallback-recovery-on-apple-silicon-macs/?share=pinterest)
* [Share on Threads (Opens in new window)
  Threads](https://eclecticlight.co/2026/02/24/use-fallback-recovery-on-apple-silicon-macs/?share=threads)
* [Share on Mastodon (Opens in new window)
  Mastodon](https://eclecticlight.co/2026/02/24/use-fallback-recovery-on-apple-silicon-macs/?share=mastodon)
* [Share on Bluesky (Opens in new window)
  Bluesky](https://eclecticlight.co/2026/02/24/use-fallback-recovery-on-apple-silicon-macs/?share=bluesky)
* Email a link to a friend (Opens in new window)
  Email
* [Print (Opens in new window)
  Print](https://eclecticlight.co/2026/02/24/use-fallback-recovery-on-apple-silicon-macs/#print?share=print)

Like Loading...

### *Related*

Posted in [Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/) and tagge...