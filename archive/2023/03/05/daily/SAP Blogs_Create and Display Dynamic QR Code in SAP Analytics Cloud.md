---
title: Create and Display Dynamic QR Code in SAP Analytics Cloud
url: https://blogs.sap.com/2023/03/04/create-and-display-dynamic-qr-code-in-sap-analytics-cloud/
source: SAP Blogs
date: 2023-03-05
fetch_date: 2025-10-04T08:43:42.875259
---

# Create and Display Dynamic QR Code in SAP Analytics Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Create and Display Dynamic QR Code in SAP Analytic...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162319&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Create and Display Dynamic QR Code in SAP Analytics Cloud](/t5/technology-blog-posts-by-members/create-and-display-dynamic-qr-code-in-sap-analytics-cloud/ba-p/13562963)

![rohitchouhan](https://avatars.profile.sap.com/4/5/id45bb5baea03cecd8e50cbc89133a047253088dae157e51b49ff169bd90a15863_small.jpeg "rohitchouhan")

[rohitchouhan](https://community.sap.com/t5/user/viewprofilepage/user-id/782213)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162319)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162319)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562963)

‎2023 Mar 04
8:14 AM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162319/tab/all-users "Click here to see who gave kudos to this post.")

3,485

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)

View products (1)

This tutorial blog guides the users on how to use the SAP Custom Widget - QR Code Widget. It includes prerequisites, installation, deployment, and usage steps. The QR Code Widget allows users to generate QR codes for various use cases such as marketing, inventory management, and product tracking.

[![preview](https://raw.githubusercontent.com/SAP-Custom-Widget/QrCodeWidget/main/screenshot.png)](https://raw.githubusercontent.com/SAP-Custom-Widget/QrCodeWidget/main/screenshot.png)

## Installation

To use this widget in your SAP application, follow these steps:

* Download the `QrCodeWidget.json` file from the URLs specified in the webcomponents property of the JSON.

* Go to your SAC Portal, select Analytic Application from the left side bar, and then go to the Custom Widget tab.

* Click on the + icon on the right side and select the `QrCodeWidget.json` file that you downloaded.

* You're done! You can now use it in your app.

Repository: <https://github.com/SAP-Custom-Widget/QrCodeWidget/>

## Methods

The widget has the following methods:

### Set Methods

|
 Method |
 Parameter Type |
 Description |

|
 setSize(size) |
 integer |
 Set QR Code Width x Height |

|
 setData(data) |
 string |
 Set Data for QR Code |

|
 setColor(color) |
 string |
 Set QR Code Foreground Color |

|
 setBgcolor(bgcolor) |
 string |
 Set QR Code Background Color |

### get Methods

|
 Method |
 Return Type |
 Description |

|
 getSize() |
 integer |
 return QR Code Width x Height |

|
 getData() |
 string |
 return Data for QR Code |

|
 getColor() |
 string |
 return QR Code Foreground Color |

|
 getBgcolor() |
 string |
 return QR Code Background Color |

## Conclusion

SAP Custom Widget provides developers with the flexibility to build and deploy custom widgets on SAP Business Technology Platform (BTP). The QR Code Widget is one such widget developed by SAP Custom Widget that provides users with a simple and efficient way to generate QR codes. By following the steps provided in this tutorial, users can easily install, deploy, and use the QR Code Widget in their applications.

* [analytic application](/t5/tag/analytic%20application/tg-p/board-id/technology-blog-members)
* [custom widget](/t5/tag/custom%20widget/tg-p/board-id/technology-blog-members)
* [QR Code](/t5/tag/QR%20Code/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcreate-and-display-dynamic-qr-code-in-sap-analytics-cloud%2Fba-p%2F13562963%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Adding calculated rows in SAP Analytics Cloud table for lightweight calculations](/t5/technology-q-a/adding-calculated-rows-in-sap-analytics-cloud-table-for-lightweight/qaq-p/14234439)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Is there a way to dynamically change the names and legends of measure items in SAC?](/t5/technology-q-a/is-there-a-way-to-dynamically-change-the-names-and-legends-of-measure-items/qaq-p/14234032)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [What's New in SAP Analytics Cloud Modeling Extensions & Integration QRC4 2025 Release](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-analytics-cloud-modeling-extensions-amp-integration-qrc4/ba-p/14208685)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Thursday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 4 |
| [![smarchesini](https://avatars.profile.sap.com/0/c/id0cf1ddd928dd875ac324a5701f9e4d9a60995d0072e5b58f718f5dd57231fae9_small.jpeg "smarchesini")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg...