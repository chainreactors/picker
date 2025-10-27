---
title: The Defender’s Guide to Windows Services
url: https://posts.specterops.io/the-defenders-guide-to-windows-services-67c1711ecba7?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2023-01-19
fetch_date: 2025-10-04T04:19:47.999778
---

# The Defender’s Guide to Windows Services

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F67c1711ecba7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fthe-defenders-guide-to-windows-services-67c1711ecba7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fthe-defenders-guide-to-windows-services-67c1711ecba7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-67c1711ecba7---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-67c1711ecba7---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# The Defender’s Guide to Windows Services

## It’s dangerous to find malicious services alone! Take this!

[![Jonathan Johnson](https://miro.medium.com/v2/resize:fill:64:64/1*ro6iOomAZwYlmMgljL7EfA.png)](https://jonny-johnson.medium.com/?source=post_page---byline--67c1711ecba7---------------------------------------)

[Jonathan Johnson](https://jonny-johnson.medium.com/?source=post_page---byline--67c1711ecba7---------------------------------------)

10 min read

·

Jan 18, 2023

--

1

Listen

Share

![]()

### Authors: Luke Paine & Jonathan Johnson

## Introduction

This is the second installment of the Defender’s Guide series. In keeping with the theme, we are discussing Windows Services, the underlying technology, common attack vectors, and methods of securing/monitoring them. Services are an important part of the Windows operating system, allowing the control and configuration of long-running processes essential to keeping the OS functional. This also allows services to be a common vector of escalation and persistence by attackers. Some services (especially custom services) run with high privilege levels, and are set to restart themselves on boot. This is a slam dunk for the enterprising attacker looking to gain a foothold in an environment.

## Underlying Technology

### Services Overview

Services, at a base level, are processes. However some significant differences exist between a service and a standard process. You can’t take a standard binary and install it as a service, expecting it to work. Services must be installed before they can be executed, and they require specific functions in order for the control mechanism to interact with them, which we will go into further detail about later in this post.

[**According to Microsoft:**](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/introduction-to-windows-service-applications)

> “Microsoft Windows services, formerly known as NT services, enable you to create long-running executable applications that run in their own Windows sessions. These services can be automatically started when the computer boots, can be paused and restarted, and do not show any user interface. These features make services ideal for use on a server or whenever you need long-running functionality that does not interfere with other users who are working on the same computer. You can also run services in the security context of a specific user account that is different from the logged-on user or the default computer account”

### Services Usage

The average user doesn’t have to interact with the services console, and even power users might rarely find themselves taking a look through the installed services. A lot of them are essential to the functionality of Windows itself, and a lot of them are installed with software over the lifecycle of the machine.

Although services can be manually controlled, the interactions with them are essentially limited to Start and Stop. Any GUI elements spawned by a service are displayed in a separate window station from the interactive one of the current user. Think of this as a hidden desktop dedicated to each service. As per Microsoft:

> “Because the station of the Windows service is not an interactive station, dialog boxes raised from within a Windows service application will not be seen and may cause your program to stop responding.”

What if you wanted to interact with those stations, or a service wanted to interact with the station you *are* able to see? Microsoft has an answer for that, too.

> “The .NET Framework also does not include classes that represent stations and desktops. If your Windows service must interact with other stations, you will need to access the unmanaged Windows API.”

In short, user interaction with Windows services is rather low. Why do we, and attackers, care about them so much? Read on, dear defender, read on.

### Services Internals

At a high level, services are backed by a Remote Procedure Call (RPC) server called the Service Control Manager (SCM). This server is stored within the services.exe binary and allows for creation, configuration, enumeration, and maintenance of services. Services are one of the core components of the Windows operating system (OS) and (depending on the service) is needed for the OS to successfully boot/run.

As previously mentioned, services are backed by a RPC server called the SCM ([MS-SCMR](https://learn.microsoft.com/en-us/openspecs/windows_protocols/MS-SCMR/705b624a-13de-43cc-b8a2-99573da3635f)) stored within the services.exe binary. However; when thinking about services, there are really 4 main components:

Press enter or click to view image in full size

![]()

### Service Control Manager (SCM)

When the service.exe binary is started during the boot process, service.exe goes through various functions to get the SCM up and running. One of which is a function that generates the service database. It does so by scanning the contents of the Services registry key (HKLM\SYSTEM\CurrentControlSet\Services\). Each entry is added to the database and is considered a service record. Every record will have the name of the service and its correlating parameters (more information on this later).

After boot, if someone wants to register a service and launch it during that same boot lifecycle, they must use the appropriate service-based Win32 APIs or call the MS-SCMR RPC methods directly. This allows communication to be sent to the SCM through RPC, which will allow for the creation of a service by creating an entry within the Services registry key, for which after the SCM will create another service record within the service database.

Someone could manually add a key to the registry within the Services registry key, however; the SCM doesn’t know how to add that as a record. To get that service to launch, a reboot is required. The SCM will then add that service into the database appropriately.

### SCM Functions

The Win32 APIs that can be used to interface with the SCM can be found in the [winsvc.h](https://learn.microsoft.com/en-us/windows/win32/api/winsvc/) or advapi32.dll/sechost.dll. When the supporte...