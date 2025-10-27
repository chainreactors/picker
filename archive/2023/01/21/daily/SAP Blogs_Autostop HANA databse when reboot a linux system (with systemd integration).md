---
title: Autostop HANA databse when reboot a linux system (with systemd integration)
url: https://blogs.sap.com/2023/01/20/autostop-hana-databse-when-reboot-a-linux-system-with-systemd-integration/
source: SAP Blogs
date: 2023-01-21
fetch_date: 2025-10-04T04:28:27.252409
---

# Autostop HANA databse when reboot a linux system (with systemd integration)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Autostop HANA database when reboot a linux system ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162379&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Autostop HANA database when reboot a linux system (with systemd integration)](/t5/technology-blog-posts-by-members/autostop-hana-database-when-reboot-a-linux-system-with-systemd-integration/ba-p/13563347)

![DominicW](https://avatars.profile.sap.com/4/7/id47adcd9753b11f74024bf497a0cbf5af7c4012fc7b35017a134e53bcf5cc7ecc_small.jpeg "DominicW")

[DominicW](https://community.sap.com/t5/user/viewprofilepage/user-id/197)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162379)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162379)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563347)

‎2023 Jan 20
10:38 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162379/tab/all-users "Click here to see who gave kudos to this post.")

7,113

* SAP Managed Tags
* [SUSE Linux Enterprise Server](https://community.sap.com/t5/c-khhcw49343/SUSE%2520Linux%2520Enterprise%2520Server/pd-p/68020287236497694019600446793069)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA, platform edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%252C%2520platform%2520edition/pd-p/01200314690800001945)

* [SUSE Linux Enterprise Server

  Operating System](/t5/c-khhcw49343/SUSE%2BLinux%2BEnterprise%2BServer/pd-p/68020287236497694019600446793069)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA, platform edition

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%25252C%2Bplatform%2Bedition/pd-p/01200314690800001945)

View products (3)

This is my first Blog so please conisder;-)

As a technical sap consultant working for large companies we are facing several challenges concerning big SAP- and HANA-landscapes. There are a lot of automated processes for administrating of these landscapes and this leads to problems in connection with HANA databases. One of these challenges I wan't to share in the following blog post.

## Initial situation

Because of security reason there is a monthly linux patching timeframe which is during night and there is no one that can stop the HANA databases before patching and rebooting the linux servers. Currently the reboot is triggered although HANA is running, so the database has always to recover after restart because there is no ordinary shutdown of the HANA database. When analyzing the traces we always see entries like the following in the startup process after a reboot (without shutdown HANA database before):

```
[4464]{-1}[-1/-1] 2023-01-04 11:16:03.399284 i Logger RecoveryHandlerImpl.cpp(00417) : Scan of open segment found log end position 0x17bb2598c0 within segment LogSegment[0x0:0x17bb234c80/Writing,ts=2023-01-04 11:02:27.351677][GUID=d0aa515f-003e-20230104-100159-223000000c/PrevGUID=e4e1a93f-003e-20230104-093146-34d000000b/PersGUID=6f3c30be-003e-20220628-080019-068000000e/RestoreGUID=f6039e5c-00af-20200513-081833-074000000f] at file position 0x931000, unused rest 0x3f6cf000
```

With the systemd integration there seems to be (not official SAP document founded) the possibility to have an ordinary shutdown process of the HANA database during reboot of Linux server.

## Activate systemd integration

### Prerequisites

* SUSE Linux Enterprise Server 15 (systemd version at least 234)

  ```
  zypper info systemd​
  ```

  ![](/legacyfs/online/storage/blog_attachments/2023/01/systemd-1.png)

* Installation of the polkit package is mandatory (see note [3139184](https://launchpad.support.sap.com/#/notes/3139184))

  ```
  zypper info polkit​
  ```

  ![](/legacyfs/online/storage/blog_attachments/2023/01/poolkit-1.png)

* HANA 2.0 SPS06 Revision 66 which is shipped with sapstartsrv 7.53 PL 1030 (at least PL 1011 is required for native systemd integration). At the time of blog writing, the HANA 2.0 SPS05 Revision 59.6 has still sapstartsrv 7.53 PL 1010 which not meet the prerequisites.

### Step-by-step guide

Register sapstartsrv for systemd integration:

1. Stop HANA database and the service

   ```
   sapcontrol -nr <NR> -function Stop

   sapcontrol -nr <NR> -function StopService
   ```

2. with user root make a new registration of sapstartsrv (you can find these Information in file /usr/sap/sapservices)

   ```
   export LD_LIBRARY_PATH=/usr/sap/<SID>/HDB<NR>/exe; /usr/sap/<SID>/HDB<NR>/exe/sapstartsrv pf=/usr/sap/<SID>/SYS/profile/<SID>_HDB<NR>_<hostname> -reg​
   ```

3. start new systemd Service

   ```
   systemctl start SAP<SID>_<NR>.service​
   ```

4. Start HANA Database (with <sid>adm)

   ```
   HDB start​
   ```

As a result, there is a modified entrie for the HANA instance in sapservices-File:

before:

```
LD_LIBRARY_PATH=/usr/sap/<SID>/HDB<NR>/exe:$LD_LIBRARY_PATH;export LD_LIBRARY_PATH;/usr/sap/<SID>/HDB<NR>/exe/sapstartsrv pf=/usr/sap/<SID>/SYS/profile/<SID>_HDB<NR>_<HOSTNAME> -D -u <sid>adm
```

after:

```
systemctl --no-ask-password start SAP<SID>_<NR> # sapstartsrv pf=/usr/sap/<SID>/SYS/profile/<SID>_HDB<NR>_<hostname>
```

There is also a new systemd service which is running in SAP.slice:

```
systemctl cat SAP<SID>_<NR>.service
```

![](/legacyfs/online/storage/blog_attachments/2023/01/systemd_service-1.jpg)

Now when you trigger a reboot of the linux system, firstly it will ordinary shutdown the HANA database before rebooting the system. When analyzing the traces after such a reboot of the system, I can se an ordinary shutdown of the HANA database (this I couldn't find before):

```
[4187]{-1}[-1/-1] 2023-01-04 10:26:35.677882 i Basis HDBConsListener.cpp(00186) : Stopping HDBCons listener

[4270]{-1}[-1/-1] 2023-01-04 10:26:35.677898 i Basis HDBConsListener.cpp(00168) : HDBCons listener stopped

[4187]{-1}[-1/-1] 2023-01-04 10:26:35.685287 i Service_Shutdown TrexService.cpp(00725) : System down
```

## Conclusion / Disclaimer

This procedure was only testing with a small HANA database. There were no other SAP instances on this server. When there is also a SAP instance on the server you have to consider the dependencies while stopping/starting. When you are a Linux-Expert (I'm not;-)) you can handle this dependencies within systemd with custom-settings.conf file.

Before use this, test it on a sandbox or development system. You have to be aware of the timeout (TimeoutStopSec) in the systemd service. If the ordinary shutdown process takes longer than the default timeout (360s) you have to adjust it otherwise the reboot will take place before the ordinary shutdown of the HANA database.

## Further Information

<https://launchpad.support.sap.com/#/notes/3139184>

<https://launchpad.support.sap.com/#/notes/3115048>

<https://blogs.sap.com/2022/04/25/sap-software-on-linux-with-systemd/>

* [sapcontrol](/t5/tag/sapcontrol/tg-p/board-id/technology-blog-members)
* [sapstartsrv](/t5/tag/sapstartsrv/tg-p/board-id/technology-blog...