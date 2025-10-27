---
title: AWS EC2 OS patching automation for SAP Landscape
url: https://blogs.sap.com/2022/10/15/aws-ec2-os-patching-automation-for-sap-landscape/
source: SAP Blogs
date: 2022-10-16
fetch_date: 2025-10-03T20:02:06.263785
---

# AWS EC2 OS patching automation for SAP Landscape

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* AWS EC2 OS patching automation for SAP Landscape

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/158992&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [AWS EC2 OS patching automation for SAP Landscape](/t5/technology-blog-posts-by-members/aws-ec2-os-patching-automation-for-sap-landscape/ba-p/13543664)

![former_member227646](https://avatars.profile.sap.com/former_member_small.jpeg "former_member227646")

[former\_member227646](https://community.sap.com/t5/user/viewprofilepage/user-id/227646)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=158992)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/158992)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13543664)

‎2022 Oct 15
5:02 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/158992/tab/all-users "Click here to see who gave kudos to this post.")

2,860

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (1)

For SAP Landscape hosted in cloud Infrastructure, keeping Linux patching up to date is a very key requirement to address security hardening, vulnerability assessment and for other mandatory compliance requirement on a regular basis. Applying Linux patching for a large SAP Landscape is a very time-consuming efforts, as it does require a clean stop and start of all SAP applications in the landscape during this exercise.

This document particularly describes the procedure that how OS patching can be fully automated using AWS System Manager for a SAP landscape hosted on AWS EC2 running on Redhat Linux with multiple SAP applications running on HANA DB.

![](/legacyfs/online/storage/blog_attachments/2022/10/Patching-steps.png)

AWS System Manager is an easy and sophisticated tool to achieve such automation.

<https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html>

## Pre-requisite

1. To perform the OS patching for EC2 using AWS SSM document ‘AWS-RunPatchBaseline’, need to define a patch baseline as per your patching classification and associate the baseline as Default with all targets EC2 instances using Patch groups.

Please refer the AWS document <https://docs.aws.amazon.com/systems-manager/latest/userguide/about-patch-baselines.html> for more detail.

![](/legacyfs/online/storage/blog_attachments/2022/10/Patch-Baseline-1.png)

Patch baseline and associated Patch Groups

2. Define necessary tagging for all EC2 instances for stop and start automation using SSM. I defined my custom SSM document for SAP Start, Stop by using reference defined in this blog, to cover all ABAP, JAVA, Dual Stack and other non-netweaver based systems like BODS, OpenText etc.

[https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-...](https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/)

## AWS SSM Document

To achieve the full patching automation, AWS SSM document is created with following parameters.

1. AutomationAssumeRole : Required to perform action on EC2 instances by SSM Automation.

2. PatchGroup : Value of EC2 tag ‘Patch Group’ to target EC2 instances for patching.

More parameters can be introduced as per overall design approach and requirements.

![](/legacyfs/online/storage/blog_attachments/2022/10/SSM-parameter.png)

Parameter for Patching SSM Automation

**Step 1**: Query all EC2 instances for the given Patch Group using EC2 DescribeInstances API. This output is not being used in subsequent steps, but still used to validate all EC2 instances in given Patch Group for troubleshoot purpose.

![](/legacyfs/online/storage/blog_attachments/2022/10/Step-1.png)

Step 1

StepName.OutputName work as a variable for subsequent automation steps. e.g  {{ QUERY\_INSTANCES\_PATCHGROUP.PatchInstances }} is used for EC2 InstanceId as string list.

**Step 2**: Query all EC2 instances for the given Patch Group that are in ‘Stopped’ status. This is to put all such EC2 instances back in status ‘Stopped’ after patching. Many unused or on-demand purpose instances can be in ‘Stopped’ status, but good to keep them patch as per patching baseline. This is very common for Non-Prod systems in cloud hosting.

![](/legacyfs/online/storage/blog_attachments/2022/10/Step-2-5.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Step-2a.png)

Step 2

This is achieved using the AWS SSM action ‘aws:executeScript’ by writing a small Python code to collect the EC2 instances as string list and Number of Stopped EC2 Instances, to use for further decision steps.

**Step 3**: Query all EC2 instances with status ‘Running’ for the given Patch Group using EC2 DescribeInstances API.

![](/legacyfs/online/storage/blog_attachments/2022/10/Step-3-4.png)

Step 3

**Step 4**: Query all SAP SID for the EC2 instances with status ‘Running’. List of SID is required to call SAP Start/Stop AWS SSM Automation document, as SAP Start/Stop SSM document are defined based on SID as input parameter.

This is achieved using the AWS SSM action ‘aws:executeScript’ by writing a small Python code to collect the SID string list array.

![](/legacyfs/online/storage/blog_attachments/2022/10/Step-4a.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Step-4b.png)

Step 4

**Step 5**: Use action ‘aws:branch’ to check if there are any SAP applications that should be stopped before patching.

![](/legacyfs/online/storage/blog_attachments/2022/10/Step-5-1.png)

Step 5

**Step 6**: In case, there are running SAP applications, automation execution will jump to this step. In this step, another custom SSM automation is called using SSM action ‘aws:executeAutomation’, to stop all SAP applications in parallel. In the ‘DocumetName’ input, provide the full arn name for the SSM document used to stop the applications.

![](/legacyfs/online/storage/blog_attachments/2022/10/Step-6.png)

Step 6

**Step 7**: Branch Step to check if any ‘Stopped’ instances should be bring to status ‘Running’ to apply patch baseline.

![](/legacyfs/online/storage/blog_attachments/2022/10/Step-7-2.png)

Step 7

**Step 8**: In this step, Start all EC2 instances in given Patch Group that are in 'stopped' status to 'running' for Patching.

![](/legacyfs/online/storage/blog_attachments/2022/10/Step-8.png)

Step 8

**Step 9**: In this step, execute action  ‘aws:runCommand’ by calling AWS owned document ‘AWS-RunPatchBaseline’ by specifying Targets based on given Patch Group input parameter. This will initiate patching for all EC2 instances in parallel with tag key ‘Patch Group’ value as input parameter.

![](/legacyfs/online/storage/blog_attachments/2022/10/Step-9a.png)

below is an edit mode to showcase inputs for APPLY\_PATCH step.

![](/legacyfs/online/storage/blog_attachments/2022/10/Step-9b.png)

Step 9

**Step 10**: Branch Step to check if...