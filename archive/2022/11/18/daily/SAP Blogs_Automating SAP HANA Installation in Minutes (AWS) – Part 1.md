---
title: Automating SAP HANA Installation in Minutes (AWS) – Part 1
url: https://blogs.sap.com/2022/11/17/automating-sap-hana-installation-in-minutes-aws-part-1/
source: SAP Blogs
date: 2022-11-18
fetch_date: 2025-10-03T23:06:23.554307
---

# Automating SAP HANA Installation in Minutes (AWS) – Part 1

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Automating SAP HANA Installation in Minutes (AWS) ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160055&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Automating SAP HANA Installation in Minutes (AWS) - Part 1](/t5/technology-blog-posts-by-members/automating-sap-hana-installation-in-minutes-aws-part-1/ba-p/13549969)

![ahmedyasin](https://avatars.profile.sap.com/5/9/id59772a056641f864351f9eb1c4930b177b2879b9ba0a0509528179c8672cf7b6_small.jpeg "ahmedyasin")

[ahmedyasin](https://community.sap.com/t5/user/viewprofilepage/user-id/627554)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160055)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160055)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549969)

‎2022 Nov 17
6:48 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160055/tab/all-users "Click here to see who gave kudos to this post.")

1,937

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (1)

This blog describes installing HANA database automatically in less than 15 minutes in AWS with some prerequisite like VPC, AMI, Subnet, Security Group, IG, EC2, EBS, AWS CLI, AWS Access Keys and SAP HANA media  others mandatory services available in place to host the HANA workloads in AWS cloud.

**Operating System (AMI):**

AMI is created with SUSE Linux environment (SLES-15 with SP4) with the latest OS update, with the following packages amazon-ssm-agent.rpm, nfs-utility, insserv-compat and libltdl7.

**Terraform & AWS CLI :**

Terraform v0.15.5 for Windows (64) bit has been installed for building the workloads though API with AWS CLI.

### **Generate Configuration File:**

Generate configuration file by using the below command for batch installation through a different machine so that the installation can be carried out in batch mode.

![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img1.jpg)

This will generate two files server.xml and server.cfg, the server.xml for maintain the master passwords and server.cfg for maintaining the following parameter

Componet\_medium=/path/to/the/media

User\_master\_password=y

Components=server

Hostname=hanadev

### **Terraform Configuration File (Main.tf):**

Create the EC2 resource through terraform with the following configuration.

![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img2.jpg)

**AMI-contains the following OS & packages pre-installed:**

* SLES-15 with SP4 latest OS update,

* nfs-utility

* insserv-compat

* libltdl7

* amazon-ssm-agent.rpm (optional)

* AWS Backint agent (optional)

**EBS-Volume: Type of volume is of your choice (GP2/GP3/io1/io2/st1)**

![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img3.jpg)

**EBS Volume (Attachment):**

![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img4-1.jpg)

**User\_data: (init-script.sh):**

![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img5.jpg)

**Mount the media which is available in the EFS folder**

1. sudo mkdir -p /mnt/efs
2. sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport 123.456.78.160:/ /efs

**Create the Physical Volume & Volume Group, FS and Mount**

3. sudo pvcreate /dev/xvdh
4. sudo vgcreate datavg /dev/xvdh

**Create logical volume for installing SAP HANA**

5. sudo lvcreate -n lvshared -L 50G datavg
6. sudo lvcreate -n lvdata -L 50G datavg
7. sudo lvcreate -n lvlog -L 50G datavg
8. sudo lvcreate -n lvusrsap -L 50G datavg

**Create “xfs” file system**

9.  sudo mkfs.xfs /dev/datavg/lvshared
10. sudo mkfs.xfs /dev/datavg/lvdata
11. sudo mkfs.xfs /dev/datavg/lvlog
12. sudo mkfs.xfs /dev/datavg/lvusrsap
13. sudo mkdir -p /hana

**Create directory and mount the file system**

14. sudo mkdir -p /hana/shared
15. sudo mkdir -p /hana/data
16. sudo mkdir -p /hana/log
17. sudo mkdir -p /usr/sap
18. mount /dev/datavg/lvshared /hana/shared
19. mount /dev/datavg/lvdata /hana/data
20. mount /dev/datavg/lvlog /hana/log
21. mount /dev/datavg/lvusrsap /usr/sap

**Trigger the batch command with pre-generated files for silent/batch installation with SID**

22. cat /efs/hanafiles/configfile.xml | /efs/hanafiles/DATA\_UNITS/HDB\_LCM\_LINUX\_X86\_64/hdblcm --read\_password\_from\_stdin=xml --sid=DE2 --components=server --use\_master\_password=yes -b

Continue: Part 2 of 2

[[https://blogs.sap.com/2022/11/18/automating-sap-hana-installation-in-minutes-aws-part-2/?preview\_id=...](https://blogs.sap.com/2022/11/18/automating-sap-hana-installation-in-minutes-aws-part-2/?preview_id=1649598&preview=true)]

* [automate](/t5/tag/automate/tg-p/board-id/technology-blog-members)
* [batch installation](/t5/tag/batch%20installation/tg-p/board-id/technology-blog-members)
* [installation](/t5/tag/installation/tg-p/board-id/technology-blog-members)
* [sap hana](/t5/tag/sap%20hana/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fautomating-sap-hana-installation-in-minutes-aws-part-1%2Fba-p%2F13549969%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Mass activation of ICF services](/t5/technology-blog-posts-by-members/mass-activation-of-icf-services/ba-p/14227490)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [🚀 SAP BTP Weekly: Practical AI, Enhanced Analytics, and a Vision for the Future](/t5/technology-blog-posts-by-sap/sap-btp-weekly-practical-ai-enhanced-analytics-and-a-vision-for-the-future/ba-p/14211112)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  4 weeks ago
* [From Text to Process to Automation](/t5/technology-blog-posts-by-sap/from-text-to-process-to-automation/ba-p/14208217)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a month ago
* [Implementation of SAP S/4HANA 2022 using SAP best Practice](/t5/technology-q-a/implementation-of-sap-s-4hana-2022-using-sap-best-practice/qaq-p/14199942)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  2025 Aug 29
* [Install SAP build process automation desktop agent for macOS](/t5/technology-q-a/install-sap-build-process-automation-desktop-agent-for-macos/qaq-p/14193005)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  2025 Aug 26

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd...