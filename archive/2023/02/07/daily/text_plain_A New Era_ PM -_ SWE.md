---
title: A New Era: PM -> SWE
url: https://textslashplain.com/2023/02/06/a-new-era-pm-swe/
source: text/plain
date: 2023-02-07
fetch_date: 2025-10-04T05:52:02.233933
---

# A New Era: PM -> SWE

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# A New Era: PM -> SWE

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-02-062023-03-20](https://textslashplain.com/2023/02/06/a-new-era-pm-swe/)Posted in[bluebadge](https://textslashplain.com/category/bluebadge/), [dev](https://textslashplain.com/category/dev/), [storytelling](https://textslashplain.com/category/storytelling/)Tags:[career](https://textslashplain.com/tag/career/), [Microsoft](https://textslashplain.com/tag/microsoft/)

*tl;dr: As of last week, I am now a Software Engineer at Microsoft.*

My path to becoming a Program Manager at Microsoft was both unforeseen (by me) and entirely conventional. Until my early teens, my plan was to be this guy:

[![](https://textslashplain.com/wp-content/uploads/2023/02/image-1.png?w=528)](https://textslashplain.com/wp-content/uploads/2023/02/image-1.png)

I went to Space Camp and Space Academy, and spent years devouring endless books about NASA history, space flight, and jet planes. I spent hours “playing” on a realistic (not graphically, but in terms of slow pacing and technical accuracy) Space Shuttle simulator, until I could land the shuttle on instruments alone.

[![](https://textslashplain.com/wp-content/uploads/2023/03/image-41-edited.png)](https://textslashplain.com/wp-content/uploads/2023/03/image-41.png)

Over time, however, three factors conspired to change my course.

* First was my realization that my few peers interested in space were all interested in *space* — stars and planets and the science, while I really only cared about the *technology* of *getting there* and *surviving*.
* Second was the discovery of a Catch-22: While astronaut pilots don’t have to have perfect vision, they *were* required to have thousands of hours of experience flying jets, which *practically* required being a military jet pilot, which *did* require perfect uncorrected vision. My distance vision was ~20/40.
* Finally, I’d started getting more and more interested in playing around with computers. I began writing “choose-your-own adventure” games in GW-BASIC starting around age 8 or so, and continued coding in school on Apple II (AppleBasic) and PCs (Logo, Pascal).

Shortly after my 15th birthday, I spent a full summer job’s earnings (*~$3000 at $4.75/hr*) on my first personal PC (*Comtrade Pentium 90 PC with a whopping 8 megs of RAM, 730mb HDD, 4X CDROM, 15.7″ monitor, bought over the telephone from an ad in Computer Shopper magazine*) and I started writing apps in Turbo Pascal, VB3 (*bought for $50 on 5.25″ floppies at the annual “Computer show” at the Frederick Fairgrounds*), and eventually Delphi 1 (*$100 at Babbages in the mall*). By my late teens, I was spending ten or more (sometimes much more) hours a week writing code, and after my senior year, I got my first programming job building custom Windows apps in Delphi for a small development shop at almost 4x minimum wage.

After high school, I majored in Computer Science at the University of Maryland, and while I largely didn’t like it (too much theory, too little practice), I had already seen that software development was a pretty solid career choice. In my sophomore year, on a whim (with the promise of free pizza) I went to a Microsoft recruiting talk on campus delivered by [Philip Su](https://peaksalvation.com/), a recent University of Maryland graduate who had joined Microsoft as a developer. Philip was a school legend, having written UMD’s web-based course planning system (a CGI written in C++ talking to the mainframe and spitting out HTML) that allowed you to specify constraints like “*I need this many credits, these specific classes, and otherwise do not want to attend class before 11am on any day.*” After Philip’s awesome talk, I went from being mildly interested in Microsoft to very excited at the prospect of getting an internship. I dropped off my resume, chatted briefly with Philip, and crossed my fingers.

I got a callback for a short interview at the campus career center a short time later. I didn’t really know what to expect, but figured my best bet was to show off the code I’d built so far. I put together a small binder of screenshots and explanations of tools I’d built in Delphi, including [SlickRun](https://textslashplain.com/2023/01/12/slickrun/), DigitalMC, and Logbook, a journaling program. Each of these was a “scratch my own itch” type of app where my goal was to use technology to **solve a problem**. In each app, I tried to build cool features, not implement fancy algorithms from scratch. Digital MC used several different libraries (text-to-speech, MP3 playback) and Logbook used an existing database engine.

My campus interviewer was a Microsoft developer in his early thirties (in hindsight, he may well have been younger) who looked a bit weary after a morning full of 15 minute interviews. After quick introductions, he asked which of the engineering roles I’d be most interested in applying for.

I told him that I thought I’d be a fine fit for any of the roles, although I was most interested in the SDE (Software Development Engineer) and PM (Program Manager) roles, and was interested in what he thought. I handed over the binder and walked him through the projects I’d built— as I explained SlickRun, his eyes lit up and he was clearly excited about it. “*Have you ever shown this to Microsoft?*” he asked excitedly. “*I guess I just did?*” I replied, wondering what exactly he meant— it wasn’t as if Microsoft toured the country looking for interesting bits of code. I asked him for advice on whether I should go for the PM or SDE role and he noted that Microsoft was looking for SDE interns with experience building 5000 line C and C++ programs. At that point, I’d built several large applications, but all were in Delphi’s Object Pascal. The only C and C++ I’d written was for class projects, and none of those had yet cracked a thousand lines. This made the decision easy— I’d submit my resume as a PM-candidate, a decision with far-ranging and long-lasting consequences. Not long after, I flew to Redmond for a day of on-site interviews with two teams in Office and got offers from both.

During my first [Office summer internship](https://learn.microsoft.com/en-us/archive/blogs/techtalk/interns-the-intern-experience-in-office) in 1999, I ramped up on a new technology (devouring the first books on XML), wrote up competitive reports on the first web-based collaboration software, and played with the nascent API for our team’s “Office Web Server (OWS)” product (eventually renamed SharePoint Team Services). I attended a bunch of training classes, read a bunch of product specs, read a pile of usability books, and generally immersed myself in learning what it meant to be a Program Manager at Microsoft. At the time, the role was hand-wavingly defined as “*The person who does everything but code and test*.” Qualifications were similarly open, with recruiters told to look for candidates with “*A passion for using technology to solve problems.”*

I returned to the same team the following summer– by this point, the product was in much more defined form, and I was paired with an Intern Developer and Intern Tester (a “feature trio”) to build a feature. Over the course of the summer, I learned that the *primary* tasks for most PMs were writing feature design specifications, shepherding them through implementation, triaging bugs found in the implementation, and getting ready for release.

SharePoint was a product based on the idea of Lists (lists of documents, lists of links, lists of contacts, etc) and my intern trio was tasked with adding a feature whereby a SharePoint user could create a list based on pre-built templates with appropriate fields (e.g. the Contact list would have fields for email address, phone number, office address, etc, etc). I wrote the spec for how the feature should look, and for the pac...