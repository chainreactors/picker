---
title: Linux History File Timestamps
url: https://www.trustedsec.com/blog/linux-history-file-timestamps/
source: TrustedSec
date: 2022-11-16
fetch_date: 2025-10-03T22:53:39.412284
---

# Linux History File Timestamps

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [The Benefits of Enabling Timestamps in Your Command-Line History](https://trustedsec.com/blog/linux-history-file-timestamps)

November 15, 2022

# The Benefits of Enabling Timestamps in Your Command-Line History

Written by
Thomas Millar

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/LinuxHistoryFileTimestamps_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695569093&s=eea4afd780c9cb37b514fcc1baab1a95)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#dae5a9afb8b0bfb9aee799b2bfb9b1ffe8eab5afaeffe8eaaeb2b3a9ffe8eabba8aeb3b9b6bfffe8eabca8b5b7ffe8ea8ea8afa9aebfbe89bfb9ffe8ebfcbbb7aae1b8b5bea3e78eb2bfffe8ea98bfb4bfbcb3aea9ffe8eab5bcffe8ea9fb4bbb8b6b3b4bdffe8ea8eb3b7bfa9aebbb7aaa9ffe8eab3b4ffe8ea83b5afa8ffe8ea99b5b7b7bbb4bef796b3b4bfffe8ea92b3a9aeb5a8a3ffe99bffe8eab2aeaeaaa9ffe99bffe89cffe89caea8afa9aebfbea9bfb9f4b9b5b7ffe89cb8b6b5bdffe89cb6b3b4afa2f7b2b3a9aeb5a8a3f7bcb3b6bff7aeb3b7bfa9aebbb7aaa9 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flinux-history-file-timestamps "Share on Facebook")
* [Share on X](http://twitter.com/share?text=The%20Benefits%20of%20Enabling%20Timestamps%20in%20Your%20Command-Line%20History%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Flinux-history-file-timestamps "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flinux-history-file-timestamps&mini=true "Share on LinkedIn")

While working at TrustedSec, I was issued a new company-furnished laptop to work from. While the Mac OS environment was useful, I found it useful to also setup an Ubuntu virtual machine. One reason is so I can have access to a Linux host that is very similar to the garden variety of Linux systems that I get to review during threat hunting and investigations. This blog post will walk you through setting up and enabling logging that I found extremely helpful not only for company work, but for projects and play too. Specifically, we will walk through setting history timestamps in the command-line history facility of the OS.

In my work, I often think about a command that needed to be run from the Terminal in a command-line manner and whether it was either useful, complicated, or had many steps to it, etc. So, if these commands needed to be recalled, we can do so using the well-known facility that has been around since the BSD editions of Unix: History. These tend to be very useful to recall what user-entered commands the OS recorded. To those of us that investigate suspicious computer activities, malware outbreaks, or breaches, the history records a wealth of key artifacts and activities. However, telling *when* it occurred might be tougher if the system is set to default (<https://par.nsf.gov/servlets/purl/10213652>).

```
tmillar@HP8200:/dev/shm$ cd /dev/shm

tmillar@HP8200:/dev/shm$ touch altair deneb vega

tmillar@HP8200:/dev/shm$ history

    1  cd /dev/shm

    2  touch altair deneb vega

    3  history
```

By looking at other examples, we may be able to draw conclusions of when commands were issued to system by the person in control of the user ID. Please keep in mind that file timestamps are like boot prints in the mud: the most recent is the one you are most likely to make out to a good degree of certainty for each, Modified (mtime), Accessed (atime), or Changed (ctime). It is also important to note that Linux file system ext2/3 will not have Created (btime); however, this has since been implemented under ext4. Additionally, it’s important to understand that file timestamps can be manipulated or altered. When this occurs, it may throw off the examiner, unless they know where else to look or validate the time values being asserted to them.

Below is an example of this sort of situation. The contents of the /etc/passwd file are listed, redirected to the folder /dev/shm, and renamed to mycopy\_passwd. The permissions to the file are then modified with the chmod command, and file stats can be checked to validate these permissions and timestamps.

```
$ cat /etc/passwd  >> /dev/shm/mycopy_passwd

$ chmod 744 /dev/shm/mycopy_passwd

$ stat /dev/shm/mycopy_passwd

  File: '/dev/shm/mycopy_passwd'

  Size: 2418          Blocks: 8          IO Block: 4096   regular file

Device: 18h/24d Inode: 3           Links: 1

Access: (0744/-rwxr--r--)  Uid: ( 1000/ tmillar)   Gid: ( 1000/ tmillar)

Access: 2022-10-07 08:20:41.091102055 -0700

Modify: 2022-10-07 08:20:41.091102055 -0700

Change: 2022-10-07 08:24:45.491107440 -0700

 Birth: -
```

The history record appears as th...