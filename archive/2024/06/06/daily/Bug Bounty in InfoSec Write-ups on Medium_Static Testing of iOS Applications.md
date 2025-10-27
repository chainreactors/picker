---
title: Static Testing of iOS Applications
url: https://infosecwriteups.com/static-testing-of-ios-applications-cb09bd8f2927?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-06-06
fetch_date: 2025-10-06T16:55:56.351918
---

# Static Testing of iOS Applications

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcb09bd8f2927&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstatic-testing-of-ios-applications-cb09bd8f2927&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstatic-testing-of-ios-applications-cb09bd8f2927&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-cb09bd8f2927---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-cb09bd8f2927---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Static Testing of iOS Applications

[![Sandeep Vishwakarma](https://miro.medium.com/v2/resize:fill:64:64/1*z0HvbsUyjs0Hipqo2SXV9w.jpeg)](https://sandeepvi.medium.com/?source=post_page---byline--cb09bd8f2927---------------------------------------)

[Sandeep Vishwakarma](https://sandeepvi.medium.com/?source=post_page---byline--cb09bd8f2927---------------------------------------)

8 min read

·

May 30, 2024

--

1

Listen

Share

Greetings fellow hackers, my name is Sandy, Security Analyst and Bug bounty hunter.

As I’m presently engaged in iOS penetration testing, I’d like to relay my experiences with you, as they may prove beneficial in addressing some of the inquiries. I had difficulty getting started on resolving answers without any more introductions.

Press enter or click to view image in full size

![]()

This guide is an extensive guide that will take you through the entire process, as well as providing an outline of what Mobile Security Framework or [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) is and how it may be used to automatically analyses an IPA file and the process of how we might hand evaluate a sample IPA file on a jailbroken iPhone. Sticking with examination, it also embraces some routine checks: The trial balances of the Info and its subsidiaries as of 31 December are as follows: Accountants checks from the Info. plist file according to various applications needs and security measures.

Based on the above points, one is left with no option than to agree that there is need for better understanding of the IPA file structure.

IPA is as of now the common form used in supplying iOS applications referring to iOS App Store Package. It is azagzipped set of files that holds all the information needed by an application to run on an iPhone. Here’s a detailed breakdown of the components found within an IPA file:Below are the features you are likely to stumble upon as you work with an IPA file:

It includes the following parts:

1. **.app Directory:**

This is the main directory inclusive of the executable and all materials required to run the app.

To get a glimpse of the contents, modify the ‘. ’The files with ipa file extension should now be saved with . zip and decompress it.

2. **Info. plist:**

This file has important property constraints which include the app’s bundle ID, version number, and capabilities of the device as well as the permissions of the app.

3. **\_CodeSignature/:**

A list that contains the code signature of the app, to guaranteeing the identity of the program.

4. **Assets. car:**

A compressed file with all the graphical components included in the app (for example, icons, images).

5. **Frameworks/:**

Includes dynamic libraries (dylib) and frameworks (framework) that the app uses.

6. **PlugIns/:**

This directory may contain app extensions, packaged as . appex files. It is not necessarily in all IPA files.

7. **Core Data:**

For storing other data and the data that synchronizes itself across the devices using iCloud.

8. **PkgInfo:**

Offices another method to define the type and creator codes for the app.

9. **Localization Files (e.g., en.lproj, fr.lproj, Base.lproj):**

These files contain the language modules and a default set of modules in the event a certain language is not recognized.

**Procedure of Performing Static Analysis on Mobile Applications using Mobile Security Framework (MobSF)**

MobSF is yet another tool that helps the user in performing static analysis on mobile applications. undefined

**Using MobSF**

Run the MobSF Web Interface:

Press enter or click to view image in full size

![]()

1. Setting up MobSF starts the server and allows you to proceed to the next steps. Connect to the web interface by going online with the help of the browser.

2. Upload the IPA File:

3. Upload the IPA file into the MobSF and after loading, proceed with the static analysis.

Press enter or click to view image in full size

![]()

4. **Review the Analysis Results:**

Look for misconfigurations and vulnerabilities, such as:

* Insecure URL schemes
* Improper permissions and App Transport Security (ATS) misconfigurations
* Unsafe binary options
* Hardcoded sensitive information (e.g., Firebase keys, email addresses)
* Other potential security issues

Some of the advantages of **manual static analysis** include increased accuracy, a detailed view of the application, and the ability to analyze a jailbroken iOS device.

That is why manual analysis of a static type helps to gain more detailed information regarding the app’s security. This process is possible only on an iOS device unlocked from its manufacturer restrictions.

**Obtaining the App Path**

1. SSH into the iOS Device:SSH into the iOS Device:

I would like to add the connection to the jailbroken device by SSH as the first step.

2. Locate the App:

Use the find command to locate the app’s plist files:Use the find command to locate the app’s plist files:

![]()

3. Identify App Locations:

> System applications are located in **/Applications**
>
> User-installed apps are located in **/private/var/containers/**
>
> Bundled apps directory: **/var/containers/Bundle/Application/**
>
> Data directory: **/var/mobile/Containers/Data/Application/**

**Checking the Binary with otool**

1. Check for Position Independent Executable (PIE):

Ensures the app loads into a random memory address, enhancing security.

![]()

2. Verify Stack Canaries:

Protects against stack overflow attacks by validating stack integrity.

![]()

3. Check for Automatic Reference Counting (ARC):

Prevents memory corruption by automatically managing memory

Press enter or click to view image in full size

![]()

4. Ensure the Binary is Encrypted:

Confirms the binary is encrypted, protecting the app from tampering.

Press enter or click to view image in full size

![]()

5. Identify Sensitive/Insecure Functions:

* Weak Hashing Algorithms:

Press enter or click to view image in full size

![]()

* Insecu...