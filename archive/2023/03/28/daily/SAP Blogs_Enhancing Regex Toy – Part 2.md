---
title: Enhancing Regex Toy – Part 2
url: https://blogs.sap.com/2023/03/27/enhancing-regex-toy-part-2/
source: SAP Blogs
date: 2023-03-28
fetch_date: 2025-10-04T10:51:02.107129
---

# Enhancing Regex Toy – Part 2

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Enhancing Regex Toy – Part 2

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46704&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Enhancing Regex Toy – Part 2](/t5/application-development-and-automation-blog-posts/enhancing-regex-toy-part-2/ba-p/13553367)

![former_member225588](https://avatars.profile.sap.com/former_member_small.jpeg "former_member225588")

[former\_member225588](https://community.sap.com/t5/user/viewprofilepage/user-id/225588)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46704)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46704)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553367)

‎2023 Mar 27
10:13 PM

[1
Kudo](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46704/tab/all-users "Click here to see who gave kudos to this post.")

702

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

This is the second in a series of six blogs describing how to enhance the regular expression tester known as Regex Toy, each blog describing a single enhancement to its capabilities.

### Before applying the second patch

The [preceding blog](https://blogs.sap.com/2023/03/26/enhancing-regex-toy-part-1/) in this series described how to patch a copy of Regex Toy to enable it to observe trailing blanks appearing in the regular expression pattern. Execute that enhanced copy of Regex Toy and follow these steps:

* Paste the following tongue twister into the Text block:

A skunk sat on a stump.  The skunk thunk the stump stunk and the stump thunk the skunk stunk.

* Place a check mark into the IN TABLE check box.

* Select the All Occurrences button.

* Specify in the Regex slot of the Input block the value “k “ – a lower case “k” followed by a single space.

* Press enter.

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-12.png)

As shown in the screen shot above, based on where our cursor is positioned when we hit enter, any trailing spaces specified in the Regex slot are observed when searching the Text block for matches, and the Matches block now shows the same six matches found by Regex Storm, as shown in the screen shot below:

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-13.png)

### The reason for the second patch

* Unlike Regex Storm, Regex Toy does not provide a way to see those spaces that match the regular expression pattern.

As illustrated above, Regex Storm uses alternating green and blue background colors to show matches, but Regex Toy uses a red foreground color, leaving spaces matching the pattern to appear the same way as spaces not matching it.

### Applying the second patch

Using your favorite ABAP editor, edit the copy of ABAP repository object DEMO\_REGEX\_TOY containing the first patch and place the series of lines shown below into method display after the final line of the REPLACE ALL OCCURRENCES OF series of statements (first and last lines, shown preceding and succeeding a comment line of all hyphens, already exist in the code as lines 183 and 185, respectively):

```
183      '@@tgr@@' IN TABLE result_it WITH '</b></font>'.

       " ------------------------------------

       " DEMO_REGEX_TOY enhancement #2

       " Change highlighting from single foreground color to

       " alternating background colors:

       constants    : color_red      type string

                        value 'color="#FF0000"'

                    , background_color_green

                                     type string

                        value 'style=background-color:"#B6D840"'

                    , background_color_blue

                                     type string

                        value 'style=background-color:"#98CCE8"'

                    .

       data         : color_toggle   type int4

                    , replacement_color

                                     type string

                    .

       clear sy-subrc.

       while sy-subrc is initial.

         color_toggle                = 01 - color_toggle.

         if color_toggle eq 00.

           replacement_color         = background_color_blue.

         else.

           replacement_color         = background_color_green.

         endif.

         replace first occurrence of color_red in table result_it

            with replacement_color.

       endwhile.

       " ------------------------------------

184

185    CLEAR result_html.
```

This is the same second patch unchanged from the E-bite. You should find, as I did recently, that with a NetWeaver 7.5 system this patch causes Regex Toy *to not work at all!* To make it work, you need to adjust the two values for the constants named background\_color\_green and background\_color\_blue, as shown below:

For the value of constant background\_color\_green,

from

```
value 'style=background-color:"#B6D840"'
```

to

```
value 'style="background-color:#B6D840"'
```

For the value of constant background\_color\_blue,

from

```
value 'style=background-color:"#98CCE8"'
```

to

```
value 'style="background-color:#98CCE8"'
```

Notice in both cases the subtle change is that the value following the HTML “style=” tag needs to include the string ‘background-color:’ within the quotation marks.

**Aside:** When I began researching why the original patch from the E-bite did not work anymore in my Netweaver 7.5 release, I learned that the HTML ‘font’ tag is no longer supported in HTML5, and that the ‘style’ tag is recommended to be used instead. I suppose I will never know whether that original patch actually worked or I had mistakenly moved the location of the opening quotation mark before the E-bite went to press, but assuming it did work, I suspect that, at some point after the Netweaver 7.4 release I originally used, SAP may have upgraded its support of HTML rendering to become compliant with HTML5, and may explain why the original patch was no longer recognized as valid HTML.

### After applying the second patch

Now activate the program and execute it using the same process described previously:

* Paste the same tongue twister into the Text block.

* Place a check mark into the IN TABLE check box.

* Select the All Occurrences button.

* Specify in the Regex slot of the Inpu...