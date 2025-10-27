---
title: Automation with the btp command-line interface: logging in with passcodes
url: https://blogs.sap.com/2022/12/09/automation-with-the-btp-command-line-interface-logging-in-with-passcodes/
source: SAP Blogs
date: 2022-12-10
fetch_date: 2025-10-04T01:05:55.253251
---

# Automation with the btp command-line interface: logging in with passcodes

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Automation with the btp and cf command-line interf...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/165105&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Automation with the btp and cf command-line interfaces: logging in with passcodes](/t5/technology-blog-posts-by-sap/automation-with-the-btp-and-cf-command-line-interfaces-logging-in-with/ba-p/13571444)

![tom_slee](https://avatars.profile.sap.com/6/f/id6fbfb39fad6d365c74068937133729469945b0bcc4f568f05403325ede856bfb_small.jpeg "tom_slee")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[tom\_slee](https://community.sap.com/t5/user/viewprofilepage/user-id/160000)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=165105)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/165105)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571444)

‎2022 Dec 09
8:39 PM

[20
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/165105/tab/all-users "Click here to see who gave kudos to this post.")

5,956

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (2)

For SAP Business Technology Platform (BTP), the btp command-line interface (CLI) is the alternative to the SAP BTP Cockpit for all users who like to work in a terminal or want to automate operations using scripts. With the btp CLI you can execute both account management operations and service management operations. The [btp CLI documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/7c6df2db6332419ea7a862191525377c.html) provides details and there are introductory tutorials available as well, like [Get Started with the SAP BTP CLI](https://developers.sap.com/tutorials/cp-sapcp-getstarted.html). The btp CLI is applicable to SAP BTP accounts using Feature Set B, which is now (December 2022) almost all SAP BTP accounts.

With the availability of [SAP HANA Cloud as a multi-environment service](https://blogs.sap.com/2022/09/21/sap-hana-cloud-goes-multi-environment-part-1-feature-overview/), the btp CLI becomes the main CLI for HANA Cloud administration, as well as for other SAP BTP services, and HANA Cloud-specific documentation is provided [here](https://help.sap.com/docs/HANA_CLOUD/9ae9104a46f74a6583ce5182e7fb20cb/06ccc32d4a824f2c92a87c657d6dcde3.html).

Despite these resources, there is one gap I found difficult to address: hence this blog post. How do you run the btp CLI securely in an automation script, when the btp login command requires a password, and (if two-factor authentication is enabled) a time-sensitive code to be entered manually? The approach here relies on [SAP Identity Authentication Service (IAS)](https://help.sap.com/docs/IDENTITY_AUTHENTICATION/6d6d63354d1242d185ab4830fc04feb1/d17a116432d24470930ebea41977a888.html). IAS is the recommended solution for identity management, and for connecting SAP BTP to external identity providers.

(The same approach applies to the Cloud Foundry cf CLI. Most of the steps are the same, and the cf login command is listed where it is relevant below)

The post goes through the process step by step, but here's an overview:

1. Set up trust between your SAP BTP global account and your IAS tenant.

2. Configure your IAS tenant to enable certificate generation and authentication

3. Define a technical user in IAS and generate a certificate. The certificate is a PK12 bundle that contains both a private key and a public key, and you need to keep it secure in a location where the btp client can have access to it.

4. Grant the technical user the role collections it needs in your SAP BTP account.

5. To login from an automation script, first use the curl command-line utility together with your certificate to obtain a passcode, which is good only for one login attempt and for a short time (five minutes)

6. With the btp CLI, login, supplying the passcode in the password field.

As the passcode is good only for one login, it does not introduce security problems to supply it when connecting. The curl command does reference the PK12 file, but it does not send the private key over the network.

## Set up IAS

This blog post does not deal with obtaining SAP IAS. If you are a customer, you buy IAS and get an e-mail containing a link to the landing page of the administration console for Identity Authentication. You can confirm the registration of your first administrator user. The IAS administration console has a URL of the form

<https://<tenant> ID>.accounts.ondemand.com/admin

The tenant ID may be a user-friendly name: for example, for our HANA Cloud product management accounts, we might have a tenant <https://hanapm.accounts.ondemand.com>.

From here on, we assume you are (or can talk to) an IAS administrator with rights to add users and change IAS settings. See [this documentation page](https://help.sap.com/docs/IDENTITY_AUTHENTICATION/6d6d63354d1242d185ab4830fc04feb1/86ee37423f8945a1898faff1e6308756.html) for how to assign authorizations in IAS.

## Configure IAS to enable certificate generation and authentication

The documentation for this step is [here](https://help.sap.com/docs/IDENTITY_AUTHENTICATION/6d6d63354d1242d185ab4830fc04feb1/1268ff5987d8484698f77cd24c91efa5.html?q=certificate%20generation). From the IAS administration console, go to *Applications & Resources > Tenant Settings*

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-08_16-30-48.png)

IAS Tenant Administration

Enable certificate authentication for the user type that corresponds to your technical user (probably "employee")

## In BTP Cockpit, establish trust with IAS

To log in with the btp CLI using IAS as the identity provider, you must establish trust with the IAS tenant at the global account level (not just from within an individual subaccount). For instructions on how to do this from the BTP Cockpit, see [the documentation](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/c36898473d704e07a33268c9f9d29515.html).Once you've done this, you'll see a value in the *BTP CLI* column ("hanapm" in the screenshot below). This is the *tenant ID* and you'll need this when logging in with the btp CLI.

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-09_14-28-43.png)

BTP Cockpit (global account)

To carry out operations within a subaccount, you will need to establish trust within the subaccount as well. Again, you do this from the BTP Cockpit by going to the subaccount and then choosing Security > Trust Configu...