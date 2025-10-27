---
title: My favourite SAP Cloud Integration feature: Content Filter
url: https://blogs.sap.com/2023/08/06/my-favourite-sap-cloud-integration-feature-content-filter/
source: SAP Blogs
date: 2023-08-07
fetch_date: 2025-10-04T11:59:35.249597
---

# My favourite SAP Cloud Integration feature: Content Filter

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* My favourite SAP Cloud Integration feature: Conten...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/164187&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [My favourite SAP Cloud Integration feature: Content Filter](/t5/technology-blog-posts-by-members/my-favourite-sap-cloud-integration-feature-content-filter/ba-p/13573911)

![MortenWittrock](https://avatars.profile.sap.com/a/c/idacebc534385e25d225809532ec3f91b5eae441a1a8a68f11f97ab7007c42df73_small.jpeg "MortenWittrock")

![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor")
[MortenWittrock](https://community.sap.com/t5/user/viewprofilepage/user-id/40)

SAP Mentor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=164187)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/164187)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13573911)

‎2023 Aug 06
6:00 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/164187/tab/all-users "Click here to see who gave kudos to this post.")

8,053

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2023/08/filter.jpg)

August has come around and it's time for part five of this [blog post series](https://blogs.sap.com/tag/myfavouritesapcifeature/), where I interview SAP Cloud Integration practitioners, developers, architects and enthusiasts about their favourite feature of the platform. For this installment, I'm talking to a luminary of the SAP integration community and a frequent Featured Contributor here on the SAP Community site: shriprasad.bhat. Let's get the interview started!

*Could you introduce yourself briefly, please?*

My name is Sriprasad Shivaram Bhat and I am currently working as an Enterprise Integration Specialist at British Telecom. I started my contribution to the community in 2015, focusing on the SAP Cloud Integration topic. Most of my time in here goes towards answering questions and giving them solutions, which makes me happy. I also write blogs when I would like to go deeper on some topic.

*Thank you! On to the central question of this blog post series: What’s your favourite SAP Cloud* *Integration feature?*

I have multiple features on my list but let us consider Content Filter this time. It is one of the most useful features for working with XML data. In my early days of blogging, I [wrote about this feature](https://blogs.sap.com/2017/06/01/sap-cloud-platform-integration-content-filter-in-detail/) and that blog still holds true today for most of the use cases.

*Why that particular feature?*

The Content Filter step comes in very handy when you want to manipulate XML data. This step helps to perform various XML operations like filtering, sorting and using different XPath functions without writing JavaScript or Groovy scripts. SAP Cloud Integration’s Content Filter supports XPath 3.0, which enables us to write kind of small XSLT lookalike functions in Content Filter.

Here's an example: We want to filter out the full-time employees and then sort their records based on their employee ID. The input XML looks like this:

```
<?xml version="1.0" encoding="UTF-8"?>

<Root>

	<Record>

		<employeeType>FTE</employeeType>

		<emplID>1</emplID>

		<emplName>C</emplName>

	</Record>

	<Record>

		<employeeType>CE</employeeType>

		<emplID>2</emplID>

		<emplName>BB</emplName>

	</Record>

	<Record>

		<employeeType>FTE</employeeType>

		<emplID>3</emplID>

		<emplName>B</emplName>

	</Record>

	<Record>

		<employeeType>FTE</employeeType>

		<emplID>5</emplID>

		<emplName>A</emplName>

	</Record>

</Root>
```

This can be solved with a single Content Filter expression:

`sort(/Root/Record[employeeType = 'FTE'],(),function($Record) { $Record/emplID })`

This is the output:

```
<Record>

	<employeeType>FTE</employeeType>

	<emplID>1</emplID>

	<emplName>C</emplName>

</Record>

<Record>

	<employeeType>FTE</employeeType>

	<emplID>3</emplID>

	<emplName>B</emplName>

</Record>

<Record>

	<employeeType>FTE</employeeType>

	<emplID>5</emplID>

	<emplName>A</emplName>

</Record>
```

*How do you see this feature evolving going forward?*

Here are some additional options that I would like to see made available for Content Filter:

* Support for other data types like JSON and plain text content.

* An explicit option to add a root element (at the moment we need to have a Content Modifier after the Content Filter to do this).

* Additional support for using properties and headers (currently it's limited to the contains operator).

* Support for removing nodelists that match certain conditions. For example, in an SAP SuccessFactors Compound Employee response, remove some specific Employment Info records and return the rest of the XML as it is.

*Thanks for joining this blog post series, Sriprasad - I appreciate it a lot!*

* [MyFavouriteSAPCIFeature](/t5/tag/MyFavouriteSAPCIFeature/tg-p/board-id/technology-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fmy-favourite-sap-cloud-integration-feature-content-filter%2Fba-p%2F13573911%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Thursday
* [Unlocking SAP Fiori and other business content on Mobile: A Practical Guide](/t5/technology-blog-posts-by-sap/unlocking-sap-fiori-and-other-business-content-on-mobile-a-practical-guide/ba-p/14230532)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [How to Send Custom Headers (e.g., Transaction-Id) in HTTP PATCH Request from SAP CPI](/t5/technol...