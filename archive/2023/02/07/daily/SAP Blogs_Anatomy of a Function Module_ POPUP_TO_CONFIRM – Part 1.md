---
title: Anatomy of a Function Module: POPUP_TO_CONFIRM – Part 1
url: https://blogs.sap.com/2023/02/06/anatomy-of-a-function-module-popup_to_confirm-part-1/
source: SAP Blogs
date: 2023-02-07
fetch_date: 2025-10-04T05:51:12.509041
---

# Anatomy of a Function Module: POPUP_TO_CONFIRM – Part 1

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Anatomy of a Function Module: POPUP\_TO\_CONFIRM – P...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47133&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Anatomy of a Function Module: POPUP\_TO\_CONFIRM – Part 1](/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-1/ba-p/13562360)

![serkansaglam](https://avatars.profile.sap.com/7/9/id792854d7ead7e95cc095dc0dada8fa8fe530068111165311d58e34b977d55692_small.jpeg "serkansaglam")

[serkansaglam](https://community.sap.com/t5/user/viewprofilepage/user-id/123447)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47133)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47133)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562360)

‎2023 Feb 06
7:54 PM

[12
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47133/tab/all-users "Click here to see who gave kudos to this post.")

16,336

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

*"I'm not a scientist, just a traveler"*¹

|  |
| --- |
| **Parts in This Blog Post**   * [Part 1](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-1/ba-p/13562360) - Introduction, Discovery, Function Interface, Flow Logic * [Part 2](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-2/ba-p/13562403) - Stories: Changing the Popup Icon, Customizing the Icons and Quick Info Buttons * [Part 3](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-3/ba-p/13562428) - Stories: Splitting Text into 48- and 57-Char Sentences and Starting on New Lines * [Part 4](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-4/ba-p/13562505) - Stories: Displaying an Unordered List, Displaying Longer Text Using a Document Object |

## Introduction

*When I need something, I look for it in the nearest place.*SAP standard codes are my main resource when it comes to ABAP development. That's why I usually lose myself in SAP codes. It's a kind of journey. The good thing is, I always get something useful from SAP at the end of every journey.

*That's why I'm a traveler.*Let me tell you about one of them. Before starting this journey, your SAP backpack should contain some ABAP knowledge, the POPUP\_TO\_CONFIRM function module, and optionally the ARBFND\_DETAILED\_LONGTEXT document object.

This journey will include the following sections including six campfire stories (*two stories in each next post)*

* Discovery
  + What is POPUP\_TO\_CONFIRM?
  + The Moment I Feel a Journey Approaching
  + Experiment: Newline Character and HTML <br> Tag
  + Function Interface (Parameters)
  + Flow Logic

* Campfire

+ Story 1: Changing the Popup Icon
+ Story 2: Customizing the Icons and Quick Info of Buttons
+ Story 3: Splitting Text into 48-Char Sentences and Starting on New Lines
+ Story 4: Splitting Text into 57-Char Sentences and Starting on New Lines
+ Story 5: Displaying an Unordered List
+ Story 6: Displaying Longer Text Using a Document Object

## Discovery

### What is POPUP\_TO\_CONFIRM?

POPUP\_TO\_CONFIRM is a standard function module used to display a message (question, document object text, or both) in a modal dialog box, and also to ask users to decide. I recommend reading the documentation before using it. To do this, please follow the steps below.

1. Launch transaction SE37.
2. Enter POPUP\_TO\_CONFIRM in the Function Module input field.
3. From the top menu, choose *Goto* → *Documentation* → *Function Module Documentation*.

### The Moment I Feel a Journey Approaching

I was writing an ABAP program that reads spreadsheet data from a Microsoft Excel file and creates a Purchasing Contract² in an SAP S/4HANA 2020 On-Premise system. The user selects a file, executes the program, and then the program uploads the file, displays the content, and performs an incompleteness check. If everything is fine, the user clicks the "Create Contract" button. To prevent accidental button clicks, the program displays the following message and asks for a confirmation.

|  |
| --- |
| ![](/legacyfs/online/storage/blog_attachments/2023/02/1-1-1.png) *An example output of the POPUP\_TO\_CONFIRM function* |

Since the second sentence was broken, a possible request would be: *"As a user, I want to see the sentences of the message start on new lines so I can read them easily"*

### Experiment: Newline Character and HTML <br> Tag

I wondered if I could make each sentence start on a new line. My first attempt was to insert a newline character (CL\_ABAP\_CHAR\_UTILITIES=>NEWLINE) between sentences (*which is probably the first thing that comes to mind*). Of course, it didn't work! Then, I started to analyze the codes of the function. When I understand the logic and noticed a few hard-coded values, I thought I could achieve something useful.

*Welcome to the anatomy of the POPUP\_TO\_CONFIRM function module!*

### Function Interface (Parameters)

Let's first explore some of the parameters.

##### TEXT\_QUESTION Parameter

The POPUP\_TO\_CONFIRM function displays the text in an HTML container. Therefore, it splits the TEXT\_QUESTION text into segments to populate an HTML table. The function uses the TEXT\_SPLIT function to do this but, sentences in the text do not start on new lines and there is no parameter to control this. In the meantime, a quick note about the TEXT\_SPLIT function. It splits the input text once in the specified line length word-compatibly. See the function's documentation for more details.

Here, we should keep in mind that we can send a maximum of 400 characters to the TEXT\_QUESTION parameter which is already mentioned in the function module documentation. That means more than 400 characters will be truncated. It is a possible risk that the last sentence is displayed incompletely.

##### USERDEFINED\_F1\_HELP Parameter

The USERDEFINED\_F1\_HELP parameter is used to provide information from a document object. When used, a third button labeled "Info" a...