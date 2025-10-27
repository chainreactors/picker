---
title: The Open Source Tool That Has Preserved 150,000 Pieces of Online Evidence
url: https://www.bellingcat.com/resources/2025/08/13/the-open-source-tool-that-has-preserved-150000-pieces-of-online-evidence/
source: bellingcat
date: 2025-08-14
fetch_date: 2025-10-07T00:49:32.253644
---

# The Open Source Tool That Has Preserved 150,000 Pieces of Online Evidence

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)

* EN
  + [Русский](https://ru.bellingcat.com)
  + [Français](https://fr.bellingcat.com)
  + [Español](https://es.bellingcat.com)
  + [Deutsch](https://de.bellingcat.com)
  + [Українська](https://uk.bellingcat.com)
* [Donate](https://www.bellingcat.com/donate)

Search for:

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)
* [Donate](/donate)

[![Profile picture for: Miguel Ramalho](https://www.bellingcat.com/app/uploads/2023/03/Miguel-1200x1200.jpg)](https://www.bellingcat.com/author/miguelramalho/)
[Miguel Ramalho](https://www.bellingcat.com/author/miguelramalho/)

Miguel is a data scientist for Bellingcat focusing on understanding online manipulation and building tools and methods for open-source research.

[![](https://www.bellingcat.com/app/uploads/2025/08/erin-269x300.jpg)](https://www.bellingcat.com/author/erinclark/)
[Erin Clark](https://www.bellingcat.com/author/erinclark/)

Erin is a developer and data engineer who specialises in using open data for transparency and accountability.

[![](https://www.bellingcat.com/app/uploads/2025/08/paddy-300x236.jpeg)](https://www.bellingcat.com/author/paddyrobertson1/)
[Paddy Roberston](https://www.bellingcat.com/author/paddyrobertson1/)

Paddy is an open source enthusiast from Wales, with a passion for creating impact through his work.

# The Open Source Tool That Has Preserved 150,000 Pieces of Online Evidence

August 13, 2025

* [Auto Archiver](/tag/auto-archiver)
* [Tools](/tag/tools)

Bellingcat’s [Auto Archiver](https://github.com/bellingcat/auto-archiver) is a tool aimed at preserving online digital content before it can be modified, deleted or taken down. [Publicly launched](https://www.bellingcat.com/resources/2022/09/22/preserve-vital-online-content-with-bellingcats-auto-archiver-tool/) in 2022, it has preserved over 150,000 web pages and social media posts to date. The Auto Archiver has been used by Bellingcat’s journalists to preserve information on dozens of fast moving events such as the [Jan. 6 riots](https://www.bellingcat.com/news/2021/01/08/the-journey-of-ashli-babbitt/) – when we first used the tool internally – as well as gather digital evidence for our [Justice and Accountability](https://www.bellingcat.com/what-is-bellingcats-ja-unit-december-2022/) project and to monitor [Civilian Harm in Ukraine](https://ukraine.bellingcat.com/).

The Auto Archiver has also been adopted by both large newsrooms and NGOs. It has been  used by individual researchers, journalists, activists, archivists, academics and developers as well.  With interest in the tool strong, we have worked hard to add to and improve it over time. But we have used the past few months to take a step back and to build a new and more robust ecosystem to further help individual organisations and researchers use and benefit from it.

Our aim has been to make it more reliable and even easier to use for more people. Today, we are happy to announce an [updated version](https://github.com/bellingcat/auto-archiver) of the Auto Archiver which includes many new features like:

* [Detailed documentation](https://auto-archiver.readthedocs.io/en/latest/) for all features and configurations
* A user-friendly [interface](https://github.com/bellingcat/auto-archiver-setup-tool) designed for teams using a [shared instance](https://github.com/bellingcat/auto-archiver-api)
* A new modular structure that improves the startup speed and reliability of the tool
* New features like chain of custody, perceptual hashing for deduplication, and techniques to avoid anti-bot measures and captchas on websites
* A user-friendly [tool to configure](https://auto-archiver.readthedocs.io/en/latest/installation/config_editor.html) the Auto Archiver, without the need to edit configuration text files

![](https://www.bellingcat.com/app/uploads/2025/08/Screenshot-of-new-Documentation-site-for-the-Auto-Archiver.jpg)

*Screenshot of new Documentation site for the Auto Archiver*

For an in-depth look at the changes made in this stable version of the Auto Archiver, see the *What Changed, What Remains* section further down in this article.

## **Automated Archiving and Collaboration – When to Use This Tool?**

The latest version of the Auto Archiver has an easy-to-use web interface and a simplified installation process that makes it more straightforward to set up than before. However, some technical skills are still required for this initial process, and there are other tools available that could meet many of your archiving needs.

![](https://www.bellingcat.com/app/uploads/2025/05/question-mark.png)

## Support Bellingcat

Your donations directly contribute to our ability to publish groundbreaking investigations and uncover wrongdoing around the world.

[Donate](https://bellingcat.com/donate?utm_campaign=article_cta)

If all you need is to archive a few unauthenticated URLs, we recommend using the [Wayback Machine](https://web.archive.org/) or [Archive.today](https://archive.today/). Alternatively, WebRecorder’s browser extension [ArchiveWebPage](https://archiveweb.page/guide) can create a replayable archive of a website you visit – even for content behind login walls. For batch processing, the Wayback Machine has a [bulk upload service](https://archive.org/services/wayback-gsheets/) that accepts Google Sheets. If you individually need to record all your browser interactions and store content along the way there are paid options like [Hunchly](https://hunch.ly/). Finally, if all you are interested in are videos and are comfortable with the command line, [yt-dlp](https://github.com/yt-dlp/yt-dlp) will probably be enough to download those, even in bulk.

But if you’re hoping to automate your archiving, or archive a large number of URLs in a collaborative environment, then this is where the Auto Archiver really shines. Its modular framework allows you or your team to customise archiving based on your needs, and provides a way to generate metadata that ensures others can trust that your archived content has not been tampered with.

Learn more about what sites the Auto Archiver can archive [here](https://auto-archiver.readthedocs.io/en/latest/modules/extractor.html).

## **The Future of Web Archiving**

Archiving the web is hard, especially when logins, captchas, and other bot prevention systems are in place. We will do our best to keep improving our Auto Archiver, but we note that it should be just one of many tools in your researcher’s toolkit. You can explore a variety of other useful tools in the Bellingcat [Open Source Investigation Toolkit](https://bellingcat.gitbook.io/toolkit).

Still, if you want to support us on this journey of archiving critical information, you can:

* Download and use this tool
* [Donate](https://www.bellingcat.com/donate) directly to Bellingcat
* Test, give feedback, and develop new features in our [GitHub](https://github.com/bellingcat/auto-archiver)

**For newsrooms:**
If you work in a newsroom or research team and want to access a demo or help to deploy the Auto Archiver internally you can reach us at [[email protected]](/cdn-cgi/l/email-protection#9ffcf0f1ebfefcebb2ebfafcf7dffdfaf3f3f6f1f8fcfeebb1fcf0f2) with the Subject “Auto Archiver at [my team/organisation]” and tell us more about your organisation and archiving needs. Building a greater adoption base is the best way to ensure the future of this tool and its versatility.

## What Changed, What Remains

## Subscribe to the Bellingcat newsletter

Subscribe to our newsletter for first access to our published content and events that our staff and contributors are involved with, including int...