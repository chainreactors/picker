---
title: Automating SAP HANA Installation in Minutes (AWS) – Part 2
url: https://blogs.sap.com/2022/11/18/automating-sap-hana-installation-in-minutes-aws-part-2/
source: SAP Blogs
date: 2022-11-19
fetch_date: 2025-10-03T23:13:16.174609
---

# Automating SAP HANA Installation in Minutes (AWS) – Part 2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Automating SAP HANA Installation in Minutes (AWS) ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160065&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Automating SAP HANA Installation in Minutes (AWS) - Part 2](/t5/technology-blog-posts-by-members/automating-sap-hana-installation-in-minutes-aws-part-2/ba-p/13550015)

![ahmedyasin](https://avatars.profile.sap.com/5/9/id59772a056641f864351f9eb1c4930b177b2879b9ba0a0509528179c8672cf7b6_small.jpeg "ahmedyasin")

[ahmedyasin](https://community.sap.com/t5/user/viewprofilepage/user-id/627554)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160065)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160065)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550015)

‎2022 Nov 18
5:11 PM

0
Kudos

1,130

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (1)

# Introduction:

This  blog is part 2 of 2 in this series  of  Automating SAP Installation in minutes, refer the part 1 of this blog for the prerequisite to get started.

(<https://blogs.sap.com/?p=1649584?source=email-global-notification-mod>)

This article provides detailed steps and commands required  to get an EC2 instance provisioned, with the 'XFS' file system built automatically  with a successfully SAP HANA DB installation in AWS.

**Walkthrough:**

**Step 1:** Create a “main.tf” and init-script.sh with necessary attributes as mentioned in the part 1 of this blog (refer the links above), got to AWS-CLI with terraform configuration pointing to the selected region with your AWS access keys and initiate the terrfarom with the below command.

Command: **terraform init**

###### ![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img6-2.jpg)

###### Figure 1: Initializing terraform

**Step 2:** We are validating the configuration for a final time for any errors before we can confirm the resource creation in the selected AWS regions.

Command: t**erraform validate** & **terraform apply**

###### ![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img7.jpg)

###### Figure 2: Validating and applying the configuration

**Step 3:** The timestamp has been captured before confirming the resource creation and at the
AWS CLI typing “yes” @ localtime 02:06:36 pm aka(14:06:36)

###### ![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img8.jpg)Figure 3: Confirming the creation and capturing local time

**Step 4:** Verify the availability of created server through AWS console and login into the host.

###### ![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img9.jpg)Figure 4: AWS Console

**Step 5:**  Verifying the file system & uptime of the EC2 host

###### ![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img11.jpg)

###### ![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img10.jpg) Figure 5: EC2 instance File system & uptime

**Step 6:** Verifying the time stamp of HANA DB installation (hdbinst.log) and the time captured includes the EC2 installation, File System Setup and HANA DB installation.

HDB Installation Start time: 02:06:36 pm aka (14:06:36)

HDB Installation End Time: 02:14:25 pm aka (14:14:25)

![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img12.jpg)

###### Figure 6: HANA DB Installation log

**Step 7:** Finally connect to the HANA DB instance through HANA studio by providing the public IP.

###### ![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img13.jpg)

###### Figure 7: HANA Studio

###### ![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-img14.jpg)

###### Figure 8: HDB Info

**References:**

#### **SAP on AWS immersion Day**

<https://catalog.us-east-1.prod.workshops.aws/workshops/754ba343-2704-404a-8abe-be7b21c4d9d5/en-US>

#### **SAP HANA Academy**

<https://blogs.sap.com/2018/02/08/sap-hana-installation-automation-by-the-sap-hana-academy/>

#### **Terraform Tutorials**

<https://developer.hashicorp.com/terraform/tutorials>

#### **Feedback:**

Kindly share your feedback and ways to improve the scripts.

* [automate](/t5/tag/automate/tg-p/board-id/technology-blog-members)
* [aws](/t5/tag/aws/tg-p/board-id/technology-blog-members)
* [hana db](/t5/tag/hana%20db/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fautomating-sap-hana-installation-in-minutes-aws-part-2%2Fba-p%2F13550015%23comment-on-this)

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
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 4 |
| [![Sandra_Ros...