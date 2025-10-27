---
title: GCP Automation – Single click VM deployment with SAP HANA DB instance installation
url: https://blogs.sap.com/2023/02/15/gcp-automation-single-click-vm-deployment-with-sap-hana-db-instance-installation/
source: SAP Blogs
date: 2023-02-16
fetch_date: 2025-10-04T06:45:36.204373
---

# GCP Automation – Single click VM deployment with SAP HANA DB instance installation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* GCP Automation - Single click VM deployment with S...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163547&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [GCP Automation - Single click VM deployment with SAP HANA DB instance installation](/t5/technology-blog-posts-by-members/gcp-automation-single-click-vm-deployment-with-sap-hana-db-instance/ba-p/13570342)

![anilnarang](https://avatars.profile.sap.com/b/b/idbb162c615f4c797cfc5a30a50134a3ce375ff98277cbfcf92763b6f57fe93296_small.jpeg "anilnarang")

[anilnarang](https://community.sap.com/t5/user/viewprofilepage/user-id/603741)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163547)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163547)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570342)

‎2023 Feb 15
11:45 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163547/tab/all-users "Click here to see who gave kudos to this post.")

2,931

* SAP Managed Tags
* [Digital Technologies](https://community.sap.com/t5/c-khhcw49343/Digital%2520Technologies/pd-p/33d804ef-26b2-4f01-b858-ddef6871cb3b)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [Cloud Operations](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Operations/pd-p/1aa2b5a9-42a9-4f0b-974f-aa4dec11e19f)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [Cloud Operations

  Topic](/t5/c-khhcw49343/Cloud%2BOperations/pd-p/1aa2b5a9-42a9-4f0b-974f-aa4dec11e19f)
* [Digital Technologies

  Topic](/t5/c-khhcw49343/Digital%2BTechnologies/pd-p/33d804ef-26b2-4f01-b858-ddef6871cb3b)

View products (3)

**Abstract**

This paper focuses on listing down the technical details and sequence of steps which are needed to accomplish the automation of Google Cloud Virtual Machine deployment along with SAP HANA DB instance installation using Terraform and Ansible scripts. Intention is not to teach about terraform or/and ansible scripting or SAP HANA but sharing my hands-on experience with assumption that reader is having basic knowledge of terraform/ansible and SAP Basis. One can also read it as an extension of my earlier blog **Automation of SAP Applications Deployment in Google Cloud** <https://blogs.sap.com/2021/09/01/automation-of-sap-applications-deployment-in-google-cloud/>

Conventional way of having a SAP HANA Database instance installed is to deploy the virtual machine based on worked out sizing using Google Console ot Terraform/Google Deployment Manager as IaC tool with identified underlying Operating System (SLES/RHEL), create the mount points at OS layer and map the storage needed for respective HANA DB mount points, download the SAP HANA media, uncompress it and set the ownership & permissions of the installation files and at the end, kick off the interactive HANA installation with intermittent manual inputs as & when it is prompted. Using both tools i.e.  Terraform and Ansible, with few initial hits & trials, we were able to successfully create a single click script to accomplish this task in one go. We tested this automation script with both operating systems - SUSE Linux Enterprise Server - SLES and Red Hat Enterprise Linux - RHEL which are certified operating systems for SAP HANA DB on Google Cloud  <https://cloud.google.com/solutions/sap/docs/sap-hana-os-support>.

**Automation tasks**

We split the task into four major steps as shown below. In the first two steps, we  are capturing all the mandatory inputs which are needed for creation of VM and installation of SAP HANA DB instance. Apparently these inputs/values, passed to script during execution for defined variables, are stored in a template which is accepted by Terraform/Ansible runtime environment. Following steps take care of putting the automation logic together and then deployment of script.

![](/legacyfs/online/storage/blog_attachments/2023/02/Tech_Blog_Image1.png)
**Preparation**

**Step 1** - As the very first step, we decided upon input parameters  for VM creation like machine type, hostname, operating system image, disks, network, region & zone and other mandatory details needed to spin up a VM in GCP. Recorded these parameter values in an input parameter file. Sample screen is given below:

```
#-------INPUT VARIABLES FOR TERRAFORM RESOURCE PROVISIONING----------------

#Instance#

instance_name  =sap-hana-vm

project        =sap-automation-112233

vm_network     =default

zone           =us-central1-a

boot_disk_size =20

image          =rhel-sap-cloud/rhel-8-4-sap-ha

machine_type   =n1-highmem-32

device_name    =sap-hana-vm-OS

disktype       =pd-balanced

#address#

address_name =hana-ip

address_type =EXTERNAL

region       =us-central1

network_tier =STANDARD
```

**Step 2** - Value for Input parameters  for HANA DB installation like DB ID, Instance number, system usage - production/test/development, SYSTEM user password for SYSTEMDB and Tenant DB etc.. are captured in the same input.patameters file in the project source repository. Sample given below:

```
#Enter SAP HANA System ID: var6

sap_hana_system_id =HDB

#Enter Instance Number [00]: var7

sap_hana_instance_number =00

#Index | System Usage | Description

#-----------------------------------------------------------------------------

 #1     | production   | System is used in a production environment

 #2     | test         | System is used for testing, not production

 #3     | development  | System is used for development, not production

 #4     | custom       | System usage is neither production, test nor development

#Select System Usage / Enter Index [4]: var9

sap_hana_system_usage =3

#Enter System Administrator (sidadm) Password: var17

system_administrator_password =<passwd>

#Confirm System Administrator (sidadm) Password: var18

confirm_system_adm_password =<passwd>

#Enter System Database User (SYSTEM) Password: var19

system_database_user_password =<passwd>

#Confirm System Database User (SYSTEM) Password: var20

confirm_system_db_user_password =<passwd>
```

Apart from capturing input values in input parameter file, following tasks are also being performed during preparation :

> Calculating the storage needed against each HANA mount point /hana/data, /hana/logs, /hana/shared, /usr/sap

> Downloading the SAP HANA DB server installation media form SAP portal and keep it in the Google storage bucket

**Step 3** **-** **Scripting**

Terraform script (.tf) is being used for deployment of Virtual Machine (VM) and Ansible script (.yaml) is utilized for SAP HANA installation. Apart from scripts, few supporting files are also being created like parameter input file, service account key file etc..

All the logic is built here in this step:

* VM creation commands are put in the terraform script(.tf) which is being called in main.sh

* HANA DB installation commands are being written in a bash script which in turn is being called in ansible(.yaml) script

* Weaving of...