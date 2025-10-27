---
title: Everything you need to know about SAP Cloud Transport Management _ End to End guide
url: https://blogs.sap.com/2023/07/04/everything-you-need-to-know-about-sap-cloud-transport-management-_-end-to-end-guide/
source: SAP Blogs
date: 2023-07-05
fetch_date: 2025-10-04T11:53:31.361483
---

# Everything you need to know about SAP Cloud Transport Management _ End to End guide

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Everything you need to know about SAP Cloud Transp...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161613&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Everything you need to know about SAP Cloud Transport Management \_ End to End guide](/t5/technology-blog-posts-by-members/everything-you-need-to-know-about-sap-cloud-transport-management-end-to-end/ba-p/13559144)

![Sookriti_Mishra](https://avatars.profile.sap.com/a/4/ida4b1c3487db981adb1a0bf5a895334e325f25359114f2cf86cd94415b088a2de_small.jpeg "Sookriti_Mishra")

[Sookriti\_Mishra](https://community.sap.com/t5/user/viewprofilepage/user-id/173946)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161613)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161613)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559144)

‎2023 Jul 04
6:38 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161613/tab/all-users "Click here to see who gave kudos to this post.")

6,979

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Cloud Transport Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Transport%2520Management/pd-p/73554900100800001901)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Cloud Transport Management

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BTransport%2BManagement/pd-p/73554900100800001901)

View products (2)

**Hello Beautiful People,
OMG! Finally, I implemented this. And, it was so easy. Well, it's always difficult until you have faced it.**

**I have always wanted to implement this, but not a single client that I worked for wanted to give this comfort of Transport Management to their developers until I met my current client, who also are enthusiasts like me, and they were like, "Sookriti, we have got to do this!".**

**And thus, I started. The first thing I did was, hit the SAP Cloud Integration Community. I gathered a couple of blogs. I am going to drop them in the reference section. This blog is a quick summary of everything I did that the bloggers mentioned, and also what they didn't.**

**It's my belief that if stumble upon my blog, and want to follow it, chances are, you won't be disappointed.**

![Image tagged in penguins squad - Imgflip](https://i.imgflip.com/1ohsr9.jpg)

# **Pre-requisites:**

A **Global Account**, a **Subaccount**, a **Space**, and below **Entitlements**:

|
 **Source****/Target** |
 **Service Name** |
 **Technical Name** |
 **Plan** |
 **Status** |

|
 **Source** |
 Cloud Transport Management |
 alm-ts |
 standard (Application) |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |

|
 **Source** |
 Cloud Transport Management |
 transport |
 standard |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |

|
 **Source** |
 Process Integration Runtime |
 it-rt |
 integration-flow |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |

|
 **Source** |
 Process Integration Runtime |
 it-rt |
 api |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |

|
 **Source** |
 Integration Suite |
 integrationsuite |
 enterprise\_agreement (Application) |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |

|
 **Source** |
 Content Agent Service |
 content-agent-ui |
 free (Application) |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |

|
 **Source** |
 Content Agent Service |
 content-agent |
 application |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |

|
 **Source** |
 Content Agent Service |
 content-agent |
 standard |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |

|
 **Target** |
 Integration Suite |
 integrationsuite |
 enterprise\_agreement (Application) |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |

|
 **Target** |
 Process Integration Runtime |
 it-rt |
 integration-flow |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |

|
 **Target** |
 Process Integration Runtime |
 it-rt |
 api |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |

---

# Create Subscription/ Instance, Service Key, and Destinations in Source and Target Subaccounts in BTP Cockpit

**Copy paste this table below in an excel sheet, and start configuring.**

|
 **Reference No.** |
 **Source/ Target** |
 **Entitlement Name** |
 **Subscription** |
 **Instance** |
 **Instance - Service (Plan)** |
 **Service Key** |
 **Destination** |
 **Destination Name** |

|
  |
  |
 **A** |
 **B** |
 **C** |
 **D** |
 **E** |
 **F** |
 **G** |

|
 **1** |
 Source |
 Cloud Transport Management |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |
 ![:cross_mark:](/html/@16A89235E533365B6992DE8C750468DF/emoticons/274c.png ":cross_mark:") |
 ![:heavy_minus_sign:](/html/@368FF45EAD2D677A9C38A9AA7A4FD3D4/emoticons/2796.png ":heavy_minus_sign:") |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |
 TransportManagementService |

|
 **2** |
 Source |
 Integration Suite |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |
 ![:cross_mark:](/html/@16A89235E533365B6992DE8C750468DF/emoticons/274c.png ":cross_mark:") |
 ![:heavy_minus_sign:](/html/@368FF45EAD2D677A9C38A9AA7A4FD3D4/emoticons/2796.png ":heavy_minus_sign:") |
 ![:cross_mark:](/html/@16A89235E533365B6992DE8C750468DF/emoticons/274c.png ":cross_mark:") |
 ![:cross_mark:](/html/@16A89235E533365B6992DE8C750468DF/emoticons/274c.png ":cross_mark:") |
 **![:heavy_minus_sign:](/html/@368FF45EAD2D677A9C38A9AA7A4FD3D4/emoticons/2796.png ":heavy_minus_sign:")** |

|
 **3** |
 Source |
 Process Integration Runtime |
 ![:cross_mark:](/html/@16A89235E533365B6992DE8C750468DF/emoticons/274c.png ":cross_mark:") |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heavy_check_mark:") |
 Process Integration Runtime (integration-flow) |
 ![:white_heavy_check_mark:](/html/@9E2667D4778E7732699FEDD0E1D4C70F/emoticons/2705.png ":white_heav...