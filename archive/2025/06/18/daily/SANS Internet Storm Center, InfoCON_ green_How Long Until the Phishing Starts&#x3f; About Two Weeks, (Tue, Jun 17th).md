---
title: How Long Until the Phishing Starts&#x3f; About Two Weeks, (Tue, Jun 17th)
url: https://isc.sans.edu/diary/rss/32052
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-18
fetch_date: 2025-10-06T22:55:13.786102
---

# How Long Until the Phishing Starts&#x3f; About Two Weeks, (Tue, Jun 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32048)
* [next](/diary/32054)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [How Long Until the Phishing Starts? About Two Weeks](/forums/diary/How%2BLong%2BUntil%2Bthe%2BPhishing%2BStarts%2BAbout%2BTwo%2BWeeks/32052/)

**Published**: 2025-06-17. **Last Updated**: 2025-06-17 13:15:42 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[5 comment(s)](/diary/How%2BLong%2BUntil%2Bthe%2BPhishing%2BStarts%2BAbout%2BTwo%2BWeeks/32052/#comments)

[This is a guest diary by Christopher Crowley, <https://montance.com>]

Here’s a good reason to include security awareness training for new hires!

I recently added an account to my Google Workspace domain (montance[dot]com). Friday, May 16th, 10:10 am, to be exact. Something interesting to note about the domain configuration is there’s a catchall account in place, so all email addresses are valid.

Starting May 28th the new account started receiving targeted phishing email messages. The subject was either blank or a variation of my name (Chris or Christopher), and the sender's "From" address had a call to action and urgency:

> `From: "EMERGENCY: PROVIDE YOUR CELL NUMBER IMMEDIATELY"
> From: "EMERGENCY:PROVIDE YOUR CELL PHONE NUMBER IMMEDIATELY ASAP"
> From: "EMERGENCY; PROVIDE YOUR CELL PHONE NUMBER IMMEDIATELY"
> From: GET BACK TO ME IMMEDIATELY
> From: JUNE THURSDAY 5TH
> From: Quick Response
> From: RESPONSE REQUIRED
> From: Timely Reminder`

The messages all indicated that there were some urgent tasks to perform and that I supposedly needed the person’s phone number. There were 8 unique email addresses used, all of which invoke the concept of urgency:

> `hoursworking605--at--gmail_com
> immediatelyofficemail79--at--gmail_com
> officeoperatedeskboxx360--at--gmail_com
> promotionaltask747--at--gmail_com
> promotiontask910--at--gmail_com
> quickreply946--at--gmail_com
> quicktask5511--at--gmail_com
> urgentmails696--at--gmail_com`

All of these went into the Spam folder until June 10th, when a couple got through.  Noteworthy, almost all of the email salutations used the recipient’s LinkedIn name. This is obvious because his name on LI includes certifications. Then on June 10th, they sent him a text message:
![](https://isc.sans.edu/diaryimages/images/text_cropped.png)

This is likely reasonably automated phishing with low targeting specificity, but the identification of the new account and fast phishing was interesting. In my case, it was easy to observe since there are so few accounts in the domain and he’s a vigilant and cyber-aware person. MFA is enabled.

One question I have for readers: does anyone have a script or know of a project that’s an equivalent of Invoke-MSOLSpray targeting Google Workspace domains? Someone must be using something like that to discover new accounts. The email address wasn’t posted online anywhere. His LinkedIn profile has a different email address. So, there was some amount of correlation the sender of the spam did.

Nothing especially surprising, but a reminder that they’re watching for opportunities. Someone new at the company and eager to appear responsive seems like a good phishing target!

---
Christopher Crowley
Author, Consultant, Instructor
<https://montance.com>

Keywords: [awareness](/tag.html?tag=awareness) [new hires](/tag.html?tag=new hires) [phishing](/tag.html?tag=phishing)

[5 comment(s)](/diary/How%2BLong%2BUntil%2Bthe%2BPhishing%2BStarts%2BAbout%2BTwo%2BWeeks/32052/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32048)
* [next](/diary/32054)

### Comments

Two weeks are quite accurate from my own xp

#### recnik

#### Jun 17th 2025 3 months ago

Same thing is happening at my organization. at first I thought it was LI but then noticed the users didnt update their profiles. Ive tried searching with no luck. I thought that maybe our address book was out there in the open but I dont think thats the case. Hoping someone can chime in with a reason/solution to this!

#### Henri

#### Jun 18th 2025 3 months ago

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)