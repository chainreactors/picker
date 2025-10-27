---
title: Discover a Magical World in ABAP
url: https://blogs.sap.com/2023/07/09/discover-a-magical-world-in-abap/
source: SAP Blogs
date: 2023-07-10
fetch_date: 2025-10-04T11:52:32.341506
---

# Discover a Magical World in ABAP

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Discover a Magical World in ABAP

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46858&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Discover a Magical World in ABAP](/t5/application-development-and-automation-blog-posts/discover-a-magical-world-in-abap/ba-p/13555640)

![nomssi](https://avatars.profile.sap.com/1/4/id143f71a48fbbff12b15a7945c686118276946a783678307eb3ed19ed759bc93e_small.jpeg "nomssi")

[nomssi](https://community.sap.com/t5/user/viewprofilepage/user-id/39762)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46858)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46858)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555640)

‎2023 Jul 09
3:47 AM

[14
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46858/tab/all-users "Click here to see who gave kudos to this post.")

6,357

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [Open Source](https://community.sap.com/t5/c-khhcw49343/Open%2520Source/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [Open Source

  Programming Tool](/t5/c-khhcw49343/Open%2BSource/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)

View products (2)

## Presenting **The Quest**, A Wizard Adventure Game

![](/legacyfs/online/storage/blog_attachments/2023/07/thequest_potion.png)

Hello, ABAP community,

I'm excited to share with you a project that originated from the [SAP Developer Code Challenge](https://blogs.sap.com/2023/05/10/sap-developer-code-challenge-open-source-abap/) held in May this year. This challenge provided an opportunity for exploring open-source development in ABAP, truly pushing the boundaries of what we can achieve with this versatile language.

During the fourth week of the challenge, we delved into the [AXAGE](https://blogs.sap.com/2022/05/13/an-abapventure/) open-source game engine for text adventures by Enno Wulff. Inspired by this, I built upon [Thomas Jung's version](https://github.com/jung-thomas/axage_example)  that leverages the [abap2UI5](https://github.com/abap2UI5/abap2UI5) open-source package, enabling the creation of UI5 applications written purely in ABAP.

In recent times, I have been using abap2UI5 to port the Workbench for my [Scheme interpreter in ABAP](https://blogs.sap.com/2018/02/01/announcing-the-abap-scheme-workbench/) to UI5. Scheme, a LISP variant, intrigued me and I remember being captivated by the brilliance of LISP through the book "Land of Lisp" by Conrad Barski. The book's approach of using games for teaching resonated with me. In fact, I had already handcrafted the [Wizard's adventure game in abapScheme](https://github.com/nomssi/abap_scheme/wiki/Play-Wizard%27s-Adventure). So, I decided to use the AXAGE engine in tandem with abap2UI5 and create a text adventure with a similar theme.

For the game narrative, scenarios, and many texts, I turned to [ChatGPT](https://blogs.sap.com/2022/12/07/are-we-ready-to-use-ai-for-abap-programming/) (as a note, I also used it to review this blog). The result is [The Quest](https://github.com/nomssi/axage), a journey where the objective is to gather three magical items: the Orb of Sunlight, the Potion of Infinite Stars, and the Staff of Eternal Moon. These mystical objects need to be combined to open a portal to the Wizard’s Guild. The player, an apprentice, will then finally gain recognition as a full-fledged wizard. The path to victory involves exploration and I look forward to your feedback to make this journey even more captivating.

![](/legacyfs/online/storage/blog_attachments/2023/07/welcome_quest.png)

Welcome to The Quest

To bring more vibrancy and visual appeal to the text-only game, I used Stable Diffusion (the [DreamStudio](https://dreamstudio.ai/) online version) to generate images from text prompts. These images have been incorporated into the game, along with a wizard ASCII art sourced from the internet.

Accommodating the game's intricacies required enhancing the engine significantly, a task that called for some ABAP wizardry. You can discover the details for yourself in the game. I'm thrilled to present a release of the game that provides a complete gaming experience.

### Code

* On Premise/Cloud at github: [nomssi/axage: ABAP teXt Adventure Game Engine (github.com)](https://github.com/nomssi/axage)

### References

* Prerequisites: [abapGit](https://abapgit.org/), [abap2UI5](https://github.com/abap2UI5/abap2UI5)

* [DreamStudio](https://dreamstudio.ai/) (Stable Diffusion)

* [ChatGPT](https://chat.openai.com/)

![](/legacyfs/online/storage/blog_attachments/2023/07/thequest_view.png)

I invite all developers to immerse themselves in this magical world and try out the game. Your feedback, suggestions, and ideas for improvements would be greatly appreciated. I believe this project could inspire more creative ventures and serve as a springboard for your own text-based adventures in ABAP.

For those who manage to complete the quest, I encourage you to post a screenshot of your victory. As an ABAP wizard, you might read through the code for hints.

However, a word of caution before you dive in – I won't be held responsible if your productivity declines because you enjoy the game too much! Jokes aside, this project stands as a testament to the fun and educational possibilities of coding, redefining what can be achieved with ABAP.

I eagerly await your thoughts and feedback on this endeavor.

Happy gaming and coding, everyone!

5 Comments

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin