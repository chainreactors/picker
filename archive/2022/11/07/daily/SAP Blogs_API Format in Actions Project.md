---
title: API Format in Actions Project
url: https://blogs.sap.com/2022/11/06/api-format-in-actions-project/
source: SAP Blogs
date: 2022-11-07
fetch_date: 2025-10-03T21:52:21.978224
---

# API Format in Actions Project

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* API Format in Actions Project

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160370&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [API Format in Actions Project](/t5/technology-blog-posts-by-sap/api-format-in-actions-project/ba-p/13557399)

![akshilv27](https://avatars.profile.sap.com/4/6/id46e523ca4af9c6e72349c1dd1d6e7b3acdcde7a848e3d9aa2b948181497d9ce2_small.jpeg "akshilv27")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[akshilv27](https://community.sap.com/t5/user/viewprofilepage/user-id/42066)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160370)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160370)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557399)

‎2022 Nov 06
9:56 AM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160370/tab/all-users "Click here to see who gave kudos to this post.")

2,525

* SAP Managed Tags
* [SAP Intelligent Robotic Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Intelligent%2520Robotic%2520Process%2520Automation/pd-p/73554900100800002142)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Intelligent Robotic Process Automation

  Software Product](/t5/c-khhcw49343/SAP%2BIntelligent%2BRobotic%2BProcess%2BAutomation/pd-p/73554900100800002142)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (3)

**Motivation**

This blog focusses on the concept and usability of API Formats within an Action of the Actions Project.

**Parent Blog**

#### [**Actions Editor – Feature List, Usage and Maintenance of Actions Project**](https://blogs.sap.com/2022/10/21/actions-editor-feature-list-usage-and-maintenance-of-actions-project/)

**Concept and Need**

Actions Project allows the citizen developer to add a format type to the parameters of the input/output tables. The format can be chosen from the API Format column of these tables. These API formats help to understand the specific data-type format for the parameter that is to be passed to invoke the API.

API Formats are introduced to bridge the gap between the date/time formats that the Action Designer expects and the formats that are internally accepted by the API.

Example:

1. Click on the specific Action Parameter for which a format needs to be specified as shown in figure 1.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2023-12-28-at-23.55.19.png)

Figure 1: Display details of a specific Action Parameter

2. Click on the API Format selection box as shown in figure 2.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2023-12-28-at-23.54.17.png)

Figure 2: Expanding API Format selection box

3. Choose the appropriate format from the API Format selection box. This change will be reflected as shown in figure 3.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2023-12-28-at-23.54.31.png)

Figure 3: Select a specific API Format for an Action Parameter

4. Add a value based on the format selected as shown in figure 4.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2023-12-28-at-23.54.47.png)

Figure 4: Input a Value corresponding to the API Format selected

**Behavior for Input and Output API Format**

When an API format is selected for input parameters, the Action Service will expect a consumer value, and the service will convert them to the specified format types to make the API call.

When an API format is selected for output parameters, the Action Service will convert the response from the selected format type and return the result to the citizen developer in the form of a consumer value.

These behaviors are illustrated in figure 5.

![](/legacyfs/online/storage/blog_attachments/2022/10/MicrosoftTeams-image-11.png)

Figure 5: Behavior of Input and Output API Formats

### Supported API Format types

As of now, Actions Project supports the following API formats:

|
 Format Type |
 Definition |
 Example value |
 Consumer value |

|
 None |
 No format type is specified. Actions will accept any value for the parameter. |
 Any value |
 - |

|
 DD-MM-YYYY |
 A date format is specified. |
 01-01-9999 |
 "9999-01-01" |

|
 MM-DD-YYYY |
 A date format is specified. |
 01-01-9999 |
 "9999-01-01" |

|
 YYYY-MM-DD |
 A date format is specified. |
 9999-01-01 |
 "9999-01-01" |

|
 HH:MM:SS |
 A time format is specified. |
 12:34:56 |
 "12:34:56Z", "12:34:56+03:00" |

|
 EDM DateTime |
 A timestamp format is specified. |
 9999-01-01T12:34:56 |
 9999-01-01T12:34:56+05 |

|
 EDM Time |
 A time format is specified. |
 PT13H20M55S |
 "12:34:56Z", "12:34:56+03:00" |

|
 EDM DateTimeOffset |
 A time format is specified. |
 9999-01-01T12:34:56Z |
 9999-01-01T12:34:56+05 |

|
 Timestamp since Epoch |
 A timestamp format is specified. |
 /Date(1492098664000)/ |
 2016-07-08T12:34:56+05 |

|
 Date since Epoch |
 A date format is specified. |
 /Date(1492098664000)/ |
 "9999-01-01" |

### Disabled or Empty API Format

The Action Designer will sometimes would not see the format selection box at all as shown in figure 6. This is because API formats are not supported for some parameter types.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2023-12-29-at-00.00.16.png)

Figure 6: Showcasing disabled or empty API Format

The following table details the relationship between the parameter type and API format:

|
 Parameter Type |
 API Format |

|
 string |
 Supported. Format selection box is shown and usable. |

|
 integer |
 Not supported. Format selection box is not shown. |

|
 boolean |
 Not supported. Format selection box is not shown. |

|
 number |
 Not supported. Format selection box is not shown. |

|
 array |
 Not supported. Format selection box is not shown. |

|
 object |
 Not supported. Format selection box is not shown. |

**Blog Reference**

* [Part 1 of the Blog Series: Actions Project - Major Changes including the Actions Editor Available No...](https://blogs.sap.com/2022/10/19/the-new-actions-project-major-changes-including-the-actions-editor-available-now/)

* [Part 2 of the Blog Series/Parent Blog: Actions Editor – Feature List, Usage and Maintenance of Actio...](https://blogs.sap.com/2022/10/21/actions-editor-feature-list-usage-and-maintenance-of-actions-project/)

Thanks for reading and I hope it helped to understand the concept of API Formats in Actions Project. Please feel free to leave a comment if there are any questions and I would be happy to receive any feedback.

Labels

*...