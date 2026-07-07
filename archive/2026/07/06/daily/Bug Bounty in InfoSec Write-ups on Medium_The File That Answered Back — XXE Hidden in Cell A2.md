---
title: The File That Answered Back — XXE Hidden in Cell A2
url: https://infosecwriteups.com/the-file-that-answered-back-xxe-hidden-in-cell-a2-20dbb8161dd8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-06
fetch_date: 2026-07-07T06:03:26.449700
---

# The File That Answered Back — XXE Hidden in Cell A2

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-file-that-answered-back-xxe-hidden-in-cell-a2-20dbb8161dd8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-file-that-answered-back-xxe-hidden-in-cell-a2-20dbb8161dd8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-20dbb8161dd8---------------------------------------)

·

1. [The Wall](/?source=post_page-----20dbb8161dd8---------------------------------------#3541 "The Wall")
2. [Learning to Read a Name](/?source=post_page-----20dbb8161dd8---------------------------------------#442b "Learning to Read a Name")
3. [The Thing About Spreadsheets](/?source=post_page-----20dbb8161dd8---------------------------------------#475a "The Thing About Spreadsheets")
4. [The First Test: Does It Reflect?](/?source=post_page-----20dbb8161dd8---------------------------------------#2a4e "The First Test: Does It Reflect?")
5. [Building the Payload: From the Inside Out](/?source=post_page-----20dbb8161dd8---------------------------------------#a1a1 "Building the Payload: From the Inside Out")
6. [The Exploit Time](/?source=post_page-----20dbb8161dd8---------------------------------------#2bd3 "The Exploit Time")
7. [Steps to Reproduce](/?source=post_page-----20dbb8161dd8---------------------------------------#6ada "Steps to Reproduce")
8. [What Comes After the Door Opens](/?source=post_page-----20dbb8161dd8---------------------------------------#ac66 "What Comes After the Door Opens")
9. [The Fix](/?source=post_page-----20dbb8161dd8---------------------------------------#0b44 "The Fix")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-20dbb8161dd8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# The File That Answered Back — XXE Hidden in Cell A2

[![Alvin Ferdiansyah](https://miro.medium.com/v2/resize:fill:64:64/1*jCQW4Dcioim59s1E0JwOqQ@2x.jpeg)](https://alvinferd.medium.com/?source=post_page---byline--20dbb8161dd8---------------------------------------)

[Alvin Ferdiansyah](https://alvinferd.medium.com/?source=post_page---byline--20dbb8161dd8---------------------------------------)

9 min read

·

Apr 21, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D20dbb8161dd8&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-file-that-answered-back-xxe-hidden-in-cell-a2-20dbb8161dd8&source=---header_actions--20dbb8161dd8---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

> Most people know XXE. Few think to look for it inside a spreadsheet upload. But beneath every .xlsx is really a ZIP archive full of XML, and the parser reading it doesn’t always know where to stop. This is the writeup of finding one that didn’t, and what it quietly handed back.

## The Wall

*The first thing I discovered wasn’t a vulnerability. It was a pattern.*

Almost every asset was behind the same wall: Imperva, a web application firewall so common in enterprise deployments that you almost expect it now. On its own, a WAF isn’t an ending. It’s a conversation. You probe, you learn what it blocks and how, you find the shape of the rules. But this one was doing something specific that changed the entire character of the hunt. *It was blocking the word `DOCTYPE`.*

Not entire payloads. Not suspicious looking XML structures. Just the presence of that one keyword, anywhere inside a POST body, was enough to return a 403 before the request ever touched any application. For context: `DOCTYPE` is the entry point for XML External Entity injection, the vulnerability class that lets you instruct an XML parser to read files off the server’s filesystem and hand them back to you. Without `DOCTYPE`, that entire attack surface disappears.

I confirmed this across the program’s Japanese portals, Korean WebLogic applications, Brazilian upload forms, AEM content management systems. Every time, a 403. The wall held.

## Learning to Read a Name

The assets in one particular region felt different from the start. Different infrastructure, different cloud providers, different WAF signatures. And among them, one domain resolved to an Alibaba Cloud IP with an F5 load balancer behind it. No Imperva signature in any response header. No `incap` cookies. No bot-detection challenges. *The wall wasn’t there*.

What was there was a URL path I had to look at twice.

```
/[REDACTED]/personal/CombineExcelUpload
```

I’ve learned over time that endpoint names are often the most honest thing about a web application. Developers name things after what they do. And this name said three things at once: it accepts Excel files, it uploads them, and it *combines*, meaning it doesn’t just store the file, it reads it. The name of the endpoint was practically a confession of the vulnerability class.

**`CombineExcelUpload`. Server-side Excel processing. No authentication required.**

## The Thing About Spreadsheets

Here is something that took me a while to really internalize, and now I think about it almost every time I see a file upload endpoint.

**An XLSX file is not a spreadsheet. Not at the parser level.**

An XLSX file is a ZIP archive containing a structured set of XML documents, defined by the Office Open XML (OOXML) standard. Open any `.xlsx` file with a ZIP extractor and you’ll find a whole internal world: folders, XML files, namespace declarations, hiding inside something that looks like a simple grid of numbers. The architecture looks like this:

```
document.xlsx  (it's actually a ZIP)
│
├── [Content_Types].xml        ← declares MIME types for every internal part
├── _rels/
│   └── .rels                  ← links the package root to the workbook
└── xl/
    ├── workbook.xml            ← defines the workbook and its sheets
    ├── _rels/
    │   └── workbook.xml.rels   ← links the workbook to its sheet files
    └── worksheets/
        └── sheet1.xml          ← the actual cell data  ←  this is where we live
```

Every file in that tree is XML. And the one that contains your cell values, `xl/worksheets/sheet1.xml`, is parsed by whichever XML library the server uses to read the spreadsheet.

If that library has external entity resolution enabled (which is the **default** in older .NET codebases, because the insecure behavior is the default, not the exception) then you can put something inside `sheet1.xml` that the parser was never meant to see. A declaration that says: \*before you read this cell’s value, go open this file on the filesyste...