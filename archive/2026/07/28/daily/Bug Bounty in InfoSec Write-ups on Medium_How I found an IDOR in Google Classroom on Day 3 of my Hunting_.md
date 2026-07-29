---
title: How I found an IDOR in Google Classroom on Day 3 of my Hunting?
url: https://infosecwriteups.com/how-i-found-an-idor-in-google-classroom-on-day-3-of-my-hunting-abffd039406c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-28
fetch_date: 2026-07-29T05:02:48.340999
---

# How I found an IDOR in Google Classroom on Day 3 of my Hunting?

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-idor-in-google-classroom-on-day-3-of-my-hunting-abffd039406c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-idor-in-google-classroom-on-day-3-of-my-hunting-abffd039406c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-abffd039406c---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-abffd039406c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# How I found an IDOR in Google Classroom on Day 3 of my Hunting?

[![Marrij Ali Khan](https://miro.medium.com/v2/resize:fill:64:64/1*1s2NXZOBQwSYUMn9pMyPxQ.webp)](https://marrijalikhan.medium.com/?source=post_page---byline--abffd039406c---------------------------------------)

[Marrij Ali Khan](https://marrijalikhan.medium.com/?source=post_page---byline--abffd039406c---------------------------------------)

4 min read

·

21 hours ago

--

3

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dabffd039406c&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-idor-in-google-classroom-on-day-3-of-my-hunting-abffd039406c&source=---header_actions--abffd039406c---------------------post_audio_button------------------)

Share

Hello Guys,

![]()

Hope you are well. This is my first writeup and I will tell you how I found IDOR on Google Classroom on Day 3 of my hunting on Google. I hope it will inspire you.

I selected my first target as Google Classroom because I use it daily for my University Assignments and Tasks.

![]()

So first, I started testing every feature, and I noticed in Burp History that Google is using Batchexecute system with ***rpcids*** for every UI functionality.

The batchexecute system at ***classroom.google.com*** is Google's internal frontend RPC protocol and it’s completely undocumented.

The batchexecute system works like, every UI action in Classroom triggers a POST request to the batchexecute endpoint with a parameter called ***rpcids*** that identifies which internal method to call.

For example when you post a comment in Classroom your browser sends something like:

![]()

Then, I started mapping different UI functionalities with rpcids, for example:

ndas7c > CREATE announcement
F7asdb > UPDATE/EDIT announcement
tQbcjc > READ/FETCH announcement
xxxxxx > POST private comment on submission thread

These rpcids helped me map every Ui functionality.

After spending time mapping every RPC method in Classroom batchexecute system, most of my tests were coming back clean. Google’s auth on the obvious attack surfaces was solid. The well-known endpoints had proper authorization checks.

I was about to move on to a different target but I decided to look more carefully one last time at the private comment functionality on assignment submissions.

Private comments in Google Classroom are a specific feature designed for confidential communication between a student and their teacher about a particular assignment submission. When a student submits work they can leave private notes for the teacher and the teacher can respond. These comments are explicitly designed to be visible only to the submission owner and the teacher. No other student should be able to see or interact with that thread.

I gave it a try and said to myself that this is the last endpoint I will test on Classroom.

I had two test accounts set up, one acting as an attacker and one as a victim, both enrolled in the same course with submitted assignments. While intercepting traffic I started looking at the requests that fired when I posted a private comment on my own submission.

## Get Marrij Ali Khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

What caught my attention was the structure of the request. Like all batchexecute calls, it contained several ID parameters such as the course ID, the coursework ID, and crucially a submission ID that identified whose submission thread the comment was being posted to.

The question I asked myself was simple, what happens if I change that submission ID?

Then, I captured my second account same request and copied the submission ID.

I replaced my submission ID with the victim’s submission ID in the request, kept my own session cookies, and sent it.

The server returned 200 OK.

I opened the victim’s account and looked at their private submission thread. Yippee, my attacker comment was sitting there, visible to the victim and their teacher.

Press enter or click to view image in full size

![]()

Victim’s View

The authorization check wasn’t there for this particular RPC method. The server accepted the request, trusted the submission ID in the payload, and posted the comment without verifying that the commenter had any legitimate relationship to that submission.

Now, there was one thing I had to figure out that how to get the victim submission ID in a realistic scenario.

I started analyzing Burp History and found a response that was showing submission IDs of all students enrolled in the class. BOOM. I tested it again and found that on a specific endpoint, if you refresh the page and capture the request, you will see submission IDs of all students in the response.

Press enter or click to view image in full size

![]()

I verified the finding from the teacher’s account as well. The unauthorized comment appeared there too.

Press enter or click to view image in full size

![]()

Teacher’s View

I documented everything and submitted the report to Google VRP. Unfortunately, The report came back as a duplicate, but I was happy that I found a legitimate issue.

Press enter or click to view image in full size

![]()

Finding a real vulnerability in a Google product as someone still building their skills felt significant, even if it ended up being a duplicate. The whole process taught me more than I expected, not just about bug hunting but about how to think like a security researcher.

Thank you for reading. Hope you enjoy it and hope it inspire you.

Follow me on Linkedin: [linkedin.com/in/marrij](http://linkedin.com/in/marrij)

![]()

Infosec Write Ups

Bug Bounty

Google

Bug Bounty Writeup

Idor

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--abffd039406c---------------------------------------)

[![InfoSec Write-ups...