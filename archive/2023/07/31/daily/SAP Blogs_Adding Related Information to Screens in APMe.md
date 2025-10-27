---
title: Adding Related Information to Screens in APMe
url: https://blogs.sap.com/2023/07/30/adding-related-information-to-screens-in-apme/
source: SAP Blogs
date: 2023-07-31
fetch_date: 2025-10-04T11:51:50.298615
---

# Adding Related Information to Screens in APMe

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Adding Related Information to Screens in APMe

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/6432&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Adding Related Information to Screens in APMe](/t5/human-capital-management-blog-posts-by-sap/adding-related-information-to-screens-in-apme/ba-p/13572472)

![PhillipButts38](https://avatars.profile.sap.com/9/0/id90f1e5b297b1fc33029ba2b7f3f7f2b6521519ab64e8c9169b8d7eddc865a4f2_small.jpeg "PhillipButts38")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[PhillipButts38](https://community.sap.com/t5/user/viewprofilepage/user-id/6209)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=6432)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/6432)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13572472)

‎2023 Jul 30
9:43 PM

[5
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/6432/tab/all-users "Click here to see who gave kudos to this post.")

582

* SAP Managed Tags
* [SAP SuccessFactors Agent Performance Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Agent%2520Performance%2520Management/pd-p/73554900100800003792)

* [SAP SuccessFactors Agent Performance Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BAgent%2BPerformance%2BManagement/pd-p/73554900100800003792)

View products (1)

Over the years, i have navigated through hundreds of thousands of APMe screens. Although the menu navigation is good, it would be even better to have data presented on a single screen for review.  By design, Broker (Producer), Producer Hierarchy , Address, License and other Producer related information is stored in different tables in APMe. Each table in APMe typically has its own screen in APMe. If a user wanted to view a Producer's address,  the user would have to select a Producer and then select the Address menu item for the Producer for the user to be able to view/edit the Producer's Address. APMe has added a way to combine related information into the parent record's screen.

Lets take a look at the Producer screen. By default, the Producer screen will have general information about the Producer as well as section defining the Producer to Vendor Relationships.

![](/legacyfs/online/storage/blog_attachments/2023/07/ProducerScreen.png)

Default Producer Screen

To view the addresses for this Producer, the user would have to click the Addresses Menu Item to view the list of Addresses for this Producer.  We can now add the Addresses directly to the Producer Screen through APMe's Entity Configuration.

Navigate to Administrator>Entity Configuration> Entity Configuration.
Assuming that Address has not been added previously, Select the + to create a New Entity Configuration. From this screen, you can configure specific options for the main Address screen as well as the Related Information to be displayed on the Producer screen.

+ Enable Comments:  Can comments be added on the Address Detail Screen?

+ Enable Attachments:  Can attachments be added on the Address Detail Screen?

+ Enable Notes: Can Notes be added on the Address Detail Screen?

+ Max Rows: How many results to you want to be listed on the Parent Entity Screen?

+ Summary Fields: These are the Address fields that will be presented on the Producer Screen.

+ Banner Fields:  These are the fields of the parent entity that will show in the header of the screen when you are in a child entity. For example: Fields that are configured on the Broker Banner Entity Configuration will be shown on the Broker's Address screen.  Address does not have a child entity so this can be left blank for the Entity Configuration for Address.

+ Default Sort Order: Allows Records to be displayed in a particular order.  This functionality is useful for dated entities (for ex: License) so that the active records can be displayed first.

Once these items have been configured, select the Save Button.

![](/legacyfs/online/storage/blog_attachments/2023/07/address.png)

Entity Configuration for Address

![](/legacyfs/online/storage/blog_attachments/2023/07/banner-2.png)

Banner Configuration for Broker On Address Screen

Once the entity configuration has been saved, it can be added to the Producer Master screen via APMe's screen Customization functionality.

Navigate to a Producer record

Manager>Producers Select a Producer.

Select the 3 dots in the upper right corner of the screen and select Configure

![](/legacyfs/online/storage/blog_attachments/2023/07/configure-1.png)

Configure Link

Select the Form that you want to configure (Note: there maybe more than customized for that you will have to configure.)

Select the grid as shown below to configure the Producer Master form.

![](/legacyfs/online/storage/blog_attachments/2023/07/grid.png)

Customizing the Form

Locate the Address component. Click and Drag the Address ribbon and place it where you want the Address section to be located.
Click Save.

![](/legacyfs/online/storage/blog_attachments/2023/07/addresspt1-1.png)

Placing the Address Ribbon

Close out the remaining open windows until you return to the Producer Master Screen.

The Address Section is now added to the Producer Master Screen.

![](/legacyfs/online/storage/blog_attachments/2023/07/AddressPt2.png)

Producer Master Screen with Address Added

In conclusion, a summary level view of entities is extremely helpful in troubleshooting issues as well a potential time saver for business users. It is easy to configure and is a "must do"!

More information on Entity Configuration can be found at: [https://help.sap.com/docs/APM\_ICM/d7c8dbefd0e64d75bdc6bf2a2e86b8e7/25896090b9694349a8c10e5aab32d924....](https://help.sap.com/docs/APM_ICM/d7c8dbefd0e64d75bdc6bf2a2e86b8e7/25896090b9694349a8c10e5aab32d924.html?LATEST)

Please Follow additional APMe resources at:

[APMe Questions](https://answers.sap.com/tags/73554900100800003792)

[APMe Blogs](https://blogs.sap.com/tags/73554900100800003792/)

Please feel free to share feedback or thoughts on this topic in a comment on this blog.

Labels

* [Technology Updates](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap/label-name/technology%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-sap%2Fadding-related-information-to-screens-in-apme%2Fba-p%2F13572472%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [1H 2026 Onboarding and Onboarding 1.0 Comp...