---
title: High Availability of SAP Launchpad Service with Amazon Route 53
url: https://blogs.sap.com/2022/11/04/high-availability-of-sap-launchpad-service-with-amazon-route-53/
source: SAP Blogs
date: 2022-11-05
fetch_date: 2025-10-03T21:45:07.161465
---

# High Availability of SAP Launchpad Service with Amazon Route 53

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Route Multi-Region Traffic to SAP Build Work Zone,...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161690&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Route Multi-Region Traffic to SAP Build Work Zone, standard edition, using Amazon Route 53](/t5/technology-blog-posts-by-sap/route-multi-region-traffic-to-sap-build-work-zone-standard-edition-using/ba-p/13561468)

![madankumarp](https://avatars.profile.sap.com/a/0/ida0c008c8745b657b0ddc869e11a3c7a99074a06ab69151ff63dd575ad7e9a70b_small.jpeg "madankumarp")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[madankumarp](https://community.sap.com/t5/user/viewprofilepage/user-id/45029)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161690)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161690)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561468)

‎2022 Nov 04
5:32 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161690/tab/all-users "Click here to see who gave kudos to this post.")

5,126

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Build Work Zone, standard edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Work%2520Zone%252C%2520standard%2520edition/pd-p/73554900100800003081)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Build Work Zone, standard edition

  Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BWork%2BZone%25252C%2Bstandard%2Bedition/pd-p/73554900100800003081)

View products (3)

**The need for Business Continuity**

The requirement for the business continuity of a modern-day tool is implicit and very essential. Nowadays, customers have zero tolerance for downtime. For business-critical applications, a failure, even of the tiniest amount, could have adverse effects. One such service that could be adversely affected by an outage is [SAP Build Work Zone](https://help.sap.com/docs/WZ_STD?locale=en-US), standard edition. The Build Work Zone, standard edition service, being the end users’ central point of entry for all the applications, is expected to be highly available and responsive.

**SAP’s promise**

The SAP Build Work Zone service in SAP Business Technology Platform promises an easy-to-configure, role-based solution to act as a gateway into all applications, by displaying them in different tiles arranged in different groups. The availability of this service is limited by SAP BTP’s limitation of a subaccount to act as a single host located in a single region. This means we need a way to better prepare for and handle failure. So, instead of having a single work zone service in a single SAP BTP subaccount, we can have a clone running in a different subaccount that is hosted in a different region. That leaves us just with the task of redirecting the traffic to the right destination.

**Amazon’s Route 53**

[Route 53](https://aws.amazon.com/route53/) is Amazon’s highly available and scalable Domain name System (DNS) web service featuring easy-to-configure traffic policies and health checks to redirect the traffic to the right target. Route 53 fits our requirements perfectly and can act as the entry point; triage the traffic, and increase the availability of the SAP Build Work Zone service.

**Architecture**

![](/legacyfs/online/storage/blog_attachments/2022/11/haJan20-2.png)

The data flow for this scenario begins with the request from the end user’s domain or the URL of the SAP Build Work Zone service. The flow then takes us to Route 53, which will check the health of the underlying systems and redirect the users to the right available target.

**High-Level Realization Steps**

 *Prerequisites*:

* Two SAP BTP subaccounts preferably in different regions

* Amazon Route 53 with access to a custom domain

Steps

1. Configure SAP Build Work Zone service in one of the SAP BTP accounts with all the necessary tiles, groups, access rules, and destinations

2. Transport the Work Zone service from this first SAP BTP subaccount to the other SAP BTP subaccount in a different region with the help of [SAP Cloud Transport Management service](https://help.sap.com/docs/TRANSPORT_MANAGEMENT_SERVICE/7f7160ec0d8546c6b3eab72fb5ad6fd8/5fef9d6b1cb047b2b18d9eb57aa15352.html?locale=en-US).

3. Map the custom domain routes by using the [Custom Domain Plugin](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/1832fcd1eec9415694de50f620e5a522.html?locale=en-US) of SAP BTP. This step must be done manually, once for each SAP BTP subaccount. This will ensure the establishment of trust between Amazon Route 53 and SAP BTP subaccounts. As a final task, an SAP service ticket must be created to accept the domain as a valid authentication and redirection URL.

4. The next step is to create a traffic policy in Amazon Route 53 and configure the right rules to redirect the traffic. This step also includes the task of creating the health check policies and the hosted zone records. Optionally, on top of the health check, the traffic policy rule can also be based on the geographic location which can help reduce the network latency.

For more details, you can check out the [git hub repo](https://github.com/SAP-samples/btp-services-intelligent-routing/tree/launchpad_aws) here

**Potential Business Use Cases and Value**

*Employee Self-Serve Portal*

The reliability and availability of a company’s employee portal with important services like personal info, paycheck, and vacation calendar are very critical. Making such a portal highly available with the above architecture will really make a positive impact on the employees.

*Service Industry – Field Portal*

Employees of a service industry who are out on the field attending to customer issues need to have a reliable single source of truth about their business at their fingertips. The information that is provided to them, apart from being always available, can also be made location specific with reduced latency to help them serve better.

**Other Points to Consider**

 The other points a customer might consider before adopting this architecture:

* The effect on the Stateful Apps: The state of the applications will not be retained when the users’ traffic gets redirected to the other launchpad and this might force the user to refresh his page because when the switch happens, the data could be served from a different App Server which might not know of the current state.

* Extra ...