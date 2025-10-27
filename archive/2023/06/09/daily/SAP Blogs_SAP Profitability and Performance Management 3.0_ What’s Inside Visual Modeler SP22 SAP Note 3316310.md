---
title: SAP Profitability and Performance Management 3.0: What’s Inside Visual Modeler SP22 SAP Note 3316310
url: https://blogs.sap.com/2023/06/08/sap-profitability-and-performance-management-3.0-whats-inside-visual-modeler-sp22-sap-note-3316310/
source: SAP Blogs
date: 2023-06-09
fetch_date: 2025-10-04T11:47:19.065990
---

# SAP Profitability and Performance Management 3.0: What’s Inside Visual Modeler SP22 SAP Note 3316310

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)
* SAP Profitability and Performance Management 3.0: ...

Financial Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-sap/article-id/7884&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Profitability and Performance Management 3.0: What’s Inside Visual Modeler SP22 SAP Note 3316310](/t5/financial-management-blog-posts-by-sap/sap-profitability-and-performance-management-3-0-what-s-inside-visual/ba-p/13555360)

![former_member776414](https://avatars.profile.sap.com/former_member_small.jpeg "former_member776414")

[former\_member776414](https://community.sap.com/t5/user/viewprofilepage/user-id/776414)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-sap&message.id=7884)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-sap/article-id/7884)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555360)

‎2023 Jun 08
10:30 AM

[7
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-sap/message-id/7884/tab/all-users "Click here to see who gave kudos to this post.")

1,293

* SAP Managed Tags
* [SAP Profitability and Performance Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Profitability%2520and%2520Performance%2520Management/pd-p/73555000100800000092)

* [SAP Profitability and Performance Management

  SAP Profitability and Performance Management](/t5/c-khhcw49343/SAP%2BProfitability%2Band%2BPerformance%2BManagement/pd-p/73555000100800000092)

View products (1)

Profitability and Performance Management 3.0 has released a new support package (SP22) with exciting enhancements and features before the halfway mark of the calendar year 2023. But, before I go into detail about the new support package, I recommend you to read the previous blog post [SAP Profitability and Performance Management 3.0: What's Inside Visual Modeler SP21 SAP Note 3278816...](https://blogs.sap.com/2023/02/13/sap-profitability-and-performance-management-3.0-whats-inside-visual-modeler-sp21-sap-note-3278816/)

Now allow me to take you through the exciting features, enhancements, and improvements covered by SAP Note [3316310 - FS-PER Rel. 3.0 SP22: Visual Modeler Screens Enhancements and Fixes (1)](https://launchpad.support.sap.com/#/notes/3316310).

**Environment Screen**

* The editing user interface has been enhanced so that it remains visible even when you scroll the screen up and down.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/Scroll-up-and-down.jpg)

* Column sorting has been improved so that even if you search for a keyword, the sorting of *Environment*, *Version*, *History* *Versions*, and *Reports* continues to work.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/column-sorting-scaled.jpg)

* The message log on screen has been enhanced to clear the messages and then collapses the message log when you choose the *Refresh* button, similar to how the browser refresh works.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/message-logs.jpg)

* The screen’s drag and drop capabilities have been improved, so that this feature remains active even if you use another browser than Google Chrome.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/firefox-drag-and-drop.jpg)

* The *More Filters* option in the *Reports* panel has been enabled to display the “Suspended”, “Aborted” and “All” options.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/more-filters.jpg)

* Previously, the downloaded comparison PDF file lacked header information. This has been improved to include the environment description in the header.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/pdf-file.jpg)

* The search box on the *Comparison* screen has been improved so that when you loose focus on it, the search result collapses. Selecting it again displays the matched value by expanding the search result.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/comparison-searched-box.jpg)

**Modeling Environment Screen**

* The *Cut* button is disabled when you select nodes inside the general entities.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/Cut-button.jpg)

* When naming a function ID, the validation error message now notifies you that an underscore is not allowed as last character.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/function-ID.jpg)

* Performance issues may occur when the number of nodes in a business function or field exceeds 10,000. Therefore, a warning message was introduced to make you aware of the implications.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/too-large-message-logs.jpg)

* The user interface for selecting master data has been enhanced so that the dropdown menu is no longer visible when you loose focus on the field containing master data.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/master-data.jpg)

* The system returns a validation error if the *Hierarchy Parent Name* is not defined in the *Value column* and is not set as a node.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/master-data-creation.jpg)

* The “Performer” and “Reviewer” group selection has been improved as follows: When you remove the “Performer” group from activities (I/O, Execution, or URL), the “Reviewer” is automatically removed and greyed out, and if the “Reviewer group” is removed, the “Performer” is still assigned.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/performer-reviewer.jpg)

* You can now use the *Erase Data* button in *Execution activity* to delete data within the selected model function.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/erase-data.jpg)

* The palette and properties panel borders have been optimized to appear when they are expanded.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/border.jpg)

* The external table has been refined to automatically convert text to uppercase during field mapping.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/mapping.jpg)

* When uploading files via FilePicker or drag and drop, the user interface has been improved so that there is no overlapping.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/file-upload.jpg)

* When you choose the *Erase Data* button, the data in the model table is immediately cleared. The system behavior depends on the setting of the *Transport Data* option.Option 1: Transport Data = “Yes
  ![](/legacyfs/online/storage/blog_attachments/2023/06/delete-button.jpg)

  Transport Data = ”No
  ![](/legacyfs/online/storage/blog_attachments/2023/06/erase-data-TD-No.jpg)

* When you save a new Model Table with *Transport Data* = “Yes”, the system automatically activates the function and a check indicator representing its activation status is displayed.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/auto-activate.png)

* The Model View OData function has been enabled and can be added and configured to the diagram.
  ![](/legacyfs/online/storage/blog_attachments/2023/06/MV-OData.jpg)

* Variable Default Value Filtering in the Query functi...