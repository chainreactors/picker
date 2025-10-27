---
title: Kali Linux On The New Modern WSL
url: https://www.kali.org/blog/kali-linux-modern-wsl/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-29
fetch_date: 2025-10-06T20:10:26.492961
---

# Kali Linux On The New Modern WSL

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

![](https://www.kali.org/blog/kali-linux-modern-wsl/images/kali-linux-modern-wsl.jpg)
Tuesday, 28 January 2025

# Kali Linux On The New Modern WSL

Table of Contents

* [Kali and WSL’s history](#kali-and-wsls-history)
* [The new WSL modern distribution architecture](#the-new-wsl-modern-distribution-architecture)
* [Kali on the new distribution architecture](#kali-on-the-new-distribution-architecture)
* [How you can test this new WSL](#how-you-can-test-this-new-wsl)

Late last year we had the pleasure of being reached out to by Microsoft in regards to participating in the launch of the new, [modern, WSL distribution architecture](https://devblogs.microsoft.com/commandline/whats-new-in-the-windows-subsystem-for-linux-in-november-2024/#new-tar-based-wsl-distro-architecture). In summary, this new architecture allows for easier distribution and installation of WSL distros. For the full explanation of how this works, please view Microsoft’s [blog post](https://devblogs.microsoft.com/commandline/whats-new-in-the-windows-subsystem-for-linux-in-november-2024/#new-tar-based-wsl-distro-architecture) and their [documentation](https://learn.microsoft.com/en-gb/windows/wsl/build-custom-distro).

With the assistance of Microsoft’s WSL team, we are proud to say that we were the first Linux distro to be accepted onto this new modern distribution list. In this blog post we will cover the journey and share how you can try out this new architecture, but if you are just looking for the hands on portion then please see [here](#how-you-can-test-this-new-wsl).

## Kali and WSL’s history

Kali has had a long history of active support for WSL and the team running it. When we first got the email about the new distribution architecture and how it would be used, we were very interested in it.

For those who aren’t familiar with how WSL works, previously it took a few steps for us to get a new version onto the Microsoft store:

* First we would have to build the root filesystem (rootfs) and compress it into a tarball. This is done through our [build script](https://gitlab.com/kalilinux/build-scripts/kali-wsl-rootfs) and can be done on most systems and OSs.
* After we have our compressed rootfs we would need to move it to a Windows system that has Visual Studio installed and configured for our needs. For a bit more information on this configuration, please see our [readme in our GitLab](https://gitlab.com/kalilinux/build-scripts/kali-wsl-app).
* Once we have Visual Studio set up and configured correctly, we would have to import the compressed rootfs and begin building the app. This is as easy as clicking a few buttons after you have it initially configured and know the output is good.
* From here we then upload the build app bundle to Microsoft’s store, which then needs to be reviewed and approved.

Overall, not a long or taxing process. However, with the new distribution architecture all of this can be cut down into just two steps.

* Build the rootfs.
* Create a merge request to [Microsoft’s WSL GitHub](https://github.com/microsoft/WSL/pull/12472) updating the distribution info list.

In fact, if we so chose, we could actually just build the rootfs and allow users to download the file and use it themselves. But why is this?

## The new WSL modern distribution architecture

This new architecture comes along with some new files that are used. These files, which are included in the rootfs, indicate to WSL what to do with the tarball. These files include information such as the Linux distribution’s name, icon, user settings, and even what should be done on first boot.

With these files in place, WSL is able to import the rootfs tarball directly and get the WSL distro properly installed and configured. And if you are on a certain version of WSL or later (currently only available in pre-release) you will be able to double-click on any `.wsl` extension tarball and instantly install that WSL distro.

As this is a basic outline of how this architecture works for end users, if you are interested it is worth reading Microsoft’s blog post and documentation shared at the start of this blog.

## Kali on the new distribution architecture

After receiving the email from the WSL team in November, 2024, we immediately began to update our build scripts to utilize this new feature. We created the necessary files and a basic out of box experience (oobe) script for WSL to use. After building it and testing it, we were impressed on how easy it was to use.

After the new year started we began to convert our existing build pipeline to fully utilize the new features offered in WSL. We modified our build script to include all of the new files, changed our build box to rename the tarball output into a `.wsl` extension, and are now utilizing kali.download, our Cloudflare mirror, to distribute the new file.

## How you can test this new WSL

The first thing you will need to do is be on the pre-release version of WSL. Run the following command in the Windows terminal:

```
wsl --update --pre-release
```

After this is installed, you should then be able to use `.wsl` files. To test this, go to our [kali.download page](https://kali.download/wsl-images/current/) and download the `.wsl` file for your computer’s architecture. Likely this will be **amd64**.

Alternatively, you can run the following command in your Windows terminal:

```
wsl.exe --install kali-linux
```

We hope that you appreciate and enjoy this new development for WSL as much as we do. Who knows what the future has in store for Kali on WSL, you may just see some new more complete Kali installs with this new easy to install `.wsl` file.

Table of Contents

* [Kali and WSL’s history](#kali-and-wsls-history)
* [The new WSL modern distribution architecture](#the-new-wsl-modern-distribution-architecture)
* [Kali on the new distribution architecture](#kali-on-the-new-distribution-architecture)
* [How you can test this new WSL](#how-you-can-test-this-new-wsl)

LIGHT
[ ] DARK

#### Links

[Home](https://www.kali.org/)
[Download / Get Kali](https://www.kali.org/get-kali/)
[Blog](https://www.kali.org/blog/)
[OS Documentation](https://www.kali.org/docs/)
[Tool Documentation](https://www.kali.o...