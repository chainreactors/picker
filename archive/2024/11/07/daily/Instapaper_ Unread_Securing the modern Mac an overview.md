---
title: Securing the modern Mac an overview
url: https://eclecticlight.co/2024/10/30/securing-the-modern-mac-an-overview/
source: Instapaper: Unread
date: 2024-11-07
fetch_date: 2025-10-06T19:23:05.578288
---

# Securing the modern Mac an overview

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
[October 30, 2024](https://eclecticlight.co/2024/10/30/securing-the-modern-mac-an-overview/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **Securing the modern Mac:** an overview

Modern Macs and macOS feature multiple layers of protection, most of which I have recently described. This article tries to assemble them into an overview to see how they all fit together, and protect your Mac from startup to shutdown. There are also many additional options in macOS and third-party products that can augment security, but I’ll here concentrate on making best use of those that come with a modern Mac and macOS. My recommendations are for the ‘standard’ user, as a starting point. If your needs differ, then you may of course choose to be different, but should always do so in the full knowledge of what you are doing and what its penalties are.

#### Startup

Whether your Mac has a T2 or Apple silicon chip, it’s designed to boot securely, which means that every stage of the boot process, from its Boot ROM to running the kernel and its extensions, is verified as being as Apple intends. To ensure that, your Mac should run at **Full Security**. For a T2 model, that means disabling its ability to boot from external disks; for an Apple silicon Mac, that means no third-party kernel extensions. If you need to run your Mac at reduced security, that should be an informed decision when there’s no good alternative.

A vital part of the Secure Boot process is the firmware loaded by the Boot ROM. That needs to be kept up to date by updating to the latest minor release of the major version of macOS. That doesn’t prevent your Mac from staying with an older supported version of macOS, as Apple supplies the same firmware updates for all three supported versions of macOS.

The System volume should be signed and sealed, as the SSV created by a macOS installer or updater. System Integrity Protection (SIP) should also be fully enabled, as without it many macOS security features work differently or not at all. Some need to disable specific SIP features, but again that should only be set when you’re fully aware of their effects and consequences, and should be the minimum needed for the purpose.

#### User Data

Having got the system up and running, the boot process moves to what is in mutable storage on the Mac’s Data volume. In the internal SSD of a modern Mac, that’s always encrypted, thanks to the Secure Enclave. Although that might appear sufficient, you should always turn FileVault on if your Mac starts up from its internal SSD. That ensures the encryption is protected by your password: an intruder then has to know your password before they can unlock the contents of its Data volume. They have limited attempts to guess that password before the Mac locks them out from making any further attempts. As FileVault comes free from any performance penalty, there’s no good reason for not using it.

Good security is even more important for Data volumes on external boot disks, where FileVault is just as important, but needs additional physical measures to ensure the external disk isn’t mislaid or stolen. That’s a more complex issue, for which the simplest solution is to start your Mac up from its internal SSD with the benefit from FileVault there.

#### Run Apps

With the user logged in successfully, and the Data volume fully accessible, the next stage to consider is running apps and other software. For this there’s another series of security layers.

When an app is launched or other code run, Gatekeeper will first check it, and in many circumstances run a check for malware using XProtect. Those shouldn’t be disabled, or macOS will still make those checks, but will simply ignore the results. XProtect looks for evidence that the code about to be run matches that of known malware. Although on its own this won’t detect unknown malware, it’s an effective screen against what’s most common. You also need to keep your Mac up to date with the latest security data updates, as those can change every week or two as new malware is identified and included.

Currently, no well-known malware has been notarized by Apple, and most isn’t even signed using a trusted developer certificate. Most therefore attempt to trick you into bypassing checks made by macOS. In Sonoma and earlier, the most common is to show you how to use the Finder’s **Open** command to bypass the requirement for notarization. As that has changed in Sequoia, those who develop malware have had to adapt, and some now try to trick you into dropping a malicious script into Terminal. Expect these to become more sophisticated and persuasive as more upgrade to Sequoia.

There are simple rules you can apply to avoid getting caught by these. The first time you run any new app supplied outside macOS or the App Store, drag the app to your Applications folder and double-click it in the Finder to open it. If it can’t be launched that way, don’t be tempted to use the Finder’s **Open** bypass, or (in Sequoia) to enable the app in Privacy & Security settings. Instead, ask its developer why it isn’t correctly notarized. Never use an unconventional method to launch an app: that’s a giveaway that it’s malicious and you shouldn’t go anywhere near it.

macOS now checks the hashes (CDHashes) of apps and code it doesn’t already recognise, for notarization and known malware. Those checks are run over a connection to iCloud that doesn’t need the user to be signed in. Don’t intentionally or inadvertently block those connections, for instance using a software firewall, as they’re in your interest.

#### Private Data

Traditional Unix permissions weren’t intended to protect your privacy. Now so many of us keep important or valuable secrets in our Home folders, privacy protection is essential. While you might trust an app to check through some files, you may not expect or want that app to be looking up details of your bank cards and accounts.

Privacy protection is centred on a system known as TCC (Transparency, Consent and Control), and its labyrinthine **Privacy & Security** settings. One of the most tedious but important routine tasks is to check through these every so often to ensure that nothing is getting access to what it shouldn’t.

No matter how conscientious we might be, there’s always the request for access that you don’t have time to read properly, or items that end up getting peculiar consents, like a text editor that has access to your Photos library or your Mac’s camera. Take the time to check through each category and disable those you don’t think are in your best interests. If you get through a lot of new apps, you might need to do this every week or two, but it needn’t be as frequent in normal use, and shouldn’t become an obsession.

There’s some dispute over whether it’s better to leave an app turned off in a category that you control, like Full Disk Access, or to remove it. I tend to disable rather than remove, with the intention of removal later, but seldom get round to that.

#### Downloaded Apps

While macOS continues checking apps in Gatekeeper and XProtect, there are a couple of other important protections you need to know about. Since macOS Catalina, every...