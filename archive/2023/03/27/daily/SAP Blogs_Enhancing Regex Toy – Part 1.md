---
title: Enhancing Regex Toy – Part 1
url: https://blogs.sap.com/2023/03/26/enhancing-regex-toy-part-1/
source: SAP Blogs
date: 2023-03-27
fetch_date: 2025-10-04T10:45:49.117439
---

# Enhancing Regex Toy – Part 1

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Enhancing Regex Toy – Part 1

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46653&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Enhancing Regex Toy – Part 1](/t5/application-development-and-automation-blog-posts/enhancing-regex-toy-part-1/ba-p/13552389)

![former_member225588](https://avatars.profile.sap.com/former_member_small.jpeg "former_member225588")

[former\_member225588](https://community.sap.com/t5/user/viewprofilepage/user-id/225588)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46653)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46653)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552389)

‎2023 Mar 26
9:18 PM

[11
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46653/tab/all-users "Click here to see who gave kudos to this post.")

2,473

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

This is the first in a series of six blogs describing how to enhance the regular expression tester known as Regex Toy, each blog describing a single enhancement to its capabilities.

**Note:** The use of the words “enhance” and “enhancement” in the sentence above is not intended to suggest that the standard SAP [Enhancement Framework](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/94/9cdc40132a8531e10000000a1550b0/content.htm?no_cache=true) is involved in facilitating what is described in this series of blogs.  Also, for reasons that will be explained in the final blog, the enhancements discussed in this six-blog series do not apply to NetWeaver release 7.55 (a.k.a CE 2008/OP 2020) and beyond.

### Background

In 2015 I wrote an E-bite for SAP PRESS titled **Regex in ABAP: Pattern Matching with Regular Expressions**, which became the first E-bite on a programming topic. Since June 2022 it is no longer available for purchase from the SAP PRESS website.

That E-bite included a chapter describing the following four regular expression testers:

* [Regex Toy](https://dokumen.tips/download/link/regex-toy-testing-regular-expressions-in-contribution-regex-toy-testing-regular.html)

* [RegexPal](http://regexpal.com/)

* [Rubular](http://rubular.com)

* [Regex Storm](http://regexstorm.net/tester) (CAUTION: the corresponding link is not a secure connection)

Regex Toy is included with a NetWeaver system and, as far as I know, is the only ABAP-based regular expression tester. Its presentation screen at that time looked like this:

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-1.png)

As I noted in the E-bite about Regex Toy:

… an upper Input section provides a Regex field accepting a RegEx pattern, and a lower Text section accepts the text to be subjected to the RegEx pattern. Matching results are shown in the Matches section following the Input section, but requires the user either to select a radio button corresponding to one of the commands in the Options section or to press the Enter key while the cursor is positioned in the Regex or Replacement fields preceding the Options section. The matching results area has a white background; those strings matching the RegEx pattern are shown using a bold red foreground text font, while non-matching text is shown with a non-bold black foreground text font.

This is a magnificent tool by which the nuances of RegEx behavior in ABAP can be tested prior to applying a pattern to productive code under development. ... this utility not only indicates whether a string of text has any matches with the specified RegEx pattern but also shows in context where these matches occur.

...

An [article](https://dokumen.tips/download/link/regex-toy-testing-regular-expressions-in-contribution-regex-toy-testing-regular.html) published by the author of Regex Toy includes a disclaimer that it isn’t so much a tool but merely a toy. However, after you try it, you might agree that the author is being too modest regarding its usefulness and applicability as a development aid.

All of the other three regular expression testers noted above are available via the Internet, and I found Regex Storm to be the most useful of them. During the time I spent composing the content of the E-bite, I decided to experiment with a copy of Regex Toy, changing its source code to determine whether I could make it behave more like Regex Storm. Once I was satisfied with the result I decided to include the necessary set of Regex Toy patches in its own chapter in the E-bite so that readers could apply them at their site to make their Regex Toy also behave like Regex Storm.

### Foreground

Fast forward to February 2023 and I found myself at a site where yet again I wanted to apply to a copy of Regex Toy the patches I had described in the E-bite. To my horror, I found that some of those patches either no longer worked or described the placement of a patch in code that no longer looked as it did when I was writing the E-Bite.

Back in 2015, when first devising the patches to be applied to Regex Toy, I had available to me a NetWeaver 7.4 system, but now in 2023 I have available a 7.5 system. A quick look at the attributes of the Regex Toy source code indicated that the program, first released in 2006, now had a change date of June 2015 – two months prior to the E-bite becoming available. In a 7.5 system its presentation screen had been changed to look like this:

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-2.png)

Notice that the Options block now contains a new checkbox titled IN TABLE. Also, the titles of the radio buttons in the Options block were converted to upper case, with the former option named Match now named FIND ^...$, as shown in the comparison below:

Options block with 7.4 version:

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-11.png)

Options block with 7.5 version:

![](/legacyfs/online/storage/blog_attachments/2023/03/blog-image-5.png)

A mistake I made when describing these Regex Toy patches in the E-bite was neglecting to provide any indication about the version of the code to which they applied. Accordingly, the patches described in this blog series apply to the ABAP repository object DEMO\_REGEX\_TOY having a last changed date of 06/01/2015.

![](/legacyfs/online/storage/blog_attachments...