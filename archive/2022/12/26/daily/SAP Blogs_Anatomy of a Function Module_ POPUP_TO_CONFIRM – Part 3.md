---
title: Anatomy of a Function Module: POPUP_TO_CONFIRM – Part 3
url: https://blogs.sap.com/2022/12/25/anatomy-of-a-function-module-popup_to_confirm-part-3/
source: SAP Blogs
date: 2022-12-26
fetch_date: 2025-10-04T02:30:59.262468
---

# Anatomy of a Function Module: POPUP_TO_CONFIRM – Part 3

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

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47140&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Anatomy of a Function Module: POPUP\_TO\_CONFIRM – Part 3](/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-3/ba-p/13562428)

![serkansaglam](https://avatars.profile.sap.com/7/9/id792854d7ead7e95cc095dc0dada8fa8fe530068111165311d58e34b977d55692_small.jpeg "serkansaglam")

[serkansaglam](https://community.sap.com/t5/user/viewprofilepage/user-id/123447)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47140)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47140)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562428)

‎2023 Feb 08
8:10 AM

[5
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47140/tab/all-users "Click here to see who gave kudos to this post.")

3,903

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

|  |
| --- |
| **Parts in This Blog Post**   * [Part 1](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-1/ba-p/13562360) - Introduction, Discovery, Function Interface, Flow Logic * [Part 2](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-2/ba-p/13562403) - Stories: Changing the Popup Icon, Customizing the Icons and Quick Info Buttons * [Part 3](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-3/ba-p/13562428) - Stories: Splitting Text into 48- and 57-Char Sentences and Starting on New Lines * [Part 4](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-4/ba-p/13562505) - Stories: Displaying an Unordered List, Displaying Longer Text Using a Document Object |

## Campfire

I know I told very simple stories in the [previous](https://blogs.sap.com/2023/02/07/anatomy-of-a-function-module-popup_to_confirm-part-2/) chapter. Now let's get into some details. I think this chapter is the most exciting, at least for me.

In this chapter:

* Different Code Versions
* Story 3: Splitting Text into 48-Char Sentences and Starting on New Lines
* Story 4: Splitting Text into 57-Char Sentences and Starting on New Lines

Before we begin, there is something important I need to tell you.

## Different Code Versions

Source code versions may differ between systems. While writing the 3rd and 4th stories, I tested my sample codes on two different systems. During my tests, I noticed that the line spacing of the sentences was different.

|  |  |
| --- | --- |
| ![](/legacyfs/online/storage/blog_attachments/2023/02/3-1a.png)  System 1: The line spacing seems normal. | ![](/legacyfs/online/storage/blog_attachments/2023/02/3-1b.png)  System 2: The line spacing is a bit much. |

First, I compared the versions of the programs that have the BUILD\_HTML subroutine. Since the last update dates are different, I scanned the codes to see how the HTML codes were generated. In debug mode, I grabbed the generated HTML codes. As you can see the "line-height" values are different.

|  |  |
| --- | --- |
| ![serkansaglam_0-1754583279902.png](/t5/image/serverpage/image-id/298075i78B96A077774BD5C/image-size/medium?v=v2&px=400 "serkansaglam_0-1754583279902.png") System 1 (last changed: 26.11.2018) | ![serkansaglam_2-1754583335154.png](/t5/image/serverpage/image-id/298078iDFAD9A891283756F/image-size/medium?v=v2&px=400 "serkansaglam_2-1754583335154.png") System 2 (last changed: 19.11.2020) |

It's important to know that line spacing can differ across systems because stories here are about splitting text into sentences and starting on new lines. Line spacing affects the number of lines that are visible without any action. In other words, it affects the number of lines that are visible in the visible area of the popup window. Of course, you can use the scrollbar to see the rest of the text.

## Story 3: Splitting Text into 48-Char Sentences and Starting on New Lines

I would like to display the following long text in a popup but each sentence must start on a new line:

Hello POPUP\_TO\_CONFIRM function module. Could you please display this message? But every sentence must start on a new line! There are a few limitations, but I know you can! You can even display one more sentence.

If we pass this text to the function, the output will be:

|  |  |
| --- | --- |
| ![](/legacyfs/online/storage/blog_attachments/2023/02/3-2a.png)  System 1: line-height: 1.75em | ![](/legacyfs/online/storage/blog_attachments/2023/02/3-2b.png)  System 2: line-height: 34px |

As we know the maximum width of the text can only be 48 or 57 characters *(the [first](https://blogs.sap.com/2023/02/06/anatomy-of-a-function-module-popup_to_confirm-part-1/) part of this blog series explains this)*, let's stick with it and try to display the message as follows:

Hello POPUP\_TO\_CONFIRM function module.
Could you please display this message?
But every sentence must start on a new line!
There are a few limitations, but I know you can!
You can even display one more sentence.

OK, but how can we do this? My plan is to split the text into segments, add the necessary spaces at the end of each, and then concatenate them again. The function module takes care of the rest *(I hope)*.

But we have an issue.

|  |
| --- |
| Mr. and Mrs. Brown Problem Since the ending (punctuation) marks that determine the end of a sentence are not used only at the end (as in the Mr. and Mrs. Brown example), I will create a text of sentences separated by a newline character in this story. |

OK, identifying a complete sentence is a different story. Let's execute the plan. Here is the recipe:

|  |  |
| --- | --- |
| **Step** | **Description** |
| 1 | Build a text by combining 5 sentences with a newline character between them. Since we do not use a user-defined button, each sentence can be up to 48 characters long. |
| 2 | Split the text into segments by "newline" characters. |
| 3 | Add the required number of spaces at the e...