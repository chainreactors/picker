---
title: Anatomy of a Function Module: POPUP_TO_CONFIRM – Part 2
url: https://blogs.sap.com/2023/02/07/anatomy-of-a-function-module-popup_to_confirm-part-2/
source: SAP Blogs
date: 2023-02-08
fetch_date: 2025-10-04T05:58:21.322893
---

# Anatomy of a Function Module: POPUP_TO_CONFIRM – Part 2

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

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47139&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Anatomy of a Function Module: POPUP\_TO\_CONFIRM – Part 2](/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-2/ba-p/13562403)

![serkansaglam](https://avatars.profile.sap.com/7/9/id792854d7ead7e95cc095dc0dada8fa8fe530068111165311d58e34b977d55692_small.jpeg "serkansaglam")

[serkansaglam](https://community.sap.com/t5/user/viewprofilepage/user-id/123447)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47139)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47139)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562403)

‎2023 Feb 07
8:52 PM

[4
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47139/tab/all-users "Click here to see who gave kudos to this post.")

7,547

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

|  |
| --- |
| **Parts in This Blog Post**   * [Part 1](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-1/ba-p/13562360) - Introduction, Discovery, Function Interface, Flow Logic * [Part 2](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-2/ba-p/13562403) - Stories: Changing the Popup Icon, Customizing the Icons and Quick Info Buttons * [Part 3](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-3/ba-p/13562428) - Stories: Splitting Text into 48- and 57-Char Sentences and Starting on New Lines * [Part 4](https://community.sap.com/t5/application-development-and-automation-blog-posts/anatomy-of-a-function-module-popup-to-confirm-part-4/ba-p/13562505) - Stories: Displaying an Unordered List, Displaying Longer Text Using a Document Object |

## Campfire

As explored in the [previous](https://blogs.sap.com/2023/02/06/anatomy-of-a-function-module-popup_to_confirm-part-1/) chapter, we have a powerful function module that we can use for different scenarios. Now that we have discovered it, let’s build a campfire and tell some stories.

In this chapter:

* Story 1: Changing the Popup Icon
* Story 2: Customizing the Icons and Quick Info of Buttons

## Story 1: Changing the Popup Icon

I know this is a bedtime story for 0-3 age but let's refresh our memories. We can change the popup icon displayed on the left. To do this, we simply specify an icon name starting with ICON\_MESSAGE\_ in the POPUP\_TYPE parameter.

```
DATA answer.

DO 5 TIMES.
  DATA(popup_type) = SWITCH icon-name( sy-index
                       WHEN 1 THEN 'ICON_MESSAGE_INFORMATION'
                       WHEN 2 THEN 'ICON_MESSAGE_WARNING'
                       WHEN 3 THEN 'ICON_MESSAGE_ERROR'
                       WHEN 4 THEN 'ICON_MESSAGE_QUESTION'
                       WHEN 5 THEN 'ICON_MESSAGE_CRITICAL' ).

  CALL FUNCTION 'POPUP_TO_CONFIRM'
    EXPORTING
      text_question = popup_type
      popup_type    = popup_type
    IMPORTING
      answer        = answer
    EXCEPTIONS
      OTHERS        = 2.
ENDDO.
```

When we run the above code, the popup will be displayed a total of 5 times, each time with a different icon.

|  |
| --- |
| ![](/legacyfs/online/storage/blog_attachments/2023/02/2-1-1.png)![](/legacyfs/online/storage/blog_attachments/2023/02/2-2-1.png)![](/legacyfs/online/storage/blog_attachments/2023/02/2-3-1.png)![](/legacyfs/online/storage/blog_attachments/2023/02/2-4-1.png)![](/legacyfs/online/storage/blog_attachments/2023/02/2-5-1.png)  *The appearance of different icons in the popup window* |

Most used icons:

* ICON\_MESSAGE\_INFORMATION
* ICON\_MESSAGE\_WARNING
* ICON\_MESSAGE\_ERROR
* ICON\_MESSAGE\_QUESTION
* ICON\_MESSAGE\_CRITICAL

You can find all icons starting with ICON\_MESSAGE\_ by displaying the ICON table or by running the SHOWICON program.

## Story 2: Customizing the Icons and Quick Info of Buttons

It is also possible to customize the icons of the first two buttons. I just wanted to include this here because sometimes it may be necessary to highlight a button with a striking icon.

```
DATA answer.

CALL FUNCTION 'POPUP_TO_CONFIRM'
  EXPORTING
    text_question         = 'What is Lorem ipsum?'
    text_button_1         = 'I know'
    icon_button_1         = 'ICON_OKAY'
    text_button_2         = 'No idea'
    icon_button_2         = 'ICON_DUMMY'
    popup_type            = 'ICON_MESSAGE_QUESTION'
    iv_quickinfo_button_1 = 'But I won''t say'
    iv_quickinfo_button_2 = 'Please tell me'
  IMPORTING
    answer                = answer
  EXCEPTIONS
    OTHERS                = 2.
```

|  |
| --- |
| ![](/legacyfs/online/storage/blog_attachments/2023/02/2-6-1.png)*Quick info appears when you hover the mouse over the first two buttons* |

Since the texts are set from text elements, we are unable to change the icon and texts of the last two buttons 'Info' and 'Cancel' (*'Info' appears when a document object is used*).

```
button_3 = 'Info'(201).
button_4 = 'Abbrechen'(200).
```

However, these texts will be displayed in the login language.

## Conclusion

In this blog post, you have learned how to customize the appearance of the POPUP\_TO\_CONFIRM function by changing the left icon and the icons of the first two buttons. You've also learned to display a hint when users hover the mouse over these buttons. These may be very simple details, but they are actually important for user-friendly development.

I know these stories are not for senior developers but may be helpful for beginners. But don't miss the next part. We'll dive quite deeper. I call it "Operation 48/57".

Upcoming stories:

* Story 3: Splitting Text into 48-Char Sentences and Starting on New Lines
* Story 4: Splitting Text into 57-Char Sentences and Starting on New Lines

See you in the [next](https://blogs.sap.com/2023/02/08/anatomy-of-a-function-module-popup_to_confirm-part-3/) chapter.

|  |
| --- |
| **Trademarks**   * SAP®, ABAP® are the trademarks or registered trademarks of SAP SE or its affiliates in Germany and in other countries...