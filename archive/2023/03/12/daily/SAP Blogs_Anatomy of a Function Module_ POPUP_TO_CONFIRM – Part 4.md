---
title: Anatomy of a Function Module: POPUP_TO_CONFIRM – Part 4
url: https://blogs.sap.com/2023/03/11/anatomy-of-a-function-module-popup_to_confirm-part-4/
source: SAP Blogs
date: 2023-03-12
fetch_date: 2025-10-04T09:21:51.284475
---

# Anatomy of a Function Module: POPUP_TO_CONFIRM – Part 4

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

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47144&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Anatomy of a Function Module: POPUP\_TO\_CONFIRM – Part 4](/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-4/ba-p/13562505)

![serkansaglam](https://avatars.profile.sap.com/7/9/id792854d7ead7e95cc095dc0dada8fa8fe530068111165311d58e34b977d55692_small.jpeg "serkansaglam")

[serkansaglam](https://community.sap.com/t5/user/viewprofilepage/user-id/123447)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47144)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47144)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562505)

‎2023 Mar 11
9:22 PM

[7
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47144/tab/all-users "Click here to see who gave kudos to this post.")

2,352

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

*"...neque porro quisquam est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit..." ¹*

|  |
| --- |
| **Parts in This Blog Post**   * [Part 1](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-1/ba-p/13562360) - Introduction, Discovery, Function Interface, Flow Logic * [Part 2](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-2/ba-p/13562403) - Stories: Changing the Popup Icon, Customizing the Icons and Quick Info Buttons * [Part 3](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-3/ba-p/13562428) - Stories: Splitting Text into 48- and 57-Char Sentences and Starting on New Lines * [Part 4](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-4/ba-p/13562505) - Stories: Displaying an Unordered List, Displaying Longer Text Using a Document Object |

## Campfire

We have come to the last part of the series. In this last chapter:

* Story 5: Displaying an Unordered List
* Story 6: Displaying Longer Text Using a Document Object

## Story 5: Displaying an Unordered List

Now that we learned how to display sentences that start on new lines in the [previous](https://blogs.sap.com/2023/02/08/anatomy-of-a-function-module-popup_to_confirm-part-3/) chapter, let's use this for a scenario like displaying text with a bulleted list.

If you click Yes, the following steps will be performed:

* Check incompleteness
* Verify the data
* Update the document
* Log the errors

```
*--------------------------------------------------------------------*
* Anatomy of a Function Module: POPUP_TO_CONFIRM - Part 4
*
* Story 5: Displaying an Unordered List
*--------------------------------------------------------------------*

REPORT sy-repid.

CONSTANTS: newline VALUE cl_abap_char_utilities=>newline,
           maxlen  TYPE i VALUE 57.

DATA: question  TYPE string,
      answer(1).

question &&=:
  |If you click Yes, the following steps will be performed:| , newline,
  |• Check incompleteness|                                   , newline,
  |• Verify the data|                                        , newline,
  |• Update the document|                                    , newline,
  |• Log the errors|                                         , newline.

SPLIT question AT newline INTO TABLE DATA(segments).
CLEAR question.

LOOP AT segments ASSIGNING FIELD-SYMBOL(<segment>).
  DO COND #( WHEN strlen( <segment> ) EQ maxlen THEN 1 ELSE ( maxlen - strlen( <segment> ) ) ) TIMES.
    <segment> &&= | |.
  ENDDO.

  question &&= <segment>.
ENDLOOP.

question &&= newline.

CALL FUNCTION 'POPUP_TO_CONFIRM'
  EXPORTING
    text_question       = question
    userdefined_f1_help = '_'
  IMPORTING
    answer              = answer
  EXCEPTIONS
    OTHERS              = 2.
```

|  |  |
| --- | --- |
| ![](/legacyfs/online/storage/blog_attachments/2023/02/4-1a.png)  System 1: line-height: 1.75em | ![](/legacyfs/online/storage/blog_attachments/2023/02/4-1b.png)  System 2: line-height: 34px |

I activated the Info button to widen the popup in this example. If sentences fit 48 chars then you don't need to.
![:warning:](/html/@E1CCF9635AFAB77BCA511065FDB7EBE3/emoticons/26a0.png ":warning:")The only side effect of displaying the Info button by setting the parameter USER\_DEFINED\_F1\_HELP with a value that doesn't exist is that the following message is displayed when the user clicks that button.

No user-defined documentation available

## Story 6: Displaying Longer Text Using a Document Object

I mentioned the document object ARBFND\_DETAILED\_LONGTEXT in the [first](https://blogs.sap.com/2023/02/06/anatomy-of-a-function-module-popup_to_confirm-part-1/) part of this series. Now it's time to use it. First, let's take a look at whether this object exists and what it contains. To do this, please follow the steps below.

1. Launch transaction SE61.
2. Choose 'Dialog Text' in the 'Document Class' field.
3. Enter ARBFND\_DETAILED\_LONGTEXT in the 'Dialog Text' input field.
4. Click 'Display'

|  |  |
| --- | --- |
| ![](/legacyfs/online/storage/blog_attachments/2023/02/4-2a.png)  Transaction SE61 | ![](/legacyfs/online/storage/blog_attachments/2023/02/4-2b.png)  Document content |

As you can see the document object contains 70 placeholders. Every placeholder can contain 75 chars. We can populate these placeholders by populating the PARAMETER parameter.

Let's try to display the text below:

Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam quaerat voluptat...