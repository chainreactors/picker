---
title: Kali Linux 2022.4 Release (Azure, Social & Kali NetHunter Pro)
url: https://www.kali.org/blog/kali-linux-2022-4-release/
source: Kali Linux
date: 2022-12-07
fetch_date: 2025-10-04T00:43:04.326985
---

# Kali Linux 2022.4 Release (Azure, Social & Kali NetHunter Pro)

* [Join Free CTF](https://www.offsec.com/events/the-gauntlet/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* [Get Kali](https://www.kali.org/get-kali/)
* [Blog](https://www.kali.org/blog/)
* Documentation

  [Documentation Pages](https://www.kali.org/docs/)
  [Tools Documentation](https://www.kali.org/tools/)
  [Frequently Asked Questions](https://www.kali.org/faq/)
  [Known Issues](https://bugs.kali.org/search.php?project_id=1&category_id[]=General%20Bug&category_id[]=Kali%20Package%20Bug&category_id[]=Kali%20Package%20Improvement&status[]=30&status[]=40&status[]=50&sticky=on&sort=id%2Clast_updated&dir=DESC%2CDESC&hide_status=-2&match_type=0)
* Community

  [Community Support](https://www.kali.org/community/)
  [Forums](https://forums.kali.org/)
  [Discord](https://discord.kali.org/)
  [Join Newsletter](https://www.kali.org/newsletter/)
  [Mirror Location](https://http.kali.org/README?mirrorlist)
  [Get Involved](https://www.kali.org/docs/community/contribute/)
* [Courses](https://www.offsec.com/kali-training/courses/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* Developers

  [Git Repositories](https://gitlab.com/kalilinux)
  [Packages](https://pkg.kali.org/)
  [Auto Package Test](https://autopkgtest.kali.org/)
  [Bug Tracker](https://bugs.kali.org/)
  [Kali NetHunter Stats](https://nethunter.kali.org/)
* About

  [Kali Linux Overview](https://www.kali.org/features/)
  [Press Pack](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip)
  [Wallpapers](https://www.kali.org/wallpapers/)
  [Kali Swag Store](https://offsec.usa.dowlis.com/kali/view-all.html)
  [Meet The Kali Team](https://www.kali.org/about-us/)
  [Partnerships](https://www.kali.org/partnerships/)
  [Contact Us](https://www.kali.org/contact/)

LIGHT
[ ] DARK

![](https://www.kali.org/blog/kali-linux-2022-4-release/images/banner-2022.4-release.jpg)
Tuesday, 06 December 2022

# Kali Linux 2022.4 Release (Azure, Social & Kali NetHunter Pro)

Table of Contents

* [Microsoft Azure](#microsoft-azure)
* [More Platforms](#more-platforms)
* [Social Networks](#social-networks)
  + [Press Pack](#press-pack)
  + [Media Enquiries](#media-enquiries)
* [Kali NetHunter Pro Release](#kali-nethunter-pro-release)
* [Kali NetHunter Update](#kali-nethunter-update)
* [Desktop Updates](#desktop-updates)
  + [GNOME](#gnome)
  + [KDE Plasma](#kde-plasma)
* [Miscellaneous](#miscellaneous)
* [New Tools in Kali](#new-tools-in-kali)
* [Kali ARM Updates](#kali-arm-updates)
* [Kali Documentation Updates](#kali-documentation-updates)
* [Recent Kali Blog Posts](#recent-kali-blog-posts)
* [Community Shout-Outs](#community-shout-outs)
* [Discord Chat](#discord-chat)
* [Get Kali Linux 2022.4](#get-kali-linux-20224)

Before the year is over, we thought it was best to get the final 2022 release out. Today we are publishing **Kali Linux 2022.4**. This is ready for immediate [download](https://www.kali.org/get-kali/) or [updating](https://www.kali.org/docs/general-use/updating-kali/) existing installations.

A summary of the [changelog](https://bugs.kali.org/changelog_page.php) since [August’s 2022.3 release](https://www.kali.org/blog/kali-linux-2022-3-release/):

* **[Microsoft Azure](#microsoft-azure)** - We are back on the Microsoft Azure store
* **[More Platforms](#more-platforms)** - Generic Cloud, QEMU VM image & Vagrant libvirt
* **[Social Networks](#social-networks)** - New homes, keeping in touch & press packs
* **[Kali NetHunter Pro](#kali-nethunter-pro-release)** - Announcing the first release of a “true” Kali Linux on the mobile phone (PinePhone / Pro)
* **[Kali NetHunter](#kali-nethunter-update)** - Internal Bluetooth support, kernel porting video, firmware updates & other improvements
* **[Desktop Updates](#desktop-updates)** - GNOME 43 & KDE 5.26
* **[New Tools](#new-tools-in-kali)** - As always, various new packages added

---

## Microsoft Azure

Its been a long time coming, but we are very happy to announce that Kali has been added to [Microsoft Azure](https://azuremarketplace.microsoft.com/en/marketplace/apps/kali-linux.kali) (again - and this time to stay)! [Following in the foot steps](https://www.kali.org/blog/kali-linux-2020-4-release/) of our [Amazon AWS](https://aws.amazon.com/marketplace/pp/B08LL91KKB) image, we are using the same [kali-cloud build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-cloud) now to automate publishing to Microsoft Azure store.

Out of the box, *currently*, there is no graphical user interface, or any tools pre-installed. Should you want the default toolset (`kali-linux-default`) or any other combination of [metapackages](https://www.kali.org/docs/general-use/metapackages/), it should be like any other Kali platform. For installing a desktop environment, we have the following kali-docs page: [Setting up RDP with Xfce](https://www.kali.org/docs/general-use/xfce-with-rdp/)

We hope in 2023 we can revisit this again and are looking at doing ARM64 architecture, as well as different variations of images, allowing you to choose from a mixture of headless bare-bones install, the traditional environment, and a mixture of everything in-between.

## More Platforms

We are now including a **QEMU** image with our [pre-generated images](https://www.kali.org/get-kali/). We hope this makes it easier for the people who use self-hosted Proxmox Virtual Environments (VE), [virt-manager](https://pkg.kali.org/pkg/virt-manager), or [libvirt](https://pkg.kali.org/pkg/libvirt)!

On that subject, [elrey (alex)](https://gitlab.com/elreydetoda) from the community has added libvirt support to our [kali-vagrant build-script](https://gitlab.com/kalilinux/build-scripts/kali-vagrant).

In Kali 2022.3, we have produced a **Generic Cloud** image. The idea of this image is that it should work in “most” cloud providers This is coming from our [kali-cloud build-scripts](https://gitlab.com/kalilinux/build-scripts/kali-cloud).
So if you are self-hosting OpenStack, this is a great way of getting Kali loaded up!

## Social Networks

We have expanded the social networks which we post on, as well as refreshing the current ones. As a recap:

* Facebook: [facebook.com/KaliLinux](https://www.facebook.com/KaliLinux/)
* **NEW** Instagram: [instagram.com/KaliLinux](https://www.instagram.com/kalilinux/)
* **NEW** Mastodon: [[email protected]](https://infosec.exchange/%40kalilinux)
* Twitter: [twitter.com/KaliLinux](https://twitter.com/kalilinux)

As a reminder, we don’t use social networks for technical support - you can receive community support via [discord](https://discord.kali.org/) or our [forums](https://forums.kali.org/) and bug reports should go to the [bug tracker](https://bugs.kali.org/)!
Instead, we automatically post [blog posts](https://www.kali.org/blog/) thus *these accounts are mostly unmonitored!*

If social networks are not your thing, you can also keep in touch via:

* Email: [Newsletter](https://www.kali.org/newsletter/)
* RSS: [kali.org/rss.xml](https://www.kali.org/rss.xml)

---

### Press Pack

We have also taken the time to create a **Press Pack** *(aka Press kit)* for Kali. Here you can find all our product media resources to use, including:

* Logomark (our dragon logos)
* Logomark and Wordmark (our iconic avatars - dragon logo with text)
* Wordmark (text as an image)
* Various different image formats (png, svg, jpg)
* Official colours

*Please bear in mind that they are under [copyright & trademark](https://www.kali.org/docs/policy/trademark/) when using them!*

You can [download them all](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip), or you can [view them online](https://gitlab.com/kalilinux/documentation/press-pack/-/tree/main/).

[![Kali Linux](images/kali-logo-dragon-blue-transparent.png)](https://gitlab.com/kalilinux/documentation/press-pack/-/tree/main/Kali/Logomark_and_Wordmark)
[![](images/kali-nethunterpro-logo-dragon-orange-transparent.png)](https://gitlab.com/kalilinux/documentation/pre...