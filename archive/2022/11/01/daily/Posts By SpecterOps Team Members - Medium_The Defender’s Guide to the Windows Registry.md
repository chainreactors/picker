---
title: The Defender’s Guide to the Windows Registry
url: https://posts.specterops.io/the-defenders-guide-to-the-windows-registry-febe241abc75?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2022-11-01
fetch_date: 2025-10-03T21:28:57.749898
---

# The Defender’s Guide to the Windows Registry

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffebe241abc75&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fthe-defenders-guide-to-the-windows-registry-febe241abc75&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fthe-defenders-guide-to-the-windows-registry-febe241abc75&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-febe241abc75---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-febe241abc75---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# The Defender’s Guide to the Windows Registry

## It’s dangerous to defend the registry alone! Take this!

[![Luke Paine](https://miro.medium.com/v2/resize:fill:64:64/0*mDdi7Cpda086t25h.jpg)](https://medium.com/%40v3r5ace?source=post_page---byline--febe241abc75---------------------------------------)

[Luke Paine](https://medium.com/%40v3r5ace?source=post_page---byline--febe241abc75---------------------------------------)

10 min read

·

Oct 31, 2022

--

6

Listen

Share

Press enter or click to view image in full size

![]()

### Authors: Luke Paine & Jonathan Johnson

### Introduction

Welcome to the Defender’s Guide. This is a series of blog posts designed to give you a ground-up start to defending a specific technology from potential attackers. While a lot of this information may be redundant to a more seasoned information security personnel, even the best of us rely on Google and blog posts to get information. These posts are designed to be a one-stop shop, bringing a lot of that information together.

While each guide will be a blog post, they will also be accompanied with a folder in our Github repository with the takeaway information in a standardized, ingestible format. These will be updated each time the next guide is released. The blog post will exist in the repo in living form, in case edits need to be made to the content.

The guides will not be limited to technology-related topics, Defender’s Guides to Detection Engineering and other process-style topics are on the horizon.

[## GitHub - Defenders-Guide/TheDefendersGuide: The Github project for defender's guides

### The Defender's Guide is a project by Luke Paine and Jonathan Johnson to put all of the best defense resources for a…

github.com](https://github.com/Defenders-Guide/TheDefendersGuide?source=post_page-----febe241abc75---------------------------------------)

## Underlying Technology

### Registry Overview

The registry is a database on Windows systems that plays a major part in the configuration and control of the system. The registry, described by [Microsoft](https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/windows-registry-advanced-users), is:

> A central hierarchical database used in Windows 98, Windows CE, Windows NT, and Windows 2000 used to store information that is necessary to configure the system for one or more users, applications, and hardware devices.
>
> The Registry contains information that Windows continually references during operation, such as profiles for each user, the applications installed on the computer and the types of documents that each can create, property sheet settings for folders and application icons, what hardware exists on the system, and the ports that are being used.

### Registry Usage

The Windows registry is one of the most interacted with parts of the operating system. The registry is used by almost every installed application on a system to store and manage user configurations. Many applications store user preference information in the registry in order to persist across updates, as well as query information from the registry in order to complete the task the application is designed to do.

The large amount of information stored in the registry makes it a noisy source of telemetry if you don’t know where to look. Any given system has tens of thousands of reads and writes to the registry in a standard work day. It can be difficult for defenders to know where to start, which makes it a perfect target for attackers.

The top reason that attackers turn to the database is persistence. There are many ways that the registry can be used by an attacker to maintain their foothold in a network. The registry has several places where you can simply write a path to a binary, and the system will start that binary on boot. You can also hide entire executables in the registry so that you don’t need to write them to disk, reconstituting them when needed to execute on the system.

For other tactics, such as Credential Access, the registry holds some importance as well. LSASS stores its list of Security Packages in the registry, which can be edited to add a new package with the ability to access LSASS.

These are just a few examples of why the registry is a gold mine for an attacker in your network.

### **Registry Internals**

It’s easy to think of the registry as one big file that is sitting on disk. This is not the case, however. The registry is split between many files on disk that get loaded by the configuration manager, the subsystem that is in charge of implementing the registry. The configuration manager is in charge of the editing and organization of the registry, hence why the kernel level registry calls have the `CM` prefix (ie — `CmCreateKey`, `CmDeleteKey`). The configuration manager will load files on disk, called **hives**, that are in charge of various settings. However; before going into those we need to understand the registry structure.

As previously mentioned, the registry is a hierarchical database that has a tree format structure. Meaning there that each node within this tree is considered a key and in turn can have subkeys and entries called values. At the very top of this database are the root keys that can be thought of as the main directories for the subkeys embedded within them. There are 5 main root keys:

![]()

Root Keys

Windows also has a concept of predefined keys, which act as a simple way for registry related functions to refer to a given root key. This concept makes traversing the registry much easier as it provides a reliable starting point to locate the sub-key(s) you wish to query, create, or modify.

Underneath these root keys are [registry hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives), which are a group of keys/values in the registry that has an associated file that the configuration manager will load and link with the root keys. Hives can be found within the registry at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\hivelist`

The following table is provided by [Microsoft](https://learn.microsoft.com/en-us/windows/win32/s...