---
title: How to Run a Deepfake Readiness Drill Before a Cloned Voice Calls Your Team
url: https://thehackernews.com/2026/10/how-to-run-deepfake-readiness-drill.html
source: The Hacker News
date: 2026-10-14
fetch_date: 2026-10-15T06:45:39.299667
---

# How to Run a Deepfake Readiness Drill Before a Cloned Voice Calls Your Team

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [How to Run a Deepfake Readiness Drill Before a Cloned Voice Calls Your Team](https://thehackernews.com/2026/10/how-to-run-deepfake-readiness-drill.html)

**The Hacker News**Oct 14, 2026Social Engineering / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEYzcrs6sSW45od6MYo5jFl29yPGuwipgy7nfS3STYqknrD9b5OcU00_c0sqjG8Arvqq36ojwHSZMbjboA3bUQ1-ZcLRRjmuEQpzTDYYXnyvySzynW0UOvHOVmYNNzp_n-J5xXmwByMCofw5kxslXe4dqAVYqrWa-1LivXxPNa_ZGOQgIBxhyhvtiLxDs/s1700-nu-rw-lo-l85-e365/icon.jpg)

*Cloned voices and synthetic video calls now show up in payment fraud, help desk resets, and access requests. A structured drill shows security teams exactly where verification breaks down, while nothing is at stake.*

The call comes in at 4:40 on a Friday. It's the CFO, or it sounds exactly like her, asking the controller to push a supplier payment out before the weekend because a deal closes Monday. She's traveling, she's rushed, and she apologizes for the bad connection. Ten minutes later an email lands with the wire details.

A couple of years ago that scenario was a conference talk. Now it shows up in incident reports. In a [2025 Gartner survey of 302 cybersecurity leaders](https://www.gartner.com/en/newsroom/press-releases/2025-09-02-why-cios-cannot-ignore-the-rising-tide-of-deepfake-attacks), 62% said their organization had experienced at least one deepfake attack in the prior 12 months. In the same survey, 43% reported at least one deepfake audio call incident and 37% had run into deepfakes on video calls.

And the wire is only the obvious ask. The same cloned voice can call the help desk to move an MFA token, or ask an identity admin to set up a new global admin ahead of an "audit." A fraudulent wire tends to surface at reconciliation. A quietly added admin account can sit there for months.

Most organizations have a policy that says to verify unusual payment and access requests. Far fewer have checked whether that policy survives a phone call from someone who sounds like the person who signs off on everyone's paycheck. A deepfake readiness drill is how you find out, on your own schedule, with nothing real on the line.

## **Why detection by ear falls short**

Security awareness training has long taught employees to look for tells. Awkward phrasing, an odd sender address, a link that doesn't match the text. Voice clones and real-time face swaps leave fewer of those tells every quarter. Asking people to hear the fake is asking a lot.

In a May 2025 warning about AI-generated voice messages impersonating senior US officials, the [FBI noted that cloned voices can sound nearly identical to the real person](https://www.ic3.gov/PSA/2025/PSA250515) and told recipients to confirm identity by calling an independently sourced phone number before acting on anything.

Security leaders already know this. In a January 2026 Osterman Research study of 128 US security and IT leaders, commissioned by IRONSCALES, 60% said they lacked confidence in their ability to counter deepfake attacks even with the training they already run.

So the defense has to rest on process more than perception. If an employee runs the same verification step every time money, credentials, or permissions are involved, the quality of the fake stops mattering much. A drill tests whether that step actually happens when someone senior is leaning on them.

## **Step 1. Map the voices worth cloning and the people worth calling**

Start with two short lists.

The first is the people an attacker would impersonate. That means executives who can approve payments or direct staff (CEO, CFO, CIO, CISO, general counsel). Then go a level down. VPs and directors in finance, IT, and HR make requests like these every week, so a call from one of them raises fewer eyebrows than a surprise call from the CEO. Add a few outside contacts with real authority over money or access, like a key supplier's accounts receivable lead or the engineer at your managed service provider.

The second is the people an attacker would call. Accounts payable, treasury, payroll, HR, executive assistants, the IT help desk, and anyone who can grant or change access in your identity platform. The help desk and the identity admins get left off these lists a lot. They shouldn't be. A cloned voice asking for an MFA reset is a fast route to Account Takeover (ATO). A cloned voice asking for a new admin account skips a few steps.

For everyone on the first list, note how much public audio and video exists. Earnings calls, podcast appearances, conference keynotes, webinar recordings, and social media clips all give an attacker training material. A CFO with three hours of recorded keynotes is a much easier clone than one who's never been on camera. It doesn't take three hours, though. A few minutes from a single webinar can be enough, which puts most directors on the list too.

What comes out of this step is a short matrix: the identities most worth faking and the people most likely to get their calls. In most organizations that's a few dozen people. Manageable.

## **Step 2. Write the verification rules before testing them**

A drill without a clear rule only measures instinct. Before running any scenario, document what employees are supposed to do. Strong verification rules tend to share a few traits.

* **Out-of-band callback.** Any request to move money, change bank details, share credentials, reset MFA, or change who has access to what gets confirmed through a number pulled from the internal directory or vendor master file. Never a number supplied in the request itself.
* **Clear thresholds.** Spell out which actions always require verification, no matter who's asking or how urgent it sounds.
* **Dual approval.** Two people sign off on new payees, changed banking details, new privileged accounts, and role changes.
* **Challenge phrases.** The most-impersonated executives and their direct support staff sha...