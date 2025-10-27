---
title: The art of artifact collection and hoarding for the sake of forensic exclusivity… – Part 3
url: https://www.hexacorn.com/blog/2024/06/05/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity-part-3/
source: Hexacorn
date: 2024-06-06
fetch_date: 2025-10-06T16:56:02.932236
---

# The art of artifact collection and hoarding for the sake of forensic exclusivity… – Part 3

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2024/05/03/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity-part-2/)
[Next →](https://www.hexacorn.com/blog/2024/06/07/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity-part-4/)

# The art of artifact collection and hoarding for the sake of forensic exclusivity… – Part 3

Posted on [2024-06-05](https://www.hexacorn.com/blog/2024/06/05/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity-part-3/ "11:48 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

(this is a very long post, sorry; took weeks to distill it into something that I hope is readable)

As promised, today I am finally going to demonstrate that the piracy is good! (sometimes)

In order to do so, I need to start in a non-sequitur way though…

There are two questions that today’s forensic and telemetry technologies fail to answer quickly, let alone clearly:

1. What will I find on this SPECIFIC system/endpoint?
2. What will I find inside this ORG? (2a probably touches on the cloud as it’s gaining momentum in this era of a digital transformation)

The first question is super important.

Before we even start that basic forensic triage, kick off these evidence collecting scripts and heat up the pipelines focused on automated forensic data processing… it would be really cool to read a basic summary of what that endpoint IS all about – showing us the ‘easy’ findings first:

* this system is *this and that OS*,
* it is *this and that OS version*,
* *it is a domain controller/server/workstation/laptop*,
* *with this and that list of updates, patches*,
* *belongs to this and that domain*…
* with *this and that list of running processes and services…*

Nuh, just kidding… it’s a trap.

So many automated-data-extraction approaches focus on all this unimportant, but easy to extract stuff that it almost always ends up delivering something that I vehemently hate: *fluff*.

Let’s remember that *activity is not a productivity*.

That is, even with all these fancy auto-generated summaries available, the question posed above will still remain unanswered…

Why?

Because the true, honest answer to this question can take many forms, and none of them really care about the ‘easy to code, but fail to answer the basic question’ type of automation cases… What it means is that we don’t want yet another ‘quantity over quality’ vulnerability scanner’s endpoint equivalent in the house… doing forensic-wannabe job, but in the end delivering nothing, but non-actionable, confusion-soaked nothingburgers.

So, without a further ado, let’s demonstrate how a proper answer could look like (and it’s 100% hypothetical). I hope you will agree that any subset of the below could be helpful:

* There are two active users on this system: FOO and BAR (active=used the OS recently aka within last few days/week/month – should be precisely defined)
* The user FOO appears to be a gamer, because we see the following games installed on the system and they are being executed repeatedly when that FOO user is logged in: *C:\gamea*, *C:\gameb*, *C:\gamec*, …
* The user FOO keeps all the personal files in the following directory: *C:\XYZ* – this is based on metadata extracted from all documents stored inside this folder
* The second user of this system (BAR) appears to be an accountant – there is a stash of accounting files stored in the following directory: *c:\beancounters*; this user doesn’t seem to be playing any of the installed games; still, it is questionable that the user BAR stores possibly sensitive customer accounting data on the system on which the user FOO is playing games…
* There is a stash of sensitive files stored in the following directories: *c:\secret*, *d:\confidential*; we don’t know who created these folders, but a couple of PDFs inside the *c:\secret* directory seem to be password-protected, and a few files from *d:\confidential* directory reference strings ‘TOP SECRET’ and ‘TLP;RED;’ – they may be of interest
* There is a number of manually created folders that may be of interest: *c:\beancounters\new folder*, *c:\beancounters\nouveau dossier*
* Whoever created *c:\beancounters\nouveau dossier* may be a francophone
* A number of dashcam videos appear to be stored inside the following folder: *c:\dashcam*; they cover the dates between *2024-01-01* and *2024-02-05*
* There is a plain-text file that appears to be storing secrets: *c:\aws\creds.txt*
* There is a pr0n collection stored inside the *c:\updates* folder
* The Instant Messengers apps found on this system are: *Skype*, *Telegram*, *WhatsApp*
* Portable Tor seems to be installed in *c:\Tor* directory
* There are 2 email clients recognized on the system: *Outlook*, *Thunderbird*
* There are 3 Instant Messaging programs recognized on the system: *Telegram*, *Skype*, *Signal*

Do you see what I am talking about here?

The *art of quick, meaningful but also early* system profiling based on the existing forensic evidence!

And yeah, it’s not an easy task, it’s also not fool-proof, and yeah, we can’t just rely solely on regular expressions or AI here that can be applied to various forensic artifacts discovered during triage/preliminary analysis, but… anything goes… any decent *commentary* we can provide about the actual system’s content before any manual forensic exam starts… is a decent start! Does it bring a bias to the exam? 100%. Does it make it easier to automate triage towards this bias? 100%.

What I posit is this:

*Given the advances in forensic technologies related to data acquisition, data collection, data processing, data triage and data analysis automation (plus maybe AI), are we in a position to move the evidence analysis flagpole forward towards… maybe not the ‘one click solution’ yet… but kinda towards it, anyway? Saving lots of personhours in the process?*

And if we extrapolate…

The question #2 is very fascinating as well…

*What will I find inside this org?*

Your asset inventory, your SBOM, your ad hoc queries combing through recent process/file/service creation telemetry are all adding value… BUT… it’s not working, long-term.

Why?

Collating information from various (very dynamic in nature) sources is HARD. The IT sector is still firmly stuck in a Don Quixotic notion believing that we can create a perfect asset inventory using available people, process, technology adjustments, but the reality is far more complicated than that and even more nuanced…

* First of all, even today it’s most of the time done in Excel or Google Sheets. Yup! and Yuck!
* Secondly, since it is usually done manually, it often expires before it even gets to the production level; hence it’s always marked as a ‘work in progress’.
* Thirdly, it’s usually owned by, and then created and maintained by people with a mindset of a single shop owner that likes to count beans, and not driven by that very wild, and far-reaching concept of co-ownership… where n-dimensional, distributed, tech debt and post-many-M&As -heavy digital transformation riders follow well-defined processes that make the asset inventory ‘build and maintain itself’. Getting there requires a lot of thinking, trial and error though, and many transformations later, many processes creations and/or adjustments later we may eventually win. Otherwise we always end up working with the old data. I don’t know if there is any company out there today that is doing it 100% right, so yeah… here’s your new startup idea… 🙂

On a practical level…

* The f...