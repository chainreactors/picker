---
title: S/4Hana Git-enabled CTS – Part 1 – Steps towards devops
url: https://blogs.sap.com/2022/11/19/s-4hana-git-enabled-cts-part-1/
source: SAP Blogs
date: 2022-11-20
fetch_date: 2025-10-03T23:16:58.053892
---

# S/4Hana Git-enabled CTS – Part 1 – Steps towards devops

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* S/4Hana Git-enabled CTS - Part 1 - Steps towards d...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160778&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [S/4Hana Git-enabled CTS - Part 1 - Steps towards devops](/t5/technology-blog-posts-by-members/s-4hana-git-enabled-cts-part-1-steps-towards-devops/ba-p/13554420)

![Naveen](https://avatars.profile.sap.com/8/3/id831388c7190ffb2136db1e14f2a2adad8043e1c02bb16c6c019b5a8348cd49e0_small.jpeg "Naveen")

[Naveen](https://community.sap.com/t5/user/viewprofilepage/user-id/1934)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160778)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160778)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554420)

‎2022 Nov 19
11:22 AM

[13
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160778/tab/all-users "Click here to see who gave kudos to this post.")

7,269

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [DevOps](https://community.sap.com/t5/c-khhcw49343/DevOps/pd-p/51112e3c-4b78-4058-a637-67f453c196c9)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [DevOps

  Programming Tool](/t5/c-khhcw49343/DevOps/pd-p/51112e3c-4b78-4058-a637-67f453c196c9)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (7)

Hello All,

In this blog i am going to talk about Git-enabled CTS which is a fiori app and available since S/4Hana 1909 onwards. I am using S/4Hana 2021 for showing gCTS Capabilities.

And how it is helping to automate ABAP objects testing and deployments.

What is Git-enabled CTS?

SAP aims to support continuous integration in an ABAP environment and to allow development processes in ABAP to be aligned with development processes that are commonly used for other development environments or languages.

This has two main components:

* Git-based versioning, including branch and merge support

* Options to connect your ABAP processes with continuous integration (CI) tools

This will be provided by extending the ABAP Change and Transport System (“CTS”). This new set of CTS features is referred to as “git-enabled CTS” (“gCTS”).

Git repositories will be used to store released ABAP transport requests. To configure connections between Git repositories and ABAP, and manage commits / development objects stored in these repositories, a UI is provided which offers the following:

* Subscribe to one or more Git reposititories where ABAP content is provided for the ABAP target systems

* Trigger updates

* Display the system"s attributes and also the subscribed Git repositories

* Select one of the repositories, display its attributes, and the avalable commit IDs

* Select one of the commit IDs to update the ABAP system with the content that is necessary to bring it to exactly the selected software state, or update a system to "the latest" state

* Configuration options:register new repositories, edit existing ones, populate a new system with initial content, delete a repository subscription

1 Git-enabled Fiori - here you can find are the dependency to enable fiori app in fiori launchpad

<https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F4158')/S24OP>

2. Fiori tile in FIori launchpad-

After assigning the required roles , users will be able to see fiori tile in fiori launchpad.

![](/legacyfs/online/storage/blog_attachments/2022/11/gCTS-Tile.png)

gCTS Tile

3. gCTS Home page

![](/legacyfs/online/storage/blog_attachments/2022/11/gCTS-Main-Page.png)

Home page of gCTS

4. Enable gCTS - All the required information such as gCTS Directory, Java Runtime, Git Client etc. information has to be provided.

![](/legacyfs/online/storage/blog_attachments/2022/11/Enable-gCTS-1.png)

Enable gCTS

5. Health check - all should be green in order to make the proper communications

![](/legacyfs/online/storage/blog_attachments/2022/11/HealthCheck.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/HealthCheck-2.png)

Health check

6. Multiple Repository can be created from here - ABAP objects can be segregated -- Waoo this is cool

![](/legacyfs/online/storage/blog_attachments/2022/11/Select-Repositery.png)

You can have multiple Git Repositery and multiple vSID in your system for pushing the objects.

![](/legacyfs/online/storage/blog_attachments/2022/11/Create1.png)

This is private repository where i have already having required configuration, let me go inside.

![](/legacyfs/online/storage/blog_attachments/2022/11/Multiple-Repositery.png)

Now we are inside the Repositories where you can see all the relevant information such as GitHub url, Type, vSID, git branch, commit, configurations, activities , etc.

![](/legacyfs/online/storage/blog_attachments/2022/11/commit22.png)

Now let me talk about how it is working -

Once we enabled gCTS in FIori after providing all the required information such as Gitpath, vSID etc.

Automatically S4P Transport  target would be created in the system where your fiori launchpad resides. And whatever transports are part of S4P Transport target that would be pushed in Fiori gCTS apps as well as git repository.

Note - You can give any name in my case S4P ![:slightly_smiling_face:](/html/@CB193FD929C1B3F628B5259D5B23C3AB/emoticons/1f642.png ":slightly_smiling_face:")

Target in SE01 you can see when you create Transports.

![](/legacyfs/online/storage/blog_attachments/2022/11/Se01.png)

S4P gCTS generated Target

![](/legacyfs/online/storage/blog_attachments/2022/11/transport.png)

Once Transport will be released , objects would be commited in gCTS fiori app as well as ...