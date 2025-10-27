---
title: Download Websites to Find OSINT
url: https://www.secjuice.com/download-a-website-to-search-for-emails-urls-crypto-addressed/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-02
fetch_date: 2025-10-04T12:12:09.437492
---

# Download Websites to Find OSINT

[![Secjuice](https://www.secjuice.com/content/images/2018/12/Logo-1.png)](https://www.secjuice.com)

* [Donate](https://opencollective.com/secjuice)
* [About Us](https://secjuice.com/about-us/)
* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/OSINT/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write With Us](https://secjuice.com/join-secjuice-writing-team/)
* [Hire A Writer](https://secjuice.com/hire-infosec-cybersecurity-writer/)
* [Rankings](https://secjuice.com/secjuice-writers-ranking/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

[OSINT](/tag/osint/)

# Download Websites to Find OSINT

* [![Tom Caliendo](/content/images/size/w100/2022/07/square-profile.png)](/author/tom-caliendo/)

#### [Tom Caliendo](/author/tom-caliendo/)

Mar 1, 2024
• 4 min read

![Download Websites to Find OSINT](/content/images/size/w2000/2024/03/IMG_7566.webp)

This AI-generated image was created on Midjourney and curated by Tom Caliendo.

#

Websites are full of useful information that is hidden in source code or small print in obscure subdomain.

*The following is an excerpt from the book,* [*The OSINT Guide*](https://www.amazon.com/Open-Source-Intelligence-Guide-Investigate-ebook/dp/B0BMXRTG7P?ref=secjuice.com)*, by Thomas Caliendo.*

Here we will walk through how to discover Open Source Intelligence (OSINT) by downloading a website to search it for email addresses, links, crypto addresses, …etc.

To clarify, this method does not search for a specific email address, instead it means searching for any email addresses that appear in the content or source code of the website. This can save the trouble of manually searching the entire website of a company for employees and their contact info. Alternatively you could download a web forum where you want to find all of the crypto addresses mentioned. Further, websites often have this kind of data in the source code but not the website content.

This is not always necessary, so consider that before going through the following process. It is also worth noting that after the first time doing this process, you can easily and very quickly run through the process again.

The process is basically to use HTTrack to download a website to your computer and then use Agent Ransack to search the downloaded website for whatever you want.

**Getting Started**

1 – Download the free versions of HTTrack ([https://www.httrack.com/page/2/](https://www.httrack.com/page/2/?ref=secjuice.com)) and Agent Ransack ([https://www.mythicsoft.com/agentransack/download/](https://www.mythicsoft.com/agentransack/download/?ref=secjuice.com))

**HTTrack**

2 – Open HTTrack and start a new “project” (website download) by clicking “Next”

3 – Fill in the sections labeled ”Project name” and “Base path.” Type anything for project name and in base path choose thelocation where you want to download the website.

4 – Type in the URL of website under “Web Address” and then just hit “Next” till it starts working

**Agent Ransack**

5 – Open Agent Ransack

6 – Under “file name” put htm or html – check the new file from HTTrack download (in C:\My Websites)
then in “containing text” type one of the strings identified below. In this example use :

[13][1-9A-HJ-NP-Za-km-z]{26,33}<

This is the string that searches for Bitcoin Addresses

7 – Under “look in:” there is a black space to the right and at then end you see a button with 3 dots, click on that to find the website mirrored file downloaded by HTTrack

Be aware that using the period literally in a search must be preceded by the ‘\’ escape character. For example: If you entered the filename as the expression ‘document.doc’ it would find any file that had ‘document’ followed by any character and then followed by ‘doc’. Therefore although it would find ‘document.doc’ it would also find document1doc’ and ‘documentXdoc’.

8 – Select the subfolders option check box. Click the options tab and set Contents to Regular Expressions

9 – Click “start”

**Search Strings Options**

Side Note: it is important to note that there are other resources for extracting links from websites though I find they are often limited or fee-based. One free resource is Link Extractor – [https://www.prepostseo.com/link-extractor](https://www.prepostseo.com/link-extractor?ref=secjuice.com)

**Search for URLs**

In the “Options” tab, under “Contents” choose “Boolean”
now you can use the \* wildcard

In the “Main” tab, in the “Containing Text:” bar type
\*.com

If the “Contents” had been set to Regular Expressions, the wildcard would not work

Side Note on Wildcards:
Zero or one character is represented by the ‘?’ character.
Zero or many, the ‘\*’ character.
One or many, the ‘+’ character.

More info on wildcard at
[https://help.mythicsoft.com/agentransack](https://help.mythicsoft.com/agentransack?ref=secjuice.com)
Or: [https://help.mythicsoft.com/agentransack/en/(occurrencecharacters)](https://help.mythicsoft.com/agentransack/en/%28occurrencecharacters%29?ref=secjuice.com).htm

**Better Version of URL Search**

Under the “Options” tab, “Contents” are set to “Regular Expression”
Then in the “Main” tab, next to “Containing text:” type the following
\b[A-Z0-9.\_%+-]+.[A-Z]{2,4}\b

**Email Addresses**

Under “Options”, “Contents” should be set to “Regular Expression”

Regular expressions are great for validating or searching for patterns such as email addresses. The following regular expression should match most email addresses:

\b[A-Z0-9.\_%+-]+@[A-Z0-9.-]+.[A-Z]{2,4}\b

**Bitcoin address:**

[13][1-9A-HJ-NP-Za-km-z]{26,33}<

If under Options and then under Contents, the search “\*.com” will not work

**Bitcoin**
/^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$/g

**Ethereum**
/^0x[a-fA-F0-9]{40}$/g

**More on “Regular Expressions at**
[https://gist.github.com/MBrassey/623f7b8d02766fa2d826bf9eca3fe005](https://gist.github.com/MBrassey/623f7b8d02766fa2d826bf9eca3fe005?ref=secjuice.com)
[https://archive.ph/wip/rme2e](https://archive.ph/wip/rme2e?ref=secjuice.com)

**Pivoting**

Upon discovering any identifiers of interest like emails or crypto addresses, then you can search for other websites that have the identifiers in their source codes.

Source code search engine ([https://publicwww.com/](https://publicwww.com/?ref=secjuice.com)) is like Google but only searches the Internet for websites’ source code, not the websites’ content. If an email address or ADsense ID is found in one website you can then look for other websites with those specific items in the source code.

**Trouble Shooting**

If HTTrack gives an error message reporting a “mirror” problem, this often means that the website is not allowing HTTrack to access it.

Web servers can redirect users to different palces based on what browser they are using. This is how cellphone browsers get redirected to mobile versions of some websites.

This site has that, but its broken. When it sees HTTrack’s fake ID of
Mozilla/4.5 (compatible; MSIE 4.01; Windows 98) it redirects to a broken page that has no links. So you get an empty mirror

**Solution**

1 – In the HTTrack process on the page where you input the url, see where it says “Preferences and mirror options:”

2 – Click “Set options”

3 – Then click the tab “Browser ID” and see the dropdown menu next to “Browser Identity”

4 – I changed it to a different option that was not the default.

The default settings uses – Mozilla/4.5 (compatible; HTTrack 3.0x;
I chose at random the option – Mozilla/4.05 [fr] (Win98; I)

And that worked for me

In an upcoming article I will walkthrough how to use Python to perform these tasks. In the meantime feel free to check out the scripts at:

[GitHub - tomcaliendo/e-scraper: Python script to extract unique email addresses from a list of domains using regular expression.

Python script to extract unique email addresses from a list of domains using regular expression. - tomcaliendo/e-scraper

![]...