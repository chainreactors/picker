---
title: Enhancing Regex Toy – Part 3
url: https://blogs.sap.com/2023/03/28/enhancing-regex-toy-part-3/
source: SAP Blogs
date: 2023-03-29
fetch_date: 2025-10-04T11:01:04.224709
---

# Enhancing Regex Toy – Part 3

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Enhancing Regex Toy – Part 3

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46748&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Enhancing Regex Toy – Part 3](/t5/application-development-and-automation-blog-posts/enhancing-regex-toy-part-3/ba-p/13553886)

![former_member225588](https://avatars.profile.sap.com/former_member_small.jpeg "former_member225588")

[former\_member225588](https://community.sap.com/t5/user/viewprofilepage/user-id/225588)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46748)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46748)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553886)

‎2023 Mar 28
9:16 PM

[2
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46748/tab/all-users "Click here to see who gave kudos to this post.")

653

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

This is the third in a series of six blogs describing how to enhance the regular expression tester known as Regex Toy, each blog describing a single enhancement to its capabilities.

### Before applying the third patch

The [preceding blog](https://blogs.sap.com/2023/03/27/enhancing-regex-toy-part-2/) in this series described how to patch a copy of Regex Toy to enable it to identify spaces matching the regular expression pattern, but ended with a description of an issue where Regex Toy does not find pattern matches where the text supplied in the Text block implicitly straddles line breaks. To illustrate this problem again, execute the enhanced Regex Toy and follow these steps:

* Paste the following tongue twister into the Text block:

A skunk sat on a stump.  The skunk thunk the stump stunk and the stump thunk the skunk stunk.

* Place a check mark into the IN TABLE check box.

* Select the All Occurrences button.

* Specify in the Regex slot of the Input block the following string

the skunk

* Press enter.

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-17.png)

As shown in the screen shot above, it finds only one of the two occurrences of the regular expression pattern. The second occurrence starts at the end of the first line and continues onto the next line.

Now do the same with Regex Storm, selecting the checkbox for Ignore Case:

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-18.png)

Perhaps that is not a fair comparison because the string “the skunk” in the tongue twister does not implicitly straddle lines in the Regex Storm example above. This is easily rectified by by placing as many spaces after the final word “thunk” such that the final string “the skunk” does straddle two lines in Regex Storm:

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-19.png)

As shown in the screen shot above, now the second occurrence of “the skunk” does straddle two lines, and it is found and highlighted accordingly by Regex Storm.

### The reason for the third patch

* Unlike Regex Storm, Regex Toy does not enable string matching across implicit line breaks.

### Applying the third patch

Using your favorite ABAP editor, edit the copy of ABAP repository object DEMO\_REGEX\_TOY containing the previous patches and apply the following 4-step change:

The first change is to be applied in method init:

1. Change line

```
wordwrap_to_linebreak_mode = cl_gui_textedit=>true.
```

to

```
wordwrap_to_linebreak_mode = cl_gui_textedit=>false.
```

The remaining changes are to be applied in method main:

2. Comment out the SPLIT statement following the statement

```
cl_gui_cfw=>flush( ).
```

3. Change the IN TABLE clauses of all FIND and REPLACE … IN TABLE … statements (six in all) in the TRY-ENDTRY block from

```
... IN TABLE result_it ...
```

to

```
... IN text_wa ...
```

4. Copy the commented SPLIT statement (commented out in step 2 above) and place it ahead of the display( ) statement as an active line.

This is the same third patch unchanged from the E-bite. However, if your system is NetWeaver 7.5, then that is not the end of the required changes. The TRY statement of the TRY-ENDTRY block referenced in step 3 above now appears in the patched version of this program on line 101 and is followed by an IF statement on line 102:

```
101      TRY.

102          IF in_table = ‘X’.
```

This IF statement did not exist in the NetWeaver 7.4 version. The variable is new in the Regex Toy selection screen definition and correlates to the new IN TABLE checkbox appearing in the Options block:

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-20.png)

After applying all the changes noted above in steps 1 through 4, you now should see an ELSE statement on line 124 and its ENDIF on line 149. Much of this code is a copy of the same six FIND and REPLACE statements you just changed according to step 3 above, but in these cases the statements do not include the word TABLE following their IN clauses.. All of these statements also will require the same relative change, this time replacing the operand result\_string with text\_wa.

**Aside:** In the E-bite, I had mentioned this about Regex Toy ...

If you click the Documentation about Regular Expressions button at the top of the screen, you’re taken to the standard SAP online documentation on RegExes.

At that time, prior to the introduction of the IN TABLE checkbox, all of the capabilities offered by Regex Toy seemed to be intuitive, so I was unconcerned about its lack of documentation describing the utility itself. But now with the introduction of the IN TABLE checkbox, it is no longer so intuitive; a user would have no reason to understand what capability of regular expressions this checkbox controls. The new IF statement noted above is one of two places where the corresponding in\_table variable controls the processing:

* + When checked it causes 1) the lines of specified Text, already placed into corresponding rows of an internal table of type string, to use the IN TABLE variation of the FIND and REPLACE statements to perform the regular expression processing, as well as 2) replacing each space in the text with its correct HTML code counterpart: “&nbsp;”. This corresponds to the way the utility behaved in NetWeaver 7.4.

  + When not checked it causes 1) thos...