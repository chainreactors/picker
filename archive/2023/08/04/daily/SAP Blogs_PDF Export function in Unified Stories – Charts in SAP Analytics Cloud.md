---
title: PDF Export function in Unified Stories – Charts in SAP Analytics Cloud
url: https://blogs.sap.com/2023/08/03/pdf-export-function-in-unified-stories-charts-in-sap-analytics-cloud/
source: SAP Blogs
date: 2023-08-04
fetch_date: 2025-10-04T12:01:41.832800
---

# PDF Export function in Unified Stories – Charts in SAP Analytics Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* PDF Export function in Unified Stories - Charts in...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/165460&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [PDF Export function in Unified Stories - Charts in SAP Analytics Cloud](/t5/technology-blog-posts-by-sap/pdf-export-function-in-unified-stories-charts-in-sap-analytics-cloud/ba-p/13572653)

![AttilaRitzl](https://avatars.profile.sap.com/1/d/id1dd2179270c19f35340adf7f569bb93f171718c1c5ee6e6816f9809d8ee524e2_small.jpeg "AttilaRitzl")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[AttilaRitzl](https://community.sap.com/t5/user/viewprofilepage/user-id/869769)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=165460)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/165460)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13572653)

‎2023 Aug 03
7:33 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/165460/tab/all-users "Click here to see who gave kudos to this post.")

2,881

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)

View products (1)

In this blog, I will demonstrate a seamless way to export a single chart within a Unified Story in SAP Analytics Cloud (SAC) with just a click of a button. We'll leverage a simple trick using custom fonts to create the button and explore the Exporting API to achieve the desired functionality. Let's dive into the process step by step!

### Prerequisites

To create the export button, refer to SAP note [2953986 - How to set up Custom Web Fonts on SAP Analytics Cloud](https://userapps.support.sap.com/sap/support/knowledge/en/2953986) which provides details on setting up Custom Web Fonts on SAP Analytics Cloud. For SAP-icons usage, ensure to pass the URL "<https://ui5.sap.com/resources/sap/ui/core/themes/base/SAP-icons.css>" to SAC during setup.

Once the custom fonts are configured, add a button to the dashboard select an icon from the [Icon Explorer](https://sapui5.hana.ondemand.com/test-resources/sap/m/demokit/iconExplorer/webapp/index.html#/overview/SAP-icons/?tab=grid). I've chosen the pdf symbol: . Be sure to copy the second option.

![](/legacyfs/online/storage/blog_attachments/2023/07/ExportSymbol.png)

Select a symbol, then click the highlighted copy button

1. Paste the copied symbol into the Text property of the button widget in SAC, selecting the "SAP-icons" font type for consistency.

![](/legacyfs/online/storage/blog_attachments/2023/07/fontSetting.png)

Formatting panel of the button widget

2. Add the Exporting API from the Scripting list to your dashboard to enable chart export functionality.
![](/legacyfs/online/storage/blog_attachments/2023/07/exportAPI.png)

3. Include two panel widgets—one set to full screen size and the other to fit the chart. Place the full screen panel over the chart panel in the outline and ensure it is at the top of the list. You also need to hide it.

4.Place a chart in the smaller panel with height and width both set to 100%.

![](/legacyfs/online/storage/blog_attachments/2023/07/outline.png)

### Theory

Everything is at hand - now let's clarify what we are going to do.

Rushing to the API and having the export done on the chart will make a simple screenshot of the whole dashboard, but only with the chart on it - in the wrong size, wrong alignment.
We have placed the panels for a quick workaround!

We'll move the chart from its original panel to the full screen one, and refresh the layout by script and then we'll run the export. Sounds easy? It is!

### Script

```
Panel_Fullscreen.moveWidget(Chart_1);

Panel_Fullscreen.setVisible(true);

Chart_1.getLayout().setHeight(LayoutValue.create(100,LayoutUnit.Percent));

Chart_1.getLayout().setWidth(LayoutValue.create(100,LayoutUnit.Percent));

ExportToPDF_1.exportView();

Panel_Chart.moveWidget(Chart_1);

Panel_Fullscreen.setVisible(false);
```

### Result

And what do we get? Let's see:

![](/legacyfs/online/storage/blog_attachments/2023/07/ExportResults.png)

Dashboard and export result

## Lookouts

* Export API - Paper Size

  + If you differ the Auto setting, make sure your layout fits the size you select here. Otherwise, your will turn out readable.

  + |
     A2 |
     ~ 7016 x 4961 px |

    |
     A3 |
     ~ 4961 x 3508 px |

    |
     A4 |
     ~ 3508 x 2480 px |

    |
     A5 |
     ~ 2480 x 1748 px |

* Export API - Included widgets

  + Ensure that all charts and tables you want to export are opted-in for export. Any widgets added after creating the API won't be included automatically.

## Conclusion

By following this straightforward approach, you can effortlessly export single charts from your Unified Story in SAP Analytics Cloud. Feel free to share your experiences and challenges in the comments below. Let's continue exploring the potential of SAC together! Happy exporting! ![:smiling_face_with_smiling_eyes:](/html/@61796F7B1C73E81D1D9470FE142AD91D/emoticons/1f60a.png ":smiling_face_with_smiling_eyes:")

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [attach pdf](/t5/tag/attach%20pdf/tg-p/board-id/technology-blog-sap)
* [Export](/t5/tag/Export/tg-p/board-id/technology-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fpdf-export-function-in-unified-stories-charts-in-sap-analytics-cloud%2Fba-p%2F13572653%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Driving AI Adoption with BTP: Highlights](/t5/technology-blog-posts-by-sap/driving-ai-adoption-with-btp-highlights/ba-p/14233554)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Transforming Healthcare Procurement: Lessons from Our S/4HANA MM Implementation](/t5/technology-q-a/transforming-healthcare-procurement-lessons-from-our-s-4hana-mm/qaq-p/14233251)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Thursday
* [Building SaaS Products on SAP BTP](/t5/technology-blog-posts-by-members/building-saas-products-on-sap-btp/ba-p/14231929)
  in [Technology Blog Posts by Members](/t5/technology-blog-po...