---
title: Enhancing Regex Toy – Part 5
url: https://blogs.sap.com/2023/03/30/enhancing-regex-toy-part-5/
source: SAP Blogs
date: 2023-03-31
fetch_date: 2025-10-04T11:14:27.423675
---

# Enhancing Regex Toy – Part 5

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Enhancing Regex Toy – Part 5

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46750&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Enhancing Regex Toy – Part 5](/t5/application-development-and-automation-blog-posts/enhancing-regex-toy-part-5/ba-p/13553974)

![former_member225588](https://avatars.profile.sap.com/former_member_small.jpeg "former_member225588")

[former\_member225588](https://community.sap.com/t5/user/viewprofilepage/user-id/225588)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46750)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46750)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553974)

‎2023 Mar 30
10:22 PM

0
Kudos

678

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

This is the fifth in a series of six blogs describing how to enhance the regular expression tester known as Regex Toy, each blog describing a single enhancement to its capabilities.

### Before applying the fifth patch

The [preceding blog](https://blogs.sap.com/2023/03/29/enhancing-regex-toy-part-4/) in this series described how to patch a copy of Regex Toy to enable it to prevent text in the Matches block from running beyond the visible area of the window, but ended with a description of an issue whereby Regex Toy now ignores explicit line breaks. To illustrate this problem again, execute the enhanced Regex Toy and follow these steps:

* Paste the following first sentence of the tongue twister into the Text block:

A
skunk
sat
on
a
stump.

such that each word is followed by an explicit line break placing it on its own line as shown above.

* Place a check mark into the IN TABLE check box.

* Select the All Occurrences button.

* Specify a single dot character in the Regex slot

* Press enter.

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-29.png)

As shown in the screen shot above, you should find that now every character of the Text matches the regular expression pattern, as it should, but now the text no longer is formatted in the Matches window with the explicit line breaks provided with the content in the Text window.

Now do the same with Regex Storm:

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-28.png)

As shown in the screen shot above, Regex Storm does observe and retain explicit line breaks.

### The reason for the fifth patch

* Unlike Regex Storm, Regex Toy does not observe explicit line breaks when presenting the matching text in the Matches block.

### Applying the fifth patch

Using your favorite ABAP editor, edit the copy of ABAP repository object DEMO\_REGEX\_TOY containing the previous patches and apply the following 2-step change in method main:

1 After the TRY statement, insert the following set of lines (first and last lines, shown preceding and succeeding a comment line of all hyphens, already exist in the code as lines 101 and 102, respectively):

```
101      TRY.

             " ------------------------------------

             " DEMO_REGEX_TOY enhancement #5

             " Convert two-character carriage-return/line-feed into

             " single-character form feed to prevent split during

             " search for any character:

             replace all occurrences

                  of cl_abap_char_utilities=>cr_lf in text_wa

                with cl_abap_char_utilities=>form_feed.

             " ------------------------------------

102          IF in_table = 'X'.
```

2. Also, change the AT clause of the SPLIT statement, following the ENDTRY statement, from

```
... AT cr_lf ...
```

to

```
... AT cl_abap_char_utilities=>form_feed ...
```

This is nearly the same fifth patch unchanged from the E-bite other than the fact that the IF statement following the TRY statement is new with the NetWeaver 7.5 version of this utility, and that the AT clause of the SPLIT statement was changed to replace the original 7.4-version operand cl\_abap\_char\_utilities=>cr\_lf with cr\_lf.

### After applying the fifth patch

Now activate the program and execute it using the same process described previously:

* Paste the following first sentence of the tongue twister into the Text block:

A
skunk
sat
on
a
stump.

such that each word is followed by an explicit line break placing it on its own line as shown above.

* Place a check mark into the IN TABLE check box.

* Select the All Occurrences button.

* Specify a single dot character in the Regex slot

* Press enter.

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-30.png)

As shown in the screen shot above, you should find that now Regex Toy retains and observes the explicit line breaks with the content supplied in the Text block.

### What’s next?

There are no more patches from the E-bite, but in the third blog of this series we discovered that the new IN TABLE checkbox causes consecutive blanks of content in the Text block to be ignored when it is presented in the Matches block. So let’s execute Regex Toy using a scenario that illustrates this behavior:

* Paste the following tongue twister into the Text block:

A skunk sat on a stump.  The skunk thunk the stump stunk and the stump thunk the skunk stunk.

* Place a check mark into the IN TABLE check box.

* Select the All Occurrences button.

* Specify a dot in the Regex slot of the Input block.

* Press enter.

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-31.png)

As shown in the screen shot above, you should find that Regex Toy determines every character of the Text block matches the pattern specified in the Regex slot, illustrating this using alternating green and blue background highlighting of each character in the Matches block. Notice especially that there are 2 spaces between the two sentences, each one shown with a different background color highlighting.

Now remove the check mark from the IN TABLE checkbox.

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-32.png)

As shown in the screen shot above, you should find that Regex Toy still determines every character of the Text block matches the pattern specified in the Regex slot, but presents only a single space between the two sentences in the Matches block. Indeed, checking and unchecking the IN TABLE checkbox in rapid succ...