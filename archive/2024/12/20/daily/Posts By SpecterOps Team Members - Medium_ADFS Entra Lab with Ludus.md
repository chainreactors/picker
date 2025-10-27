---
title: ADFS Entra Lab with Ludus
url: https://posts.specterops.io/adfs-entra-lab-with-ludus-9bffbc51673f?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-12-20
fetch_date: 2025-10-06T19:42:28.649583
---

# ADFS Entra Lab with Ludus

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9bffbc51673f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fadfs-entra-lab-with-ludus-9bffbc51673f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fadfs-entra-lab-with-ludus-9bffbc51673f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-9bffbc51673f---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-9bffbc51673f---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# ADFS Entra Lab with Ludus

[![Beyviel David](https://miro.medium.com/v2/resize:fill:64:64/1*n1_RuvzUoXprq_32Xui9AA@2x.jpeg)](https://medium.com/%40bagelByt3s?source=post_page---byline--9bffbc51673f---------------------------------------)

[Beyviel David](https://medium.com/%40bagelByt3s?source=post_page---byline--9bffbc51673f---------------------------------------)

6 min read

·

Dec 19, 2024

--

1

Listen

Share

## TLDR

This blog walks you through setting up an ADFS lab using Ludus and/or a flexible hybrid cloud environment for testing.

The associated GitHub repo is [here](https://github.com/bagelByt3s/ludus_adfs).

## Introduction

I was recently on an engagement where the customer was using Active Directory Federated Services (ADFS). ADFS is an Identity Provider (idP) by Microsoft that allows third-party applications and internal applications to delegate authentication to Active Directory.

I see ADFS all the time during my engagements, and although I knew about this technology in theory, I wanted to gain more experience with it. How fun would it be to spin up an ADFS lab, learn how it works under the hood, practice attacks, and analyze possible detection’s? The possibilities are endless with a home lab!

I’m a heavy Ludus user, and I use [Zach Stein](https://www.linkedin.com/in/zacharydstein?trk=contact-info)’s [SCCM Ludus range](https://github.com/Synzack/ludus_sccm) all the time, so going with Ludus was a no brainer. [Erik Hunstad](https://www.linkedin.com/in/erik-hunstad?trk=contact-info) developed Ludus which simplifies lab deployments, making it a powerful tool for managing virtual environments. If you’re not familiar with it yet, be sure to check out the [Ludus documentation here](https://docs.ludus.cloud/).

## Entra Challenge

While I was building the lab, I wanted to see if it would be possible to automate the process for integrating Microsoft 365 apps with ADFS for authentication. To do this on a domain-joined system, I would need to run the **AzureAdConnect.msi** installer, which replicates objects from an on-prem Active Directory environment to Entra ID and when configured can also write changes from Entra ID back to on-prem AD. Automating this became more difficult than I anticipated.

Instead, I’ve created an Ansible role called “entra\_prep”, which prepares a dedicated server to connect your on-prem AD environment to Entra ID. You can find more details in the “Roles” section on how this works. Keep in mind that you’ll need your own Entra tenant to move forward. Once that’s set up, the only other step is running the AzureADConnect installer and following the wizard. Everything else you need for a hybrid cloud lab is ready to go.

What makes this lab super flexible is that it is essentially “choose your own adventure”. You have the freedom to decide exactly how you would like to structure your lab.

* Don’t want to use ADFS, but just want a hybrid cloud lab? This setup works for that!
* Want to experiment with ADFS locally and not use the cloud? Perfect!
* Desire to understand how password hash syncing works under the hood? We have a winner!
* Interested in playing with setting up Office Apps with ADFS and researching potential weaknesses? This works for that as well!
* Want to test how a Golden SAML attack works and pivot from on-prem AD to the cloud? This lab will help you get there!

You get the picture, there’s a lot you can do with this home lab. I do believe this lab strikes a good balance between automation and manual setup that lets you set up how you want the cloud environment to be and still save you some time.

## Roles

Ludus uses Ansible roles to manage the software and configurations in the lab environment. The following are roles that I created for this lab.

### install\_adfs

This role installs the ADFS role on a server, creates an ADFS service account, and requests a certificate that ADFS uses.

### import\_root\_cert

This role requests the root certificate from the certificate authority (CA) and imports it into the local machine security store. This is necessary to remove the following certificate error which is caused because the lab machine does not trust the CA that signed the cert being used by ADFS.

Press enter or click to view image in full size

![]()

## entra\_prep

This role adds an alternative user principal name (UPN) to the local domain which is required before connecting an on-prem domain to Entra ID. This role also installs TLS 1.2 which **AzureAdConnect.msi** requires. Next, this role creates a service account which is used for syncing AD objects from on-prem AD to Entra ID. There are some settings that allow Entra ID to replicate changes to on-prem AD such as group writeback, device writeback, or password writeback. If any of these settings are configured, then some changes in Entra ID like group creation, or password resets will be replicated from Entra ID to on-prem AD. Finally, this role downloads the AzureAdConnect.msi installer to the server that will be used for replication between on-prem AD and Entra ID.

## Installation

I won’t be covering the installation of Ludus as this is already heavily documented in the [Ludus docs](https://docs.ludus.cloud/docs/intro). Installation of the ADFS range is simple, you just need to clone the ludas\_adfs repo.

```
git clone https://github.com/bagelByt3s/ludus_adfs /opt/ludus_adfs
```

Then you add the Ansible collection to Ludus.

```
ludus ansible collection add /opt/ludus_adfs
```

Review the sample range configuration file, updating fields to suit your desired environment:

**ADFS-Range.yml**

```
ludus:
  - vm_name: "DC01-WinServer2022"
    hostname: "DC01"
    template: win2022-server-x64-template
    vlan: 10
    ip_last_octet: 10
    ram_gb: 8
    cpus: 4
    windows:
      sysprep: true
    domain:
      fqdn: ludus.nuketown
      role: primary-dc
    roles:
      - bagelByt3s.ludus_adfs.install_adcs

  - vm_name: "ADFS-WinServer2022"
    hostname: "ADFS"
    template: win2022-server-x64-template
    vlan: 10
    ip_last_octet: 11
    ram_gb: 8
    ram_min_gb: 2
    cpus: 4
    windows:
      sysprep: true
    domain:
      fqdn: ludus.nuketown
   ...