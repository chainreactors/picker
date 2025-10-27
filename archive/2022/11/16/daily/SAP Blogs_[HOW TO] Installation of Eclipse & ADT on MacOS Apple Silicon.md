---
title: [HOW TO] Installation of Eclipse & ADT on MacOS Apple Silicon
url: https://blogs.sap.com/2022/11/15/how-to-installation-of-eclipse-adt-on-macos-apple-silicon/
source: SAP Blogs
date: 2022-11-16
fetch_date: 2025-10-03T22:52:34.715036
---

# [HOW TO] Installation of Eclipse & ADT on MacOS Apple Silicon

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* [HOW TO] Installation of Eclipse & ADT on MacOS Ap...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47454&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [[HOW TO] Installation of Eclipse & ADT on MacOS Apple Silicon](/t5/application-development-and-automation-blog-posts/how-to-installation-of-eclipse-adt-on-macos-apple-silicon/ba-p/13568709)

![preetamr](https://avatars.profile.sap.com/7/2/id7222cef97e0dabd9da2d32fc7cc3eb47bd1cc70c0d81fd37a99bda2881bb305f_small.jpeg "preetamr")

[preetamr](https://community.sap.com/t5/user/viewprofilepage/user-id/198621)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47454)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47454)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568709)

‎2022 Nov 15
9:48 PM

[5
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47454/tab/all-users "Click here to see who gave kudos to this post.")

8,257

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

With SAP TechEd 2022 few days away and surely many of you have registered for virtual workshop session that requires installing Eclipse and ADT beforehand as a prerequisites. This is a breeze when you do it on Windows PC. However, that may not be the case for you if you are on MacOS on any of the current Apple products that comes shipped with Apple Silicon (M1, M2, etc.)

There is already a great [blog post](https://blogs.sap.com/2021/09/27/how-to-install-sap-gui-for-java-and-eclipse-adt-on-m1-macbook/) for something similar by philywu . If that worked for you, then this blog is not for you. This is for someone who come across some issues even after that (as evident from comments section of above mentioned blog). Being one of those user for whom the installation was not as smooth, I initially thought of adding it as a comment for anyone going through the same. However after some evaluation, blog post seemed like a better option.

Let me discuss the two problems that I faced and later on, I will list out the installation steps.

#### **Problem 1: JCo initialisation failed**

After installation of ADT, Restart of Eclipse. A popup comes up stating JCo initialisation has failed as shown below in the screenshot

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-11-at-3.46.06-PM.png)

This occurs because currently SAP doesn't support SAP Java Connector (JCo) for ARM based architecture as evident from download section of [product page](https://support.sap.com/en/product/connectors/jco.html) . This may change in future as SAP starts rolling out support for ARM (evident from release of SAP GUI for Java 7.80 with ARM support)

Also one of the point to note from the error popup is, it tries to find ***sapjco3*** in Java Path. So the installed JDK may be the cause for this issue. I will install the JDK x86\_64 in later section to remediate this.

*NOTE:**SAP clearly states in [Installation Guide](https://help.sap.com/doc/2e9cf4a457d84c7a81f33d8c3fdd9694/Cloud/en-US/inst_guide_abap_development_tools.pdf) [Page 17, Section 3.3 ADT Support PAM] following:*
> *"Architecture AArch64 (Apple silicon) is also sup­ported, but you must use the x86\_64 version of Eclipse."*

#### **Problem 2: After successful installation of Eclipse (x86\_64) & SapMachineJDK (x86\_64), Eclipse won't open on system restart.**

So, let's say you have installed x86\_64 version of Eclipse & SapMachineJDK and it works just fine. But you restart your MacOS and Eclipse stops working, Your Mac says "Code signature Invalid" as shown in image below.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-11-at-4.47.12-PM.png)

MacOS Code Signature Invalid report dialog

This is very interesting issue and gave me an opportunity to understand a bit about gatekeeper component of MacOS. Let's understand the steps to reproduce the issue.

It seems changing **Info.plist**or **eclipse.ini** changes the package and MacOS considers it a threat and blocks the application which is good thing in itself. However, not applicable for this case since we know we have to make changes in either of this file to use custom JDK. To avoid this, we will perform a code sign of the Eclipse package as demonstrated in next section.

## **Installation Steps**

I know this has been a long read on the problem itself. Now let's jump right into the action.

Following config & tools are used in this guide:
**Eclipse**: 4.5, 2022-09 (x86\_64)
**SapMachineJDK**: 17.0.5 (x86\_64)
**OS**: macOS Monterey (12.6)
**Chip**: Apple M1

Before we start, quick disclaimer: I will be working on a custom directory instead of changing anything in standard configuration e.g. JAVA\_HOME variable, PATH variable to avoid any effect on other applications (non-SAP) which works with ARM based JDK.

#### **Step 1: Prepare Custom directory**

We will be using this directory to store our JDK & Eclipse executable. Open a terminal window, Create a directory anywhere that you wish to, I prefer one within the user directory.

```
$ cd ~

$ mkdir DEV_TOOLS
```

#### **Step 2: Download & Install JDK**

You can either directly use command line tool like cURL to download the file on to the path or download via. web browser on <https://sap.github.io/SapMachine/>

***Option 1: Download via. cURL***

```
$ cd ~/DEV_TOOLS

$ curl -L https://github.com/SAP/SapMachine/releases/download/sapmachine-17.0.5/sapmachine-jdk-17.0.5_macos-x6... -o sapmachinejdk17.tar.gz
```

***Option 2: Download with Web Browser***

Visit website <https://sap.github.io/SapMachine/> and download as shown in following screenshot:
![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-11-at-5.03.57-PM.png)

Download Options for SapMachineJDK

Once you have downloaded & moved the *tar.gz* file to directory we create in step 1. We will unpack the archive. Time to jump back to terminal.

```
$ tar -xvzf sapmachinejdk17.tar.gz
```

*NOTE: Replace "sapmachinejdk17.tar.gz" with the filename you have downloaded*

After unpack, a new directory ***sapmachine-jdk-17.0.5.jdk***created.

```
$ cd ~/DEV_TOOLS/sapmachine-jdk-17.0.5.jdk/Contents/Home/bin

$ echo $PWD"/java"
```

Copy the output of second command and keep a note of it. We will be ...