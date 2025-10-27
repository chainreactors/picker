---
title: Second thoughts on the great Mastodon Migration
url: https://blogs.sap.com/2022/11/12/second-thoughts-on-the-great-mastodon-migration/
source: SAP Blogs
date: 2022-11-13
fetch_date: 2025-10-03T22:37:54.311276
---

# Second thoughts on the great Mastodon Migration

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Sustainability](/t5/sustainability/gh-p/sustainability)
* [Blog Posts](/t5/sustainability-blog-posts/bg-p/sustainabilityblog-board)
* Second thoughts on the great Mastodon Migration

Sustainability Blog Posts

Delve into SAP sustainability blogs. Gain insights into tech-driven sustainable practices and contribute to a greener future for businesses and the planet.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/sustainabilityblog-board/article-id/1731&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Second thoughts on the great Mastodon Migration](/t5/sustainability-blog-posts/second-thoughts-on-the-great-mastodon-migration/ba-p/13569620)

![JimSpath](https://avatars.profile.sap.com/1/9/id19e0902ffb151e54856445a6cc9bb1df4e8202ab913d64c6e2e2d8625cd7bf0a_small.jpeg "JimSpath")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[JimSpath](https://community.sap.com/t5/user/viewprofilepage/user-id/184)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=sustainabilityblog-board&message.id=1731)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/sustainabilityblog-board/article-id/1731)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569620)

‎2022 Nov 12
4:23 PM

[7
Kudos](/t5/kudos/messagepage/board-id/sustainabilityblog-board/message-id/1731/tab/all-users "Click here to see who gave kudos to this post.")

1,297

* SAP Managed Tags
* [Corporate Social Responsibility](https://community.sap.com/t5/c-khhcw49343/Corporate%2520Social%2520Responsibility/pd-p/611794787045402236540598973198809)

* [Corporate Social Responsibility

  Topic](/t5/c-khhcw49343/Corporate%2BSocial%2BResponsibility/pd-p/611794787045402236540598973198809)

View products (1)

Earlier this week, I posted on [the spinning up of Mastodon](https://blogs.sap.com/2022/11/07/is-it-time-to-join-the-elephant-parade-or-what-is-this-mastodon-doing-in-my-web/) as the Twitter platform spirals down. People shared several interesting perspectives so far; one that caught my eye concerned accessibility (by SAP's lee.barnard ).

*... features like alt texts for images, subtitles for videos - assuming that Mastodon would support these important accessibility features.*

For clarity, "second thoughts" in the title means more thoughts, not the idea of stopping the migration. Both Twitter and Mastodon allow for "alt text" in images yet neither enforces them.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-12-083825-a.png)

Screenshot of ~No description added~ on image upload.

The Mastodon platform I've joined has an option for "detect text from picture," which the other does not.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-12-083855-b.png)

On my first test, though, no results came back in a short time. So I decided to test a bit more, and waited.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-12-090823-a.png)

Screenshot of ~preparing OCR~

Ten minutes went by, then 20, then after around 30 minutes I closed the pop-up window. Having installed and run open source OCR (optical character recognition) code, I understood the CPU cycles might be significant. I guess I expected a timeout warning or other error message that would show some user feedback.

Then, I started searching for bug reports and found several with the same pattern:

1. [Image OCR feature is broken (since 3.5?) #18266](https://github.com/mastodon/mastodon/issues/18266)

2. [OCR fails to load and Tesseract errors in console #18750](https://github.com/mastodon/mastodon/issues/18750)

3. [Automatic text extraction from images not possible on Chrome 104 #19107](https://github.com/mastodon/mastodon/issues/19107)

This leaves us with the good news/bad news "it depends" scenario where the code is open source, and anyone (within reason) can contribute to the fix. But during a great migration time, when many users are joining, servers become overloaded, administrators struggle to keep up with maintenance, and I doubt those running sites want to play with new features or fix old obscure bugs.

The administrators of the site I'm on said, "To resolve the many question when we will upgrade to chaos.social to mastodon v4: Not before there is a stable release for v4." [[link](https://chaos.social/web/%40ordnung/109313714846880097)]

From one of the "find your followers" scripts produced to ease the migration I see a few sites on a 4.x "release candidate". Good for them; hope it stays well.

Slight post-release edit, as I saw this reply to a well-known person, who didn't put alt-text in an image:

![](/legacyfs/online/storage/blog_attachments/2022/11/alt-text-please.png)

any chance you can post a description of the text in the image?

Back to the general accessibility topic; what does Mastodon offer now, and what is coming; is it better than other sites?

* I think the "no description added" is a good reminder to add accessible content; I've seen plenty of tweets begging/coaxing people to do that, but after the fact,

* The OCR feature could be sweet for images that are primarily text; plant and animals not so much.

* It is open source. If organizations like SAP want to contribute to the code base for such features it will happen faster.

* Content warnings are built-in and pretty useful.

As the Fleetwood Mac song refrain goes:

```
Tusk! Tusk!
```

* [accessibility](/t5/tag/accessibility/tg-p/board-id/sustainabilityblog-board)
* [alt-text](/t5/tag/alt-text/tg-p/board-id/sustainabilityblog-board)
* [mastodon](/t5/tag/mastodon/tg-p/board-id/sustainabilityblog-board)
* [ocr](/t5/tag/ocr/tg-p/board-id/sustainabilityblog-board)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fsustainability-blog-posts%2Fsecond-thoughts-on-the-great-mastodon-migration%2Fba-p%2F13569620%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Top kudoed authors

| User | Count |
| --- | --- |
| [![Lorenz4](https://avatars.profile.sap.com/c/3/idc31ec1a89be647c2ec4c98b7ad14b4c0c77fb06396d8f1cbf46dda4c5e480725_small.jpeg "Lorenz4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Lorenz4](/t5/user/viewprofilepage/user-id/2010221) | 1 |
| [![AmitTandon](https://avatars.profile.sap.com/8/e/id8e8e96c053d7ea47f6aa6de4010ff00f0c647c7652b563e17184420027f2e86d_small.jpeg "AmitTandon")  AmitTandon](/t5/user/viewprofilepage/user-id/1585113) | 1 |

[View all](/t5/forums/kudosleaderboardpage/board-id/sustainabilityblog-board/timerange/one_week/page/1/tab/authors)