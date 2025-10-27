---
title: Azure CloudQuarry: Searching for secrets in Public VM Images
url: https://securitycafe.ro/2024/11/19/azure-cloudquarry-searching-for-secrets-in-public-vm-images/
source: Security Café
date: 2024-11-20
fetch_date: 2025-10-06T19:18:03.565014
---

# Azure CloudQuarry: Searching for secrets in Public VM Images

[Skip to content](#content)

[Security Café](https://securitycafe.ro/)

Security Research and Services

* [Things we do on a daily basis](https://securitycafe.ro/security-services-for-business/)
  + [Red Team (DORA/TIBER) exercises](https://securitycafe.ro/security-services-for-business/dora-tiber-exercises/)
  + [Web Application Penetration Testing](https://securitycafe.ro/security-services-for-business/web-application-penetration-testing/)
  + [Mobile Application Penetration Testing](https://securitycafe.ro/security-services-for-business/mobile-application-penetration-testing/)
  + [Infrastructure Penetration Testing](https://securitycafe.ro/security-services-for-business/infrastructure-penetration-testing/)
  + [Vulnerability Assessment](https://securitycafe.ro/security-services-for-business/vulnerability-assessment/)
* [CVEs, Talks and Tools](https://securitycafe.ro/cves-talks-and-tools/)
* [Contact](https://securitycafe.ro/contact/)
* [About](https://securitycafe.ro/about/)

[![](https://securitycafe.ro/wp-content/uploads/2015/01/cropped-cropped-coffee-banner-2-4.jpg)](https://securitycafe.ro/)

![](https://securitycafe.ro/wp-content/uploads/2024/10/featimage1.jpg?w=840)

# Azure CloudQuarry: Searching for secrets in Public VM Images

[November 19, 2024](https://securitycafe.ro/2024/11/19/azure-cloudquarry-searching-for-secrets-in-public-vm-images/ "12:12 pm") [Stefan Tita](https://securitycafe.ro/author/stitakpmgcom/ "View all posts by Stefan Tita") [Azure](https://securitycafe.ro/category/cloud-security/azure/), [Cloud Security](https://securitycafe.ro/category/cloud-security/), [Research](https://securitycafe.ro/category/research/) [Leave a comment](https://securitycafe.ro/2024/11/19/azure-cloudquarry-searching-for-secrets-in-public-vm-images/#respond)

After the initial investigation entitled “[AWS CloudQuarry: Digging for secrets in Public AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/)” was finalized, we continued with the same idea on Azure in order to search for hidden and forgotten secrets in **Azure VM Images**.

I will try to keep this article short and present how we managed to collect approximately 120GB of data by scanning 15.000 images. This was achieved by using a simple and efficient tool we created called “**Azure Image Scanner**” or **AIS** ([GitHub Link](https://github.com/phenix-sec/azure_image_scanner)).

Article author: Stefan Tita (<https://www.linkedin.com/in/stefan-tita-55a349a3/>)

Shoutout to Eduard and Matei for the original idea on AWS.

## Table of Contents

1. [Collecting Public Azure Images](https://securitycafe.ro/2024/11/19/azure-cloudquarry-searching-for-secrets-in-public-vm-images/#1-collecting-public-azure-images)
2. [Azure Image Scanner (AIS)](https://securitycafe.ro/2024/11/19/azure-cloudquarry-searching-for-secrets-in-public-vm-images/#2-azure-image-scanner-ais)
   1. [Running AIS](https://securitycafe.ro/2024/11/19/azure-cloudquarry-searching-for-secrets-in-public-vm-images/#2-1-running-ais)
   2. [AIS functionalities](https://securitycafe.ro/2024/11/19/azure-cloudquarry-searching-for-secrets-in-public-vm-images/#2-2-ais-functionalities)
3. [Results](https://securitycafe.ro/2024/11/19/azure-cloudquarry-searching-for-secrets-in-public-vm-images/#3-results)
4. [Wrap-up](https://securitycafe.ro/2024/11/19/azure-cloudquarry-searching-for-secrets-in-public-vm-images/#4-wrap-up)

## 1. Collecting Public Azure Images

When you want to deploy a new VM in Azure you have the option to choose a public image template from **Azure Marketplace** or **Community Images**.

**Community images**, as the name suggests, can be shared by anyone and can have an unknown and unverified source, that is why you should probably avoid using such images unless you know and trust the source. At the time of conducting this investigation there were a total of approximately 6.000 community images, but this number keeps increasing so you can find the updated list at the following link:

* <https://portal.azure.com/#browse/Microsoft.Compute%2Flocations%2FcommunityGalleries%2Fimages>

Generating the community images file is easy as the Azure Portal allows “Export to CSV” and the exported file can be used with *Azure Image Scanner*.

**Azure Marketplace** images on the other hand come from validated providers and can be used for commercial purposes, but you should still practice some care and avoid using expensive images or unknown providers when deploying VMs.

![](https://techproject.ro/wp-content/uploads/2024/10/image.png)

Deploying VM using expensive image (expensive is an understatement…)

At the time of the investigation there were approximately 52.000 Marketplace Images, but this number has also been increasing over time. The following command generates the updated list of Marketplace Images ready to be used when running the *AIS* tool.

```
#export marketplace images to file (removes multiple spaces and table headers)
az vm image list --all -o table | sed 's/  */ /g' | tail -n +3 > images_marketplace.txt
```

Once we exported the images we proceeded to exclude images from well known providers and decided to scan a total of 15.000 images from lesser known providers (10.000 Marketplace Images and 5.000 Community Images).

## 2. Azure Image Scanner (AIS)

Deciding on the best approach to scan 15.000 images was not difficult because Azure allows creating Managed Disks from images and attaching them to virtual machines. This can be observed in the following image:

![](https://techproject.ro/wp-content/uploads/2024/10/diagram2.png)

Azure Image Scanner workflow

So we created [Azure Image Scanner](https://github.com/phenix-sec/azure_image_scanner) to automate the above process and scan Managed Disks to extract potential secrets.

The initial downside was that each of these commands (create, attach, detach, delete Managed Disk) takes some time to complete, and waiting for each command is very inefficient. In order to solve this issue AIS **executes all steps in advance and in the background**. Then each step checks that prerequisites are met before executing. By doing this it saves precious time on each image scanned (at least 30 seconds).

### 2.1. Running AIS

Initiating a scan with AIS is a rather simple process that includes the following steps.

1. Deploy a Debian/Ubuntu based VM in Azure. The AIS script should run on any size VM that is Debian/Ubuntu based.

2. Copy the AIS script along with the exported images file to any location on the VM.

3. Edit the following variables inside the AIS script. You will need to create an Azure Storage Account container and a SAS token, so that AIS can store the extracted data.

```
#MUST CHANGE
imagesfile="images.txt"
containerurl=""   #Storage account container for data storage
sastoken=""   #Required to access the container
```

4. Using the root user, install Azure CLI on the VM and log into your Azure account.

```
sudo su
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az login
```

5. Run Azure Image Scanner as root. (Optional: use “screen” command to run the script in a background session)

```
sudo su   #root access required to execute elevated commands
screen -L   #run screen session and log data to file
bash AIS.sh
```

### 2.2. AIS functionalities

Let us go over some of the functionalities and constraints of the tool:

* First of all, the process for deploying and attaching Managed Disks is different between marketplace and community images. That is why there are two different AIS scripts.

* A Managed Disk created from a community image can only be used and attached to a VM within the same region as the community image. This Azure restriction means that you need to deploy a VM in each region to scan all community images. This restriction only applies to community images, it does not apply to marketplace images.

* It only scans volumes that are bigger than 1.8 GB and smaller than 260 GB in order to avoid wasting time and costs.
...