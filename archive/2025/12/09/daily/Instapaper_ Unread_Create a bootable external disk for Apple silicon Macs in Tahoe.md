---
title: Create a bootable external disk for Apple silicon Macs in Tahoe
url: https://eclecticlight.co/2025/12/09/create-a-bootable-external-disk-for-apple-silicon-macs-in-tahoe/
source: Instapaper: Unread
date: 2025-12-09
fetch_date: 2025-12-10T03:23:03.444826
---

# Create a bootable external disk for Apple silicon Macs in Tahoe

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
[December 9, 2025](https://eclecticlight.co/2025/12/09/create-a-bootable-external-disk-for-apple-silicon-macs-in-tahoe/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# Create a bootable external disk for Apple silicon Macs in Tahoe

![](https://eclecticlight.co/wp-content/uploads/2025/12/extboot1.jpg?w=1024)

The Achilles heel of T2 Macs is booting from external storage. Although it’s simple to create a bootable external disk for a T2 Mac, to boot from it you have to allow the Mac to boot from *any* external disk, removing much of its boot security. Apple silicon Macs were designed to boot almost as securely from external disks as they do from the internal SSD, and that makes setting up a bootable external disk more complicated. This article explains how you can do that for macOS 26 Tahoe.

In this respect, Apple silicon Macs have two central principles:

* They always start the boot process from their internal SSD. If that’s not functioning correctly, then they can’t boot at all.
* They will only transfer the boot process to an external system when the user has access to a private key making them an Owner of that system, through the Mac’s LocalPolicy system. That’s the part that can cause problems.

#### Planning

There are alternatives to booting from external storage. If there’s sufficient space, you can install multiple versions of macOS on the internal SSD, or you can run macOS as a guest operating system in a virtual machine (VM). VMs are limited in some important respects, though, as they can’t run most apps from the App Store or use AI, although they can now access iCloud and iCloud Drive.

Like any other Mac, Apple silicon models can only boot from versions of macOS they’re compatible with. You can check which your Mac can run using [Mactracker](http://mactracker.ca). A VM is the only solution for running older and incompatible versions of macOS, and it gets messy installing versions that are compatible but older than the currently installed major version of macOS. This is because its installer may be blocked by the more recent macOS, for which you’ll need to create a bootable installer disk and run the installation from that. Apple describes how to do that [in this support article](https://support.apple.com/101578). For the remainder of this article, I assume that you’re installing a second or subsequent copy of the current version of macOS to an external disk.

#### Connect and prepare the external disk

First catch your disk, and connect it to one of the [non-DFU ports](https://support.apple.com/120694) on your Mac. For example, on my Mac mini M4, that’s either the left or right Thunderbolt port, as the middle one is its DFU port. On all other Apple silicon Mac minis, that’s either the centre or right port as you look from the rear, as their DFU port is the one on the left. If you try to install macOS to a drive connected to an Apple silicon Mac’s DFU port, then it’s doomed to fail, and that’s the most common cause of failure. More information on the DFU port [is here](https://eclecticlight.co/2025/01/14/thunderbolt-ports-arent-all-the-same/).

Reformat that disk as you want to use it, with at least one APFS container containing a single APFS volume in regular APFS format, not encrypted.

#### Download and run the installer

Next catch your installer. Oddly, Apple seems to have stopped providing the current release of macOS through the App Store, so the simplest way to download it in the GUI is from the links [provided by Mr. Macintosh](https://mrmacintosh.com), and there are many alternatives. You want a regular installer, not an IPSW image file that you might use to create virtual machines.

Run the installer app from your main Applications folder.

[![](https://eclecticlight.co/wp-content/uploads/2025/12/extboot1.jpg)](https://eclecticlight.co/wp-content/uploads/2025/12/extboot1.jpg)

When it asks you whether you want to install macOS on your current system, click on **Show All Disks…**

[![](https://eclecticlight.co/wp-content/uploads/2025/12/extboot2.jpg)](https://eclecticlight.co/wp-content/uploads/2025/12/extboot2.jpg)

Select your external disk from the list and click **Continue**. If your disk isn’t recognised or listed there, reformat it and start again.

##### Ownership

This is the important part of the installation; if it fails, the external disk won’t be bootable.

For the macOS system on your external disk to be bootable, it needs a LocalPolicy created for it on your Mac’s internal SSD. To ensure that only fully authorised users can configure and change LocalPolicy, those Image4 files are signed, and an Owner Identity Certificate (OIC) is attached to them. Creating and maintaining LocalPolicies requires a user to have access to the private Owner Identity Key (OIK) in the Secure Enclave, making that user an Owner.

Any user with access to the Volume Encryption Key for the internal storage also has access to the OIK, and has Ownership. By default, that includes all users added after FileVault encryption is enabled on a Data volume, for example. To be able to boot from that second OS, it requires a LocalPolicy with an OIC attached, and Ownership has to be handed off to an Install User created when that OS is installed.

Handing off Ownership to the Install User is more of a problem, as users are only created when the installation is complete. To accommodate that, macOS offers to copy a user from the current boot system as the Install User, and the primary admin user, on the second OS. Provided that you agree to that, the Install User created is actually a Key Encryption Key (KEK) for your password and hardware keys, which is then used to encrypt the OIK as it’s handed over to the new copy of macOS on the external disk. Thus, the installer requests that user’s password to gain access to the OIK for the new macOS in the Secure Enclave.

Following these steps should ensure that works correctly.

[![](https://eclecticlight.co/wp-content/uploads/2025/12/extboot3.jpg)](https://eclecticlight.co/wp-content/uploads/2025/12/extboot3.jpg)

When prompted to select the user to be owner of the new boot volume group, pick the current admin user, and tick to copy their account settings.

[![](https://eclecticlight.co/wp-content/uploads/2025/12/extboot4.jpg)](https://eclecticlight.co/wp-content/uploads/2025/12/extboot4.jpg)

You’ll then be prompted to enter that user’s password to authenticate as the owner.

#### Completing installation

Installation follows, and is (as ever) highly non-linear, and may even appear to stall. Persevere, and it will then close apps and restart to complete.

[![](https://eclecticlight.co/wp-content/uploads/2025/12/extboot5.jpg)](https://eclecticlight.co/wp-content/uploads/2025/12/extboot5.jpg)

When you’re eventually prompted to **Create a Computer Account**, it’s simplest to create a local admin account for the owner. The new copy of macOS will then take you through personalising your new system, and, if you’ve added support for your Apple Account, it will do the 2FA dance for iCloud and Apple Account, and so on.

Once configured, you can share that external disk between Macs, but each time you boot from it on a different Mac,...