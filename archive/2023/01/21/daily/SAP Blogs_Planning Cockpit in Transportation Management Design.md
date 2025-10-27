---
title: Planning Cockpit in Transportation Management Design
url: https://blogs.sap.com/2023/01/20/planning-cockpit-in-transportation-management-design/
source: SAP Blogs
date: 2023-01-21
fetch_date: 2025-10-04T04:28:37.974907
---

# Planning Cockpit in Transportation Management Design

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Planning Cockpit in Transportation Management Desi...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/5009&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Planning Cockpit in Transportation Management Design](/t5/supply-chain-management-blog-posts-by-members/planning-cockpit-in-transportation-management-design/ba-p/13571403)

![oscarmzvzz](https://avatars.profile.sap.com/4/1/id41941652e5c1f14a3f2d150bd551b8d8645c01b224ed3144cc5386174c1e6f64_small.jpeg "oscarmzvzz")

[oscarmzvzz](https://community.sap.com/t5/user/viewprofilepage/user-id/567196)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=5009)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/5009)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571403)

‎2023 Jan 20
9:44 PM

[8
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/5009/tab/all-users "Click here to see who gave kudos to this post.")

6,785

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Transportation Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Transportation%2520Management/pd-p/01200615320800000686)
* [LE (Logistics Execution)](https://community.sap.com/t5/c-khhcw49343/LE%2520%28Logistics%2520Execution%29/pd-p/264113000323749692806973999948926)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Transportation Management

  SAP Transportation Management](/t5/c-khhcw49343/SAP%2BTransportation%2BManagement/pd-p/01200615320800000686)
* [LE (Logistics Execution)

  Software Product Function](/t5/c-khhcw49343/LE%2B%252528Logistics%2BExecution%252529/pd-p/264113000323749692806973999948926)

View products (3)

After 5 years as an SAP Logistics Consultant I have been able to work with different planning tools for supply chain. Recently I got immersed on the Transportation Management module of S/4. It took me a while and multiple learning hours, including an S/4 implementation,  to feel confident navigating trough the Transportation Management logic. There are a few outstanding functionalities that I consider very important to understand especially if you are a native SD or MM consultant just like me.

On this blog I would like to share some of the knowledge I recently acquired about the planning options used in  SAP Transportation; more specifically about the Transportation Planning Cockpit which is a very efficient tool to drive your planning trough a completely panoramic view with the main purpose of having all the needed information available within one single screen.

In this blog, I would love to share with you how I created and customized a planning layout according to my needs. I'm confident it might be useful for anyone who is diving in on the TM world just like me.

The below screenshots were taken by my during some training that I have been executing

My layout will be called ***Layout 04***

1. In my main Fiory environment I opened the corresponding tile to create a planning layout for transportation cockpit:

![](/legacyfs/online/storage/blog_attachments/2023/01/1-46.png)

2.- Start Creating Cockpit layout, you need to give it a name, on this case I used my name as a description. After this all the content of the layout will open to start filling up the details

Create Layout

![](/legacyfs/online/storage/blog_attachments/2023/01/2-25.png)

3.- We need fill up the general data making sure that we maintain the Transportation proposal layout required and most important which other additional layouts will be available if we need to switch to another standard/ predefined view.

![](/legacyfs/online/storage/blog_attachments/2023/01/3-15.png)

Other layouts available for a switch

4.- If we keep scrolling we will find the available buttons that we will have available on the header of the layout, in this example I'm ticking all those buttons related with Update Map and Optimizer Planning.

![](/legacyfs/online/storage/blog_attachments/2023/01/4-15.png)

Enabling Buttons

5.- Scroll down and we will come to the interesting part, this is where we need to assemble our puzzle, we could arrange different components as per our best convenience, in my example I want to split my screen in 5 with the following visual structure:

|
 Freight Units | |

|
 Schedule and Trucks |
 Freight Orders/Freight Bookings |

|
 FU Stages |
 Map |

Based on this I will add the Freight Unit stages on the top left area making sure that I give 100% Width to this part of the screen.

|
 **Freight Units** | |

|
  |
  |

|
  |
  |

6.- Every time we want to add any content on any specific area we should press the 'add content button' so we can choose from specific information available, in this case I want the Freight Unit Stages

![](/legacyfs/online/storage/blog_attachments/2023/01/Lat.png)

Add Content

![](/legacyfs/online/storage/blog_attachments/2023/01/5-16.png)

When this is added, and since I don't want to add any information on the top of the screen, I will continue to add information on lower levels, in this case I choose 'Add area' and 'below'

Assemble Top Area

![](/legacyfs/online/storage/blog_attachments/2023/01/6-14.png)

7.- On this case, I do want to share the middle space with two different spaces so I will proceed as follows

|
 Freight Units | |

|
 **Schedule and Trucks** |
 **Freight Orders/Freight Bookings** |

![](/legacyfs/online/storage/blog_attachments/2023/01/7-12.png)

 8.- I will continue with the lowest part of my screen adding the last to pieces of information that I want to have visible then again, making sure I do share the width space 50% for each data box

|
 Freight Units | |

|
 Schedule and Trucks |
 Freight Orders/Freight Bookings |

|
 **FU Stages** |
 **Map** |

This is how the final outcome of my planning cockpit looks like.

![](/legacyfs/online/storage/blog_attachments/2023/01/8.5.png)

Final Design

Visualize Planning cockpit as designed

9.- As a last step I will add this layout as a default for my planning profile

![](/legacyfs/online/storage/blog_attachments/2023/01/8.6.png)

Planning Cockpit

![](/legacyfs/online/storage/blog_attachments/2023/01/8-12.png)

10.- As you can see, my planning cockpit is retrieving the information as I requested, in this case I don't have a lot of information planned but it does give me the facility to drag, drop and expand any of this five sections that I arranged.

![](/legacyfs/online/storage/blog_attachments/2023/01/9-7.png)

Planning profile update

In a nutshell, Transportation Management planning cockpit is now coming as a support not only for planning activities in SAP but also for logistics and execution. If you are interested to expand your knowledge about these and other topics I would recommend taking a glance to the following SAP Learning journey

[Learning Journey: SAP S/4HANA - Transportation Management](https://help.sap.com/learning-journeys/265f9ae5e2784a818225c41d4d...