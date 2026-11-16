---
title: Your Google Calendar Is Probably Public. Here's Why That's Terrifying.
url: https://pentester.ca/blog/google-calendar-public
source: Over Security
date: 2026-11-15
fetch_date: 2026-11-16T08:48:45.359460
---

# Your Google Calendar Is Probably Public. Here's Why That's Terrifying.

[Skip to main content](#main)

[](/assets/images/Orbs/PT_Orb_LoopDark.webm)
![](/assets/images/Logos/Pentester.ca_Full_Logo_Dark.svg)

[](/assets/images/Orbs/PT_DarkPink_Orb.webm)

* Based in Tokyo,
  [E: [email protected]](/cdn-cgi/l/email-protection#7e0916170a1b161f0a3e0e1b100a1b0d0a1b0c501d1f)
* Japan
  --:--:-- (GMT+9)

* [Home](/)
* [What You Get](/#what-you-get)
* [Why Hire Me?](/#why-hire-me)
* [Who Have I Helped?](/#who-helped)
* [The Feedback](/#feedback)
* [Blog](/blog)
* [Contact](#contact)

[![Pentester.ca - home](/assets/images/Logos/Pentester.ca_Full_Logo_Light.svg)](/)

[![](/assets/images/Title_Element_Black.svg)
BLOG](/blog)

# Your Google Calendar Is Probably Public. Here's Why That's Terrifying.

By Kaeden | Pentester.ca | April 2, 2026

Google Calendar has a setting that makes your entire calendar visible to anyone with your email address. Not just your availability. Full event details: titles, descriptions, attendees, Zoom links with passwords, and any documents linked in the description. All anyone needs is your email and a URL like calendar.google.com/calendar/u/0/[[email protected]](/cdn-cgi/l/email-protection). No authentication. No notification to the owner.

This whole rabbit hole started by accident. I was doing security research on MSCHF, the viral product company behind Big Red Boots and Blur, and ran an employee's email through GHunt, an OSINT tool. It flagged their Google Calendar as public. I clicked through, and suddenly I was looking at every upcoming product drop planned through 2025, internal meeting notes, and links to Google Docs, Spreadsheets, and Figma files that were viewable by anyone. One spreadsheet contained celebrity addresses.

I reported it directly. To their credit, the calendar was made private within hours. But the linked documents took longer to lock down, and I had to send a follow-up listing every exposed file I'd found. To be clear: I didn't access anyone's accounts, join anyone's meetings, or do anything beyond looking at what was already publicly available to anyone with an email address.

## How Big Is This?

After MSCHF, I wrote a script and started checking email addresses at scale. Open calendars everywhere. Fortune 500 companies across tech, entertainment, automotive, and consumer goods. Events linking to unlisted internal spreadsheets. Google Drive folders containing recorded meetings anyone could watch.

Government agencies were the worst. In 2025, Business Insider identified a DOGE staffer through his public Google Calendar. I found the same issue across multiple US federal agencies, not just NASA and NOAA. One agency alone had over 200 employees exposed. State government employees across more than a dozen states had theirs open too, along with UK government departments. Investment banks and brokerages as well.

Security researcher Avinash Jain documented this same problem back in 2019, finding over 8,000 exposed calendars. That was six years ago. It's only gotten worse.

## Then I Started Looking at Meetings

I took it further and built something that specifically looked for meetings with video call links: Zoom, Google Meet, Teams, Calendly. Every meeting has attendees. Every attendee has an email. Every email might lead to another open calendar. An endless loop. I also fed in email addresses scraped from public GitHub commits, which worked very well. Developer emails led straight to open calendars at companies you'd recognize.

In a few hours, that pulled 143,000 meetings. Over 91,000 were upcoming with join links anyone could click, belonging to government agencies, several Fortune 500 companies, and thousands of other organizations and individuals. Zoom passwords in event descriptions. Netlify site credentials. Confidential business details in plain text. And that only counts meetings with meeting links. If I'd collected everything, the number would be significantly higher.

## Why It Happens

Google shows a warning when you enable public sharing: "Making your calendar public will make all events visible to the world, including via Google search. Are you sure?" People click through without understanding what that means. They think coworkers can see when they're busy. It actually means anyone on the internet can read their Zoom passwords.

This is also the kind of thing traditional security assessments never catch. Pentest firms test web apps and APIs. They don't check whether the CEO's calendar is leaking the product roadmap. I do.

## What You Should Do

* Check your settings right now. Go to Settings, click your calendar, scroll to "Access permissions for events." If "Make available to public" is checked, uncheck it.
* Audit your linked documents. If calendar events link to Google Docs or Drive folders, make sure those aren't viewable by anyone with the link. A public calendar with links to public documents is a full data leak.
* If you're a Workspace admin, audit your organization's defaults. A single misconfigured setting can expose your entire company's meeting schedule.

[Get a Free Consultation
![](/assets/images/Top_Right_Arrow_Black.svg)](https://cal.com/whitehat/30min?user=whitehat)
[![](/assets/images/Top_Right_Arrow_Black.svg)Back to all posts](/blog)

## Read About My Work

* [![](/assets/images/Top_Right_Arrow_Black.svg)Blog](/blog)

© 2026 Designed by [PixelPonderer](https://pixelponderer.com/)

## Got Security?

[[email protected]](/cdn-cgi/l/email-protection#34435c5d40515c55407444515a4051474051461a5755)

[Let's Connect
![](/assets/images/Top_Right_Arrow_Black.svg)](https://cal.com/whitehat/30min?user=whitehat)

## Where to Find Me

* [![](/assets/images/Top_Right_Arrow_Black.svg) LinkedIn](https://www.linkedin.com/in/kaeden69420/)

Based in Tokyo, Japan

Disclaimer: Got Vulnerabilities?® is a parody. Got Milk?® is a registered trademark of the California Milk Processor Board.