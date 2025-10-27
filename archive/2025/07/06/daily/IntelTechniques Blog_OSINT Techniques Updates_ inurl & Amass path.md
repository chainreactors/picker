---
title: OSINT Techniques Updates: inurl & Amass path
url: https://inteltechniques.com/blog/2025/07/05/osint-techniques-updates-inurl-amass-path/
source: IntelTechniques Blog
date: 2025-07-06
fetch_date: 2025-10-06T23:28:08.028176
---

# OSINT Techniques Updates: inurl & Amass path

[Skip to content](#main)

[# IntelTechniques](https://inteltechniques.com)

[IntelTechniques Blog](https://inteltechniques.com/blog/)

* [Training](https://inteltechniques.com/training.html)
* [Services](https://inteltechniques.com/services.html)
* [Resources](https://inteltechniques.com/links.html)
* [Tools](https://inteltechniques.com/tools/)
* [Blog](https://inteltechniques.com/blog/)
* [Podcast](https://inteltechniques.com/podcast.html)
* [Magazine](https://unredactedmagazine.com)
* [Books](https://inteltechniques.com/books.html)
* [Contact](https://inteltechniques.com/contact.html)

# OSINT Techniques Updates: inurl & Amass path

* [Posted on
  July 5, 2025](https://inteltechniques.com/blog/2025/07/05/osint-techniques-updates-inurl-amass-path/)
* Posted in
  [OSINT](https://inteltechniques.com/blog/category/osint/)

In my book [OSINT Techniques, 11th Edition](https://inteltechniques.com/book1.html), I discuss the ability to use Google search operators to both isolate and eliminate specific data. This is more important than ever with the substantial increase of AI-generated content infiltrating our queries. We are testing some new techniques which practically eliminate sites created by AI, but more research is necessary. For now, I want to focus on a change at Google which requires us to pivot our query structure for specific types of pages.

In the book, I give the following Google search example which would identify any FTP servers which possess PDF files that contain the term OSINT within the file.

inurl:ftp filetype:pdf "osint"

This still works, but results become lost in the slew of junk. The book then gives the following query to eliminate any HTTP or HTTPS results.

inurl:ftp -inurl(http|https) filetype:pdf "osint"

This worked for a while, but Google has now enforced some specific behaviors, which I really should have included anyway. The following query is now required to present only FTP sites without general web sites. The change is the colon after "inurl".

inurl:ftp -inurl:(http|https) filetype:pdf "osint"

This query provided only the four results I wanted. Replacing "ftp" with your desired content should be more productive now.

I also modified the updates.sh script (line 58) within our Linux VM build to properly remove the Amass zip file downloaded during the update. This only impacted a minority of users, but the change is cleaner.

Thank you to all of the readers who report the issues which need corrected. More details are in the [book](https://inteltechniques.com/book1.html).

* [« Previous Post](https://inteltechniques.com/blog/2025/04/02/new-digital-book-provider/)
* [Next Post »](https://inteltechniques.com/blog/2025/07/05/extreme-privacy-update-knockknock-script/)

The RSS feed for this blog is at
<https://inteltechniques.com/blog/feed/>.

#### Recent Posts

* [UNREDACTED Magazine Issue 008](https://inteltechniques.com/blog/2025/09/05/unredacted-magazine-issue-008/)
* [Extreme Privacy Update: E2EE Email Guide](https://inteltechniques.com/blog/2025/07/12/extreme-privacy-update-e2ee-email-guide/)
* [Virtual Currency Payments Return](https://inteltechniques.com/blog/2025/07/11/virtual-currency-payments-return/)
* [Extreme Privacy Update: Self-Hosted SearXNG Guide](https://inteltechniques.com/blog/2025/07/11/extreme-privacy-update-self-hosted-searxng-guide/)
* [Extreme Privacy Update: Windows 10 EOL](https://inteltechniques.com/blog/2025/07/08/extreme-privacy-update-windows-10-eol/)
* [Extreme Privacy Update: KnockKnock Script](https://inteltechniques.com/blog/2025/07/05/extreme-privacy-update-knockknock-script/)
* [OSINT Techniques Updates: inurl & Amass path](https://inteltechniques.com/blog/2025/07/05/osint-techniques-updates-inurl-amass-path/)
* [New Digital Book Provider](https://inteltechniques.com/blog/2025/04/02/new-digital-book-provider/)
* [New Ebook Updates](https://inteltechniques.com/blog/2025/04/02/new-ebook-updates/)
* [Executive EDC Bags](https://inteltechniques.com/blog/2025/01/05/executive-edc-bags/)
* [Books Updated](https://inteltechniques.com/blog/2024/11/29/books-updated/)
* [OSINT Techniques 11th Edition Now Available](https://inteltechniques.com/blog/2024/11/10/osint-techniques-11th-edition-now-available/)
* [Digital Guide Updates 2024.11.01](https://inteltechniques.com/blog/2024/11/02/digital-guide-updates-2024-11-01/)
* [Digital Guide Updates 2024.10.01](https://inteltechniques.com/blog/2024/09/30/digital-guide-updates-2024-10-01/)
* [UNREDACTED Magazine Issue 007](https://inteltechniques.com/blog/2024/09/16/unredacted-magazine-issue-007/)
* [Major Books Update](https://inteltechniques.com/blog/2024/09/12/major-books-update/)
* [Digital Guide Updates 2024.09.01](https://inteltechniques.com/blog/2024/09/01/digital-guide-updates-2024-09-01/)
* [Extreme Privacy 5th Edition Now Available](https://inteltechniques.com/blog/2024/08/08/extreme-privacy-5th-edition-now-available/)
* [Extreme Privacy 5th Edition Available Soon](https://inteltechniques.com/blog/2024/08/05/extreme-privacy-5th-edition-available-soon/)
* [Digital Guide Updates 2024.08.01](https://inteltechniques.com/blog/2024/08/01/digital-guide-updates-2024-08-01/)
* [The Next Books](https://inteltechniques.com/blog/2024/07/01/the-next-books/)
* [Digital Guide Updates 2024.07.01](https://inteltechniques.com/blog/2024/07/01/digital-guide-updates-2024-07-01/)
* [More Bad Gun Safe OPSEC](https://inteltechniques.com/blog/2024/06/07/more-bad-gun-safe-opsec/)
* [Darter Pro Part 2: Truly Secure Dual-Booting](https://inteltechniques.com/blog/2024/06/03/darter-pro-part-2-truly-secure-dual-booting/)
* [Self-Publishing Guide Update](https://inteltechniques.com/blog/2024/06/01/self-publishing-guide-update/)

* Copyright © 2009-2024 IntelTechniques.com
* All Rights Reserved
* [Privacy Policy](https://inteltechniques.com/privacy.html)