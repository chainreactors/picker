---
title: SAP HANA Hardware Directory – Overview & FAQ
url: https://blogs.sap.com/2022/12/08/sap-hana-hardware-directory-overview-faq/
source: SAP Blogs
date: 2022-12-09
fetch_date: 2025-10-04T00:59:48.864203
---

# SAP HANA Hardware Directory – Overview & FAQ

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Additional Blog Posts by SAP](/t5/additional-blog-posts-by-sap/bg-p/additional-blog-sap)
* SAP HANA Hardware Directory - Overview & FAQ

Additional Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/additional-blog-sap/article-id/52835&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP HANA Hardware Directory - Overview & FAQ](/t5/additional-blog-posts-by-sap/sap-hana-hardware-directory-overview-faq/ba-p/13568505)

![gursimransingh63](https://avatars.profile.sap.com/7/c/id7c435b16cf5811881d9b1acb03ff0a27cffc6428b89ab8fe2babebbf4d3bd34d_small.jpeg "gursimransingh63")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[gursimransingh63](https://community.sap.com/t5/user/viewprofilepage/user-id/832208)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=additional-blog-sap&message.id=52835)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/additional-blog-sap/article-id/52835)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568505)

‎2022 Dec 08
8:47 PM

[8
Kudos](/t5/kudos/messagepage/board-id/additional-blog-sap/message-id/52835/tab/all-users "Click here to see who gave kudos to this post.")

7,754

* SAP Managed Tags
* [Integration and Certification Center](https://community.sap.com/t5/c-khhcw49343/Integration%2520and%2520Certification%2520Center/pd-p/539667611584404255845040674498708)

* [Integration and Certification Center

  Topic](/t5/c-khhcw49343/Integration%2Band%2BCertification%2BCenter/pd-p/539667611584404255845040674498708)

View products (1)

Technology has changed rapidly over the last decade and so is [SAP HANA Hardware directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=v:deCertified) Its latest revamp happened in Q4, 2020.

As I hear lot of conversations about this topic, with this blog I would like to give an overview of HANA Hardware directory with few FAQ which might help to answers your queries.

## Overview:

The SAP Hana Hardware directory has a list of all certified and supported SAP HANA Hardware. The list includes Appliances, Enterprise Storage solutions, IaaS Platforms, Hyper-Converged Infrastructure (HCI) Solutions, Supported Intel® systems and Supported Power® systems. The certification confirms the existence of product features in accordance with SAP certification procedures and is valid for a specific time period.

To date, there are total 950+ solutions present in HANA Hardware directory which include both Certified and Supported SAP Hana Hardware. Out of above-mentioned numbers 550+ are certified by SAP.

SAP HANA appliance are like building blocks with all necessary components pre-configured and pre-installed. If you change Appliance configuration it becomes [TDI](https://blogs.sap.com/2015/02/18/sap-hana-tailored-data-center-integration-tdi-overview/). All servers from Appliances and Intel/Power Supported Servers can be used within so called Tailored Data-Center Integration (TDI) Program.

Also, you can get detailed information under 'read more' section of each individual listing in [SAP HANA Hardware directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=v:deCertified)

## FAQ's

1. **Why Can't we see supported Intel Systems even though we have check marked 'Supported Intel Systems'**
   > By default, only certified solutions are visible so you need to clear the filters first and then you will be able to see all the solutions including 'Supported Intel Systems'
   >
   > # ![](/legacyfs/online/storage/blog_attachments/2022/12/Capture1.jpg)
   >
   >
   >
   > Without clearing filters

   > ![](/legacyfs/online/storage/blog_attachments/2022/12/Capture2.jpg)
   >
   >
   >
   > After clearing filters and then select Supported Intel Systems

2. **Appliance solution was certified 3 years ago and is already expired, customer want to know if it will be still supported:**
   > The hardware is required to have a valid SAP HANA Hardware certification at the point of purchase by the customer. Once the validity date of the certification has passed, the hardware will continue to be supported by the Partner until the end of maintenance as indicated by the Partner.

3. **Some Company, which is not SAP Partner, wants to certify an Appliance solution and get it listed in HANA hardware directory.**
   > Prerequires before any hardware certification is to be SAP Global Technology Partner and a business case generating significant new license revenue for SAP with operation of SAP solutions on your planned offering. Again, getting SAP Global Technology Partner is on invitation only by SAP executive sponsor based on a joined cooperation. Certification is by invitation only by SAP HANA council.

4. ****Customer wants to know if any listed HCI solution is certified for SAP Business One****
   > For HCI any workload is allowed also for SAP B1. Individual sizing applies for SAP B1.
   >
   > See SAP Notes:
   > [2020657](https://launchpad.support.sap.com/#/notes/2020657) - SAP Business One, version for SAP HANA virtualized
   >
   > [2718982](https://launchpad.support.sap.com/#/notes/2718982) - SAP HANA on VMware vSphere and vSAN) for SAP HANA HCI support on VMware
   >
   > [2836729](https://launchpad.support.sap.com/#/notes/2836729) - Installing SAP Business One for SAP HANA in a virtualized environment using Nutanix HCI

5. ****Some Company, which is not SAP Partner, wants to certify an Enterprise Storage Solution and get it listed.****
   > Enterprise Storage solution needs to be a building block that acts as a SAN or NAS solution to be accessed by the SAP HANA compute nodes. Also, company overview has to be provided with a proper business case how it will help SAP business and if there are any customer references where there is such a request. With this having HANA skill set is also a crucial requirement.
   >
   > For more details contact hwc@sap.com.

6. **Scenario:** Partner's last SAP HANA Appliance certified OS for SUSE is SLES 15.2 and is not planning to certify anymore a new SUSE service pack, but there are Customers which would like to upgrade to SLES 15.3 or SLES 15.4 because these OSs are SAP validated (between SAP and SUSE) and the server model it is still hardware supported by Partner. **In such a scenario will SAP support the customer or not at all.**
   > SAP will treat it as TDI (assuming it follow the TDI rules)

##

## Final Words

Before asking any questions, please try to play with the filters of the directory and go through the read-more section as most of the information you may ask is already there. By the time you are reading this blog probably there are already 1000+ solutions listed. Also, as [SAP HANA Hardware directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=v:deCertified) is evolving, I will try to update this blog in the future. Will also add more FAQ as they pop-up.

If the blog is helping you in anyway then please don’t forget to like the post and please comment in case of any confusions.

2 Comments

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP IQ to SAP HANA Cloud, Data Lake Migration Overview](/t5...