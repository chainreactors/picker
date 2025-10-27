---
title: ABAP: Fast JSON Serialization
url: https://blogs.sap.com/2022/10/27/abap-fast-json-serialization/
source: SAP Blogs
date: 2022-10-28
fetch_date: 2025-10-03T21:06:37.153878
---

# ABAP: Fast JSON Serialization

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* ABAP: Fast JSON Serialization

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46884&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [ABAP: Fast JSON Serialization](/t5/application-development-and-automation-blog-posts/abap-fast-json-serialization/ba-p/13556816)

![TimoStark](https://avatars.profile.sap.com/f/6/idf602bbbfa2f26e921adb9f7f021ed2052b04be4cde158d8490435cec2e0e09d4_small.jpeg "TimoStark")

[TimoStark](https://community.sap.com/t5/user/viewprofilepage/user-id/171010)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46884)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46884)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556816)

‎2022 Oct 27
9:02 PM

[35
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46884/tab/all-users "Click here to see who gave kudos to this post.")

20,462

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

*tldr; Install <https://github.com/timostark/abap-json-serialization> and enjoy the fastest possible JSON serialization. The result will be a 10x faster JSON serialization and deserialization compared to /UI2/CL\_JSON at the same quality. Be warned though: Read the limitation section first.*

Oh no - another JSON Serialization Blog Post? Hey - At least no blog about excel exports ![:slightly_smiling_face:](/html/@ACD7EA91588099437A7ECEEAAE5D5B40/emoticons/1f642.png ":slightly_smiling_face:")

So why are we in need of a "new" way for JSON serialization? The reason is simple: Runtime! Especially when working with custom REST services with a big payload you will notice a lot of runtime getting lost in JSON serialization. Loosing 30% of your runtime in JSON serialization makes me very unhappy (when I just optimized my more difficult business class).

So, what are our goals:

1. Fast

2. Support Camel-Case

3. Support real booleans and numbers

4. Not need to be easy or generic (I will accept a bad life as a developer if it is fast and reliable).

There are already multiple solutions out there - just to mention the most important ones:

* [/UI2/CL\_JSON](https://blogs.sap.com/2019/09/02/abap-and-json-3/) (plain ABAP)

* [CALL TRANSFORMATION](https://blogs.sap.com/2013/01/07/abap-and-json/)  (Kernel solution, using XSLT or Simple Transformation Mapping)

* [CL\_TREX\_JSON\_SERIALIZER](https://codezentrale.de/tag/cl_trex_json_serializer/) (plain ABAP)

* [**XCO\_CP\_JSON**](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/492ccdb87b224a35a8ed20e53325dfce.html) (S/4 Only, not stable, extremely slow and crashes - therefore let's keep that one out for the moment)

So how are they behaving from runtime perspective. Let's take a very simple example and serialize 5.000 lines of SFLIGHT lines and a very complex and deep structure:

![](/legacyfs/online/storage/blog_attachments/2022/10/runtime.png)

So what does that tell us?

Not really surprisingly the only feasible solution on a ABAP stack is the usage of CALL TRANSFORMATION - as this is executed directly in the Kernel, thus not depending on slow ABAP String concat and/or field-symbol traversal.

It might be strange but always remember: Building up strings using concats and traversing over field-symbols inside a structure is very slow in ABAP compared to native languages --> Where possible Kernel Modules like Simple Transformations are preferable performance wise.

There are however quality problems when using CALL TRANSFORMATION ID:

1. No Camel-Case

2. No real "booleans" (instead 'X' is printed.. tell that somebody outside of the SAP world)

3. No real NUMC (instead leading 0s are printed)

There is one solution which was [already mentioned](https://blogs.sap.com/2019/10/21/abap-to-json-with-custom-transformation/) in a blog post, using a custom ABAP transformation to at least support camel case. Unfortunately, that throws away the performance benefit as the fast kernel module has to go up to the ABAP stack for a simple "to-camel-case" transformation.

My suggested solution is, that we use CALL TRANSFORMATION for what it is actually thought: to transform data using ST transformations (Simple Transformation). Remark: CALL TRANSFORMATION can also be used for XSLT Transformation (which are much more powerful but also slower - see remark by [@Sandra](/t5/user/viewprofilepage/user-id/22232) Rossi), but this is simply not required here. This means we are creating **an own Simple transformation** for the structure/table-type we want to serialize (nested structures are of course possible).

Let's see an example transformation for the table SFLIGHT (shortened):

![](/legacyfs/online/storage/blog_attachments/2022/10/example_Transformation_xsl.png)

Nobody wants to write that code (and for sure nobody with a right mind will want to keep that transformation up to date) - but let's first see the runtime impact.

![](/legacyfs/online/storage/blog_attachments/2022/10/runtime_with_own.png)

==> **The solution is around 10 times faster than /UI2/CL\_JSON, while having the same quality as a result.**

As already said of course nobody wants to write these ST mappings - especially for deeply nested structures this is horrible.

Therefore, I've published a small helper program ZJSON\_TO\_XSLT under MIT license to GitHub which allows you to directly create those transformation for any structure/table

![](/legacyfs/online/storage/blog_attachments/2022/10/2022-10-27-21_46_45-Clipboard.png)

Output (next to the generated transformation).

![](/legacyfs/online/storage/blog_attachments/2022/10/2022-10-27-21_48_23-Output.png)

Execute the transformation using normal CALL TRANSFORMATION call:

```
DATA(lo_writer_json) = cl_sxml_string_writer=>create( type = if_sxml=>co_xt_json ).

CALL TRANSFORMATION ZSFLIGHT SOURCE root = lt_flights RESULT XML lo_writer_json.

DATA(lv_json) = cl_abap_codepage=>convert_from( lo_writer_json->get_output( ) ).
```

In my customer projects I am using the API called in the program in a regular job (including a mapping-table) which updates the transformations on the development system in a regular manner. If you want to spend a lot of time you could even create the transformations "live" as local objects on the first access. I personally do not like the approach...