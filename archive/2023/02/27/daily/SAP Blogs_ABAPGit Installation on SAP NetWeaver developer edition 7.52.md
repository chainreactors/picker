---
title: ABAPGit Installation on SAP NetWeaver developer edition 7.52
url: https://blogs.sap.com/2023/02/26/abapgit-installation-on-sap-netweaver-developer-edition-7.52/
source: SAP Blogs
date: 2023-02-27
fetch_date: 2025-10-04T08:10:59.332831
---

# ABAPGit Installation on SAP NetWeaver developer edition 7.52

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* ABAPGit Installation on SAP NetWeaver developer ed...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160448&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ABAPGit Installation on SAP NetWeaver developer edition 7.52](/t5/technology-blog-posts-by-members/abapgit-installation-on-sap-netweaver-developer-edition-7-52/ba-p/13552377)

![dukejib5](https://avatars.profile.sap.com/e/0/ide0a223e3c33130300235f8c46d7c47c8366412de94a73fb1687ddf440948d81a_small.jpeg "dukejib5")

[dukejib5](https://community.sap.com/t5/user/viewprofilepage/user-id/710276)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160448)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160448)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552377)

‎2023 Feb 26
11:13 AM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160448/tab/all-users "Click here to see who gave kudos to this post.")

2,747

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP NetWeaver Application Server for ABAP](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver%2520Application%2520Server%2520for%2520ABAP/pd-p/01200314690800000234)

* [SAP NetWeaver Application Server for ABAP

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver%2BApplication%2BServer%2Bfor%2BABAP/pd-p/01200314690800000234)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (2)

Hi,

In this blog post, we will learn to activate [AbapGit](https://docs.abapgit.org/) on SAP NetWeaver Developer Edition 7.52 with an **alternate way** of installing server certificates and ensuring AbapGit is working as it should be.

Recently, i had the pleasure of installing the SAP NetWeaver Developer Edition 7.52 on my PC. The first thing i wanted was to have backup of my code available to me.

Luckily, we have a wonderful tool [AbapGit](https://docs.abapgit.org/) at our disposal. [Installation](https://docs.abapgit.org/guide-install.html) was a breeze, as it was very well documented, however, [SSL Setup](https://docs.abapgit.org/guide-ssl-setup.html) was a bit of a problem, as some of the directions are bit vague , and provided steps were not fruitful at least at my end. However, with little bit of work, i was able to have it work on my SAP installation. Here i am putting up the steps, so that those who are facing the issues, will be able to solve them at their ends.

Little bit of BASIS work is also required.

I am not going to reproduce the steps of installation here, however, i suggest that one should download ,

[zabapgit\_standalone](https://raw.githubusercontent.com/abapGit/build/main/zabapgit_standalone.prog.abap) source code and save it as text file. Create a Program of this code and assign a transaction code to it ( zabapgit is for me). if you run this program, you will see this screen.

![](/legacyfs/online/storage/blog_attachments/2023/02/abapgit.jpg)

Abap GIT Main Page

For testing of our connectivity to Github, we have one more program on our disposal, [zabap\_test\_ssl](https://raw.githubusercontent.com/abapGit/docs.abapgit.org/main/src/zabapgit_test_ssl.abap)  , download it and create a program in SE38 and execute it. Following screen will appear.

![](/legacyfs/online/storage/blog_attachments/2023/02/test_ssl-2.jpg)

Upon executing this program, you will receive some errors like below or some others , now we need to find a way to solve these errors.

![](/legacyfs/online/storage/blog_attachments/2023/02/errors.jpg)

#### Let's Solve The Problem

[AbapGit SSL Setup](https://docs.abapgit.org/guide-ssl-setup.html) mentions adding some parameters to SAP Default Profile. First of all, add those parameters if not already added.

Mentioned Parameters are;

```
ssl/ciphersuites             = 135:PFS:HIGH::EC_X25519:EC_P256:EC_HIGH

ssl/client_ciphersuites      = 150:PFS:HIGH::EC_X25519:EC_P256:EC_HIGH

icm/HTTPS/client_sni_enabled = TRUE

ssl/client_sni_enabled       = TRUE

SETENV_26 = SECUDIR=$(DIR_INSTANCE)$(DIR_SEP)sec

SETENV_27 = SAPSSL_CLIENT_CIPHERSUITES=150:PFS:HIGH::EC_X25519:EC_P256:EC_HIGH

SETENV_28 = SAPSSL_CLIENT_SNI_ENABLED=TRUE
```

There parameters can be added through Transaction Code : RZ10. Here is a picture

![](/legacyfs/online/storage/blog_attachments/2023/02/rz10-before.jpg)

And here is RZ10 after adding the parameters.

![](/legacyfs/online/storage/blog_attachments/2023/02/rz10-after.jpg)

When you save the profile, SAP will prompt you to activate it and then mentions in popup that you must restart the SAP to have this changes be effective.

**Logout and restart your SAP Application.**

It is worth noting that, before making any changes to your SAP System profile, one should make a backup copy, so that in case of problems, you can revert back to old settings.

```
On Terminal:

cp DEFAULT.PFL DEFAULT.PFL.BKP
```

Once, SAP is back online, we need to add Server Certificates to Transaction Code Strust. On multiple available videos on youtube & [AbapGit SSL Setup](https://docs.abapgit.org/guide-ssl-setup.html) , solution is to add extract certificate from your browser and upload it to Strust, however , in my testing , it was not working, so i applied another way of extracting the Certificate for Strust by using Transaction Code : SMICM and extracting the Certificate from Trace Files.

**Steps:**

* Run Transaction : **SMICM**

* On Menu : **Goto -> Trace File -> Reset** (This will clear the Trace file)

* Then On Menu : **Goto -> Trace Level -> Set** (Select **level 3** and press **Pen** icon)

* Go To Transaction : **SE38**

* Run [zabap\_test\_ssl](https://raw.githubusercontent.com/abapGit/docs.abapgit.org/main/src/zabapgit_test_ssl.abap) program (This will again result in error, but this time **SMICM** will show us the full error log with server certificate information.

* Exit **SE38**

* Run Transaction : **SMICM**

* Then On Menu : **Goto -> Trace Level -> Set** (select **level 1** and press **Pen** icon)

* Then on Menu : **Goto -> Trace File -> Display All**

* Search for Value "**Trace Level**" and select "**changing Trace Level to 3**"

Now, we need to look at the Trace File and find the following line

```
Subject: CN=github.com, O="GitHub, Inc.", L=San Francisco, SP=California, C=US

Issuer: CN=DigiCert TLS Hybrid ECC SHA384 2020 CA1, O=DigiCert Inc, C=US

Serial Number: 0C:D0:A8:BE:C6:32:CF:E6:45:EC:A0:A9:B0:84:FB:1C
```

Just below this, there is a section with **---BEGIN CERTIFICATE---** as heading, Copy all of it and save it with the name of **github.cer** file. Make sure, the text starts with

```
-----BEGIN CERTIFICATE-----
```

and ends with

```
-----END CERTIFICATE-----
```

Notice 5 **"-"** in lead & end.

If you go down on the trace, you will find another certificate just below this mentioning  **CN=digicert ,** just skip it and go further down, until you came across the fo...