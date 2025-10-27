---
title: Enhancing Regex Toy – Part 4
url: https://blogs.sap.com/2023/03/29/enhancing-regex-toy-part-4/
source: SAP Blogs
date: 2023-03-30
fetch_date: 2025-10-04T11:06:50.337985
---

# Enhancing Regex Toy – Part 4

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Enhancing Regex Toy – Part 4

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46749&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Enhancing Regex Toy – Part 4](/t5/application-development-and-automation-blog-posts/enhancing-regex-toy-part-4/ba-p/13553913)

![former_member225588](https://avatars.profile.sap.com/former_member_small.jpeg "former_member225588")

[former\_member225588](https://community.sap.com/t5/user/viewprofilepage/user-id/225588)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46749)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46749)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553913)

‎2023 Mar 29
10:13 PM

[1
Kudo](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46749/tab/all-users "Click here to see who gave kudos to this post.")

662

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

This is the fourth in a series of six blogs describing how to enhance the regular expression tester known as Regex Toy, each blog describing a single enhancement to its capabilities.

### Before applying the fourth patch

The [preceding blog](https://blogs.sap.com/2023/03/28/enhancing-regex-toy-part-3/) in this series described how to patch a copy of Regex Toy to enable it to identify matches even when the matching text straddles implicit line breaks, but ended with a description of an issue whereby Regex Toy formats text in the Matches block such that it runs beyond the visible area of the window and is accompanied by a horizontal scroll bar. To illustrate this problem again, execute the enhanced Regex Toy and follow these steps:

* Paste the following tongue twister into the Text block:

A skunk sat on a stump.  The skunk thunk the stump stunk and the stump thunk the skunk stunk.

* Place a check mark into the IN TABLE check box.

* Select the All Occurrences button.

* Specify in the Regex slot of the Input block the following string

the skunk

* Press enter.

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-22.png)

As shown in the screen shot above, the text runs off to the right of the visible area of the Matches window, requiring the use of the horizontal scroll bar to see it.

Now do the same with Regex Storm, selecting the checkbox for Ignore Case:

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-23.png)

As shown in the screen shot above, with Regex Storm the text does not run off to the right of the visible area of the Input block.

### The reason for the fourth patch

* Unlike Regex Storm, Regex Toy does not facilitate keeping the text shown in the Matches block from running beyond the constraints of the visible area of the Matches window.

### Applying the fourth patch

Using your favorite ABAP editor, edit the copy of ABAP repository object DEMO\_REGEX\_TOY containing the previous patches and apply the following 2-step change in method display:

1. Ahead of the CONCATENATE LINES OF statement, insert the following set of lines (first and last lines, shown preceding and succeeding a comment line of all hyphens, already exist in the code as lines 216 and 217, respectively):

```
216   APPEND '<html><body><font face="Arial monospaced for ...

      " -----------------------------------

      " DEMO_REGEX_TOY enhancement #4

      " Format result text using approximate window width

      " specified by line_len:

      constants     : html_space     type string value '&nbsp;'

                    , html_special_character_start

                                     type string value '&'

                    , html_special_character_end

                                     type string value ';'

                    , html_format_start

                                     type string value '<'

                    , html_format_end

                                     type string value '>'

                    .

      data          : visible_text_length

                                     type int4

                    , html_last_space_length

                                     type int4

                    , cause_line_break

                                     type flag

                    , html_string    type string

                    , html_excess    type string

                    , html_stack     type standard table

                                       of string

                    .

      loop at result_it

         into result_wa.

        clear: html_string, visible_text_length.

        while strlen( result_wa ) gt 00.

          case result_wa+00(01).

            when html_format_start.

              while result_wa+00(01) ne html_format_end.

                concatenate html_string

                            result_wa+00(01)

                       into html_string.

                shift result_wa left by 01 places.

              endwhile.

            when html_special_character_start.

              if strlen( result_wa ) ge 06.

                if result_wa+00(06) eq html_space.

                  if visible_text_length gt line_len.

                    cause_line_break = abap_true.

                  endif.

                endif.

              endif.

              while result_wa+00(01) ne

                    html_special_character_end.

                concatenate html_string

                            result_wa+00(01)

                       into html_string.

                shift result_wa left by 01 places.

              endwhile.

              add 01 to visible_text_length.

              if cause_line_break eq abap_false.

                html_last_space_length

                                     = strlen( html_string ) + 01.

              endif.

            when others.

              add 01 to visible_text_length.

          endcase.

          concatenate html_string

                      result_wa+00(01)

                 into html_string.

          shift result_wa left by 01 places.

          if cause_line_break eq abap_true.

            clear html_excess.

            if html_last_space_length gt 00.

              html_excess =

                     substring( val = html_string

                                off = html_last_space_length )...