---
title: Troubleshooting Fiori Applications: Tips and Tricks for S/4 HANA
url: https://blogs.sap.com/2023/07/16/troubleshooting-fiori-applications-tips-and-tricks-for-s-4-hana/
source: SAP Blogs
date: 2023-07-17
fetch_date: 2025-10-04T11:52:43.485538
---

# Troubleshooting Fiori Applications: Tips and Tricks for S/4 HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Troubleshooting Fiori Applications: Tips and Trick...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161472&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Troubleshooting Fiori Applications: Tips and Tricks for S/4 HANA](/t5/technology-blog-posts-by-members/troubleshooting-fiori-applications-tips-and-tricks-for-s-4-hana/ba-p/13558606)

![VijayCR](https://avatars.profile.sap.com/5/d/id5dec9917d1d4a6afdb1c924dc1f0d19cccdfabf28cb31d70a37ff6e8b182bcc2_small.jpeg "VijayCR")

[VijayCR](https://community.sap.com/t5/user/viewprofilepage/user-id/38084)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161472)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161472)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558606)

‎2023 Jul 16
12:47 PM

[22
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161472/tab/all-users "Click here to see who gave kudos to this post.")

39,955

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)

View products (2)

Hello S4 HANA Experts,

Since all of us have started working with S/4 HANA systems usage of Fiori launch pad and Fiori apps has increased in place of SAP GUI transactions .

In the below blog I will be addressing most frequently encountered issues and Tipps to resolve the issues :

***Standard Apps and Catalogues do not exist :***

When the latest front end server upgrade notes are installed in any FES (Front end Server), some business catalogues might be removed from the Fiori launch pad designer.

To check this, use the transaction /UI2/FLPCM\_CUST or the Fiori app FLP content manager: Search to find the App name and that you discovered the Fiori app and business catalogue.

Run the following Transaction /UI2/APPDESC\_GET\_ALL or Report /UI2/APPDESC\_GET\_ALL

All back-end and reproducible catalogues for all system aliases are replicated.

**Step 1 :** Run the test to see whether there are any erroneous business catalogues, as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/07/MicrosoftTeams-image-20.png)

**Step2 :** Perform the Actual run and the missing business catalogs will be replicated

![](/legacyfs/online/storage/blog_attachments/2023/07/clip_image002.jpg)

     Once execution recheck Fiori launchpad content manger or refresh Fiori Launchpad and search for the App the apps should be appearing.

***Troubleshooting******the errors :***

**Frontend related errors :**

In case of the troubleshooting to be done from the frontend side use the Developers tools

* Use the elements tab, click on the UI element, and then right-click on Inspect to display and bring up the element for CSS troubleshooting.

* To debug the SAP UI5 application use the source tab as shown in the below screentshot and open the component-preload.js and click on the curly brackets as shown below to get the right format to place a debugging for debugging UI5 content .In case you do not want to debug the compressed app but look for all Views and Controllers use the parameter "**sap-ui-debug=true**" to URL of your Fiori apps as below

<port>/sap/bc/ui2/flp?**sap-ui-debug=true**#AccountingDocument-manage

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-16_15h42_49.png)

* To check the Odata calls related errors open the tab network and look for the fitler batch where most of the Odata calls are performed ( In some very rare cases Odata Calls will be non batch )

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-16_15h56_54-2.png)

* To check the exact entity names and the response use the payload and Response tabs ( In case of the SADL model or Fiori programming model or RAP model we could find the CDS entities that used for the entities.

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-16_16h01_09.png)

**Backend related troubleshooting:**

The backend-related errors could have been caused by either of the two primary problems:

* OData Services or not active or the Ui5 Application is not active .

* Follow the below steps to check the backed related errors :

  + Use the transaction /IWFND/ERROR\_LOG for the Odata related errors

  + /IWBEP/ERROR\_LOG could be also leverated for the backend errors

* Use the transaction /UI2/FLPCM\_CUST or the Fiori app FLP content manager: Search the app name and check if both the services are active or not ?

* If not active activate the Ui5 App from the transaction SICF and the Odata service using the transaction /IWFND/MAINT\_SERVICE
  ![](/legacyfs/online/storage/blog_attachments/2023/07/MicrosoftTeams-image-19-1.png)
  ![](/legacyfs/online/storage/blog_attachments/2023/07/Picture3-10.png)![](/legacyfs/online/storage/blog_attachments/2023/07/Picture5-9.png)![](/legacyfs/online/storage/blog_attachments/2023/07/Picture6-10.png)

* If there are any Custom theme related rendering issues for the SAP GUI for HTML based apps use the below WEBGUI URL to get standalone in webgui to understand the redering issues .

           <PORT>/sap/bc/gui/sap/webgui?sap-client=100

***Caches: Different types of Cache***

**Browser Cache**

If there is any change in the existing App or new Application is transported from one to other there is always a possibility that the browser cache is not deleted either you do not see the app or see the same version of the application:

In this scenario if you’re using the Chrome browser use the Incognito mode and try to login into Fiori Launch pad

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture2-12.png)

Check the applications in a private window if you're using Edge browser.
If you do not want to open a new browser, you can clear your caches through the browser settings by Deleting the cookies and caches.

**Backend and Front End Caches :**

* Execute the transaction /IWBEP/CACHE\_CLEANUP in the event that the CDS annotations/ Odata Metadata have been changed and moved and the cache needs to be cleaned out .

![](/legacyfs/online/storage/blog_attachments/2023/07/metadata.png)

* Execute the transaction /IWFND/CACHE\_CLEANUP to perform cache clearing for the ODATA Gateway Model .A star (\*) may need to be entered in the Model Identifier field.

![](/legacyfs/online/storage/blog_attachments/2023/07/MicrosoftTeams-image-16.png)

**Front End Caches :**

* The report /UI5/APP\_INDEX\_CALCULATE has to be executed every time the content of the SAPUI5 ABAP repository is modified. The execution of the report to update the index is not, automatically triggered in some uncommon circumstances, such as applying a SAP Note, thus we must manually run the report in these cases.

* you can place \* in case this has to be run f...