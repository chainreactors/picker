---
title: Identifying Groups of "Bot" Accounts on LinkedIn, (Tue, Nov 29th)
url: https://isc.sans.edu/diary/rss/29282
source: SANS Internet Storm Center, InfoCON: green
date: 2022-11-30
fetch_date: 2025-10-04T00:06:45.663958
---

# Identifying Groups of "Bot" Accounts on LinkedIn, (Tue, Nov 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29276)
* [next](/diary/29288)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Identifying Groups of "Bot" Accounts on LinkedIn](/forums/diary/Identifying%2BGroups%2Bof%2BBot%2BAccounts%2Bon%2BLinkedIn/29282/)

**Published**: 2022-11-29. **Last Updated**: 2022-11-29 15:46:37 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Identifying%2BGroups%2Bof%2BBot%2BAccounts%2Bon%2BLinkedIn/29282/#comments)

As some have noted, LinkedIn has recently removed many accounts after identifying them as "bots" or "disingenuous" [1]. These removals are relatively easy to spot if they affect large companies like Amazon, Apple, and others. But they are a bit more challenging to spot if the fake accounts claim to work for smaller, relatively unknown companies.

First, a bit about the "why": Why do bots exist on LinkedIn? I define a "bot" as an account claiming to be someone they are not. Some may have a human operator associated with them.

**Influence Operations**

Any nation-state trying to be taken seriously in "Cyber" these days is using social media for influence operations in some form. Typically this involves amplifying a particular political point by either re-posting supporting content or posting comments attempting to harm opposing views.

**Spam**

Simple advertising. I stopped accepting connection requests from people on LinkedIn from certain groups of companies ("Explainer Animation Videos..") as they almost always connect to sell their wares. I have also been less likely to accept connections from individuals with job titles like "marketing" or "sales" if they are not infosec related.

**Recognizance**

This is probably the most severe, frequent attack using social media, particularly LinkedIn. Attacks attempt to map out social networks to find relationships like who reports to whom or who works with whom. This can be used to identify supplier relationships and used for more targeted phishing attacks. For example, gift card scams may have used LinkedIn profiles announcing that they just joined a company to figure out who that person reports to. This information can be used to initiate a nicely targeted message claiming to be from the new boss, asking the victim, still eager to please the new boss, to purchase gift cards.

So how do you recognize these less-than-genuine accounts? First of all: There is no way to say for sure. But let me give you a few examples that I think are not genuine. And sorry if I misidentified some.

Recently, an individual at SANS.edu received a connection request from this account:

![](https://isc.sans.edu/diaryimages/images/Screenshot%202022-11-29%20at%2010_13_42%20AM(1).png)

The experience and education section looks plausible overall, but there are a few oddities about the profile

![](https://isc.sans.edu/diaryimages/images/Screenshot%202022-11-29%20at%2010_15_57%20AM.png)

First, the heavy use of bulleted lists is a bit odd, but not the weird "reverse comma" used after the numbers. This "ideographic comma" is sometimes used in Chinese and Japanese. So it does somewhat match the person's background. But let's now look at other profiles for that same company.

![](https://isc.sans.edu/diaryimages/images/Screenshot%202022-11-29%20at%2010_23_47%20AM.png)

Not all profiles are public, but the public profiles all use the same last name (maybe a family-run company?). Not only that. They also use identical/similar biographic information sporting the same ideographic comma.

Recently, LinkedIn added a new feature to make it a bit easier to spot fake profiles. If you click on "More" and "About this profile" in a user's profile, you will get information about the age of the profile and if any information is verified.

![](https://isc.sans.edu/diaryimages/images/Screenshot%202022-11-29%20at%2010_27_10%20AM.png)

For this set of profiles, the phone number is verified. It is usually not that difficult to obtain a "burner" phone number for little money. The profiles are all very new, which may be suspicious.

I usually also try to do a reverse image search on profile pictures. Lately, I do not have much luck with that. In the past, I sometimes ended up with images from fashion catalogs that were reused as profile pictures. But I believe recently, more of them rely on modified "fake image generators," or they use images not easily indexed by standard image search engines like Google, Tineye, or Yandex.

**Lessons Learned**

Everything you do and say on social media is public. I am not very careful about accepting connections on LinkedIn. I do not use LinkedIn to share secrets, nor should you (or use any other social media platform for this). Social media platforms are great at disseminating information and horrible at keeping them secret.

Social media platforms should also not be seen as authoritative information about who is working for a particular company. Bad actors can hijack even legitimate accounts. Do not trust messages received via social media platforms, mainly if they are out of character.

Report fake profiles, and block them. Reporting fake profiles helps social media platforms identify trends they may miss. The account may not get taken down right away. Still, stop them.

Alert coworkers about fake accounts claiming to work for your company. If you receive an odd request from a coworker: Ask them directly to verify. Depending on your organization's policies, you may want to report fake messages to your security or HR department to take action.

Should you be careful about what connections to accept? But you will be unable to effectively use a social media platform and avoid connecting to a few fake profiles. Assume that it will happen or likely already has happened. And if you will not accept any fakes: Some of your connections will, which may give the bots access to your profile. Understand that we use social media to make things we share public, not to keep things a secret.

[1] https://krebsonsecurity.com/2022/10/battle-with-bots-prompts-mass-purge-of-amazon-apple-employee-accounts-on-linkedin/

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [social media](/tag.html?tag=social media) [linkedin](/tag.html?tag=linkedin)

[0 comment(s)](/diary/Identifying%2BGroups%2Bof%2BBot%2BAccounts%2Bon%2BLinkedIn/29282/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29276)
* [next](/diary/29288)

### Comments

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
* [Tools](/t...